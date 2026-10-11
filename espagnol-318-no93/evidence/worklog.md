# BnF Espagnol 318 no. 93 (f. 118): work log

First version: 9 October 2026. Corrected on 11 October 2026, after the audit ([audit.md](audit.md)).
"I" in this log is the model that did the work.

## Result

- **The letter reads.** The key is rebuilt from the letter itself: 55 sign types for 24 letters and "ll", and
  64 of 72 code words.
- **Wording: first reading known to us; key rebuilt from the letter; no period decipherment found (searches
  listed).** The Spanish court read this letter in 1504. So the claim is about a reading that is known today.
- **Counts: 91.0 % firm, 97.3 % with the probable values** (1,094 and 1,170 of 1,202 tokens).
- **It is not in the cipher of no. 94** (the neighbour letter, [../../espagnol-318](../../espagnol-318/)). The
  two keys have the same build and share seven signs. The code words are different.
- **The year 1504 is proved by the content.** Sanuto dates the Pope's brief and the news of the truce to
  22-23 February 1504.

## The page images

- Gallica view 446 = **f. 118 recto**. I saw the folio number in the top right corner: "116" struck out, "118"
  beside it, in red ink.
- Gallica view 447 = **f. 118 verso**. It ends with the clear words "de Venecia xx iiii de febrero". Below is a
  later note and a paraph. The page has no address and no signature.
- The two frames were on disk from the work on no. 94 (4 October 2026). Views 452 to 455 are no. 94.

## What the letter is

| Point | Value | Source |
|---|---|---|
| Place and day | Venice, 24 February | Seen: clear text at the end of f. 118v |
| Year | 1504 | The catalogue (Morel-Fatio 1892, p. 62-63); proved by the content (Sanuto) |
| Writer | Lorenzo Suárez (de Figueroa), Spanish ambassador at Venice | The catalogue. The page has no signature. Sanuto has "l'orator yspano" in the College on 23 and 26 February with the same matter |
| Addressee | Ferdinand and Isabella | The catalogue. The text speaks to "V. Al." (a code word of grade B) |
| Hand | One cipher clerk; not the hand of no. 94 | Seen |
| Cipher lines | 33 on the recto, 17 on the verso = 50 | Seen |
| Clear text | Only the date clause | Seen |

## The two transcription passes

- I cut a strip for each line (three tiles, each tile follows the slope of the line).
- The signs are not those of no. 94. I made a new list of sign names: `transcription/SIGNS.md`. The file is the
  instruction sheet that the blind agents got.
- Pass A: by me, all 50 lines.
- Pass B: three blind agents (recto 1-17, recto 18-33, verso). Each agent had the sign list and the strips only.
- Settled text: `transcription/f118r_final.txt`, `transcription/f118v_final.txt`. I settled each difference on an
  enlarged crop.

| Measure (`agree.py`) | f. 118r | f. 118v |
|---|---|---|
| Tokens that agree | 857 of 891 = 96.2 % | 380 of 406 = 93.6 % |
| Cipher signs | 682 of 689 = 99.0 % | 299 of 307 = 97.4 % |
| Code words | 175 of 202 = 86.6 % | 81 of 99 = 81.8 % |
| Decoded characters that agree | 89.0 % | 85.6 % |

Main differences: `pie` against `pie~` (23 times: pass B saw a stroke over the word; both have the value "que");
`III` against `m`; the last letter of rare code words (ris / rus / rig, fam / fau, rer / ren).

Changes after the passes, all on the image:

- `m 4` is one sign (`m4` = g).
- Four signs were split from others: `tf` (a short "t" joined to a long s = s), `#3` (three strokes with a bar
  and no hook = o), `gib` (not `gab`), and `E` (an "e" with a long tail, once).
- `ris gue` in r03 is `ris gue~`. The `qp` in r09 is `pq`. The boxed sign in r13 is a deletion.
- `lo` is a code word, not a sign.

## Is it the cipher of no. 94? No.

I mapped each sign of no. 93 to the sign of no. 94 with the same shape (27 pairs), and applied the key of no. 94
as it is.

- Result: no Spanish. The score was -17.6 for each group of five letters. Shuffled Spanish scores -17.8.
- Code words: no. 93 has 72 spellings, no. 94 has 100. Only 7 spellings are in both (mae, mul, muy, myl, pet,
  pif, pot). Where both have a value, the values differ: pet = para in no. 94 and si in no. 93; pif = no and
  qual. The common words differ: que = raz and pie; de = muy and gad; no = pif and mat; en = mys and heg.
- The group "otto" is c in no. 94 and n in no. 93 (tienen, años, manifyesta, Sesena).
- Seven signs have the same shape and the same letter in both keys: the pin with a ring = a, three strokes = r,
  joined rings = o, two long s = n, "4" = e, "n" with a bar = d, "3" with a tail = z. So the two keys come from
  one office and one stock of signs. They are two different keys.
- The "Gran cifra" of the Catholic Monarchs (Bergenroth's sheet): one sign fits (m4 = g). Its code word
  luq = capitán does not fit: here `luq` = "ha" (ha-blado, ha-zen, ha-gan, ha-blar).
- No new value for no. 94 comes from this letter.

## How the key was found

1. **The solver failed.** I adapted the solver of no. 94 (a hill climber on a table of Spanish five-letter
   groups, several signs for one letter, code words as breaks). Six starts, 120,000 steps each. It did not
   converge: six different keys, and no clear word. Cause: only 900 signs, in 187 short runs.
2. **By hand, from the runs of signs.**
   - `pie` (35 times) and `gad` (25 times) are the commonest code words: que, de.
   - The run `C. oo n- ^ III` came twice, once after "de": **poder**. Then `C. III ^ dl m p fs n- oo` =
     **preciando**, `dl oo III p dl tto ff` = **coraçon**, `p + O. ^ fs gto p n- oo` = **asentado**,
     `gto III ^ m4 qp p` = **tregua**, `n- m X .ll. III ^ fs dl m p` = **diferencia**.
   - Each later value came from a word in context.
3. The controls then confirmed the key. No name served as a crib.

## Grades and counts (`counts.py`)

- **A = firm**: fixed by three or more clear words.
- **B = probable**: fits every place, but few places; or one place, with the sense confirmed by an outside source.
- **C = guess**, or a value that the alphabet rule puts in doubt.

| | Types | Tokens | Grade A | Grade B | Grade C | No value |
|---|---|---|---|---|---|---|
| Signs for letters | 56 | 901 | 43 types, 884 tokens | 9 types, 13 tokens | 3 types, 3 tokens | 1 type, 1 token |
| Code words | 72 | 301 | 18 types, 210 tokens | 31 types, 63 tokens | 15 types, 20 tokens | 8 types, 8 tokens |
| **All** | 128 | **1,202** | **1,094 = 91.0 %** | 76 = 6.3 % | 23 = 1.9 % | 9 = 0.7 % |

- Before the audit: 1,094 tokens of grade A (91.0 %), 72 of grade B, 25 of grade C, 11 with no value. The first
  notes said "97.0 % read". That was the sum of A and B.
- 31 of the 72 code words stand once. A value for such a word "fits every place" by default. Read grade B with
  this limit.
- The pause marks (`Z` 58 times, `÷` 14 times) are not in the count of tokens.

## Controls

1. **Shuffled keys** (`control.py`). Score = mean log-probability for each group of five letters, on a table of
   Spanish. Control = the same transcription with the letter values shuffled among the sign types, 500 times.

   | Text | Key | 500 shuffled keys: mean, best | Shuffled keys that reach the key |
   |---|---|---|---|
   | Settled, signs and code words of grades A and B, corrected key (1,349 groups) | -11.17 | -15.87, -14.68 | 0 of 500 |
   | The same with the key before the audit (1,298 groups) | -11.20 | -16.04, -14.85 | 0 of 500 |
   | Settled, signs only (329 groups) | -11.65 | -18.70, -17.41 | 0 of 500 |
   | Pass A alone, signs only | -11.85 | -18.70, -17.40 | 0 of 500 |
   | Pass B alone (blind), signs only | -11.96 | -18.70, -17.42 | 0 of 500 |

   Real Spanish scores -10.87 on the same table. The same letters shuffled score -17.80. Limit: I built the key
   by hand on pass A, so the score on pass A is not independent. Pass B is independent of my reading and gives
   the same score.
2. **The blind audit**: 27 of 27 hidden values restored; in a second run on the weak values, 12 exact, 1 near
   and 5 wrong of 18. See [audit.md](audit.md), part 1.
3. **The alphabet rule** of the code list (`bands.py`): correlation 0.69 at the audit, 0 of 20,000 shuffled
   keys reach it; 0.81 with the corrected key. See [audit.md](audit.md), part 1.
4. **The facts** against Sanuto, Zurita and Guicciardini. See [audit.md](audit.md), part 2. I did not open
   these sources when I made the reading; the first notes said that the matches were from memory and had to be
   checked.
5. **Inside the text**: a proverb comes out whole, "quien a Dios tiene todo tiene", and the names Faença,
   Arímyno, Sesena, Venosa, Portogal, Francia (a code word), Go. Fernández.

## What the audit changed

| # | Change | Where |
|---|---|---|
| 1 | `hog` = estos and `ren` = Venecianos. They were the wrong way round. Grade C to B | Key; r01, r15, r24, r32, r33, v11, v12 |
| 2 | r29-r31 reads "Antes, o me hagan medianero o no, entiendo por vías esquisitas de trabajar que estén como están" | Reading |
| 3 | `noe` = para (it was "a"). Probable, grade B | Key; r05, r17 |
| 4 | `hu` = embaxador, `hac` = entre, `poz` = rey de Francia: settled in sense by Sanuto. Grade C to B. The exact word stays open | Key; r01, r02 |
| 5 | `rud` = servicio and `mul` = mal: taken over as guesses, grade C | Key; r29, r15 |
| 6 | `got`, `fij`, `muy`: grade B to C, because they lie outside their alphabet band. `gaf`, `fab`, `pot` (already C) get the same mark | Key |
| 7 | `rus` = ya and `fin` = bueno stay grade C. The sense of v16 is supported by the facts; the words are not | Key; v16 |
| 8 | The alphabet rule is a control now | README, audit.md |
| 9 | The counts are a firm share and a share with the probable values | README |
| 10 | The facts have their sources. The Sultan line (v06-v07) is marked doubtful | README, reading |
| 11 | The search for earlier work has the audit's full list, with what was not opened | README, audit.md |
| 12 | 55 valued sign types (not 56). Decoded characters that agree between the passes: 89.0 % and 85.6 % | This log |
| 13 | The English of r18-r21 says that the Pope's side got the castles of Cesena | Reading |

Of the ten values that lay outside their alphabet band at the audit, three are inside it now (`hog`, `ren`,
`noe`). Six are marked doubtful. The tenth, `me~` = por, stays firm: the text fixes it in 14 places. It is listed
as an exception to the rule.

## Earlier work

On 9 October 2026 I checked the three other projects only, and I made no search for a period decipherment. The
audit made the full search on 11 October 2026. Its list, with what was not opened, is in [audit.md](audit.md),
part 3.

## Open points

- Not settled: r07 `gab`; r09-r10; r13-r14 (`rus`, `rie~`, `mut`); r15 `gag`; v01 (`hue`, `nae`, `meq`); v14 `roo`.
- Doubtful: v06-v07 (the Sultan's embassy); v16 (the sense is supported, the words are not); the six values
  outside their band.
- r01: no stroke is seen over `gie`; the sense asks for `gie~` (del). The first two signs of r01 are a cross and
  a pause mark. The cross can be the usual cross at the head of a letter. Then "ayer" has no "a".
- r03 and r17: the sign `tb` = d does not fit ("posedendo", "ynterpudsiese"). The sign needs a new look on the
  image.
- r18-r21: who "wished to settle".
- `pie` often has a stroke above it, as pass B wrote. The value does not change. `fin` in v16 has a stroke above it.
- The writer and the addressee come from the catalogue, not from the page.
- The solver failed. The key rests on words read in context. The controls support it.
- **Next test:** the two sister letters at the Real Academia de la Historia, Salazar A-10 f. 20 (5 February
  1504) and A-11 f. 400 (10 February 1504). If they are in this cipher, the key can be tested on them.
- No palaeographer has checked the transcription or the reading.

## Files that are not in this folder

The line strips, the enlarged crops, the failed solver, the test with the key of no. 94, and the packages of the
blind audit stay in the working folder. The table of Spanish five-letter groups for `control.py` is too large
for the repository (47 MB).
