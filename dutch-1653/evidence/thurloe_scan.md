# More text in the Boreel ring cipher of 1653? Notes

Date of work: 4 Oct 2026. Folder: `dutch1653/more/`. I changed no file above this folder. Nothing was committed,
pushed or published. I did not log in anywhere.

Marks: **[IMG]** = I read it on a page image. **[WEB]** = a web text or an OCR text says it. **[CALC]** = a script
in this folder gives it.

## 1. Result in short

- **No other letter in this cipher is in print in Thurloe.** I scanned all seven volumes in two texts (British
  History Online, and the OCR text of archive.org). The scan finds the two known letters and nothing else:
  0 new letters, 0 new groups. The corpus stays at 136 + 12 = 148 groups.
- **The Verbael says why.** The cipher lived for about five weeks. Boreel sent it after 18 Aug 1653. The deputies
  used it on 1 Sept. On 8 Sept they wrote that the covers with the ciphers had been opened. On 29 Sept they wrote
  that the English "konnen ... hebben by copye" Boreel's cipher. By 20 Oct they had a new one (section 4).
- **Code words above 100.** They belong to the old general cipher of the States General, not to the ring.
  `128` = "den Koningh van Denemarcken" is now certain: a second Dutch minute and an English gloss confirm it
  (Thurloe i.316, Verbael p. 16). `168` = general Cromwell rests on the English gloss. `117` = the fleet of the
  States rests on one place in the minute (section 5).
- **"6" is "16".** The two sixes stand in two alphabets. In each, 16 gives the letter of the minute (h, then g).
  A fixed sign cannot have two values. This is as far as the print can go (section 6).
- **"xxd" stays open.** No new text bears on it (section 6).

## 2. What I scanned

| Source | Volumes | How | Files |
|---|---|---|---|
| British History Online, `thurloe-papers/vol1` ... `vol7` | 7 volumes, 450 pages (80, 58, 48, 57, 57, 69, 81) | `fetch_bho.py`: one request at a time, 3 seconds apart, each page saved, no page fetched twice. Vols 1-2: the earlier copies in `../src/bho1`, `../src/bho2` were copied. | `src/bho1` ... `src/bho7`, `src/fetch_log.tsv` |
| archive.org OCR text, `collectionofstat0Nthur_djvu.txt` | vols 1-5 and 7 (earlier agent's copies) | read only | `../src/thurloeN_djvu.txt` |
| archive.org OCR text of vol. 6 | `collectionofstat06thur` still gives HTTP 500. I used the other scan, `bim_eighteenth-century_a-collection-of-the-stat_thurloe-john_1742_6` (microfilm; the OCR is poor). | one request | `src/thurloe6_bim_djvu.txt` |

Limits of the two texts:

- BHO page `vol1/pp445-455` redirects to a login check. I did not open it. It holds Thurloe i.454 (Boreel, 13 Sept).
  The OCR text and the page image cover it.
- BHO marks 590 paragraphs "[Paragraph contains cyphered content — see page image]". In these it prints the small
  gloss of the 1742 edition and drops the numbers under the gloss (seen at i.301 and i.316 [IMG]). Numbers with no
  gloss stay in the text. Five of the 590 are in letters of the Dutch envoys, all in vol. 1 (De Witt cipher and Van
  de Perre cipher). The rest are letters of intelligence from The Hague (198) and English and French letters.
- So the OCR text is the second, independent pass. It keeps the glossed numbers.
- BHO breaks a paragraph inside a cipher run (i.435, after "519. 21. 21."). The scan lists the second part as a
  run with no indicator (class NEAR).

## 3. The scan and its controls [CALC]

Scripts: `scan.py` (find and decode candidate runs), `rank.py` (classes), `loose.py` (second, looser pass).

- Candidate run: 4 or more number groups close together, at least 80 % of the two-digit groups in 10 to 33.
- FITS: 5 or more groups; at most 30 % have three digits; 90 % of the two-digit groups in 10 to 33; an indicator
  group (first digit 1 to 5, last two digits 10 to 33); 80 % of the groups decode to a letter.
- NEAR: 6 or more two-digit groups, all in 10 to 33, no indicator. `rank.py` prints all 24 shifts for these.

| Text | Candidate runs, vols 1 to 7 | FITS | NEAR |
|---|---|---|---|
| BHO | 9, 3, 2, 1, 7, 2, 98 | 3 (the three runs of i.435) | 1 (second half of run 2 of i.435) |
| OCR | 56, 4, 2, 2, 26, 34, 134 | 4 (the three runs of i.435, and i.454) | 2 (second half of run 2; vol. 5, "12 18 11 28 21 31 11 28") |

- **Positive control.** The scan finds both known letters with no help, in both texts (i.454 only in the OCR text,
  because BHO does not serve that page).
- **The one other NEAR run** (vol. 5): no shift of the ring gives a word (`fits.tsv`). It is a list of numbers in
  an English letter.
- **Loose pass** (`loose.py`, `loose_hits.tsv`): windows of 10 numbers with 9 in the ring or of indicator form.
  84 hits. 26 are the two known letters. The others are: the Van de Perre cipher (vol. 1), an article list
  (vol. 2), ciphers with numbers to 49 and above (vols 3, 6, 7), a ship list (vol. 7). None has indicator groups
  and a readable decode.
- Vol. 7 has many candidate runs because of the English ciphers of 1658-59 (numbers 2 to 49 with words above 100).
  They do not fit: the two-digit groups go above 33, and most three-digit groups are not of indicator form.

Other places I checked for letters in cipher that Birch did not print:

- Macray, *Catalogi codicum ... Bodleianae*, part V fasc. 1 (1862), Rawlinson A.5 to A.7 (the Thurloe papers of
  Aug to Oct 1653), OCR text of archive.org `CatalogiCodicumManuscriptorumBiblioth` (`src/macray_djvu.txt`) [WEB].
  He lists the items that Birch left out. For these volumes he names one cipher letter of the Dutch: Van de Perre
  to Bruyne, 17 Oct 1653 (A.7 p. 47), which is another cipher. He names no letter of Boreel or to Boreel in cipher.
- The letter of Boreel to the greffier of 22 Aug 1653 (Thurloe i.436) has seven gaps printed as `****`. The print
  gives no numbers there.

## 4. Why there are only two letters: the life of the cipher (Verbael, 1725) [IMG]

Google Books id `EGBLAAAAcAAJ`, page images 1600 px in `src/verbael_pNN.jpg`. I found the pages with the book
search (`jscmd=SearchWithinVolume2`, word "cyffer", 11 hits).

| Date (N.S.) | Verbael | What it says |
|---|---|---|
| 4 July 1653 | p. 16-17, No. 10, to the greffier | "mits de voorgaende Cyffers van langen tydt in gebruyck ... een kleyne veranderinge ten dienste van onse Handelinge alhier te maeken, gelyck die by Copye hier nevens gaet". The journal calls it "een nieuw Concept van Cyffer". |
| 18 Aug 1653 | p. 88-89, No. 2, to Boreel | "Wy weten niet, of U Excellencie gedient is van het selve cyffer dat van eenigen tydt herwaerts in gebruyck is ... of een minute van cyffer dat ons apart in dese correspondentie kan dienen" |
| 1 Sept 1653 | p. 97-98, No. 6, to Boreel | They have the same cipher, and they will use "het nieuwe, daer nevens toegesonden" for the particular words (earlier agent). = Thurloe i.435. |
| 8 Sept 1653 | p. 102, No. 8, to Boreel | "alle de andere in onsen vorigen gementioneert, ook die daer de cyffers in waeren alle syn geopent geweest". New route through R. J. B. Pocquelin. |
| 13 Sept 1653 | not printed | Boreel to the deputies = Thurloe i.454. |
| 29 Sept 1653 | p. 111, No. 14, to Boreel | "de cyffers van haer Hoog Mog. al ten deelen ontdeckt syn, immers dat van U Excellencie konnen sy hebben by copye"; they wait for "een ander cyffer door dien nieuwen wegh". |
| 2 Oct 1653 | p. 112, No. 15, to Boreel | "een ander cyffer, daerin wy mogen gerust syn, dewylen de voorgaende buyten eenige twyffel ontdeckt syn; Wy moeten ondertusschen nootsaeckelyck alle Correspondentien uytstellen" |
| 20 Oct 1653 | p. 130-131, No. 31, to Boreel | Boreel's letters to the 11th came, "de laetste twee door den nieuwen weg, ende met cyffer in goede verseeckeringh, sulcks nu daer mede met gerustheydt schryven konnen" |

So the ring cipher was in use from about 25 Aug to the end of Sept 1653. Thurloe prints three letters between the
deputies and Boreel in this time: 1 Sept (cipher), 13 Sept (cipher), 20 Sept (no cipher, i.470). The deputies'
letter of 8 Sept went by the other route and did not arrive in Paris (Verbael p. 131). Thurloe does not print it.
After 20 Oct the two sides used the next cipher. Thurloe prints no letter of this correspondence after 20 Sept 1653.

The English read the general code in 1653: the print has their gloss "general Cromwell ;" above `168`. The gloss
stops there. It does not cover the ring groups `116. 11. 16. ...` [IMG].

## 5. Code words above 100 (`codewords.tsv`)

Two lists exist. Do not mix them.

- **The old general cipher of the States General.** Letters: numbers 1 to 66 in alphabet order (the key that Fruin
  printed in 1906). Names: numbers above 100. The deputies used it to 4 July 1653, and Boreel kept it.
- **The list of the deputies, changed on 4 July 1653** (Verbael p. 16-17). Kernkamp (1906, p. 92 n. 2) saw that the
  change touched only the numbers above 100. The letters to De Witt and Nieupoort after that date use it.

The letters to and from Boreel use the old list. Proof: 128 has the same value on 4 July (to the greffier) and on
1 Sept (to Boreel); and Cromwell is 168 for Boreel but 297 in the changed list.

| Code | Value | Evidence | Certainty |
|---|---|---|---|
| 128 | den Koningh van Denemarcken | (a) Thurloe i.316, 4 July 1653: "go so high against 128", gloss "Denmark." [IMG]; Verbael p. 16: "soo hoogh gaen tegen den Koningh van Denemarcken" [IMG]. (b) Thurloe i.435, 1 Sept 1653: "a private instruction from 128" [IMG]; minute: "met een secrete voor den Koningh van Denemarcken". (c) Thurloe i.301, 27 June 1653: "in regard of 128 a great animosity" [IMG]; no Dutch text, but the same sense as (a). | certain |
| 168 | generael Cromwell | Thurloe i.454: gloss "general Cromwell ;" above "168. 116." [IMG]. No Dutch text. | probable (gloss only, 1 place) |
| 117 | de Vloote van haere Hoog Mog. | Thurloe i.435, run 2. The minute has these words at this place. As ring group 1\|17 it gives q. No gloss. | probable (1 place); the exact words are not proved |
| 289 (of) 135 | the council of state | Thurloe i.301: gloss "The council of state." above "289 of 135" [IMG]. BHO drops the two numbers. | gloss only |
| 170 | France (?) | Kernkamp's guess. Thurloe i.302 "the business of 170". | not proved |
| 171, 190 | not read | Thurloe i.301 | open |

Changed list (not Boreel's), for contrast: 297 = Cromwell (gloss, Thurloe i.442 [IMG]); 330 = Prince of Orange
(Dutch text of 1919); 309 Scotland, 387 assembly, 400 Opdam, 434 455 States General, 502 states (glosses, OCR text
only [WEB]).

The letters of intelligence from The Hague in the same volume use a third list (104 States General, 105 States of
Holland, 128 council of state, 135 money, 140 France, 142 Denmark, 171 peace: glosses in the OCR text). It is the
code of that agent with Thurloe. It has nothing to do with the Dutch lists. The number 128 occurs in both by chance.

No other place in Thurloe has 117 or 168 in a Dutch letter [CALC: search of the BHO and OCR texts of vols 1-2].

## 6. The open points of the key

**"6" for "16": settled as far as the print allows.** The two places are in two alphabets:
run 2, alphabet 2, "sc6epen": 16 = h, the minute has "schepen"; run 3, alphabet 3, "rug6e": 16 = g, the minute
has "rugge". A fixed sign "6" would have one value; here it needs h and then g. A null would give "scepen" and
"ruge", and the chance that 16 gives the letter of the minute in both places is about 1 in 24 x 24. The same
volume prints 6 for 16 three times in the letter of 18 July 1653, where the key and the Dutch text are known
(earlier agent). So 6 is 16 with the first digit lost. Only the manuscript can say who lost it: the copy clerk
or the printer.

**"xxd" for "eene(n)": open.** No new text has these values. What I can add:

- The other errors of the print in this cipher change one digit: 52 for 32 (i.454), 17 for 27 and 23 for 22
  ("plotsn" for "vloten"), 6 for 16.
- With one-digit changes, `29 29 26` becomes `24 24 24` = "eee". With the next group 11 this is "eeen". The minute
  has "eenen" = `24 24 11 24 11`. So the cheapest repair is three changed digits (9, 9, 6 for 4) and one lost
  group (11). This is a guess. It is weak: the print has 24 right in all other places of the letter.
- No shift of the ring gives "een" for `29 29 26 11` [CALC]. The shift that makes 29 = e gives "eelv"; with the
  ring read the other way it gives "eeyo". So a wrong alphabet does not explain the three groups.

**117: open** in the strict sense (one place). See section 5.

**Not seen in any text:** alphabet 4, and indicators above 5.

## 7. Novelty and prior art (checked 4 Oct 2026)

| Where | Found |
|---|---|
| `raw.githubusercontent.com/dbourdeau/cyphersolver/main/CATALOGUE.md`, `SOLVED_CATALOGUE.md`, `targets/thurloe/NOTES.md` | Boreel letter still "stuck". No word on 128 = Denmark, on the Verbael, or on other letters in this cipher. [WEB] |
| `raw.githubusercontent.com/NoAutopilot/cipher-lab/main/PROGRESS.tsv` | No line with Boreel, Beverning or Verbael. One Thurloe line (Stamford 1655, another cipher). [WEB] |
| `raw.githubusercontent.com/aaymeloglu/unsolved-ciphers/main/TARGETS.md` | Row 16: "closed-negative 14 Sept 2026 ... Needs more text in the cipher or a Dutch-side crib." Row 22: the Van de Perre letter in MS Rawl. A.7 is blocked. [WEB] |
| `cryptiana.web.fc2.com/code/unsolved.htm` | No change for this item. [WEB] |
| Web search: Boreel 1653 cipher Thurloe; "128" Denmark "168" Cromwell Verbael cyffer | No reading and no code table. One hit: Aymeloglu's pull request 19 on the Van de Perre letters (another cipher). [WEB] |

What this task adds is small: a negative result for the seven volumes, the dated life of the cipher from the
Verbael, and the proof of 128 from a second minute. The values 128 = Denmark and 168 = Cromwell are in the glosses
of the 1742 print, so they are **reproduced**, not new. The link of the gloss at i.316 with the Verbael minute
p. 16 is ours; I found no earlier note of it.

## 8. What stays open, and what can move it

- No more text in this cipher is in print. More text needs manuscripts: Bodleian MS Rawlinson A.5 p. 240 and
  A.6 p. 58 (the two known letters; they settle the misprints), and the Dutch side: Nationaal Archief,
  Staten-Generaal, liassen Engeland and Frankrijk 1653, and the Boreel family archive (1.10.10). I did not find
  images of these on line.
- The key enclosure itself: Boreel's letter of about 25 Aug 1653 with "het nieuwe [cyffer], daer nevens
  toegesonden". The English opened that cover (Verbael p. 102). A copy can be in the Thurloe papers. Macray does
  not list one for A.5 to A.7.
- 117; the three groups "xxd"; alphabet 4.
- The glosses of the changed list (309, 387, 400, 434 455, 502) are from the OCR text only.
- The OCR text of vol. 6 is poor. For vol. 6 the result rests mainly on the BHO text.

## 9. Files

| File | Content |
|---|---|
| `letters.tsv` | One row for each letter in this cipher: the two known letters, and the result row (no new letter) |
| `codewords.tsv` | The code words above 100 with their evidence |
| `fetch_bho.py`, `scan.py`, `rank.py`, `loose.py` | The fetch, the scan, the classes, the loose control pass |
| `candidates_bho.tsv`, `candidates_ocr.tsv`, `fits.tsv`, `loose_hits.tsv` | The output of the scripts |
| `src/bho1` ... `src/bho7`, `src/volN_index.html`, `src/fetch_log.tsv` | The saved BHO pages |
| `src/thurloe6_bim_djvu.txt`, `src/macray_djvu.txt`, `src/prior/` | OCR text of vol. 6, Macray's catalogue, the tracker pages |
| `src/verbael_pNN.jpg`, `src/vNN_top.png`, `src/vNN_bot.png` | Verbael pp. 15-17, 88-89, 102, 111-112, 130-131 |
| `src/thurloe1_p316.jpg`, `p317`, `p436`, `p441`, `p442`, crops `t316_part4.png`, `t301_part2.png`, `t442_top.png`, `t435_128.png` | Thurloe page images (archive.org, 2400 px) |

There is no reading file: there is no new letter. No file name was refused.

To repeat: `python3 fetch_bho.py` (uses the saved pages; fetches nothing that exists), then
`python3 scan.py bho && python3 scan.py ocr && python3 rank.py && python3 loose.py`.

Passes: the scan had two independent texts (BHO and OCR). The code-word places at i.301, i.316, i.435, i.442 and
i.454 had one reading by me on the page image; the OCR text agrees with each. The Verbael quotations had one
reading by me on the page image.

## 10. Log

1. Read the rules, the README and the earlier notes. Wrote `fetch_bho.py`; ran it in the background (450 pages).
2. Ran `scan.py` on the OCR texts of vols 1-5 and 7: only the two known letters fit.
3. Got an OCR text of vol. 6 from the second archive.org scan. Nothing fits.
4. Checked the trackers and Macray's catalogue.
5. Searched the Verbael for "cyffer"; read pp. 16-17, 88-89, 102, 111-112, 130-131. This gave the life of the cipher.
6. Saw on the page image of i.301 that BHO drops glossed numbers ("289 of 135"). Listed the 590 marked paragraphs.
7. Read i.316 on the page image: "against 128", gloss "Denmark."; Verbael p. 16 has "den Koningh van Denemarcken".
8. Read Kernkamp's note: the change of 4 July 1653 touched the numbers above 100. Checked 297 = Cromwell at i.442.
9. Fetch ended. Ran the scan, the classes and the loose pass on all seven volumes. Wrote the files.
