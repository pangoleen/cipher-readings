# The Spanish ambassador at Venice to Ferdinand and Isabella, 24 February 1504: the cipher rebuilt and read

A letter all in cipher, written in the days when Venice heard of the truce between Spain and France.

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| By the catalogue: Lorenzo Suárez de Figueroa, Spanish ambassador at Venice, to Ferdinand and Isabella, Venice, 24 February 1504 | Paris, BnF, ms. Espagnol 318, no. 93, f. 118r-v (Gallica `btv1b52503046q`, views 446-447) | On the lists of unsolved ciphers; no key, no reading | [reading with an English translation](READING.md): 91.0 % of the tokens have a firm value, 97.3 % with the probable values |

**Status: 11 October 2026.** The work was done by a model. No palaeographer has checked it. The reading has gaps.
Corrections are welcome: please open an issue.

## What this is

- A letter of 50 lines, all in cipher. Only the date is in clear: "de Venecia xx iiii de febrero".
- The page has no signature and no address. The writer and the addressee come from the catalogue of the
  library. The year comes from the catalogue too, and the content proves it (see "The facts").
- The cipher has signs for letters and code words for common words. It is not the cipher of the neighbour
  letter, no. 94 ([espagnol-318](../espagnol-318/)).
- The neighbour letter is the model for this folder. The two readings were made in the same way.

## What is new

**This is the first reading known to us. The key is rebuilt from the letter. We found no period decipherment (the
searches are listed below).**

- The Spanish court read this letter in 1504. The chronicler Zurita used other letters of the same ambassador in
  clear. So a period decipherment existed. We did not find it, and we did not find a printed text.
- The claim is "first reading known to us". It stands only with the list of searches, and with the list of what
  was not opened.
- No key sheet was used. No name served as a crib.

## The state

| Measure | Value |
|---|---|
| Cipher lines | 50, on two pages |
| Tokens (signs and code words) | 1,202: 901 signs and 301 code words |
| Tokens with a firm value (grade A) | 1,094 of 1,202 = 91.0 % |
| Tokens with a firm or a probable value (grades A and B) | 1,170 of 1,202 = 97.3 % |
| Tokens with a guess or a doubtful value (grade C) | 23 = 1.9 % |
| Tokens with no value | 9 = 0.7 % |
| Sign types with a value | 55, for 24 letters and "ll" |
| Code words with a value | 64 of 72 |

So the short form is: **91 % firm, 97 % with the probable values.** Do not read "97 %" as "97 % sure".

- **Firm (A)** = fixed by three or more clear words.
- **Probable (B)** = fits every place, but the places are few; or one place, with the sense confirmed by an
  outside source.
- **Guess or doubtful (C)** = a guess, or a value that the alphabet rule puts in doubt.
- 31 of the 72 code words stand once in the letter. A value for such a word fits "every place" by default. Read
  grade B with this limit.

## The cipher

- **Signs for letters.** 55 sign types for 24 letters and "ll". A common letter has 2 to 5 signs (o has five,
  e and s have four). Four joined groups stand for one letter each: `gto` = t, `gt` = e, `otto` = n, `tto` = o.
- **Code words.** 72 words of two or three small letters, as `pie` = que, `gad` = de, `heg` = en. A code word
  can stand for a syllable inside a word: `pet` = si in "si-tiado", `mat` = no in "Ve-no-sa".
- **Two pause marks.** One is a small pause, one is a strong pause.
- **The code list follows the alphabet.** Code words in f stand for words in a or b, code words in g for words
  in c or d, and so on to r for s to y.
- The key is in [KEY_TABLE.md](KEY_TABLE.md) and `key.py`. The names of the signs are ours
  ([transcription/SIGNS.md](transcription/SIGNS.md)).

## What the letter says

The full text, line by line, with an English translation and with the gaps left as gaps: [READING.md](READING.md).
In short:

- "Ayer llegó aquí a Venecianos letra ... que tienen en Francia": Venice heard of a truce of three years
  between Spain and France. "Enbiaron luego por mí para notificármelo".
- Venice showed pleasure. The ambassador let them think that he believed it. His own view: the joy "estava en el
  rostro, y el dolor en el coraçón".
- Of the truce he says: "quien a Dios tiene todo tiene".
- Venice and the Pope are in a quarrel over Faenza and Rimini. They talk of a go-between. "El Papa me escrivió un
  breve", to thank him. He will accept the part "si me conbidan", and he waits for an order.
- His plan: "o me hagan medianero o no, entiendo por vías esquisitas de trabajar que estén como están". He means
  to keep the two apart, so that Venice must join Spain.
- "El Papa se declina a la parte de Francia."
- "Luys d'Arce está sitiado en Venosa."
- Venice makes light of "el negocio de Portogal". The people are "en gran confusión" over the spice trade.
- Doubtful: the embassy of the Sultan is put off. Supported in sense, not in the words: Gonzalo Fernández is
  well again.

## How to check by hand

1. Open the check page: <https://pangoleen.github.io/cipher-readings/espagnol-318-no93.html>. It shows the key and
   three lines of the letter. Each sign stands beside its image, with its name and its value.
2. Or take one line yourself. Line 22 of the recto is a good one. Its tokens are in
   `transcription/f118r_final.txt`, row `r22`. Look up each token in [KEY_TABLE.md](KEY_TABLE.md). You get
   "El Papa me escrivió un breve, gradecien-".
3. Compare with an outside source. Sanuto's diary, 23 February 1504, has the Spanish ambassador in the College:
   the legate had given him a brief of the Pope that thanked him (vol. 5, col. 891).
4. Compare the two transcription passes. They are in `transcription/`. `python3 agree.py` counts where they differ.
5. Run `python3 decode.py`. It decodes all 50 lines with the key. [DECODE_RAW.md](DECODE_RAW.md) holds this
   output.
6. Run `python3 counts.py` for the counts above, and `python3 bands.py` for the alphabet rule.

## The controls

Details and limits: [evidence/audit.md](evidence/audit.md) and [evidence/worklog.md](evidence/worklog.md).

1. **Two transcription passes.** The second pass was blind: three agents had the sign list and the line images
   only. The passes have the same token in 96.2 % (recto) and 93.6 % (verso) of the places. For the signs alone:
   99.0 % and 97.4 %. For the code words alone: 86.6 % and 81.8 %.
2. **Shuffled keys.** The key scores -11.17 for each group of five letters on a table of Spanish. 500 keys with
   shuffled letter values score -15.87 in the mean and -14.68 at best. Real Spanish scores -10.87. The blind
   pass alone, with the signs only, scores -11.96; shuffled keys reach -17.42 at best.
3. **A blind audit of the key, 11 October 2026.** A second run of the model, with a new context, hid 27 values
   of the key (12 signs and 15 code words, drawn at random). A fresh reader got the transcription, the rest of
   the key, and the decode with gaps. **It restored 27 of 27.**
4. **A second run of the audit, on the weak values.** All 18 values of grade C were hidden. The fresh reader
   gave 12 exact, 1 near and 5 wrong. Two of the wrong answers were right against the key: the code words `hog`
   and `ren` were the wrong way round. The key is corrected.
5. **The alphabet rule.** The first letter of a code word follows the first letter of its value. The rank
   correlation was 0.69 for the 62 code words of the key at the audit. 0 of 20,000 keys with shuffled values
   reach 0.69. With the corrected key it is 0.81. The first reading did not know this rule, so the rule is a
   control that does not come from the sense of the text.
6. **The facts.** The content agrees with Sanuto's diary of the same days. See the next part.

Limits of the blind audit:

- The 27 hidden values of the first run all occur 3 times or more. They are of grade A or B. The first run does
  not test the weak values. The second run does.
- When one sign of a letter is hidden, the other signs of the same letter still show most of each word. So to
  restore a sign is easy. The 15 code words are the harder half.
- The fresh reader is a model of the same family as the first reader. The two can share a wrong habit.
- Nobody can prove that the fresh reader opened no other file. It says so, and its answers cite the package only.

Ten values lay outside their band of the alphabet at the audit:

| Code word | Value | State now |
|---|---|---|
| `hog` | was "venecianos" | Corrected to "estos". In its band |
| `ren` | was "estos" | Corrected to "Venecianos". In its band |
| `noe` | was "a" | Corrected to "para" (probable). In its band |
| `got` | piensan | **Doubtful.** The band asks for a word in c or d ("creen", "dizen") |
| `fij` | esto | **Doubtful.** The band asks for a word in a or b ("aquello") |
| `gaf` | los | **Doubtful.** The band asks for a word in c or d ("dos", "ciertos") |
| `fab` | yo | **Doubtful.** The band asks for a word in a or b. No other value found |
| `pot` | el | **Doubtful.** The band asks for a word in q, r or s. No other value found |
| `muy` | aunque | **Doubtful.** The band asks for a word in l, m or n. The sense "though" fits all three places |
| `me~` | por | Outside its band, but firm: the text fixes it in 14 places ("Por-togal", "porque") |

## The facts, with their sources

The first reader says that it did not open these sources: its notes call the matches "from memory" and ask for
a check. The auditor read the sources on 11 October 2026, in full text on archive.org.

| Fact in the letter | Source |
|---|---|
| A truce of three years between Spain and France; each side keeps what it holds | Sanuto, *Diarii*, vol. 5, col. 880 (under 22 February 1504): "le trieve per 3 anni, con questo, chi ha si tegna"; cols. 921-922. Zurita, *Hernando*, book V, ch. 65. Guicciardini, *Storia d'Italia*, book VI, ch. 10 |
| "Yesterday" Venice had the news by a letter from its ambassador in France, and told the Spanish ambassador | Sanuto, col. 880 (the letter from Lyon) and col. 891 (23 February: the Spanish orator comes to the College and is told of the truce) |
| He showed pleasure | Sanuto, col. 891: "Li piaque" |
| The Pope wrote him a brief of thanks | Sanuto, col. 891 (23 February): the legate gave him "uno breve dil papa che lo ringratiava". This is the strongest single match |
| The quarrel over Faenza and Rimini; he may be the go-between | Sanuto, cols. 880, 893, 899-900 (26 February: the Spanish orator offers himself as "medio" between the Pope and Venice). Guicciardini, book VI |
| The castles of Cesena | Sanuto, col. 900: the Pope's side gets them in these days. The letter does not name the side |
| The Pope leans to France | Sanuto, col. 880. Zurita, book V, ch. 65 |
| Louis d'Ars besieged in Venosa | Sanuto, cols. 846 and 910. Zurita, book V, ch. 63 and 66. Guicciardini, book VI, ch. 10 |
| The spice trade and "the business of Portugal" | Sanuto, cols. 827, 841-843, 903-905. Zurita, book V, has "el negocio, y trato de la Especería" from the ambassador's letters of this year |
| Gonzalo Fernández is well again (the words are guesses) | Zurita, book V, ch. 66, and Sanuto, cols. 846 and 856: he was gravely ill in January and February 1504 |
| **Doubtful:** the embassy of the Sultan is put off | Sanuto, cols. 951-952 and 962: an envoy of the Sultan was in Venice on 6 and 9 March 1504. So it was not put off for long. Either the ambassador reports a false rumour, or our words in this line are wrong |

- No fact speaks against 24 February 1504. Sanuto dates the brief and the news of the truce to 22 and
  23 February 1504. So the content proves the year.
- The column numbers of Sanuto come from the text file of the scan. A number can be one column off.
- The chapters of Zurita are read in a print of the 17th century.
- The table with the quoted words is in [evidence/audit.md](evidence/audit.md), part 2.

## Earlier work

All searches are of 11 October 2026. The full list is in [evidence/audit.md](evidence/audit.md), part 3.

Searched, with no decipherment and no printed text of this letter:

- The catalogue of the Spanish manuscripts of the BnF (Morel-Fatio 1892): "Lettre en chiffre de Lorenzo Suarez
  aux Rois Catholiques. Venise, 24 février 1504." It notes no decipherment.
- The catalogue of the Colección Salazar y Castro (Real Academia de la Historia), in full text. It has four
  sister letters of the ambassador, all in cipher, none with a decipherment. It has no entry for 24 February 1504.
- Zurita, book V. He used the ambassador's letters of 1504 in clear. He does not quote this one.
- Rodríguez Villa's books on Rojas (1896) and on the Great Captain; Bergenroth's Calendar (February and March
  1504); three searches in PARES for Simancas.
- Phrases of the reading in the full text of archive.org and on the web: no hit on this letter.
- The other projects: S. Tomokiyo's list still has the letter under "unknown ciphers". NoAutopilot/cipher-lab
  has it as open. D. Bourdeau's [cyphersolver](https://dbourdeau.github.io/cyphersolver/) lists it as open, with
  no reading.

**Not opened:**

- L. Suárez Fernández, *Política internacional de Isabel la Católica*, vol. 6.
- A. de la Torre, *Documentos sobre relaciones internacionales de los Reyes Católicos*, vol. 6.
- The digital library of the Real Academia de la Historia (only the text of its catalogue was used).
- The full-text search of Gallica, Google Books and HathiTrust.
- The papers at Simancas themselves. PARES describes few papers of 1504 one by one.
- Three lists of other projects were not checked on that day: el-descifrador/cabinet-noir, Satoru's index, and
  A. Aymeloglu's list.

## Limits

- No palaeographer has checked the transcription. No historian has checked the reading.
- The writer and the addressee come from the catalogue. The page does not name them.
- Eight code words have no value. Fifteen more have a guess or a doubtful value. The reading marks each place.
- Lines r08-r10, r13-r14 and v01 are not settled. The line on the Sultan's embassy (v06-v07) is doubtful.
- One sign for d does not fit two words (r03, r17). One sign in r10 has no value.
- The solver that read no. 94 failed on this letter: the text is too short. The key rests on words read in
  context, and on the controls above.
- The exact words for "ambassador", "between" and "king of France" in lines r01-r02 are open. Sanuto confirms
  the sense.
- The blind readers of the audit are models of the same family as the first reader.
- The next test is ready: two sister letters at the Real Academia de la Historia (Salazar A-10 f. 20, 5 February
  1504, and A-11 f. 400, 10 February 1504). If they are in this cipher, the key can be tested on them. We did
  not see them.
- `control.py` needs a table of Spanish five-letter groups that is too large for this repository (47 MB).

## Contents

| File | Content |
|---|---|
| `READING.md` | The reading in Spanish, line by line, with an English translation and notes on single lines |
| `DECODE_RAW.md` | The machine decode of the settled transcription and of both passes |
| `KEY_TABLE.md`, `key.py` | The key: signs, code words, grades, and a note on each corrected or doubtful value |
| `transcription/` | The sign list, the two passes for each page, and the settled text |
| `decode.py`, `lib.py` | The decoder |
| `counts.py`, `bands.py`, `agree.py`, `control.py` | The counts, the alphabet rule, the comparison of passes, the shuffled-key control |
| `evidence/worklog.md` | The work log |
| `evidence/audit.md` | The summary of the audit: the blind test, the facts with their sources, the search for earlier work |
| `images/f118r.jpg` | The first page, reduced, with the credit "gallica.bnf.fr / BnF" |

## Credits

- **Satoshi Tomokiyo** ([Cryptiana](https://cryptiana.web.fc2.com/code/crypto.htm)) described the ciphers of the
  Catholic Monarchs and listed this letter as unsolved.
- **Daniel Bourdeau** and **NoAutopilot/cipher-lab** listed the letter as open.
- **Bibliothèque nationale de France / Gallica** provides the page images.
- The Internet Archive provides the texts of Sanuto, Zurita, Guicciardini and the catalogues.
- **The work was done by a model**: Claude, by Anthropic, running as Claude Code with subagents. Paolo Rosson
  directed it. No palaeographer has checked it.

## Licence

Code: MIT. Text: CC BY 4.0. Images: reduced from Gallica, under the BnF's conditions of reuse; the source is
"gallica.bnf.fr / BnF".
