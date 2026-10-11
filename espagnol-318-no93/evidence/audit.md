# Audit of the reading of BnF Espagnol 318 no. 93: summary

Date of the audit: 11 October 2026. This file is a summary of the audit report. It keeps the numbers, the
limits and the lists of searches of the report.

Who did it: a second run of the same model (Claude, by Anthropic, as Claude Code with subagents), with a new
context. The auditor did not make the reading. The auditor changed no file of the reading. The fixes were made
after the audit, and this file lists them at the end.

Two words in this file: SEEN = the auditor read it on the page image or in the source text. INFERRED = the
auditor concluded it from grammar or context.

## Verdict of the audit

1. **Is the key right? Yes, in its firm part.** About ten code words needed a change or a question mark.
2. **Is "first reading" a fair claim? Yes, in these words:** first reading known to us; key rebuilt from the
   letter; no period decipherment found (searches listed). The Spanish court read this letter in 1504, and
   Zurita used sister letters of the same ambassador in clear. So the claim is about a reading that is known
   today, and it stands only with the list of searches.
3. The audit asked for eleven fixes before publication. All are made (last part of this file).

## 1. Blind audit of the key

### Method

- A script hid a random set of values (seed 93): 12 of the 43 signs that occur 3 times or more, and 15 of the
  27 code words that occur 3 times or more. The hidden items cover 226 of 901 sign tokens and 109 of 301
  code-word tokens.
- A package held four files only: a brief, the transcription, the key with the hidden values as "?", and the
  decode with the hidden items as gaps. The true values were outside the package.
- A fresh reader (a separate agent with a new context) read the package and wrote its answers. It states that it
  read those four files only.
- A script scored the answers.

### Run 1: 27 of 27

| | hidden | exact | near | wrong |
|---|---|---|---|---|
| signs for letters | 12 | 12 | 0 | 0 |
| code words | 15 | 15 | 0 | 0 |
| **total** | **27** | **27** | **0** | **0** |

- Signs restored: `2=` b, `5` i, `C.` p, `O.` s, `P` j, `X` f, `gt` e, `ir` o, `p` a, `qp` u, `tf` s, `tto` o.
- Code words restored: gie como, gie~ del, gue con, hif es, hoe el, hug esta, mae la, mat no, mud negocio,
  myl mas, nan papa, pet si, pif qual, roc se, rup "vuestras altezas" (the key writes "V. Al."; counted as exact).
- Confidence of the fresh reader: 25 high, 2 medium.
- The fresh reader also read line r29 better than the first reader. It saw that the sign `tb` = d does not fit
  lines r03 and r17.

### Limits of run 1

- The pool held only items that occur 3 times or more. All 27 are of grade A or B. The run does not test the
  values of grade C, the code words with no value, or the 31 code words that occur once.
- A letter has 2 to 5 signs. When one sign is hidden, the other signs of the same letter still show most of each
  word. So to restore a sign is an easy task. The 15 code words are the harder half.
- The fresh reader is a model of the same family as the first reader. It can share a wrong habit of Spanish.
- Nobody can prove that the fresh reader opened no other file. The audit relies on its statement and on its
  answers, which cite places in the package only.

### Run 2: all the weak values hidden

Run 1 leaves the weak values with no test. So the auditor made a second package: all 18 values of grade C were
hidden (3 signs, 15 code words; 22 code-word tokens), and nothing else. A second fresh reader read it. It knew
only that `ren` and `hog` "both name a party".

| | hidden | exact | near | wrong |
|---|---|---|---|---|
| signs for letters (`E`, `o`, `ttc`) | 3 | 3 | 0 | 0 |
| code words | 15 | 9 | 1 | 5 |
| **total** | **18** | **12** | **1** | **5** |

- Exact: fab yo, fin bueno, gue~ de las, hab embaxada, hac entre, hu embaxador, maq mucho, moq muchas, rus ya.
- Near: poz "rey" (the key: "rey de Francia").
- Wrong, all five:

| code word (places) | the key then | fresh reader | its confidence | does its value read as well? |
|---|---|---|---|---|
| `hog` (3) | venecianos | **estos** | medium | Better. Line v11 needs a word like "estos" before the noun "desdeños". **A warning about the key** |
| `ren` (4) | estos | **venecianos** | medium | As well or better (r24, r32). **A warning about the key** |
| `gaf` (1) | los | ciertos | low | As well. One place only |
| `hig` (1) | ello | esto | low | As well. The same sense |
| `pot` (1) | el | su | low | As well: "que su alegría estava en el rostro". One place only |

- The pair `hog` and `ren` is the one real warning. The fresh reader reached the swap alone. The auditor reached it
  from lines v11-v12 on the image before seeing that answer.
- Limits of run 2: ten of the 15 code words occur once, and several words fit such a place. The reader says so.
  An exact answer with confidence "low" proves little: the two readers are models of one family and can make the
  same guess. The second reader also used the build of the code list (next point), not only the Spanish.

### A third control: the code list follows the alphabet

The second fresh reader saw that the first letter of a code word follows the first letter of its value. The
auditor tested it. The first reading did not use or name this rule.

| code words that begin with | f | g | h | l | m | n | p | r |
|---|---|---|---|---|---|---|---|---|
| values begin with | a, b | c, d | e | f, h | l, m, n | p | q, r, s | s, t, u, v, y |

- Rank correlation between the two first letters: **0.69** for the 62 code words of the key as it was (grade A
  alone: 0.99). **0 of 20,000** keys with shuffled values reach 0.69. So the code list is a one-part list in the
  order of the alphabet, and the key as a whole is right. This control does not come from the sense of the text.
- 52 of 62 values lay in the band of their code word. The ten that did not:

| code word (places) | value then | grade then | the band asks for | a value that fits band and text | what was done |
|---|---|---|---|---|---|
| `hog` (3) | venecianos | C | e | estos | changed to **estos**, grade B |
| `ren` (4) | estos | C | s to y | venecianos | changed to **Venecianos**, grade B |
| `noe` (2) | a | B | p | para: r05 "enbiaron luego por mí para notificármelo", r17 "para hablar en concordia" | changed to **para**, grade B |
| `got` (2) | piensan | B | c, d | creen or dizen (v07, v11) | kept, marked doubtful, grade C |
| `fij` (1) | esto | B | a, b | aquello (r20) | kept, marked doubtful, grade C |
| `gaf` (1) | los | C | c, d | dos or ciertos (r20); Sanuto writes "le roche di Cesena" | kept, marked doubtful, grade C |
| `fab` (2) | yo | C | a, b | none found; "yo" also fails in r09 | kept, marked doubtful, grade C |
| `pot` (1) | el | C | q, r, s | none found ("su" is `ree` in the key) | kept, marked doubtful, grade C |
| `muy` (3) | aunque | B | l, m, n | none found; the sense "though" fits all three places | kept, marked doubtful, grade C |
| `me~` (14) | por | A | l, m, n | none. "por" is certain (POR-to-gal, POR QUE). SEEN on two crops: "mp" with a stroke. The words with a stroke may be a list of their own | kept, grade A, listed as an exception |

- With `hog` and `ren` swapped the correlation is 0.76. With the corrected key (64 code words) `bands.py` gives
  0.81, and 0 of 20,000 shuffled keys reach it.
- Three tests agree on the swap: grammar (v11-v12), the blind reader, and the alphabet.
- The values in the fifth column are INFERRED by the auditor. They are not in the key.

### The reading's own controls, run again

- The shuffled-key control gave the same scores as the first notes. SEEN.
- Two small corrections: the key gives a value to 55 sign types (not 56). The decoded characters that agree
  between pass A and pass B are 89.0 % and 85.6 % for the two pages.

### Ten random tokens against the image

Ten tokens of the settled transcription were drawn at random (seed 1504) and read on the line images:
r10 no. 21 `pif`; r25 no. 4 `nez`; r32 no. 8 `n-`; v02 no. 12 `mae`; v10 no. 16 `m`; v11 no. 13 `n-`;
v11 no. 23 `gad`; v14 no. 4 `:/`; v14 no. 24 `qp`; v16 no. 25 `5`. **10 of 10 are the same.**
Limit: the auditor knew the expected token.

## 2. The facts

All sources were read in full text on archive.org on 11 October 2026.

- **Sanuto** = *I diarii di Marino Sanuto*, vol. 5 (<https://archive.org/details/idiariidimarinos05sanu>). The
  column numbers come from the OCR text. A number can be one column off. Sanuto wrote day by day in Venice. He sat
  in the College in these weeks.
- **Zurita** = *Historia del rey don Hernando el Católico*, book V, a print of the 17th century
  (<https://archive.org/details/historia-del-rey-don-hernando-el-catholico>). The folio numbers come from the
  running heads of the OCR text. They are not checked on the page images.
- **Guicciardini** = *Storia d'Italia*, ed. Panigada, vol. 2, Bari 1929
  (<https://archive.org/details/121GuicciardiniLibri58Si147>).
- **Rojas** = A. Rodríguez Villa, *Don Francisco de Rojas, embajador de los Reyes Católicos*, 1896
  (<https://archive.org/details/don-francisco-de-rojas-embajador-de-los-reyes-catolicos>).

| # | Fact in the reading | Source, place, date | Fits 24 February 1504? |
|---|---|---|---|
| 1 | A truce of three years between Spain and France; each side keeps what it holds (r02-r03) | Sanuto col. 880: a letter of the Venetian orator in France, Lyon 11 Feb, entered under 22 Feb: "è zonto di Spagna le trieve per 3 anni, con questo, chi ha si tegna". Sanuto cols. 921-922: the articles; the truce starts at Naples on 25 Feb 1504. Zurita V.65, f. 321v-322r: "por tiempo de tres años". Guicciardini VI.10, p. 137: "che ciascuno ritenesse quello possedeva" | **Fits.** SEEN |
| 2 | "Yesterday a letter reached the Venetians from the ambassador whom they have in France. They sent for me at once to tell me" (r01-r05) | Sanuto col. 880 (the letter, under 22 Feb) and col. 891, 23 Feb: "Vene l'orator yspano, al qual li fo ditto di le trieve etc. Li piaque, perchè chi ha si tegna; et lui nulla havia di questo" | **Fits.** The College told him on 23 Feb. That is "yesterday" for a letter of 24 Feb. Sanuto enters the letter from France one day before (22 Feb). SEEN |
| 3 | "They showed much pleasure. I let them think that I believed it" (r05-r07) | Sanuto col. 891: "Li piaque" (he showed that it pleased him). Sanuto col. 880: the King of France and Rouen say that the truce is "not good" | **Fits.** Sanuto saw the ambassador's outside face. The letter gives the inside. SEEN |
| 4 | "The Pope wrote me a brief, to thank me for some of what I had said here" (r22-r23) | Sanuto col. 891, 23 Feb: "disse che eri il legato li apresentò uno breve dil papa che lo ringratiava di quanto si havia operato per soa santità" | **Fits exactly** (the brief was given on 22 Feb). SEEN. This is the strongest single match |
| 5 | Venice against the Pope over Faenza and Rimini; talk of a go-between; "I will accept if they ask me" (r15-r26) | Sanuto col. 880 (Rimano e Faenza); col. 893 (24 Feb, the legate on Cesena and Rimini); cols. 899-900, 26 Feb: "Vene l'orator yspano, oferendosi medio in queste cosse tra il papa e la Signoria nostra". Rojas, doc. XXVIII (26 April 1504): the Kings order Rojas and "Lorenzo Suárez" to work "entre Su Santidad y Venecianos". Guicciardini VI: Venice offers all but Faenza and Rimini | **Fits.** One nuance: the letter says that he will not press the business before an order. Two days later he offers himself in the College. The two can stand together: he offers, he does not press. SEEN |
| 6 | "though they have had the castles of the land of Cesena" (r19-r20) | Sanuto col. 900, under 26 Feb: a letter from Faenza of 22 Feb, "hanno accordà le roche di Cesena e Bertonoro" (the Pope's side gets the castles). Sanuto col. 903 (Rome, 20 Feb): the handover is still awaited | **Fits the days.** The subject is the Pope's side, not Venice. The letter does not name it. INFERRED |
| 7 | The Pope leans to France (v02) | Sanuto col. 880 (Lyon 11 Feb, known at Venice on 22 Feb): the Pope's orator offers the King of France 300,000 ducats and men-at-arms to come back to the Kingdom, and wants Rimini and Faenza for it. Zurita V.65, f. 321: "Solo el Papa era el que osava declararse contrario". Rojas doc. XXVIII: "el Papa no haga con nos lo que debe" | **Fits.** SEEN |
| 8 | Louis d'Ars besieged in Venosa (v05) | Sanuto col. 846 (Naples, 3 Feb): "Luis d'Ars si dice è tirato a Venosa". Sanuto col. 910 (Trani, 10 and 16 Feb): "Alvise d'Ars è pur in Venosa". Zurita V.63, f. 319r-v, and V.66, f. 322v: Alviano and Pedro de Paz hold him shut in Venosa. Guicciardini VI.10, p. 134, 137 | **Fits.** SEEN |
| 9 | **Doubtful.** The Sultan's embassy, "of which it had been written that they were coming", is put off (v06-v07) | Sanuto cols. 951-952, 6 March 1504: "l'orator dil soldan venuto de qui, videlicet el guardian dil Sepulcro ... va etiam a Roma et al re di Spagna". Col. 962, 9 March: "il guardian di Jerusalem, di nation yspano" in the College. Zurita V, f. 332r: Venice sends its own envoy to the Sultan in secret | **Fits in part.** An embassy of the Sultan was expected, and it concerned Spain. It was NOT put off for long: the envoy was in Venice ten days later. Either the ambassador reports a false rumour, or the weak words of v06-v07 are wrong (`hab` = embaxada is grade C). **The line is marked doubtful** |
| 10 | "The business of Portugal"; the people "in great confusion" over the spice trade (v10-v14) | Sanuto col. 827 (Alexandria: no spices, the galleys leave empty); cols. 841-843 (copy of a letter from Lisbon: the Calicut fleet, 33,000-34,000 cantara of spices); cols. 903-905 (two caravels from India at Lisbon). Zurita V, f. 332r: "el negocio, y trato de la Especería ... yva cessando por la navegación que hazían los Portugueses a la India" | **Fits.** Zurita uses the same two words, "negocio" and "Especería", from the ambassador's letters of this year. SEEN |
| 11 | Gonzalo Fernández "is now(?) well(?), thanks be to God" (v16) | Zurita V.66, f. 322r: "una grave enfermedad ... de que llegó a punto de muerte", when he was about to leave Naples against Louis d'Ars. Sanuto col. 846 (Naples, 3 Feb): "el gran capitanio è stà amalato da cataro con febre; pigliò medecine, sta meglio". Sanuto col. 856 (Rome, before 12 Feb): "amallato et à pezorato" | **Fits.** He was gravely ill in January and February 1504. News on 24 Feb that he is well is what one expects. The two code words stay grade C. The sense is supported. INFERRED |
| 12 | Style: "por vías esquisitas" (r30) | Zurita V, f. 331v, from the ambassador's letters of 1504: "por vías muy exquisitas trataban de ponerle en alguna necessidad" | **Fits** the ambassador's own words. SEEN |

No fact contradicts 24 February 1504. The year 1504 is proved by the content: Sanuto dates the brief and the news
of the truce to 22-23 February 1504. The catalogue year (Morel-Fatio 1892) is right.

The matches 2, 3 and 4 are private details of one audience. The first reader says that it did not open Sanuto.
Nobody can prove that. If it is true, these matches are a full outside control of the key.

## 3. The search for earlier work

### (a) A period decipherment or a clear copy

| Where | What was done | Result |
|---|---|---|
| Catalogue of BnF Espagnol 318 | A. Morel-Fatio, *Catalogue des manuscrits espagnols* (1892), full text on archive.org (`cataloguedesman00monygoog`), p. 62-63 | "93. (Fol. 118-118 v°.) Lettre en chiffre de Lorenzo Suarez aux Rois Catholiques. Venise, 24 février 1504." No "Déchiffrement" item for nos. 92-95. SEEN (OCR text) |
| Real Academia de la Historia (RAH), Colección Salazar y Castro | Full text of the RAH catalogue on archive.org (`salazary-castro-22-nov-2016`, 30 MB of text): every entry with "Lorenzo Suárez" (272 lines), every entry dated February and March 1504 | Sister letters, all "en cifra", none with a decipherment: A-10 f. 17 (7 May 1503, part in cipher), **A-10 f. 20 (5 Feb 1504)**, **A-11 f. 400 (10 Feb 1504)**, A-11 f. 422 (19 Dec 1504). No entry for 24 Feb 1504. SEEN |
| Zurita, *Hernando*, book V | Read ch. 63-66 and ff. 331-332; searched the book for rostro, exquisitas, especería, Soldán, Suárez | Zurita used the ambassador's letters of 1504 in clear ("respuesta que dio Lorenço Suarez al Rey desde Venecia", f. 332r). He does not quote the letter of 24 Feb. So the court's decipherments existed. This one was not found |
| Rodríguez Villa, *Rojas* (1896) | Full text searched for the three phrases, Venosa, Lorenzo Suárez | It prints the Kings' letters to Rojas of 2 and 26 March, 26 and 30 April 1504. Not this letter |
| Rodríguez Villa, *Crónicas del Gran Capitán* (1908) | A text copy, searched | Not this letter |
| Bergenroth, *Calendar of State Papers, Spain*, vol. 1 | british-history.ac.uk, pages 324-325 (February and March 1504), through a tool that gives a summary of the page | Two entries only (nos. 392, 393, both Henry VII). No letter of Suárez |
| Archivo General de Simancas, through PARES | Three searches: "Lorenzo Suárez Figueroa Venecia 1504", "Lorenzo Suárez Figueroa embajador Venecia", "embajador Venecia 1504 cifra" | No record of this letter. This is weak: PARES describes few papers of 1504 one by one |
| CODOIN and other printed collections | Only through the full-text search of archive.org (below) | No hit |

**Not opened:**

- L. Suárez Fernández, *Política internacional de Isabel la Católica*, vol. 6 (no full text online found).
- A. de la Torre, *Documentos sobre relaciones internacionales de los Reyes Católicos*, vol. 6.
- The digital library of the RAH itself (only the text of the catalogue was used).
- The full-text search of Gallica.
- Google Books and HathiTrust (not searched).
- The two sister letters at the RAH (5 and 10 February 1504). They are the place to look next: if they are in
  this cipher, the key can be tested on them.

### (b) Three phrases, on the web and in the full text of archive.org

| Query | Hits |
|---|---|
| "alegría estaba en el rostro"; "alegria en el rostro" "dolor en el coraçon" | 0; 0 |
| "quien a Dios tiene todo tiene" | 0 |
| "quien a Dios tiene todo lo tiene" | 17, none on this letter (Molinos 1675; a sermon book cites St Bernard). The saying is real and old |
| "se declina a la parte de Francia"; "declina a la parte de Francia" | 0; 0 |
| "sitiado en Venosa"; "restituir a Faenza ni Arimino"; "Faenza ni Arimino"; "Faença ni Arimino" | 0 each |
| "Lorenzo Suarez" with Venecia, 1504, tregua, Faenza, Soldán, Luis de Ars (7 queries) | No text of this letter |

Two queries failed with a server error and were not run again: "alegria estava en el rostro" and
"alegría en el rostro y el dolor en el corazón".
Web search (3 queries with the phrases, 2 with the catalogues): no hit on this letter.

### (c) The other projects, state of 11 October 2026

| Project | State |
|---|---|
| D. Bourdeau, cyphersolver (<https://dbourdeau.github.io/cyphersolver/>) | It lists no. 93 as open, with no reading |
| NoAutopilot/cipher-lab (<https://github.com/NoAutopilot/cipher-lab>) | Its catalogue has the letter as "Open". It has no folder and no progress row for no. 93 |
| S. Tomokiyo, Cryptiana (<https://cryptiana.web.fc2.com/code/unsolved.htm>, "Last modified on 11 October 2026") | No. 93 is still under "unknown ciphers". No post on it |

Not checked on that day: el-descifrador/cabinet-noir, satoru.net/crypt, and A. Aymeloglu's list of unsolved ciphers.

## 4. The open points after the audit

- **Settled by grammar:** `ren` = Venecianos, `hog` = estos. With the old values, v11-v12 gave "Venecianos
  desdeños se muestran por estos", which is not Spanish. With the swap: "Estos desdeños se muestran por
  Venecianos, por esforçar al pueblo". Nothing is added. INFERRED.
- **Settled by grammar:** r29-r31, "Antes, o me hagan medianero o no, entiendo por vías esquisitas de trabajar
  que estén como están". Only "ante[s]" lacks a letter. INFERRED. It matters for the history: the ambassador
  means to keep the Pope and Venice apart.
- **Settled in sense by the facts (the exact word stays open):** `hu`, `hac`, `poz` in r01-r02 (ambassador,
  between, king of France). `rus fin` in v16 ("is now well"): the sense fits, and `rus` = ya does not fit its
  other place. `rud` in r29 ("servicio") and `mul` in r15 ("mal") are guesses.
- **Not settled:** r07 `gab`; r09-r10; r13-r14; r15 `gag`; v01; v14 `roo`. The Sultan's embassy in v06-v07. The
  sign `tb` in r03 and r17. Who "have had" the castles in r18-r21. In r01, no stroke is seen over `gie`, and the
  sense asks for `gie~` (del).

## 5. The fixes that the audit asked for, and what was done

| # | The audit asked | Done |
|---|---|---|
| 1 | Swap `hog` and `ren`; give both grade B; correct r01, r15, r24, r32, r33, v11, v12 and the English | Yes |
| 2 | Read r29-r30 as "Antes, o me hagan medianero o no, ..." | Yes |
| 3 | `noe` = para. Mark `got`, `fij`, `gaf`, `fab`, `pot`, `muy` with a question mark and name the other value | Yes. The six are grade C now |
| 4 | Say "91 % firm, 97 % with the probable values", not "97 % read" | Yes. The counts were made again: 91.0 % and 97.3 % |
| 5 | Put the outside sources on the page; state the year 1504 as proved by them | Yes |
| 6 | Mark as doubtful: v06-v07, v16 `rus fin`, r09-r10, r13-r14 | Yes |
| 7 | Say that the Pope's side got the castles of Cesena, or mark the subject as open | Yes, both |
| 8 | Wording: "first reading known to us, key rebuilt from the letter". Name what was searched and what was not opened. Name the two sister letters at the RAH as the next test | Yes |
| 9 | Add the alphabet rule to the notes as a control, with the ten exceptions | Yes |
| 10 | 55 valued sign types, not 56; the agreement figures 89.0 % and 85.6 % | Yes |
| 11 | State the limits of the blind audit | Yes |

Three more changes follow from the audit's part 4. `hu`, `hac` and `poz` went from grade C to grade B: Sanuto
confirms their sense, the second blind reader gave the same words, and they lie in their band. `rud` = servicio
and `mul` = mal entered the key as guesses (grade C). `rus` and `fin` stay grade C.
