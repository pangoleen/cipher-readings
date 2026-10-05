# The "Garbino" cipher of 1528 (BnF fr. 3022 no. 20; fr. 2988 ff. 2, 9; fr. 3019 f. 73)

Work of 5 October 2026. Status: **not read**. The owner of the cipher is found. The structure is found. About 25 values are probable.

## 1. Result of the crib hunt

**The cipher belongs to Martino Centurione, the Genoese envoy at the court of Charles V, and his son Girolamo (Hieronimo) in Genoa. "Garbino" is a cover name, not a person.**

Evidence:

1. Molini, *Documenti di storia italiana* ii (Florence 1837), no. CLXIV, pp. 3-10, prints a clear letter of Martino Centurione to his son, Burgos, 16-17 January 1528. Its source is "Vol. 8547 a c. 58" = BnF fr. 3022 f. 58 (catalogue item 26). OCR text: `cribhunt/molini_documentidistor03.txt`, lines 423-790 (archive.org `documentidistor03moligoog`).
   - Old docket: "... Ieronimo Centurione di Genova havere in cifra da posser scrivere le novelle in corte di Cesare ... le lettere sono a nome del Garbino ...".
   - Postscript: "... l'altra scripta in zifra in nome del Garbino de Luca ali x ...".
   - Postscript: "Poi che vedo havere tu receputo el zifra mandato per via de Roma del quale hay usato ti scrivo con esso / et a la l[itte]ra r agiongeraili recevut. r336 et receu. r337 / & a la l[itte]ra G garbino g215".
2. I read this last passage on the page image (Gallica btv1b90601558 view 116; crop `img/fr3022_v116_keyvalues_crop.jpg`). The three values are the same as in the "Aditione nel zifra" (f. 50, view 97): r336 recevut., r337 receu., g215 Garbino.
3. The hand of f. 58 is the hand of no. 20 and of the addition sheet (my comparison at reduced size; one pass).
4. The same formulas: January "Altro non mi accade che dire al presente" and "del seguente me avisarai"; no. 20 "Altro non mi accade che dire al presente" and "& del seguente farete avisato".
5. The cover-name list (ff. 48-49, views 94-95) has "Jacobo Centurione", "Stephano Centurione", "Julian de la Speza", "Ansaldo Grimaldo", "Bartholomeo Lomelino", "Secretario Perez". The January letter names the same persons.
6. Address of no. 20 (f. 47v, view 93): "R.do d. ... garbino" and "Luca" (Lucca; others read "Lura/Luna"). The leaf fr. 2988 f. 11v (btv1b9059908w view 22) has the same address, "Luca" and "tripta". So the letters signed "V.o Hieronimo Ranzo" went to the same cover address. Who wrote them is open (Ranzo himself, or a cover signature). They are marked "dup." and "tripta": copies sent by different routes, as the January letter orders.

Consequences: no. 20 (Madrid, 11 April 1528, postscript 19 April) is a letter of Martino Centurione to his son under cover. It is not a report of a Venetian agent, and "Hieronimo Ranzo to Garbino" is not proved. The French held Genoa and took the mail.

Not found: a decipherment or a clear copy of any cipher passage. Searched with no hit: Sanuto vols 44-49 (OCR tested), Bornate (Misc. st. it. 48), Gattinara's testament (Misc. 18), AS Vercelli inventory, CSP Spain iii.2, Salinas letters, the printed catalogue of fr. 2988, 3019, 3022 (no "déchiffrement" for these items). Others searched before us: CSP Venice iii-iv, Lanz i, Sanuto 43 (cipher-lab). Not reached: ASGe Lettere ministri Spagna 2410, Simancas, Clair. 327 and 314 (Bourdeau: no decipherment). Details: `cribhunt/cribhunt_notes.txt`.

## 2. Prior art (checked 5 October 2026)

- S. Tomokiyo, unsolved.htm and venetian.htm (local copies of 5 Oct): unsolved; "probably a report of a Venetian agent"; base letter = initial; a1-a326 then additions. ai.htm (5 Oct): "probably an alphabetical code".
- D. Bourdeau, `targets/vasto1527/NOTES.md`, commit a439937 (3 Oct 2026), write-up vasto1527.html: full transcription (no. 20: 1,315 groups; Ranzo: about 2,600); writer "almost certainly Hieronimo Ranzo"; numbering "not alphabetical" (z = -0.5); word annealer 46 % tokens on a control; stopped for lack of key or crib.
- NoAutopilot/cipher-lab, `ciphers/fr3022-garbino-1528` and `fr2988-ranzo-1520s`, commit 69238c1 (5 Oct 2026 08:09 UTC): edition checks, the clear postscript of f. 47r, the duplicate fr. 3019 no. 27; status open.
- None of these pages has the name Centurione. Two web searches ("Garbino" "Centurione" cipher; "Martino Centurione" cipher "fr. 3022") gave no link. The clear letter itself is in print since 1837: we **reproduce** Molini; the link to the unsolved cipher is new as far as we checked.

## 3. The system

- Group = base letter + superscript number. The base letter is the first letter of the value (u and v one letter; j = i).
- List lengths before the additions, from the addition sheet (read on view 97-98): a 326, b 156, c 326, d 307, e 217, f 227, g 214, h 105, i 321, l 144, m 269, o 176, p 399, r 335, s 393, t 196, v 250, x 19, z 35. No additions for n and q (lengths not known; about 150 and 80).
- The additions are full words, stems with a point ("defens.", "ingrat.") and endings (are, ato, ano, ere, one, rano). So the base list did not have "cosa", "certo", "stato", "suo", "fare", "havendo". The text uses many syllables and endings. This is why a word-for-group attack fails.
- **The numbers from 10 upward run in alphabetical order.** Test (`work/test_order.py`, `test_order2.py`): the frequency profile of the numbers, in number order, is aligned with the frequency profile of Italian units in alphabetical order. The alignment keeps the order and ignores the spacing. Null: the numbers shuffled inside each letter, 2,000 times.
  - all groups: z = 4.1, rank 1 of 2,001;
  - no. 20 alone: z = 4.5, rank 1 of 2,001; Ranzo letters alone: z = 3.9, rank 1 of 2,001;
  - numbers from 13 upward, first reference unit removed: z = 3.0, rank 1 of 2,001;
  - controls: a synthetic alphabetical code z = 6.8 and 7.5; the same code shuffled z = 0.0 and -0.8.
  - Bourdeau's test used ten fixed bins and a list of words only. A binned test of that type gives z = 1.7 on the real text here (`test_alpha.py`). The spacing of the real list is not the spacing of a modern word list.
- Numbers next to each other are often homophones: d34, d35, d36, d37 all stand before "la, le, li, soa" (107 tokens). 
- Numbers 6 to 9 of one letter are one value with four signs (the number 8 is the most used for every letter). These values attach to a neighbour group: m6-m10 after a209, s116, s323, s346, f12, a104; n6-n9 after t10, r10, e67, a62, a84; s6-s9 after p308 (9 of 9); h7-h9 before d246, d245, t74, t30.
- z6-z9 and z15 (191 tokens) are most probably nulls or stops. The lists "y" (113 tokens, numbers 2-53) and "Q" (35 tokens) are not explained.

## 4. Probable values (grade: context and position agree; none has an outside proof)

| group | value | ground |
|---|---|---|
| c170 | che | 109 tokens |
| p149, p153 | per, pero | "non ho [p153] voluto" |
| h10, h57 | ha, ho | before v205 l130 t89 |
| v205 l130 t89 | vo-lu-to | 4 times after h57 or h10 |
| n89 (n90) | non | before "ho pero voluto", "ha voluto" |
| i100, i295 | in, Italia | "i100 i295" 4 times |
| l10, l47, l77 | la, le, li | after d34-d37 |
| d34-d37 | de | before la, le, li, soa |
| d78 | del | "d78 p308 s7" then clear "& del seguente farete avisato" |
| a127 | al | "a127 p308 s*" 5 times |
| p308 + s6-s9 | presente (?) | "al / del / la presente"; the part of s6-s9 is not clear |
| t89, t10, t30, t74 | to, ta, te, ti (?) | endings; order |
| r41 | re (?) | 79 tokens |
| m6-m10 | -mente (?) | after stems, before function words |
| d246 | -do (?) | after h7-h9 (havendo?), e49, f75 |

Order check on the values that the context gives (ha/ho; per/pero/pre-; la/le/li/lu; de/del/do; in/Italia): 14 pairs inside one letter, 14 in alphabetical order. The identification was not blind to the position, so the formal control is the test of section 3.

## 5. The attempt to read, and why it stays closed

- `work/solver.py`: every group gets a string with the right first letter; the order inside a letter is kept alphabetical; a 5-gram letter model (Sanuto vols 44-49 and the January letter) scores the text.
- Matched control (`work/control.py`): the January letter of Centurione, put into a synthetic alphabetical code (3,900 tokens, 772 types). The solver gets 51-56 % of the tokens (63-71 % of the types with 10 or more tokens, 5-7 % of the types that occur once). Without the order constraint: 31 %. On a shuffled code: 27 %.
- Real text: the output is a skeleton of small words (`work/machine_proposals_NOT_A_READING_s*.json`). The score is -2.5 for each letter; the control gets -2.2. A second order test with the letter model is not conclusive (z = 1.0, rank 16 of 101; `test_lm_order.py`).
- Reason: about 950 types in 3,900 tokens, half of them seen once; the real list has stems, endings and homophones that the model does not know; no clear text for any cipher passage.

## 6. Transcription

No new transcription. All counts use D. Bourdeau's files (URL and commit in `prior/get_prior.sh`; not copied, the repository has no licence file). I checked two lines of f. 44r and the last cipher line of f. 44v on the images. Known faults: "t41" for r41 in three Ranzo pages; "g" for "s" above g222; cipher-lab measured 3.5 % errors on two pages.

## 7. What would open it

1. The cipher letter that Girolamo wrote "in nome del Garbino de Luca" on 10 December 1527, or the father's cipher letters of January 1528, with a decipherment: Archivio di Stato di Genova (Archivio segreto, Lettere ministri Spagna 2410; Centurione papers), or Simancas if the son's letters reached the court.
2. The base table "mandato per via de Roma" (autumn 1527).
3. A second full transcription with measured agreement; then a human pass with the alphabetical windows. The clear parts of no. 20 and the January letter give the writer's words.
4. Fr. 3019 no. 36 (f. 94, "Reporto de homo venuto da Genova", in cipher): not looked at.

## Files

- `cribhunt/`: notes and downloaded texts (Molini, Sanuto 44-49, Bornate, catalogue, CSP Spain, Salinas).
- `img/`: Gallica images. fr. 3022 (btv1b90601558) views 86-99 full size, 100-123 at 1000 px; fr. 2988 (btv1b9059908w) views 6-9, 17, 20-22 at 1500 px.
- `work/`: scripts and control outputs. Set `BD_N20` or run `prior/get_prior.sh` first. The scripts build caches (`lex.pkl`, `lm_*.npy`) on the first run.
- `reading.md`: the few phrases, with marks.
