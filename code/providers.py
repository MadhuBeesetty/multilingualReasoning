"""Minimal provider abstraction for calling a real, independently-hosted
model-under-test (generator) via the Anthropic or OpenRouter (OpenAI-compatible)
APIs.

This module is pure library code: no CLI, no file I/O, no prompt-building.
Both run_inference.py and inspect_traces.py import from here.

API keys are always read from environment variables — never accepted as
constructor/CLI arguments — so they can't leak into shell history or process
listings.
"""

from __future__ import annotations

import os
from typing import Protocol

import anthropic
import openai

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

ANTHROPIC_API_KEY_ENV = "ANTHROPIC_API_KEY"
OPENROUTER_API_KEY_ENV = "OPENROUTER_API_KEY"
OPENROUTER_DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"

# Documented fallback only. run_inference.py makes --model required, so this
# constant is never actually exercised by the CLI. Deliberately NOT reused as
# the inspector's hardcoded model constant in inspect_traces.py, so a future
# change to this fallback can never accidentally change the fixed inspector.
DEFAULT_ANTHROPIC_MODEL = "claude-sonnet-5"

DEFAULT_MAX_RETRIES = 5
# Current Claude models (e.g. claude-sonnet-5) run adaptive thinking by default
# when no `thinking` param is sent, and max_tokens is a hard cap on thinking +
# response text combined. A generous default leaves headroom so a generator
# model's invisible thinking doesn't starve its visible answer.
DEFAULT_MAX_TOKENS = 8192

REFUSAL_SENTINEL = "[REFUSAL] model declined to answer"
TRUNCATION_SENTINEL_SUFFIX = "\n\n[TRUNCATED: response cut off at max_tokens]"


# ---------------------------------------------------------------------------
# Errors
# ---------------------------------------------------------------------------


class ProviderError(RuntimeError):
    """Raised for missing API keys and for non-retryable SDK errors
    (auth / bad-request / not-found), so callers can catch one thing and
    fail fast with a clear message."""


# ---------------------------------------------------------------------------
# Provider protocol
# ---------------------------------------------------------------------------


class Provider(Protocol):
    def generate(self, system_prompt: str, user_prompt: str) -> str:
        """Return the raw text completion for a single-turn request.
        No parsing, no answer extraction — just the model's raw text."""
        ...


# ---------------------------------------------------------------------------
# Anthropic provider
# ---------------------------------------------------------------------------


class AnthropicProvider:
    """Calls an Anthropic-hosted model (Claude family) as the generator.

    Uses client.messages.stream(...) + get_final_message() internally rather
    than a plain messages.create() call. The Anthropic SDK docs recommend
    streaming for long/high-max_tokens requests, and a non-streaming call can
    raise ValueError if the SDK estimates the request will take too long.
    Streaming sidesteps that guard regardless of max_tokens, which matters
    here because a --provider anthropic generator model's output length is
    unpredictable.
    """

    def __init__(
        self,
        model: str,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        api_key = os.environ.get(ANTHROPIC_API_KEY_ENV)
        if not api_key:
            raise ProviderError(
                f"{ANTHROPIC_API_KEY_ENV} is not set. Export it before running "
                f"(never pass API keys as CLI arguments)."
            )
        self.model = model
        self.max_tokens = max_tokens
        self._client = anthropic.Anthropic(api_key=api_key, max_retries=max_retries)

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            with self._client.messages.stream(
                model=self.model,
                max_tokens=self.max_tokens,
                system=system_prompt,
                messages=[{"role": "user", "content": user_prompt}],
            ) as stream:
                message = stream.get_final_message()
        except (
            anthropic.AuthenticationError,
            anthropic.PermissionDeniedError,
            anthropic.BadRequestError,
            anthropic.NotFoundError,
        ) as e:
            raise ProviderError(
                f"Anthropic request failed (non-retryable): {type(e).__name__}: {e}"
            ) from e

        if message.stop_reason == "refusal":
            return REFUSAL_SENTINEL

        text = "".join(block.text for block in message.content if block.type == "text")
        if message.stop_reason == "max_tokens":
            # Sonnet-5-and-later models run adaptive thinking by default, and
            # max_tokens caps thinking + response text combined, so a tight
            # budget can truncate the visible answer without raising. Mark
            # this inline (rather than silently returning partial text) so
            # it's visible in the generation output and downstream inspection.
            text += TRUNCATION_SENTINEL_SUFFIX
        return text


# ---------------------------------------------------------------------------
# OpenAI-compatible provider (OpenRouter, or any other OpenAI-compatible host)
# ---------------------------------------------------------------------------


class OpenAICompatibleProvider:
    """Calls a model behind an OpenAI-compatible chat-completions API.

    Defaults to OpenRouter, but base_url and api_key_env are constructor-level
    knobs so this class isn't hardwired to OpenRouter specifically.
    """

    def __init__(
        self,
        model: str,
        base_url: str = OPENROUTER_DEFAULT_BASE_URL,
        api_key_env: str = OPENROUTER_API_KEY_ENV,
        max_tokens: int = DEFAULT_MAX_TOKENS,
        max_retries: int = DEFAULT_MAX_RETRIES,
    ) -> None:
        api_key = os.environ.get(api_key_env)
        if not api_key:
            raise ProviderError(
                f"{api_key_env} is not set. Export it before running "
                f"(never pass API keys as CLI arguments)."
            )
        self.model = model
        self.max_tokens = max_tokens
        self._client = openai.OpenAI(
            api_key=api_key, base_url=base_url, max_retries=max_retries
        )

    def generate(self, system_prompt: str, user_prompt: str) -> str:
        try:
            response = self._client.chat.completions.create(
                model=self.model,
                max_tokens=self.max_tokens,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt},
                ],
            )
        except (
            openai.AuthenticationError,
            openai.PermissionDeniedError,
            openai.BadRequestError,
            openai.NotFoundError,
        ) as e:
            raise ProviderError(
                f"OpenRouter/OpenAI-compatible request failed (non-retryable): "
                f"{type(e).__name__}: {e}"
            ) from e

        return response.choices[0].message.content or ""


# ---------------------------------------------------------------------------
# Factory
# ---------------------------------------------------------------------------


def get_provider(name: str, model: str, **kwargs) -> Provider:
    """Dispatch to the right provider by name.

    kwargs are passed through to the provider constructor (e.g. base_url for
    openrouter). Unknown kwargs left as None by the CLI (e.g. an unset
    --base-url) should be filtered out by the caller before calling this.
    """
    key = name.lower()
    if key == "anthropic":
        return AnthropicProvider(model=model, **kwargs)
    if key == "openrouter":
        return OpenAICompatibleProvider(model=model, **kwargs)
    raise ValueError(f"Unknown provider: {name!r} (expected 'anthropic' or 'openrouter')")


# ---------------------------------------------------------------------------
# Shared inspector helper
# ---------------------------------------------------------------------------


def build_anthropic_client(max_retries: int = DEFAULT_MAX_RETRIES) -> anthropic.Anthropic:
    """Return an authenticated, retry-configured Anthropic client, reading
    ANTHROPIC_API_KEY from the environment and failing fast if it's unset.

    Exposed standalone (rather than only via AnthropicProvider) so
    inspect_traces.py can get a client without going through the generic
    text-only Provider interface — the inspector needs the structured-output
    call shape (output_config.format), not plain generate().
    """
    api_key = os.environ.get(ANTHROPIC_API_KEY_ENV)
    if not api_key:
        raise ProviderError(
            f"{ANTHROPIC_API_KEY_ENV} is not set. Export it before running "
            f"(never pass API keys as CLI arguments)."
        )
    return anthropic.Anthropic(api_key=api_key, max_retries=max_retries)
