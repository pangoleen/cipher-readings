# The cipher of Cardinal Scipione Gonzaga and the Duke of Nevers, 1590

Paris, BnF, ms. français 4698 holds letters in Italian from Cardinal Scipione Gonzaga in Rome to Louis de Gonzague,
Duke of Nevers, with long passages in cipher. This folder rebuilds the cipher, links the letters to period
decipherments in two other volumes, tests the rebuilt code against them, and reads the passages that have no
decipherment.

**Status: 3 October 2026.** The work was done by a model. No palaeographer has checked it. No key sheet was found.
Corrections are welcome: please open an issue.

## What is new and what is not

| | Item | State |
|---|---|---|
| Reproduced | The plain text of the letters of 21 January and 16 February 1590 | It is the text of Nevers's own clerk of 1590 (BnF fr. 4702). We transcribed and translated it. It is not a new decipherment. |
| New | The link between the two volumes | fr. 4702 ff. 94r-95r, f. 97r-v and f. 108r are the decipherments of fr. 4698 ff. 30r-31r, f. 104r and f. 34r. The printed catalogue describes them as letters of "un agent du duc de Nevers" and does not link them. We found no source that does. |
| New | The reconstruction of the cipher | Three layers; a word code of 448 values in 14 lists; a symbol alphabet. Built without a key sheet. |
| New | A second, larger test | BnF fr. 4696 holds about 56 letters of the Cardinal of 1585 to 1589 with the clear text written above the cipher. It is the same cipher from October 1586. The table of 378 values, built before this volume was seen, gives the glossed word for 452 of 463 units (97.6 %). |
| New, small | Passages of fr. 4696 with no gloss, and two minutes of Nevers | [fr4696/readings.md](fr4696/readings.md) |
| New | A blind test of the method | A partial reading was made and frozen before the period decipherments were found. It is scored below. |
| New, with gaps | The letters of 24 March and 31 March 1590 (ff. 26v-27r, ff. 36r-37r) | No period decipherment was found for them. They are read here with the rebuilt code: [24 March](reading/f26v-27r_1590-03-24.md), [31 March](reading/f36_1590-03-31.md). |

## The documents

| Cipher (BnF fr. 4698, Gallica `btv1b9058291p`, microfilm) | Period decipherment | Here |
|---|---|---|
| f. 17r-v, letter of 16 February 1590, five cipher lines | fr. 4698 f. 105r | `transcription/f105_decipherment_1590.txt` |
| ff. 30r-31r, letter of 21 January 1590 | fr. 4702 ff. 94r-95r (Gallica `btv1b530546654`, colour) | [edition](editions/edition_1590-01-21_f30.txt) |
| f. 104r, cipher sheet sent with the letter of 16 February 1590 | fr. 4702 f. 97r-v | [edition](editions/edition_1590-02-16_f104.txt) |
| f. 34r, letter of 19 February 1590 | fr. 4702 f. 108r | `alignment/alignment_f34.tsv` |
| ff. 26v-27r, letter of 24 March 1590 | none found | [reading](reading/f26v-27r_1590-03-24.md) |
| ff. 36r-37r, letter of 31 March 1590 | none found | [reading](reading/f36_1590-03-31.md) |
| f. 108r and f. 179r, minutes of Nevers to the Cardinal (28 February and 9 July 1590) | none found | [fr4696/readings.md](fr4696/readings.md) (f. 108r is weak) |
| BnF fr. 4696 (Gallica `btv1b9059540q`), letters of 1585 to 1589 | written above the cipher, in the volume | [fr4696/](fr4696/) |

ff. 11-16 of fr. 4698, which the catalogue lists as "Chiffre", hold three clear letters and no cipher.

## The system

Three layers.

1. **A word code.** A two-digit figure, 10 to 99, stands for one word in its dictionary form. A mark on the figure
   says which list the figure belongs to. Each list is a slice of one alphabetical word list (a one-part
   nomenclator). The order is by the first letters, loosely; u and v count as one letter.

| Mark on the figure | Slice |
|---|---|
| none, or one dot above | a to ca |
| one dot above | cat to di |
| two dots above | dis to f |
| two dots below | g to in |
| bar below | in to lu |
| dot below | ma to ne |
| circumflex above | no to pe |
| caron below | pi to qu |
| circumflex above and caron below | qu to r |
| dot above and bar below | s |
| bar above and dot below | su to v |
| two bars | small words, a to q |
| round brackets | small words s to v, auxiliaries, pronouns, titles |
| bar above | persons and names (not alphabetical) |

2. **A symbol alphabet** of about 45 signs, with several signs for each common letter, for words that are not in
   the lists.
3. **A verb sign.** An arc above a figure means: read the verb of the noun in the list. The Cardinal states this
   rule in clear on f. 17v, and promises a new cipher when he has time.

The table is [tables/lists_v4.tsv](tables/lists_v4.tsv): 448 values with a period gloss. `tables/lists_v3.tsv` is
the table of 378 values as it stood before fr. 4696 was seen, and `tables/interp_v3.tsv` holds 27 window
proposals. Eighteen pairs break the alphabetical order; most are swaps of close neighbours.

The Cardinal made the cipher himself. On 18 November 1585 he writes that he forgot the word "Suizzeri" under the
letter S, so that the numbers after it move up by one (fr. 4696 f. 3v). On 11 August 1586 he sent a new word list,
"un mezo Dittionario", and cancelled the first two (f. 32v). The symbol alphabet stayed the same from 1585 to 1589. [images/marks.jpg](images/marks.jpg) shows the marks.

**Not the key:** Tomokiyo's no. 35 (BnF fr. 3995 f. 64), which another project names for this volume. In that key the
figures 11 to 40 are letters; on f. 17r it gives a value for 11 of 28 figures and no Italian.

## How it was done, in order

1. The glosses inside fr. 4698 (f. 105r, and words written above the cipher on ff. 21v, 22r, 26r, 93r, 101r) gave
   about 150 code values and the symbol alphabet.
2. The values of each mark, sorted by figure, turned out to be in alphabetical order. This gives a window for every
   figure with no gloss.
3. A partial reading of the letter of 21 January 1590 was made, and a second agent read the marks blind. That
   state is kept in [evidence/before_fr4702/](evidence/before_fr4702/) and in the first commit of this repository.
4. A search of the printed catalogue of the sister volumes then found three decipherments with no author named, in
   fr. 4702. They gave the full text of three letters, 1,528 aligned code units, and the larger table.
5. With that table, the two letters that have no decipherment were transcribed by two agents each, blind, and
   decoded.

## The blind test

The partial reading of step 3 was scored against the clerk's text of 1590
([evidence/blind_score.md](evidence/blind_score.md)).

| Kind of word in the partial reading | Right |
|---|---|
| Spelled words (symbol alphabet) | 96 % of letters |
| Code words with a period gloss | 344 of 371 (93 %) |
| Code words chosen inside an alphabetical window | 42 of 64 (66 %), and 8 near misses in the same window |
| True word inside the predicted window | 47 of 61 (77 %) |

Nearly every failure has one cause: a mark read as the mark of another list. On the full alignment the mark seen on
the film names the right list for 87 % of the units. So a word with a period gloss is fairly safe, and a word chosen
by window is a proposal.

## The test against fr. 4696

fr. 4696 was found after the table of 378 values was finished. Eleven of its glossed pages (1586 to 1589) were
transcribed, one blind pass each: 587 figure units ([fr4696/agreement_table.md](fr4696/agreement_table.md)).

| Measure | Value |
|---|---|
| Units whose word is in the table of 378 values | 463 |
| The gloss on the page is the word of the table | 452 (97.6 %) |
| Word and mark both agree | 408 (88.1 %) |
| Conflicts | 1 (figure 87 of the list o to pe: "perfidia" against "pericolo") |
| The same test with a shuffled table | 2 of 572 |
| Window proposals confirmed by a gloss | 8; one is contradicted |

So the word values hold. The marks stay the weak point: in about one unit in ten the mark that was read names
another list.

## The two letters with no period decipherment

**24 March 1590 (ff. 26v-27r).** Two blind transcription passes agree on the figure for 95 % of 586 units and on
the mark for 90 % of those. 84 % of the units have a glossed value (an upper bound), 5 % a window value, 7 % none.
The letter reports that a person left Rome "per una sua devotione", that the Spanish ambassador pressed the Pope,
and that the Pope called the cardinals: "il parere di {quasi} tutti fu che non conveniva a dignità di Papa il far
alcuna delle cose domandate". The names of persons are inferred, and the reading says where.

**31 March 1590 (ff. 36r-37r).** The two passes agree on the mark for only 72 % of the units, so this reading is
weaker. After the news of Mayenne's defeat the Congregation voted: "la {maggiore} parte fu di parere che si
{dovesse} ... di danaro primo et poi di arme". The verso is weak.

In both readings, CAPITALS are spelled words, plain words have a period gloss, and words in {braces} are window
proposals. The events are known to historians from other sources; we did not compare the letters with them.

## Limits

- The cipher is on black-and-white microfilm. One dot against two dots, and a dot on a figure that contains a 1,
  often cannot be decided. A wrong mark gives a wrong word that looks real.
- The editions of the letters of 21 January and 16 February follow the clerk. In 49 units the editor preferred the
  cipher to the clerk's word; each case is in the alignment tables and needs a second reader.
- The alignment of f. 34r had one pass.
- The pages of fr. 4696 had one transcription pass each. The older word lists of May to September 1586
  (ff. 20r-37v) were not studied.
- Nevers's minutes in BnF fr. 3612, 3375, 4697 and 4701 are not on Gallica and were not seen.

## Earlier work

Searched on 3 October 2026 (last at 13:56 UTC): D. Bourdeau's `cyphersolver` (the volume is in his queue with
key no. 35 named; no reading), `NoAutopilot/cipher-lab`, `el-descifrador/cabinet-noir`, satoru.net/crypt,
S. Tomokiyo's pages on the Nevers ciphers and on unsolved ciphers, the printed BnF catalogue of the sister volumes (fr. 4680 to 4720)
for stand-alone decipherments, and web searches for phrases of the text. No reading of these letters and no note
of the link between fr. 4698 and fr. 4702 was found. A printed edition that is not online can exist.

## Contents

| Path | Content |
|---|---|
| `editions/` | The letters of 21 January and 16 February 1590: the clerk's text in the order of the cipher, with an English translation |
| `decipherments_1590/` | Line-by-line transcriptions of fr. 4702 ff. 94r-95r and f. 97r-v |
| `reading/` | The letters of 24 and 31 March 1590 |
| `tables/` | The word lists, the window proposals and the symbol alphabet |
| `alignment/` | One row for each code unit of ff. 30, 104 and 34: figure, mark, clerk's word, value |
| `transcription/` | The cipher transcriptions |
| `evidence/` | The blind score, the survey of fr. 4702, the blind passes, the work logs, and the state before fr. 4702 was found |
| `fr4696/` | The test against the glossed letters of 1586 to 1589, the readings of the passages with no gloss, the transcriptions, and the work log |
| `images/` | Reduced images: the marks, three cipher pages, and two pages of fr. 4702 |

## Credits

- **Satoshi Tomokiyo** catalogued the cipher keys of the Duke of Nevers in BnF fr. 3995
  ([cryptiana, "Ciphers of the Duke of Nevers"](https://cryptiana.web.fc2.com/code/nevers.htm)).
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`) listed the volume as a candidate in September 2026.
- **Nevers's clerk of 1590** deciphered three of the letters.
- **Bibliothèque nationale de France / Gallica** provides the page images. Images here are reduced, with the
  credit "gallica.bnf.fr / BnF".
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code and tables: MIT. Text: CC BY 4.0. Images: reduced images from Gallica, under the BnF's conditions of reuse,
with the credit "gallica.bnf.fr / BnF". Details are in [LICENSE.md](LICENSE.md).
