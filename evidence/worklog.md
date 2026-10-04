# Dutch cipher of 1653 (Thurloe i.435) - notes

Date of work: 4 Oct 2026. Folder: `dutch1653/`. Nothing was committed, pushed or published.

Marks: **[IMG]** = I read it on a page image. **[WEB]** = a web or OCR text says it. **[CALC]** = a script in this folder gives it.

## 1. Result in short

- The letter of the Dutch deputies to Boreel of 1 Sept 1653 (Thurloe i.435, 136 groups) is read. The crib is the
  minute in the *Verbael* (1725), pp. 97-99, No. 6. **The text is reproduced**: the minute gives it in clear.
- **The key is rebuilt.** The cipher is a ring of 24 numbers with a shifted alphabet and an indicator digit. I found no
  earlier reconstruction of this key (section 6).
- The same table reads the one other letter in this cipher that I found: Boreel to the deputies, 13 Sept 1653
  (Thurloe i.454), 12 groups: `[168 = general Cromwell] in iames p[a]rc`. No clear text of that letter is in print.
  The deputies' printed reply names the place ("Conferentie in St. James Parck"), so the fact is not new.
- The letters to De Witt (Thurloe i.301, 308-309, 339-340, 351, 418) use **another cipher**. Its key is in print since
  1906 (Fruin). Those letters are reproduced, not solved by us.

## 2. Sources

| What | Where | How read |
|---|---|---|
| Thurloe i.435, cipher groups | archive.org `collectionofstat01thur`, leaf n464, 2400 px (`src/thurloe1_p435.jpg`) | [IMG] all 136 groups, equal to the BHO text |
| Thurloe i.435, English text | BHO `thurloe-papers/vol1/pp435-445` | [WEB] |
| Verbael No. 6, pp. 97-99 | Google Books `EGBLAAAAcAAJ`, page images 1600 px (`src/verbael_p97.jpg` ...) | [IMG] my transcription in `verbael_no6.txt` |
| Verbael pp. 106, 110, 111 | same | p. 110 and 111 [IMG]; p. 106 from the search snippet [WEB] |
| Thurloe i.454 (Boreel, 13 Sept) | archive.org leaf n483 (`src/thurloe1_p454.jpg`) | [IMG] |
| Thurloe i.301, 308, 309, 340, 418 | archive.org leaves n330, n337, n338, n369, n447 | [IMG] cipher lines |
| Fruin's key; Kernkamp's note; letter of 18 July 1653 in Dutch | resources.huygens.knaw.nl/retroboeken/dewitt, sources 3 and 1 | [WEB] OCR text only |
| De Leeuw, *Cryptology and statecraft in the Dutch Republic* (thesis, 2000) | pure.uva.nl/ws/files/3074957/12760_Thesis.pdf | [WEB] pdftotext |

Google Books gave the page images through `books?id=...&pg=PA97&jscmd=click3` (signed image links), and a search in the
book through `jscmd=SearchWithinVolume2`. The plain `img=1&zoom=3` link returns "image not available".

## 3. The system

1. **Ring.** The 24 numbers 10 to 33 stand in a ring in this order:
   `32 30 28 26 24 22 20 18 16 14 12 10 11 13 15 17 19 21 23 25 27 29 31 33` (then 32 again).
   Even numbers go down, odd numbers go up.
2. **Alphabet.** 24 letters: `a b c d e f g h i k l m n o p q r s t v w x y z` (i = j, v = u). They follow the ring.
3. **Indicator.** In alphabet k the letter `a` is the k-th number of the ring: a = 32, 30, 28, 26, 24 for k = 1 to 5.
   Each step of the indicator moves the alphabet one place.
4. **Grouping.** A 3-digit group is the indicator digit and the number of the first letter: `222` = alphabet 2, 22 = e.
   The 2-digit groups that follow stay in that alphabet until the next 3-digit group. The clerk changes the alphabet
   between phrases, not at fixed lengths.
5. **No nulls, no syllables, no words** in the ring part. Words of the general code of the States (128 = King of Denmark,
   168 = general Cromwell) are separate 3-digit groups. They look the same as indicator groups.
6. This is why the two other projects failed: their solvers modelled one alphabet. The letter has four.

The minute says the same in words: "Wy syn gedient van 't selve cyffer ende sullen eghter tot de expressien van de
paticuliere woorden ons liever dienen van het nieuwe, daer nevens toegesonden, op de maniere als daer onder het selve
geëxtraheert staet" (Verbael p. 97-98). The old cipher is the code of the States; the new one is Boreel's ring.

Key table: `key.tsv` (5 alphabets x 24 letters = 120 values; alphabet 4 is not used in the letters).
The whole key is the ring and one rule. `model.py` holds it.

## 4. Fit of the crib (`alignment.tsv`, `align.py`) [CALC]

Reading of the three runs with the model:

```
RUN1 |1| omdoor xxdn |2| expressen afgesonden de plotsn |3| van desen staet te doen |5| recognoszceren
RUN2 [117] |2| met de coopvaerdieschepen |5| noortwaerts aen is vertrocken
RUN3 |3| te rvgge convoyern
```

Minute: "om door eenen Expressen afgesonden, de Vlooten van desen Staet te doen recognosceeren" / "de Vloote van haere
Hoog Mog. met de Koopvaerdyschepen Noordtwaerdts aen is vertrocken" / "te rugge convoyeren".

| Class | Groups | Detail |
|---|---|---|
| fit | 124 | model letter = letter of the minute |
| fit, with 6 read as 16 | 2 | run 2 "sc[h]epen", run 3 "rug[g]e" |
| spelling | 3 | the sent letter has `c` for k, `i` for y, and one more `e`: "coopvaerdieschepen" |
| conflict | 6 | see below |
| open | 1 | 117 |
| total | 136 | |

Conflicts (the model letter is not the letter of the minute):

- Run 1, alphabet 1: `29 29 26` give `x x d` where the minute has "eene(n)". The next group, 11 = n, fits.
  "eenen" needs 24 24 11 24 11. I cannot explain these 3 groups.
- Run 1, alphabet 2: `17 10 15 25 23 13` gives "plotsn"; the minute has "Vlooten". 17 (p) stands for 27 (v), 23 (s) for
  22 (e). The other four groups fit "vlot.n".
- Run 1, alphabet 5: `29 26 20 16` gives "szce" in "recognos.ceren". 26 (z) is one group too many.

Open: `117`. It is at the start of run 2. As indicator 1 + number 17 it is the letter q, which is not Dutch here. The
minute has "de Vloote van haere Hoog Mog." at this place. It is most likely a group of the general code, like 128 and
168. Its exact value (the fleet, or the fleet of Their High Mightinesses) is not proved.

The number `6` is outside the ring. Both times 16 gives the letter of the minute. Three more "6 for 16" occur in the
same volume in the letter of 18 July 1653, where the key and the Dutch text are known (see 5c). So I read 6 as a
misprint of 16. A fixed sign "6 = h" or a null cannot be excluded for the Boreel letter alone.

Differences between the sent letter and the minute: only spelling (vloten, coopvaerdieschepen, noortwaerts,
recognosceren, convoyern), plus the code groups 117 and 128. Thurloe's translator has "dated in Paris the 25th" where
the minute has "den 23."; that is in the clear part.

## 5. Controls

a) **One number, one value.** [CALC] Inside one alphabet a number has one crib letter, with two exceptions: 17 and 23
   of alphabet 2 (p x3 and v x1; s x4 and e x1). These are two of the six conflicts. Across alphabets the same number
   has other values, as the system requires. 48 pairs (alphabet, number) fit the model; 19 of them occur one time only.
   But no value rests on one occurrence alone: all values come from the ring and one shift per alphabet, and the shift
   follows the indicator digit.

b) **Structure used to predict.** I found the ring from alphabets 2 and 5 alone (segments "expressen afgesonden",
   "met de koopvaerdy...", "noortwaerts aen is vertrocken"). Then I predicted alphabets 1 and 3 with the rule
   "a = k-th number". The prediction gave "om door", "van desen staet te doen", "te rugge convoyeren" at once.
   [CALC] 41 of 43 groups of alphabets 1 and 3 fit (`control.py`). The 2 misses are the "xx" above.

c) **Second test without a crib.** Boreel's letter of 13 Sept 1653 uses six values of alphabet 1 that the first letter
   does not show (i, a, e, s, p, c). They give "in iames p.rc". The deputies' reply confirms the place.

d) **Random rings.** [CALC] 5000 random orders of the 24 numbers, with the best shift chosen freely for each alphabet:
   at most 60 of 131 groups fit, 35 on average. The ring gives 127 of 131 with no free shift.

e) **Error rate of the print.** The letter of 18 July 1653 (Thurloe i.340, 207 groups) has a published key and a
   published Dutch text. 12 of its 207 groups are wrong in Birch's print (5.8 %). The Boreel letter has 6 conflicts and
   2 sixes in 136 groups (5.9 %). The conflicts are at the level of the misprints of this volume.

## 6. Prior art (searched 4 Oct 2026)

| Where | What I found |
|---|---|
| D. Bourdeau, github.com/dbourdeau/cyphersolver, `targets/thurloe/NOTES.md` (last commit 3 Oct 2026 06:07 UTC) | Letter (a) "stuck", control of 22 Sept 2026. Model: "monoalphabetic letters + small nomenclator", 8 "code groups". No Verbael. [WEB] |
| A. Aymeloglu, github.com/aaymeloglu/unsolved-ciphers, `TARGETS.md` row 16 (last commit 28 Sept 2026) | "closed-negative 14 Sept 2026 ... Needs ... a Dutch-side crib." His page on Vande Perre says the Boreel letter "uses a different cipher and remains unread". [WEB] |
| Same, `vande-perre-1653/evidence-audit/README.md` | He **names the 1725 Verbael** (Google Books `545Vf-pifTMC`) for the Vande Perre letters, as "incompletely inspected". He does not link it to the Boreel letter. The scout's line "neither names the Verbael" is true only for the Boreel target. [WEB] |
| NoAutopilot/cipher-lab, `PROGRESS.tsv` (commit 4 Oct 2026 12:44 UTC) | No line with Boreel, Beverning, Verbael, Dutch, 1653. [WEB] |
| S. Tomokiyo, unsolved.htm (local copy, 4 Oct 2026), dutch.htm, thurloe.htm, blog feed (25 posts to 4 Oct 2026) | The item is listed as unsolved. No post on it. [WEB] |
| K. de Leeuw, thesis 2000, pp. 18-20 | He describes the slide ciphers of the States' code books (alphabet moved against fixed rows of numbers, a number in front to name the table) from the Fagel books after 1672 and the Hochepied booklet of 1747. He sees it "already ... under ... De Witt" from a letter of 1668. Boreel occurs one time (same code book in 1650 and 1664). No word on Thurloe, on 1653 or on this ring. [WEB] |
| Kernkamp, Brieven van De Witt i (1906), p. 92 n. 2 | He names the Thurloe letters to De Witt and to Ruysch. He does not name the letter to Boreel. [WEB] |
| Web search (Verbael + Thurloe + cipher; "113. 10. 26. 13"; Boreel 1653 cipher) | No reconstruction found. [WEB] |

Conclusion: the clear text is in print since 1725. I found no publication of the key. The ring of 1653 is a small, early
case of the slide principle that De Leeuw describes for the later code books. That link is my reading, not his.

Not searched: De Leeuw's articles in *Cryptologia* outside the thesis; Vroomen and Nissen (2018); the Nationaal Archief.

## 7. Other letters (step 4)

Search for the ring cipher: OCR text of Thurloe vols 1-5 and 7 (archive.org) and BHO vols 1-2, for runs of numbers in
10..33 with 3-digit groups. Vol. 6 did not download (HTTP 500). BHO page `vol1/pp445-455` did not load.

| Letter | Cipher | Printed clear text | Status | File |
|---|---|---|---|---|
| Boreel to the deputies, 13 Sept 1653, Thurloe i.454 | ring | none found; reply in Verbael p. 111 names the place | read with the rebuilt table, 12 groups | `reading_boreel_to_deputies_1653-09-13.txt` |
| Beverning and Nieupoort to De Witt, 18 July 1653, i.339-340 | De Witt cipher | yes: Brieven aan De Witt i (1919) pp. 80-83 | reproduced; key printed 1906 | `reading_dewitt_cipher_letters_1653.txt` |
| Beverning to De Witt, 27 and 30 June 1653, i.301, 308-309 | De Witt cipher | none found | key printed 1906; Kernkamp says they can be read | same file |
| De Witt to Beverning, 24 July 1653, i.351 | De Witt cipher | in Brieven van De Witt i (not compared) | reproduced | same file |
| Beverning to Nieupoort, 22 Aug 1653, i.418 | De Witt alphabet + code | none found | 3 short places read with Fruin's key | same file |
| Vande Perre to De Bruyne, 5 letters | third cipher | - | Aymeloglu, 14 Sept 2026 | not done here |

Why only two letters: on 29 Sept 1653 the deputies wrote to Boreel that the English "konnen ... hebben by copye" his
cipher, and that they wait for another one (Verbael p. 111 [IMG]).

## 8. Open

- The 3 groups `29 29 26` in run 1 ("xxd" for "eene").
- The value of code group 117; whether 6 is a misprint of 16 or a sign.
- Alphabet 4 and alphabets above 5 are predicted, not seen.
- The manuscripts were not seen (Birch cites "Vol. v. p. 240" and "Vol. vi. p. 58" of the Thurloe papers, now Bodleian
  MS Rawlinson A). They can settle the misprints.
- Thurloe vol. 6 and the Nationaal Archief were not searched for more letters in the ring cipher.
- Fruin's key and the Dutch text of 18 July 1653 were read from OCR text, not from page images.

## 9. Files

`thurloe_groups.txt`, `verbael_no6.txt`, `alignment.tsv`, `key.tsv`, `reading_boreel_to_deputies_1653-09-13.txt`,
`reading_dewitt_cipher_letters_1653.txt`, `model.py`, `align.py`, `control.py`, `src/` (page images, web copies, scan
scripts). No file name was refused. The two reading files are `.txt`; the De Witt letters share one file because they
share one published key.

## 10. Log

1. Read the scout notes and the notes of Bourdeau and Aymeloglu. Took their count (136 groups, numbers 6-33, eight 3-digit groups).
2. Got the Verbael pages as images; transcribed No. 6. Got the Thurloe page image; checked all groups.
3. "afgesonden de" and "koopvaerdyschepen" gave alphabet 2. The third segment did not read with it: the alphabet changes.
4. "recognosceeren" and "noortwaerts aen is vertrocken" gave alphabet 5. Compared 2 and 5: every number moves by 6,
   up or down. That is a ring. 222 = e of "expressen" showed that the last two digits of a 3-digit group are a letter.
5. Predicted alphabets 1 and 3. They read. Wrote `model.py`, `align.py`, `control.py`.
6. Searched Thurloe for more text. The De Witt letters are in alphabet order (my own table), then found Fruin's key of 1906.
7. Found Boreel's letter of 13 Sept in the OCR text; BHO did not serve that page. Read it with the ring.
8. Prior-art search.
