# Phase 2: checker's blind marks against the first agent's transcription and lists (ff. 30v lines 1-14, 30r lines 1-6)

Files: `phase1_passA.txt`, `phase1_passB.txt`, `phase1_marks_f30.txt` (blind; checksums in `phase1_sha.txt`),
`phase2_units.tsv` (one row for each unit), `work/compare.py` (the script that made the numbers).
Not blind: 15 units (f. 30v line 11 units 1-4, line 12 units 1-11), because `sheets/marks.jpg` prints their captions.

## (a) Figures

- Units aligned: 345 (330 blind). Same figure: 332 of 345 = 96%.
- The first agent's file has no entry for 7 units at the end of the last clear line of f. 30r (my L00):
  `82^. 65^._. 63^. 68= 61 82^. 89=`. By the lists: "di molto(M 65) cosa(C 63) ma(PT 68) [61] di [89=]".
- The 13 differences, after a 4x zoom (this zoom is NOT blind):

| place | checker | first agent | what the zoom shows |
|---|---|---|---|
| 30v L1, L2, L4; 30r L1 | (15) | (25) | first agent is right: the 2 of (25) differs from the 1 of (15) in lines 5 and 7. My error, 4 units |
| 30v L2 | 49^: | 89d | figure 89 is more likely (first agent). The mark is two dots, one above each digit |
| 30v L1 | (35) | (38) | I see (35) = lui; not settled |
| 30v L1, L7 | 95= | 93= | not settled in lines 1 and 7; the same word in line 24 is a clear 95 with two bars |
| 30v L12 (twice) | 98_v | 99v | second digit is an 8 with two loops: 98, caron. Gives "{quanto} a interesse ... et {quanto} a riputatione" |
| 30r L1 | 34^. | 39? | 34 with a dot above |
| 30r L3 | 62= | 52= | 62 |
| 30r L6 | 84 (dot above?) | 89 | second digit is a 4 |

- Two units where both of us wrote 13 and the zoom shows 12: f. 30v L4 `12^._-` (dot above, bar below) and f. 30r L5 `12_-`.
  Both stand before "fede" and "SEDE". This supports the interpolation S 12 = {santo}.

## (b) Marks as seen on the page (units with the same figure)

- Same mark: 273 of 332 = 82%. Blind units only: 260 of 319 = 82%. Units where I had no doubt: 261 of 309 = 84%.
- The 59 differences by kind (first agent -> checker):
  - 12 x no mark -> dot above. 9 of them are 69 "da" (the first agent says the same in NOTES section 22).
  - 10 x bar below -> two bars (74, 79, 71, 29, 31, 30, 56 twice, 75, 89).
  - 3 x two dots above -> one dot above (41, 53, 46); 82 in L4 I gave as doubt.
  - 3 x caron -> circumflex and caron (76, 81 twice).
  - 2 x no mark -> circumflex (59 in L11; 94 in L1 where the first agent wrote an arc).
  - about 8 x a dot on a figure with a 1 (10, 12, 13, 41, 51, 91): cannot be decided on this film.
  - the rest: single cases (87 dot below -> bar above and dot below; 86 two bars -> bar above and dot below; 59 none -> two dots below; ...).
- I saw no verb arc in these 20 lines. The first agent has an arc on 94 (L1), 64 (L13), 14 (L14); I see a circumflex, two bars, two bars.

## (c) Does my mark name the list that the first agent used?

"List used" = the list from which `lst.py` took the word for the first agent's token. "glossed" = the token's own mark names
that list and the value has a gloss. "by order" = the value is interpolated, or `lst.py` took it from a neighbour list
(its "*" values). Strict = my first choice only; the dot of a figure 1 is not counted. Lenient = my second choice or the
dot of the 1 is allowed. Mark "dot above and dot below" is counted as list M (the first agent does the same).

| list | mark | all units strict | all lenient | glossed strict | by order strict | by order lenient |
|---|---|---|---|---|---|---|
| A | none | 12/12 | 12/12 | 10/10 | 2/2 | 2/2 |
| C | dot above | 58/64 | 59/64 | 43/46 | 15/18 | 15/18 |
| E | two dots above | 2/10 | 4/10 | 1/1 | 1/9 | 3/9 |
| G | two dots below | 22/22 | 22/22 | 20/20 | 2/2 | 2/2 |
| I | bar below | 4/12 | 4/12 | 1/3 | 3/9 | 3/9 |
| M | dot below (seen: dot above and dot below) | 6/7 | 6/7 | 5/5 | 1/2 | 1/2 |
| O | circumflex | 6/9 | 6/9 | - | 6/9 | 6/9 |
| P | caron | 12/15 | 12/15 | 10/13 | 2/2 | 2/2 |
| Q | circumflex and caron | 8/8 | 8/8 | 8/8 | - | - |
| S | dot above and bar below | 5/11 | 9/11 | 2/3 | 3/8 | 6/8 |
| T | bar above and dot below | 11/11 | 11/11 | 8/8 | 3/3 | 3/3 |
| PT | two bars | 54/64 | 54/64 | 47/55 | 7/9 | 7/9 |
| BR | round brackets | 45/45 | 45/45 | 44/44 | 1/1 | 1/1 |
| N | bar above | 7/7 | 7/7 | 5/5 | 2/2 | 2/2 |
| **all** | | **252/297 = 85%** | 259/297 = 87% | 204/221 = 92% | **48/76 = 63%** | 53/76 = 70% |

So: for the units that the first agent placed by alphabetical order, my blind mark names the same list in 63% of the
cases (70% with the lenient rule). For glossed units it is 92%.

## (d) Units where my mark names another list

Column "word in my list": a glossed or interpolated value that the tables already hold for that figure in my list.
Column "candidate": MY inference, a word inside the window of my list that fits the sentence. A candidate is not a reading.

| place | checker | first agent (list, word) | my list | word in my list | candidate and note |
|---|---|---|---|---|---|
| 30v L9 | 87^-_. | 87b, M {necessario} | T | volontà/volontieri (glossed) | "lui VEDREBE volontieri che V.E. FACESSE ..." Zoom confirms bar above |
| 30v L9 | 76^^_v | 76v, P promettere | Q | risolutione (glossed) | "FACESSE risolutione di APPOGGIARSI" |
| 30v L11 | 59^^ | 59, C corrivo* | O | {parola} | "queste parole" (the reading file already says so) |
| 30v L8 | 59_: | 59, C corrivo* | G | honore (glossed) | "di honore" |
| 30v L10 | 86^-_. | 86=, PT {però} | T | - | window 67 vero .. 87 volontà (u = v): "un". Zoom confirms |
| 30v L10 | 51 dot below | 51d, C contrario | M | - | window 46 .. 54 mio: "ministro". Together: "quanto PUÒ PROMETTERE un ministro senza {ordine} di suo {Signore}" |
| 30v L12 | 29^._. | 29d, C con | M | - | window 10 male .. 33 medesimo: "mano": "essere in mano di {tale} che ..." (but see M 21 in line 22) |
| 30v L2, L4; 30r L4; (L19, L21) | 74= | 74_ / 74=, I Lega* | PT | - | window 72 manco .. 75 ne: "molto" ("non MI FERMO molto"). Not "Lega" |
| 30v L4 (L21) | 90= | 90=, I {lungo}* | PT | - | window 87 più .. 97 qualche: poi / pure. In L1 `90_-` has one bar: {lungo} can stay there |
| 30r L5 | 45= | 45=, I intentione* | PT | - | window 44 fino .. 46 {forse}: "finché" |
| 30r L6 | 71= | 71_, I laudare | PT | - | window 68 ma .. 72 manco: "maggiormente" / "mai" |
| 30r L1 | 79= | 79_, I lettera | PT | - | window 77 nondimeno .. 82 o vero; open |
| 30v L1; 30r L2, L4, L6 | 63_- | 63_, PT la | I | - | bar below only, 4 times of 4 here (and 4 more in lines 20-23). "la" fits list I by order (45 intentione < la < 71 laudare). Sense unchanged |
| 30v L8; 30r L4 (twice) | 68_- | 68_, PT ma | I | - | bar below only. Window 63 la .. 71 laudare: "la quale" (as G 67 il, G 68 il quale). "ma" = 68 with two bars (30r L00) |
| 30v L1 | 68 bar below, dot? | 68_b, PT ma | I or S | S: {singolarmente} | zoom: a dot between the digits, so S. Agrees with the reading file |
| 30v L7; L8, 30r L1 | 32_v; 61_v | 32v, O {ordine}*; 61v, O {passo}* | P | - | both of us see a caron. P 61, window 52 pretesto .. 76 promettere: "principalmente" ("CAGIONATA principalmente da ..."). P 32 open |
| 30r L1, L4 | 81^^_v | 81v, P proposta | Q | - | window 78 rispetto .. 88 rotta; an adjective ("ERANO [81] et [52]"); not "proposta" |
| 30r L1, L4 | 52^. | 52d, E {esaltatione}* | C | - | both of us see one dot. Window 51 contrario .. 53 convenire. Not "esaltatione" |
| 30r L5 | 66^. | 66, E età* | C | - | window 64 credere .. 69 da; open ("qualche [66] HEROICA") |
| 30r L1 | 32^._- | 32_, PT {così}* | S | - | window 30 scritto .. 34 segno; open |
| 30r L4 | 79^._- | 79_d, I lettera* | S | - | both see dot and bar. Window 68 .. 91 stato; open |
| 30v L14 | 46^. | 46dd, E {espediente} | C | - | I see one tick; the first agent says it rechecked two dots. Open |
| 30v L7 | 53^. | 53dd, E {errore} | C | convenire | pass A had two dots as second choice. Open |
| 30v L3 | 41 with dots | 41dd, E {efficacia} | A or E | altro | zoom: one dot over each digit. E is possible |
| 30v L4 | 82^. or 82^: | 82dd, E {fede} | C or E | di | zoom: two dots. E stands |
| 30v L8 | 73 | 73, E fallire* (reading: Umena) | A | - | plain. The plain series seems to hold names after 72 (73 Umena, 75 Savoia, 78 S. Duca) |
| 30v L10 | 42_- | 42_, S servitio* | I | - | no dot here; dot present in L4 and 30r L5. Scribe's slip or another word |
| 30v L2, L4, L12, L13; 30r L4, L5 | 13, 12, 91 with the dot of the 1 | S or C | - | - | dotted-1 cases; they agree if the dot counts |
| 30v L4 | 48 | 48, C {contento}* | A | - | part of the group `40 48 08`; see below |

Other things seen:
- `40 48 08` (L4), `30 36 06` (L19) and `90 92 02` (L15) have one pattern: a0, ab, 0b. All stand where a sentence ends.
  They look like null groups or stops. They are not words of the lists.
- List M on these pages is written with a dot above AND a dot below (33 medesimo 4 times, 73 mostrare twice, 65, 29, 41, 44, 46, 72).
  A single dot below without a 1 in the figure I saw only together with a bar above (list T).
- `lst.py` lets I, PT and S replace each other, and (A, C, E), (G, M), (O, P, Q), (T, N). That is where "list by order,
  not by mark" enters the decode. Most of the wrong words above come from this fallback.

## Verdict on "the mark names the list"

The claim survives, and it is stronger when the marks are read strictly.
- Well supported by blind marks: BR (45/45), G (22/22), T (11/11), Q (8/8), N (7/7), A (12/12), C (58/64), PT with two bars (54/64), M (6/7, with the mark "dot above and below").
- Not supported as the first agent assigned them:
  - E (two dots above): 2/10 strict. Of 9 units placed by order, the zoom confirms 2 ({efficacia} 41, {fede} 82), leaves 2 open
    ({errore} 53, {espediente} 46) and rejects 5 (52 twice, 66, 73: one dot or no dot).
  - I (bar below): 4/12. The units 74, 45, 90 (L4), 71, 79 that it gave to I have two bars (list PT). In return 63 "la" and 68 have one bar (list I).
  - O for 32 and 61 with a caron (they are list P). O itself (circumflex) is fine: 94 {persona}, 20 {officio}, 21 {ogni}, 32 {ordine} in L11, 59 {parola}.
  - S: 5/11 strict, 9/11 lenient. The doubt is only the dot of the figure 1.
- Where my mark and the first agent's list differ, my list gives a glossed word or a window word that fits the sentence in
  at least 8 places (volontieri, risolutione, honore, parole, un ministro, molto, finché, principalmente). In 3 places the sense
  favours the first agent's list against my strict mark (42 in L10, 12 in 30r L5, 46 in L14); each is a missing or doubtful dot.
  This is evidence for the rule, and against the fallback.
- Limits: a dot above a figure with a 1; one dot against two dots above; my own figure errors ((25) four times).
