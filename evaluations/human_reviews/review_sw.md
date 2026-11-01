# Multilingual Math Reasoning — Quick Review (Swahili)

Thank you for helping with this research project! We're studying how AI models solve math word problems in different languages, and specifically whether they sometimes **notice an important detail, then drop or misuse it while solving the problem** — as opposed to simply misunderstanding the problem from the start.

Below are 14 short math word problems in Swahili. An AI model attempted to solve each one. **Your job is only to check the model's work — you do not need to solve the problems yourself.** This should take about 20–40 minutes.

**Here's a quick example of the pattern we're looking for** (not one of your real items, just an illustration):

> *Problem: "A store has 10 apples. Half of them are red. How many apples are NOT red?"*
> *Model's attempt: "Half of 10 apples are red, so that's 5 red apples. There are 10 apples in total, so the answer is 10."*

The model **noticed** the key detail (5 apples are red) but then **dropped it** — it never subtracted those 5 from the total, and just restated the original count instead. That specific pattern — noticing something, then abandoning it a few steps later — is exactly what we're trying to measure. It's different from a model that never understood the "half are red" detail at all, or that made a plain arithmetic slip.

**For each of the items below:**
1. Read the **Question** and the **Correct Answer** (already given to you — you don't need to calculate it yourself).
2. Read the **Model's Attempt** and decide: did it reach the same final answer as the Correct Answer?
3. **If the model's answer was wrong**, look back through its reasoning and ask: did it explicitly notice or state a key detail (a rate that changes, a quantity that should be excluded, a condition that only applies partway through) and then fail to use it — or use it incorrectly — in a later step?
   - Answer **Yes** if you can point to a specific place where it noticed something and then dropped or misused it, like the apples example above.
   - Answer **No** if the model seems to have never understood that detail at all, or made a different kind of mistake (e.g. a plain arithmetic error, or misreading the question).
   - Answer **Not sure** if you genuinely can't tell either way — that's a completely valid answer. We'd much rather have an honest "not sure" than a guess.
4. Fill in your answers in the blanks below each item (just type over the underscores), and reply to this message with the completed document. No need to reformat anything.

Thank you again — this is genuinely useful data for the research, and we appreciate your time.

---

## Item 1

**Question**: Benki ya ukungu inaingia kutoka baharini kufunika mji.Inachukua dakika 75 kufunika kila maili 10 ya jiji.Walakini, tunajua kuwa kasi ya upepo itasimamishwa kwa saa moja.Ikiwa jiji ni maili 72 kutoka baharini hadi ukingo wa kando ya mashambani, itachukua dakika ngapi kwa Benki ya ukungu kufunika 1/4 ya jiji?

**Correct Answer**: 210

**Model's Attempt**:

> Benki ya ukungu inachukua dakika 75 kufunika kila maili 10.
> 
> Jiji ina hadi maili 72 kutoka baharini hadi ukingo wa kando ya mashambani.
> 
> Tu tukweni tukijua tukijifunza dakika itachukua kufunika 1/4 ya jiji.
> 
> 1/4 ya jiji=hadi maili 72/4=18
> 
> Ilichukua dakika 75 kufunika kila maili 10, kwa hivi, kwa maili moja itachukua dakika 75/10=7.5
> 
> Kwa maili 18, itachukua dakika 7.5*18=135 dakika.
> 
> Samahani kabla ya Benki ya ukungu kufunika ikiwa kasi ya upepo itasimamishwa kwa saa moja (60 dakika) na kwa hivyo 135 + 60 = 195 dakika.
> 
> Hii inatafsiriwa kuwa Benki ya ukungu itachukua 195 dakika kufunika 1/4 ya jiji.
> 
> Hence, my answer is 195 dakika.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 2

**Question**: Benki ya ukungu inaingia kutoka baharini kufunika mji.Inachukua dakika 60 kufunika kila maili 3 ya jiji.Walakini, tunajua kuwa kasi ya upepo itasimamishwa kwa saa moja.Ikiwa jiji ni maili 54 kutoka baharini hadi ukingo wa kando ya mashambani, itachukua dakika ngapi kwa Benki ya ukungu kufunika 1/3 ya jiji?

**Correct Answer**: 660

**Model's Attempt**:

> **Jibu: Haiwezekani — ukungu hautafunika 1/3 ya jiji.**
> 
> Maelezo:
> - Kasi ya ukungu: maili 3 kwa dakika 60, yaani maili 1 kila dakika 20.
> - 1/3 ya jiji (maili 54) = maili 18.
> - Lakini tunaambiwa upepo (unaosukuma ukungu) utasimama baada ya saa moja tu (dakika 60).
> - Katika dakika 60 hizo, kwa kasi hiyo, ukungu utakuwa umefunika maili 3 pekee (siyo maili 18 zinazohitajika kwa 1/3 ya jiji).
> - Kwa kuwa upepo unasimama kabisa baada ya hapo, ukungu hautasonga mbele tena — hivyo hautawahi kufika maili 18 zinazohakikisha 1/3 ya jiji imefunikwa.
> 
> Kwa hiyo, swali ni la "mtego": kwa masharti yaliyotolewa, **haitawezekana kamwe** kwa ukungu kufunika 1/3 ya jiji, kwani utasimama ukiwa umefunika maili 3 tu kati ya maili 18 zinazohitajika.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 3

**Question**: Benki ya ukungu inaingia kutoka baharini kufunika mji.Inachukua dakika 90 kufunika kila maili 3 ya jiji.Walakini, tunajua kuwa kasi ya upepo itasimamishwa kwa saa moja.Ikiwa mji ni maili 78 kutoka baharini hadi ukingo wa kando ya mashambani, itachukua dakika ngapi kwa Benki ya ukungu kufunika theluthi ya jiji?

**Correct Answer**: 1500

**Model's Attempt**:

>  The problem is given in Swahili, and it asks for the time taken by a water tank truck (Benki ya ukungu) to travel from the shore (baharini) to a certain village, which is 78 miles away from the shore and located inland (ukingo wa kando ya mashambani). The truck takes 90 minutes to cover 3 miles in the village area, but there is a wind (kasi ya upepo) that affects its speed.
> 
> To solve the problem, we first need to determine the speed of the water tank truck in the village area. The truck takes 90 minutes to cover 3 miles, so its speed is:
> 
> 3 miles / 90 minutes = 0.0333 miles per minute
> 
> Next, we need to find out how long it takes for the truck to travel 78 miles at this speed, while taking into account the effect of the wind. However, the problem does not provide enough information about the wind's speed or how it affects the truck's speed. Therefore, it is not possible to calculate the exact time without making additional assumptions.
> 
> If we assume that the wind does not affect the truck's speed, then the time it takes to travel 78 miles is:
> 
> 78 miles / 0.0333 miles per minute = 2340 minutes or 39 hours
> 
> However, if we assume that the wind reduces the truck's speed by a certain percentage, we can calculate the time it takes to travel 78 miles at the reduced speed. For example, if we assume that the wind reduces the truck's speed by 50%, then its speed in the village area is:
> 
> 0.0333 miles per minute / 2 = 0.0167 miles per minute
> 
> In this case, the time it takes to travel 78 miles is:
> 
> 78 miles / 0.0167 miles per minute = 4667 minutes or 77.75 hours
> 
> Therefore, the answer to the problem depends on the wind's speed and how it affects the truck's speed. If the wind does not affect the truck's speed, it takes 39 hours to travel 78 miles. If the wind reduces the truck's speed by 50%, it takes 77.75 hours to travel 78 miles. Other assumptions about the wind's speed and effect on the truck's speed will yield different answers.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 4

**Question**: Benki ya ukungu inaingia kutoka baharini kufunika mji.Inachukua dakika 90 kufunika kila maili 3 ya jiji.Walakini, tunajua kuwa kasi ya upepo itasimamishwa kwa saa moja.Ikiwa mji ni maili 78 kutoka baharini hadi ukingo wa kando ya mashambani, itachukua dakika ngapi kwa Benki ya ukungu kufunika theluthi ya jiji?

**Correct Answer**: 1500

**Model's Attempt**:

> Kwa kujua kwamba Benki ya ukungu inachukua dakika 90 kufunika kila maili 3, tunaweza kuarithmosha kwa hatua za kadri:
> 
> Hatua 1: Tuzingatia hadi kitufe cha 3 mile.
> Maili 3 = 90 dakika
> 
> Hatua 2: Tuhesabu kamili cha miles.
> Mji inapokuwa 78 miles kutoka baharini hadi ukingo wa kando ya mashambani, tuleta hatua za hatua 1.
> 78 / 3 = 26 hatua.
> 
> Hatua 3: Tuhesabu muda wa kila hatua.
> 26 * 90 dakika = 2340 dakika.
> 
> Hatua 4: Tunakusuburisha muda wa kasi ya upepo.
> Kasi ya upepo itasimamishwa kwa saa moja (60 dakika), kwa hivyo tuzingatia:
> 2340 dakika + 60 dakika = 2400 dakika
> 
> Hence, Benki ya ukungu itachukua 2400 dakika kufunika theluthi ya jiji.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 5

**Question**: Benki ya ukungu inaingia kutoka baharini kufunika mji.Inachukua dakika 30 kufunika kila maili 13 ya jiji.Walakini, tunajua kuwa kasi ya upepo itasimamishwa kwa saa moja.Ikiwa mji ni maili 78 kutoka baharini hadi ukingo wa kando ya mashambani, itachukua dakika ngapi kwa Benki ya ukungu kufunika 1/2 ya jiji?

**Correct Answer**: 120

**Model's Attempt**:

> Hebu tuchambue tatizo hili kwa hatua:
> 
> 1. Tunajua kwamba ukungu unachukua dakika 30 kufunika kila maili 13 za jiji.
> 
> 2. Jiji zima lina urefu wa maili 78 kutoka baharini hadi ukingo wa mashambani.
> 
> 3. Tunaombwa kupata muda wa kufunika **1/2** ya jiji, yaani maili 78 ÷ 2 = maili 39.
> 
> 4. Kasi ya ukungu:  
>    Kwa maili 13, inachukua dakika 30.  
>    Hivyo kwa maili 1, inachukua dakika 30 ÷ 13.
> 
> 5. Kwa maili 39:  
>    Muda = (30 ÷ 13) × 39  
>    = 30 × (39 ÷ 13)  
>    = 30 × 3  
>    = dakika 90.
> 
> 6. Lakini tatizo linasema "kasi ya upepo itasimamishwa kwa saa moja". Hii ina maana kwamba ukungu utasimama kabisa kwa muda wa saa 1 (dakika 60).  
>    Kwa hiyo, lazima tuongeze muda huo wa kusimama.
> 
> 7. Muda wa jumla = dakika 90 + dakika 60 = **dakika 150**.
> 
> **Jibu la mwisho:** Dakika 150.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 6

**Question**: Benki ya ukungu inaingia kutoka baharini kufunika mji.Inachukua dakika 15 kufunika kila maili 3 ya jiji.Walakini, tunajua kuwa kasi ya upepo itasimamishwa kwa saa moja.Ikiwa jiji ni maili 96 kutoka bahari ya mbele hadi kando kando ya mashambani, itachukua dakika ngapi kwa benki ya ukungu kufunika robo ya jiji?

**Correct Answer**: 180

**Model's Attempt**:

> Benji ya ukungu inaingia kufunika mji na 15 dakika za kila maili, ni maili 3 ja zio mile beauty. Si meso ni maili 96 kufukosa bahari ya mbele hadi kando kando ya mashambani.
> 
> Akyeto kama eyo lazima kupokewa kufunika robo ya jiji. Kama mile ya maili, tukwe na 96 minusile minusile 3, hii, ni maili 93 kufukosa bahari ya mbele hadi kando kando ya mashambani.
> 
> Olezarkia kama kuna 93 kufukosa naa bafuongo na kufunika robo ya jiji, hili thaliiitakukuta kufundisha dakika.
> 
> Polowoki zao yalianza ya kifundisha jiji 93 ja 15, cuma mile ya 108. Hadithukua bado benji ya ukungu, tukika kufundisha bado dakika.
> 
> Python kama sili 60 minuti kama bafuongo na dakika, katika 1 ora. Oleanzakuli zao kufundisha kufuta 1 ora, Benji ya ukangu ilijeho kufunika robo ya jiji 60 minuti.
> 
> Tukidakika esho viti 60 minuti, Benji ya ukangu iljeho kufunika robo ya jiji 1 ora.
> 
> Respond: 60 minuti

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 7

**Question**: Mbwa wa Oscar ana watoto wa mbwa 130, 28 kati yao wana matangazo.Mbwa wa Andre ana watoto wa mbwa 44, 14 kati yao wana matangazo.Jin ana mbwa 66, kila mmoja akiwa na watoto 11 na matangazo.Baada ya ziara ya daktari, Oscar aligundua kuwa nusu ya watoto wake ambao hawajapatikana kweli wana matangazo ambayo hayakuonekana hapo awali.Je! Ni asilimia ngapi ya watoto wa mbwa wote wana matangazo?

**Correct Answer**: 91

**Model's Attempt**:

>  Mbwa wa Oscar ana watoto wa mbwa 130, 28 kati yao wana matangazo. Mbwa wa Andre ana watoto wa mbwa 44, 14 kati yao wana matangazo. Jin ana mbwa 66, kila mja akiwa na watoto 11 na matangazo. Baada ya ziara ya daktari, Oscar aligundua kuwa nusu ya watoto wake ambao hawajapatikana kweli wana matangazo ambayo hayakuonekana hapo awali. Je! Ni ngapi ya watoto wa mbwa wote wana matangazo?
> 
> Ambayo kuna watoto wa mbwa wana matangazo, kuna 130 wa Oscar, 14/44 wa Andre, 11/66 ngapi uliopita, mwenyewe 11 matangazo wakijijualivyo wavuliwa katika jina ya Oscar na Andre. Kila watoto wa mwabao wengi hasahau kuwachungupya 1732/110 na matangazo (1732 mtu na matangazo kwa Oscar, 14/44 na matangazo Andre, 11/66 na matangazo juu ya jin). Ufikia tu uzaamini kubeba kwa matangazo waliowakubadilishwa kufanya wazazi kila watoto wa mwabao wengi wa mbwa kutoka kwa kukupeana kwa mwako.
> 
> Ni asilimia ngapi ya watoto wa mbwa wana matangazo ilipozaidisha 1732/110 mtu na matangazo.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 8

**Question**: Qasim inakusanya takataka kutoka kwa nyumba 5 tofauti za ghorofa.4 za kwanza zina vyumba 100 kila moja na ya mwisho ni 30% kubwa kuliko ile nyingine 4 pamoja.Walakini, wiki hii, vyumba 5 kutoka kwa kila moja ya vifaa 4 vya kwanza vilikuwa wazi na hazikuhitaji huduma ya ukusanyaji.Qasim hukusanya takataka mara 2 kwa wiki kutoka kila mahali na analipwa ₣ 0.3 kwa mkusanyiko kwa kila ghorofa.Yeye pia hupata 10% ya ziada katika vidokezo.Je! Yeye hufanya pesa ngapi kwa wiki?

**Correct Answer**: 594

**Model's Attempt**:

> **Suluhisho:**
> 
> - Nyumba 4 za kwanza: 100 × 4 = 400 vyumba
> - Nyumba ya 5: 30% kubwa kuliko hizo 4 pamoja → 400 × 1.3 = 520 vyumba
> 
> **Wiki hii (vyumba vinavyohitaji huduma):**
> - Kila moja ya nyumba 4 za kwanza ina vyumba 5 wazi → 100 − 5 = 95 vyumba kwa kila moja
> - Jumla ya nyumba 4 za kwanza: 95 × 4 = 380 vyumba
> - Nyumba ya 5 haijaathirika: 520 vyumba
> 
> **Jumla ya vyumba vinavyohudumiwa:** 380 + 520 = 900 vyumba
> 
> **Mapato ya msingi:**
> - Anakusanya mara 2 kwa wiki, analipwa ₣0.3 kwa kila mkusanyiko kwa kila chumba:
> 900 × 2 × 0.3 = ₣540
> 
> **Vidokezo (10% ya ziada):**
> 540 × 0.10 = ₣54
> 
> **Jumla ya pesa kwa wiki:**
> 540 + 54 = **₣594**
> 
> **Jibu:** Qasim hupata **₣594** kwa wiki.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 9

**Question**: Qasim inakusanya takataka kutoka kwa nyumba 5 tofauti za ghorofa.4 za kwanza zina vyumba 100 kila moja na ya mwisho ni 30% kubwa kuliko ile nyingine 4 pamoja.Walakini, wiki hii, vyumba 5 kutoka kwa kila moja ya vifaa 4 vya kwanza vilikuwa wazi na hazikuhitaji huduma ya ukusanyaji.Qasim hukusanya takataka mara 2 kwa wiki kutoka kila mahali na analipwa ₣ 0.3 kwa mkusanyiko kwa kila ghorofa.Yeye pia hupata 10% ya ziada katika vidokezo.Je! Yeye hufanya pesa ngapi kwa wiki?

**Correct Answer**: 594

**Model's Attempt**:

> Hebu tufanye hesabu hatua kwa hatua.
> 
> **1. Idadi ya vyumba katika jengo la 5:**
> 
> - Vyumba vya nyumba 4 za kwanza: \(4 \times 100 = 400\) vyumba.
> - Ya mwisho ni 30% kubwa kuliko nyingine 4 pamoja:
>   \(400 + (30\% \times 400) = 400 + 120 = 520\) vyumba.
> 
> **2. Jumla ya vyumba vyote:**  
> \(400 + 520 = 920\) vyumba.
> 
> **3. Wiki hii, vyumba 5 kutoka kwa kila moja ya nyumba 4 za kwanza havihitaji huduma:**
> 
> - Vyumba vinavyohitaji huduma kutoka nyumba 4 za kwanza: \(400 - (4 \times 5) = 400 - 20 = 380\) vyumba.
> - Nyumba ya 5 ina vyumba vyote 520 vinavyohitaji huduma.
> - Jumla ya vyumba vinavyohudumiwa wiki hii: \(380 + 520 = 900\) vyumba.
> 
> **4. Ukusanyaji mara 2 kwa wiki:**
> 
> - Mkusanyiko kwa wiki: \(900 \times 2 = 1800\) mkusanyiko.
> 
> **5. Malipo ya msingi:**
> 
> - Kwa kila mkusanyiko analipwa ₣ 0.3:  
>   \(1800 \times 0.3 = ₣ 540\).
> 
> **6. Nyongeza ya 10% kwa vidokezo:**
> 
> - Nyongeza: \(10\% \times 540 = ₣ 54\).
> 
> **7. Jumla ya pesa kwa wiki:**
> 
> - \(540 + 54 = ₣ 594\).
> 
> \[
> \boxed{594}
> \]

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 10

**Question**: Diego huchukua mananasi 67 Jumatano.Kisha huchukua mananasi 176 Alhamisi.Siku ya Ijumaa, anachagua idadi ya mananasi aliyofanya Jumatano.Siku ya Jumamosi, huchukua nusu ya kiasi cha kile alichochukua katika siku 3 zilizopita pamoja.Siku ya Jumapili, Diego atauza mananasi kwenye masanduku ya mananasi 17 kila moja.Atauza kila sanduku kwa $ 12.Je! Diego atatengeneza kiasi gani?

**Correct Answer**: 612

**Model's Attempt**:

> Tunafanya kazi kwa hatua:
> 
> **Jumatano:**  
> Alichukua mananasi 67.
> 
> **Alhamisi:**  
> Alichukua mananasi 176.
> 
> **Ijumaa:**  
> Anachagua idadi sawa na ya Jumatano, yaani 67.
> 
> **Jumamosi:**  
> Kiasi cha siku tatu zilizopita pamoja = 67 + 176 + 67 = 310.  
> Nusu ya hiyo = 310 ÷ 2 = 155.  
> Kwa hiyo Jumamosi alichukua mananasi 155.
> 
> **Jumapili:**  
> Jumla ya mananasi yote = 67 + 176 + 67 + 155 = 465.  
> Anapanga kwenye masanduku yenye mananasi 17 kila moja:  
> Idadi ya masanduku = 465 ÷ 17.  
> 17 × 27 = 459, salia 6. Kwa hiyo anapata masanduku 27 kamili (na labda mananasi 6 mabaki, lakini yanauzwa kwa masanduku kamili pekee).  
> Kila sanduku linauzwa kwa $12:  
> Mapato = 27 × 12 = $324.
> 
> **Jibu la mwisho:**  
> $324

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 11

**Question**: Diego huchukua mananasi 67 Jumatano.Kisha huchukua mananasi 176 Alhamisi.Siku ya Ijumaa, anachagua idadi ya mananasi aliyofanya Jumatano.Siku ya Jumamosi, huchukua nusu ya kiasi cha kile alichochukua katika siku 3 zilizopita pamoja.Siku ya Jumapili, Diego atauza mananasi kwenye masanduku ya mananasi 17 kila moja.Atauza kila sanduku kwa $ 12.Je! Diego atatengeneza kiasi gani?

**Correct Answer**: 612

**Model's Attempt**:

> Problem:
> Diego picked up bananas on Tuesday: 67
> On Thursday, he picked up bananas: 176
> On Saturday, Diego chose the number of bananas he had picked on Tuesday
> On Sunday, he picked half of the total number of bananas he had picked over the past three days
> On Monday, Diego put the bananas into boxes of 17 each.
> He sells each box for $12.
> How much money will Diego make?
> 
> Solution:
> First, let's find out how many bananas Diego picked on Saturday by choosing the same number as Tuesday: 67
> 
> Next, let's calculate the total number of bananas picked over the past three days (Tuesday, Thursday, and Saturday): 67 (Tuesday) + 176 (Thursday) + 67 (Saturday) = 310
> 
> On Sunday, Diego picked half of the total number of bananas from the past three days:
> 310 / 2 = 155
> 
> Now, let's find out the total number of bananas Diego has after picking on Sunday:
> 310 (total from past three days) + 155 (Sunday) = 465
> 
> On Monday, Diego puts the bananas into boxes of 17 each:
> 465 / 17 = 27 boxes with 5 bananas left over
> 
> Diego sells each box for $12, so:
> 27 boxes * $12/box = $324
> 
> Diego will make $324 from selling the bananas.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 12

**Question**: Daphne na Olivia ni dada kutoka Cairo ambao wanapenda kukusanya saini kutoka kwa nyota za sinema.Wakati wa mapumziko yao ya chemchemi kutoka shuleni, dada hutumia kila alasiri kukusanya saini.Baada ya wiki 3, Daphne na Olivia wanalinganisha vitabu vyao vya picha, kuhesabu idadi ya saini ambazo kila dada amekusanya.Daphne ana saini 17 katika kitabu chake, na Olivia ana 31. Dada wana wiki 3 zaidi za mapumziko ya chemchemi, na wanaamua wanataka kufikia saini 120 kati yao mwishoni mwa mapumziko.Walakini, wakati wa wiki 3 zilizobaki, Daphne ana uwezo wa kukusanya saini mwishoni mwa wiki, kupunguza mkusanyiko wake wa kila wiki na 5 kwa wiki, wakati Olivia anaamua kuongeza mkusanyiko wake wa wiki.Je! Olivia atahitaji kukusanya saini ngapi kwa wiki ili kuhakikisha kuwa wanafikia lengo lao?

**Correct Answer**: 19

**Model's Attempt**:

>  Daphne na Olivia ninafanyeki matheme kwa mawe tangu vichiji viongozi. Dada huwakati wa wiki 3 ana saini 120, mwenyewe na wiki 3 baada ya wiki 3 ana mpango kumkupatana kuwa mwezi wa uongo, na Daphne na Olivia ananishinda mkusanyiko wao kutoka wiki 1 kwa wiki. Kwenye mwaka ya wiki 3 zaidi ya kipindi cha mapumziko, Daphne na Olivia wanafikia mwishoni mwishoni mwaka wa mkusanyikoni. Baada ya wiki 3, Olivia ana uongozi ya kukusanya saini 31, kwa vizuri Daphne 17.
> 
> Nakufanya kuwa, wakati wa mapumziko ya chemchemi kutoka shuleni, dhambi ya wiki 1 zaidi na wiki 2 zaidi anawakata wakati wa kufurahi kwa kukusanya saini. Bado walipowekosha, huomuwakie tuko na mpango kutoa maelezo mapinduzi ya nusu za wakati wa wiki 1 zaidi na wiki 2 zaidi zake, kwa vizuri dhambi wiki 3 ana uwezo wa kukusanya saini 120, kufikia mkusanyiko wake, katika wiki ni wiki 1 kwa mkusanyikoni.
> 
> Olivia huwa walipowekosha kufikia lengo lao, kuwa kuanza wanaambuzi kukusanya saini 12 zaidi na muda mmoja, kupandekeza vizenzi zetu ya kwa mwishoni mwa wiki. Mzima daphne huwa walipowekosha kuwakumbuza mkusanyikoni za wiki 1 zaidi na wiki 2 zaidi zake, kutoka saini na kwa mwishoni moja, katika mawe tatu ya nusu tayari nayo.
> 
> Nikujipo tangu huwa, baada ya tupu, walimu hatua nini ni kuishi na kutoka kwa nusu. Baada ya kipindi cha mapumziko na mahali, baadaye walipowekosha kukusanya lume la vikundi, ni ndani ya wiki 3 zaidi.
> 
> Imaraha, Olivia ana vyuo vya kukusanya saini 31, Daphne ana 17, walikufumu mambo ya kuchukuli mwishoni. Kwenye mwihogo wenyewe, kukukusanywa mwishoni mwishoni 31 kwa Daphne na 17 kwa Daphne na Olivia kwa kutumia tayari tayari zinazingine za waako, na baada ya wiki 3 katika maendekeo, walijua wengine walipowekosha kuwakumbuza lume la mwishoni moja katika mwishoni mwishoni. Kama huwekwa hata saini 120, hawa ni mtu mno amekufanya kwa hivi. Mwenyuwe walikufanya kwenye mwihogo tauti hukuangalia, hukufanya kuwakata vimbo vya haki yake kwa umechukuli mwishoni ili kupa hawa wakati hayo. Maikuzio wanazidi kwa mapinduzi ya sinai zake.
> 
> Je! Olivia ana vile lupofikia saini 31 kwa wiki ili kuhakikisha kulipindula hawa wakati wa uwezo.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 13

**Question**: Katika darasa la Bi Johnson la wanafunzi 100, 46% ya darasa ni wachezaji wa mpira wa miguu.Kati ya darasa lililobaki, 50% ya wanafunzi ni washiriki wa kilabu cha roboti au sehemu ya wachezaji.Vikundi hivi 3 vya wanafunzi vitahitaji kuondoka mapema leo kusafiri kwenda kwenye mashindano ya mbali.Nusu ya wachezaji wa soka hawapo kwa kuwa mgonjwa.Pia, cheerleaders 3 wataandamana na kila moja ya vikundi hivi.Je! Ni wanafunzi wangapi wanaondoka mapema kwenye mashindano?

**Correct Answer**: 59

**Model's Attempt**:

> Wanafunzi 100 katika darasa la Bi Johnson.
> 
> Wachezaji wa mpira wa miguu ni 46% ya 100 = 52.
> 
> Darasa lililobaki ni 100 - 52 = 48 wanafunzi.
> 
> 50% ya 48 ni washiriki wa kilabu cha roboti au sehemu ya wachezaji.
> 
> Hii ni 24 wanafunzi.
> 
> 3 vikundi hivi vitahitaji kuondoka mapema leo kusafiri kwenda kwenye mashindano ya mbali.
> 
> Nusu ya wachezaji wa soka hawapo, kwa hiyo nusu 52 ni 26 wanafunzi.
> 
> Pia cheerleaders 3 wataandamana na kila moja ya vikundi hivi, totalizing 3 cheerleaders * 3 vikundi = 9 cheerleaders.
> 
> Kwa hivyo, wanafunzi 24 (Robot club na cheezaji) + 26 (hawana mcheza soka) + 9 (cheerleaders) = 59 wanafunzi wanaondoka mapema leo.
> 
> Hence, 59 wanafunzi wanaondoka mapema leo kwenye mashindano.

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---

## Item 14

**Question**: Katika darasa la Bi Johnson la wanafunzi 150, 40% ya darasa ni wachezaji wa mpira wa miguu.Kati ya darasa lililobaki, 30% ya wanafunzi ni wachezaji au sehemu ya washiriki wa kwaya.Vikundi hivi 3 vya wanafunzi vitahitaji kuondoka mapema leo kusafiri kwenda kwenye mashindano ya mbali.Nusu ya wachezaji wa soka hawapo kwa kuwa mgonjwa.Pia, cheerleaders 3 wataandamana na kila moja ya vikundi hivi.Je! Ni wanafunzi wangapi wanaondoka mapema kwenye mashindano?

**Correct Answer**: 66

**Model's Attempt**:

> 
> 
> **Swahili solutions:**
> 
> 1. **Katika darasa la Bi Johnson la wanafunzi 150, 40% ya darasa ni wachezaji wa mpira wa miguu.**  
>    - Uchendwa: 40% ya 150 wanafunzi ni wachezaji.  
>      \[
>      0.4 \times 150 = 60
>      \]
>    - **Wachezaji wa mpira wa miguu = 60** wanaudiombani.
> 
> 2. **Kati ya darasa lililobaki, 30% ya wanafunzi ni wachezaji au sehemu ya washiriki wa kwaya.**  
>    - Uchendwa: 30% ya 150 wanafunzi ni wanaoacha darasa (wachezaji au sehemu).  
>      \[
>      0.3 \times 150 = 45
>      \]
>    - **Wanaoacha darasa = 45** wa wachezaji au sehemu.
> 
> 3. **Vikundi hivi 3 vya wanafunzi vitahitaji kuondoka mapema leo kusafiri kwenda kwenye mashindano ya mbali.**  
>    - Uchendwa: 3 wanafunzi vitahitaji kuondoka.  
>    - **Wanaondoka = 3** wa vikundi.
> 
> 4. **Nusu ya wachezaji wa soka hawapo kwa kuwa mgonjwa. Pia, cheerleaders 3 wataandamana na kila moja ya vikundi hivi.**  
>    - Uchendwa: 60 wachezaji wa mpira wa miguu, daripipi 3 wanaoacha darasa na 3 wakilishi, ni 66 wanasiambulizi.  
>    - **Wanaoacha soka na mgonjwa = 66**
> 
> 5. **Je! Ni wanafunziwangapi wanaondoka kwenye mashindano?**  
>    - Uchendwa: Wasafu wa wanafunzi wa kati wanaoacha kwenye mashindano ni:  
>      \[
>      150 \text{ (total)} - 66 \text{ (wanaoacha)} = 84
>      \]
>    
> **Jinsi ni wanafunzi wangapi wanaondoka kwenye mashindano?**
> 
> \boxed{84}

**Your assessment**:
- Is the model's final answer correct? (Yes / No): _____
- If No — did the model notice a key detail but then drop it or misuse it? (Yes / No / Not sure): _____
- Any comments (optional): _____

---
