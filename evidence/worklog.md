# Gonzaga 1590 — notes (BnF fr. 4698, Cardinal Scipione Gonzaga to the Duke of Nevers)

Session of 3 October 2026. Status: **system identified; symbol alphabet recovered; word code only partly
recovered; one unread letter (ff. 30r-v) partly read; f. 104r transcribed but not read.** No file was
committed, pushed or published.

Rule in this file: "verified" = I saw it on the image. "Inferred" = I did not.

## 1. Material (Gallica btv1b9058291p; view N = f.(N-4)v left, f.(N-3)r right)

Triage of the half pages in `img/` (contact sheets in `sheets/`):

| folio | image | letter | cipher | period gloss | my work |
|---|---|---|---|---|---|
| 17r-v | v20_R, v21_L | 16 Feb 1590 | 2 + 3 lines | f. 105r (separate sheet) | read twice; crib |
| 21v, 22r | v25_L, v25_R | (date not read) | 4 short passages | interlinear | read; check |
| 26r | v29_R | 24 Mar 1590 | about 12 short passages | interlinear | read (most); crib |
| 26v | v30_L | 24 Mar 1590 | about 22 lines | a few words | not done |
| 27r | v30_R | 24 Mar 1590 | about 10 lines | none | not done |
| 30r | v33_R | 21 Jan 1590 (check) | 6 lines | none | transcribed once, partly read |
| 30v | v34_L | same letter | 24 lines | none | transcribed once, partly read |
| 31r | v34_R | same letter | 1 line | none | not done |
| 34r | v37_R | Feb 1590 (check) | 7 + 3 lines | none | not done |
| 36r | v39_R | (not read) | 4 lines | none | not done |
| 36v | v40_L | (not read) | 5 + 2 lines | none | not done |
| 104r | v107_R | "con la lettera di 16 febraro 1590" | 21 lines | none | transcribed once, not read |
| 11-16 | views 14-20 | nos. 2-4 | ? | ? | images not fetched |

**Correction of the brief.** f. 105r is not the decipherment of f. 104r. It is the decipherment of the five
cipher lines of f. 17r-v, as the printed catalogue says (no. 44). Proof (verified): f. 17r line 1 has 29 units
and paragraph 1 of f. 105 has 29 words, one word for each unit; the code numbers 39 and 57 that the decipherer
left above "potentia ricordato" are the last two units of that line; the number 64 that he left above "credenza"
is in f. 17v line 2. So f. 104r has no answer key. f. 104v and f. 105v (v108_L, v109_L) looked blank in the thumbnails; check.

## 2. The cipher system

Three layers (all verified on f. 17r-v against f. 105r, and again on the glosses of ff. 21v, 22r, 26r):

1. **Word code.** A two-digit figure is one word, in its dictionary form. A mark on the figure selects another
   word list: plain; bar above; bar below; both bars; dot above; two dots above; dot below; two dots below;
   circumflex above; caron below; and figures in round brackets. Brackets hold pronouns, auxiliaries and
   particles ((50) V.E., (36) lei, (34) io, (35) lui, (43) S.S.tà, (45) S.A., (32) havere, (27) essere, (11) se,
   (22) troppo). A bar above holds persons (32 Papa, 44 Re di Francia, 47 Re di Spagna). The same figure with
   another mark is another word: 39 with arc = potere, (39) = sono, 39 with two dots below = grandissimo;
   10 = a, 10 with dot below = Amb.re, 10 with dot above = male. (First session: I wrote here that the lists are not alphabetical. That was WRONG. See section 15: each list is alphabetical.)
   This is why the marks matter and why a small error in a mark gives a wrong word.
2. **Symbol alphabet** (about 45 signs, homophones for all common letters) for words that are not in the code.
   See the table below. The sign "diamond with a dot" is "et".
3. **Verb sign.** An arc above a figure says: this word is a noun in the list, read the verb. Scipione explains
   it himself in clear on f. 17v (verified): "Io procurerò, come habbia un poco di tempo, che certo non l'ho, di
   formar una nuova cifra; intanto per sua maggior facilità V. Ecc. sarà avvertita, che dove io ho posto sopra il
   numero questo segno ⌒, significa che quella parola non è nome come sta nella cifra, ma verbo."
   (My reading of the hand; "maggior" and "avvertita" are abbreviated.) Examples: 39⌒ potentia -> potere,
   57⌒ ricordo -> ricordare, 64⌒ credenza -> credere, 80⌒ fatto -> fare, 60⌒ parte -> far parte.
   Nevers's decipherer did not know the rule in February: he wrote the nouns and left the numbers above them.

Clear words stand inside cipher lines ("dico che", "potendo", "sarà", "facendo", "fanno").

### Symbol alphabet (names are my ASCII names in the transcription files)

| letter | signs |
|---|---|
| a | `qo` circle with tail below; `a` diamond with stem on top; `sig` diamond with tail to the right |
| b | `tri` inverted triangle |
| c | `#` hash; `dd` double-barred upright |
| d | `=` two bars; `ll` two upright strokes |
| e | `T`; `t` (upright with bar to the right); `t2` (bar to the left); `perp` (inverted T) |
| f | `xx` double x |
| g | `ca` small caret; `gl` lambda with hook |
| h | `K` |
| i | `v` small v; `L` Lambda without bar |
| l | `F3` (F with three bars); `F3r` (mirrored) |
| m | `pi`; `xu` underlined X |
| n | `oX` circle with cross on top; `Q` circle with cross below |
| o | `phi` circle with upright; `phid` the same with a dot; `oh` circle with a level bar; `al` double loop |
| p | `R` reversed R; `gam` open loop (also read as o once: "trovarmi") |
| r | `r` lambda with long leg; `y` |
| s | `S` Sigma; `xi` three bars |
| t | `om` small omega; `om2` capital Omega |
| u, v | `E` round E; `E3` reversed E; `sh` three-pronged sign; `piv` (v in "volendo") |

Doubts: I often confused `phi`/`qo`/`phid`/`oh` (a and o) and `#`/`xx` (c and f) when I transcribed. The pair
`L r` after a consonant seems to be one sign for r ("richieder-mi", "credo", "scriver"). A second pass must fix this.
How I got the alphabet: f. 105 gives "habia" (K a tri L a, twice) and "dire" (ll v r T). The rest came from
f. 30v itself, where long words fix the values ("replicandomi due o tre volte", "stimo honorevole",
"ha voluto mostrar meco", "sa pesare e distinguere", "che volendo scrivermi").

### Word code: values with a period gloss

`secure.tsv` (values glossed in two places or more) and `code.tsv` (all values that I collected, with source;
it also holds guesses marked `ctx` — do not use those). `gloss_f26r.txt` has the word-by-word alignments of
ff. 21v, 22r and 26r. About 110 values. Useful new ones from ff. 21v-26r: 63 cosa, 14 (bar) suo, 87 (bar) volontà,
16 accettare, 49 animo, 50 gusto, 42 (underbar) servitio, 96 (underbar) maggiore, 37 conforme, 44 consentire,
51 contrario, 81 proposta, 85 necessità, 92 (dot) nocumento, 92 (underbar) presto, 75 (dot) deliberare,
(22) troppo, 22 (dot below) tanto, 86 breve, 88 rotta, 73 Umena (Mayenne), 84 (caron) protesta, 40 (underbar)
dodici, 19 città, 89 protettione, 75 Duca di Savoia.

### Key sheets in BnF fr. 3995 (Gallica btv1b525085665; images in `keys/`)

I looked at the sheets that Tomokiyo's catalogue (https://cryptiana.web.fc2.com/code/nevers.htm, fetched
3 Oct 2026) makes possible. **None is this cipher. I did not find its key sheet.**
- no. 34 and no. 33 (fol. 63r, canvas 128), no. 32 (fol. 62v, canvas 127): reconstructed alphabets of other
  ciphers ("di Parigi", "Fiorenza"). Not this one.
- no. 47 (fol. 88; 1592, Spanish names): not this one, from his description. I did not fetch the page.
- no. 37 (fol. 68-69, canvases 137-139; "Nevers 1590 Maggio"): figures 12-95 are letters, 1-100 are words,
  a bar marks names ("C. Scipion 19"). Not this cipher (there 67 = non; here 67 = il). It may be the "nuova
  cifra" that Scipione promises on f. 17v. This is a guess.
- no. 5 (fol. 11-12, canvases 28-30; 1585): a symbol alphabet with vowel signs. Not this cipher.
- no. 35 (fol. 64): figures 11-40 as letters. Not this cipher (Bourdeau's catalogue note is wrong for
  Scipione's letters; it is right for the Duke of Mantua's letters).
Not checked: the other 60 sheets of fr. 3995. The key may be there (it must list about 600 words in ten series).

## 3. What I read

- `f105_decipherment_1590.txt`: f. 105r aligned word by word with the cipher of f. 17r-v. This is the period
  reading; I reproduce it. New from me: the alignment, and the verb-sign explanation of the three left numbers.
- `reading_f30_1590-01-21.md`: ff. 30r-v, **partial**. The spelled words are read; the nouns in code mostly not.
- `reading_f104r_partial.md` and `f104_transcription.txt`: f. 104r, transcription and a skeleton. **Not read.**

## 4. Controls and measured rates

(a) Held-out tests.
- Symbol alphabet. I fixed the table (`dec.py`) on f. 30v. Then I transcribed f. 30r and f. 104r and applied it
  with no change. f. 30r: 16 of 16 spelled groups give Italian words (cagionata, andava spargendo, le haveva
  accennato, più volte, bisognava, tener, mandar, erano, dura, durerà, heroica, sede, mi prometto, verrà a
  conoscere, fa, ha dato). f. 104r: 7 of 10 groups of three signs or more (collocar, sarà, vallersi, cederle,
  siano, dice, fu dato; failed: "LEFLCI", "LCISARA", "PRE"). Together 23 of 26 = 88%.
  On f. 30v itself about 48 of 67 groups read as words with no correction; about 19 need one or two corrected
  signs (marked (?) in the reading). This count is by eye, not by script.
- Word code. I fixed the values from f. 17/f. 105 in `code.tsv` first. Then I compared them with the glosses of
  f. 21v (13 units), f. 22r (6 units) and f. 26r (about 25 units): all the units that occur in both agree
  (di, non, la, da, che, a, il, il quale, havere, Papa, parola, lei, V.E., S.S.tà, mostrare, medesimo, Amb.re,
  Re di Spagna, fatto -> fare). **This test is not blind**: the gloss is written above the cipher and I saw it.
  A try at a blind crop of f. 22r failed (I cropped the gloss by mistake). I report no blind rate for the code.
  Three figures gave another word with another mark (49, 15, 71). This is the system, not an error.
(b) Fit. The read words fit January 1590: the Pope (Sixtus V), the King of Spain, "che si trova in Parigi",
  "vivente il [..]". The glosses of f. 21v name the "rotta di Umena" (Ivry, 14 March 1590) and f. 22r the
  twelve towns of Provence that took the protection of the Duke of Savoy.
(c) Unresolved units: listed at the end of each reading file. In f. 30v 42% of the code units have no value;
  in f. 104r about 53%.
(d) Passes: f. 17r-v twice. f. 30r, f. 30v, f. 104r once. f. 26r glosses: two crops of each line, read once.
  The brief asked for two passes of f. 104r. I did one.

## 5. Prior art (checked 3 October 2026)

- D. Bourdeau, `dbourdeau/cyphersolver`: CATALOGUE.md line 78 still lists "BnF fr. 4698 nos. 2-5, 47, 92 ...
  Nevers key no. 35 (gonzaga1590)" as queued. SOLVED_CATALOGUE.md has no "4698" and no "Scipione". The folder
  `targets/gonzaga1590/` is about fr. 3979 ff. 92-93 (Mantua, key 35). Latest commit seen: 3 Oct 2026 06:07 UTC
  ("Site: 95% pushes ..."); no commit title names 4698. Copies in `prior/recheck/`.
  https://github.com/dbourdeau/cyphersolver
- `NoAutopilot/cipher-lab` PROGRESS.tsv, `el-descifrador/cabinet-noir` README, satoru.net/crypt index,
  Tomokiyo's "unsolved" page and Nevers page: no "4698", no "Scipione" (grep, copies in `prior/recheck/`).
  Tomokiyo's Nevers page lists only "no. 80 (fol. 149) Nevers to Cardinal Sipione, 1586, undeciphered" (another volume).
- Web search (3 queries): "Scipione Gonzaga" Nevers 1590 cifra "fr. 4698"; the phrases "replicandomi due o tre
  volte", "o ritirarsi o intepidirsi", "sa pesare e distinguere"; an edition of Scipione's letters to Nevers.
  Results: the BnF catalogue entry (https://archivesetmanuscrits.bnf.fr/ark:/12148/cc57748k) and biographies
  (Treccani DBI "Gonzaga, Scipione"). No edition and no decipherment found.
- Verdict: I found no prior reading of ff. 30r-v or f. 104r. The reading of f. 17r-v is the period one
  (f. 105r): "reproduced". My search was short. An edition in print that is not online can exist.

## 6. Open

1. The key sheet. Look through all of fr. 3995 (and fr. 4698 itself) for a list with ten series of 10-99.
2. More cribs. Nevers's own letters to Scipione in this volume have "chiffre et déchiffrement" (catalogue
   nos. 38-41, 54, 67-69; ff. 89-101, 120, 139-144). If Nevers used the same code, they give many more values.
   f. 26r has more glossed lines than I aligned. f. 26v has a few glossed words.
3. A second pass of f. 30v and f. 104r with a fixed sign table (a/o signs, c/f signs, the `L r` pair, the marks).
4. The unread pages: ff. 26v, 27r, 31r, 34r, 36r-v, and ff. 11-16 (views 14-20, not fetched).
5. The sign `ll'` and the figures 94, 98, 41, 86, 87, 48, 89, 93.

## 7. Files

`crop.py`, `strips.py`, `strips2.py`, `fetch.sh` (one request each 6 s, never refetches), `dec.py` (decoder),
`code.tsv`, `secure.tsv`, `gloss_f26r.txt`, `f30r_transcription.txt`, `f30v_transcription.txt`,
`f104_transcription.txt`, `f105_decipherment_1590.txt`, `reading_f30_1590-01-21.md`, `reading_f104r_partial.md`,
`crops/` (all strips), `keys/` (fr. 3995 pages), `prior/recheck/` (prior-art copies of today).
Gallica requests made today by me: 32 half pages of fr. 4698 and 13 pages of fr. 3995, one at a time.

---

# Second session (3 Oct 2026, afternoon): Nevers's own letters as cribs

## 8. Result in short

- Nevers's office used **the same word code and the same symbol alphabet** to write to Scipione. Test page: f. 93r
  (view 95 R), end of a minute of Nevers with the cipher written above the clear words: 20 values agree with
  `code.tsv` as it stood (67 il, 28= che, 42_ servitio/servire, 78d desidero, 64 credere, 63_ le, 79_ lettere, 13_ sapere,
  (11) se, 76= non, 81 proposta, 82d di, 83= per, (27) essere, 68= ma, 10 a, 10 with dot Amb.re ...). One conflict
  (80 with dot: "detto" there, "fatto" on f. 105).
- **The reply to the letter of 21 January exists in clear.** ff. 97r-98r is headed "Cif. dicifrata della mia di 31 gen. 90":
  the clear text of Nevers's cipher letter to Scipione of 31 January 1590. f. 101r (view 103 R) is the minute of the
  same letter, with the first half in cipher. It begins: "Due cose ho da dire a V.S.Ill.ma sopra quello che me ha
  scritto ultimamente; l'una che desidero essere chiaro in qual modo intende l'Amb.re di Spagna che debba servire
  il Re Catt.co, sia fuor di questo Regno et in qual grado, o vero in questo Regno et con qual intentione et
  carica ..." This confirms from an independent clear text what f. 30v says: the Spanish ambassador asked,
  through Scipione, that Nevers serve the King of Spain.
- The other "chiffre et déchiffrement" pages of Nevers (f. 120v, f. 142r) are in the unseparated-figure cipher
  (Tomokiyo no. 35 type, letters to the Duke of Mantua). They are another cipher. I did not harvest them.
- Pages fetched in this session: views 92R-105L, 123R, 124L, 142R-148L (40 half pages, one at a time, 6 s apart).

## 9. Code table

`code_v1_before_nevers.tsv`: 151 entries (first session; about 110 with a gloss, the rest guesses).
`code.tsv` now: 217 entries, 26 marked "confirmed" (seen with the same value in two independent places).
Sources are given per entry (folio and line). Conflicts are marked in the table: 70 with dot (danaro f. 105 /
autorità f. 101r), 16 (accettare / chiaro), (44) (V.S. / S.M.tà), 50 with underbar (fuori f. 101r / "come subito"
f. 26r), 14 with dot (so / bontà), 80 with dot (fatto / detto), 49 with arc (pagò f. 105, but 49 = animo three times).
I think most are two figures that differ by a mark that I cannot see on the microfilm.

## 10. Blind test (f. 101r against ff. 97r-v)

`f101r_transcription.txt` was made and decoded (`blind_f101r_decode.txt`) before I read ff. 97r-v. Lines 1, 13, 15
are left out because I had seen their clear text in a thumbnail. In lines 2-10 and 12 there are 190 code units.
The table of that moment (169 entries) proposed a value for 130 units (68%); 101 of the 130 are right (78%).
So 53% of all code units were read right, blind. The clear copy is a paraphrase, not a word-for-word gloss, so
about 10 of the 29 misses cannot be judged. Spelled words: all read (5 needed one sign fixed).

## 11. Second pass and new coverage

- f. 30v: second pass on other crops for lines 1-6 in full and parts of lines 7-10. No figure changed; seven spelled
  words became sure. Lines 11-24: one pass only. **f. 104r: no second pass (not done).**
- Coverage = code units that have a glossed value in the table (guesses marked `ctx` or "?" are not counted):

| page | code units | first table (134 glossed) | table now (203 glossed) |
|---|---|---|---|
| f. 30r | 121 | 61% | 69% |
| f. 30v | 432 | 61% | 71% |
| f. 104r | 679 | 56% | 69% |

  (The first report gave 55%, 58% and 47-49%; those used the stricter two-gloss list `secure.tsv`.)
- A value in the table is not the same as a right word: the blind test says about 78% of proposed values are right.
  So about half of the code units of f. 30v and f. 104r are read right. f. 30v is carried by its 67 spelled groups;
  f. 104r has few spelled groups and stays unread.
- Alphabet additions from Nevers's pages: the figure 10 is also used as the letter a inside a spelled word
  ("f-10-r-l-o" = farlo); mirrored F = l ("lo tengo"); there are two hash signs (c and f).

## 12. Date of ff. 30r-31r

Verified on f. 31r: "Di Roma a xxi di Gen.o 1590". Under it one cipher line, read once at low zoom:
"Questa lettera si MANDA per {via} di {l'Amb.re} di Spagna, et [..] VIENE per {via} di {S. Duca}" (braces = inferred).

## 13. Prior art, second check (3 Oct 2026, end of session)

Bourdeau CATALOGUE.md and SOLVED_CATALOGUE.md refetched: byte-identical in size to the morning copies; line 78 still
lists fr. 4698 as queued with key no. 35; no "Scipione"; latest commit still 2026-10-03T06:07:56Z. cipher-lab
PROGRESS.tsv, Tomokiyo nevers.htm and unsolved.htm refetched: no "4698", no "Scipione". Copies: `prior/recheck/*2_*`.
Note for whoever takes Bourdeau's queue item: key no. 35 does not fit Scipione's letters; it fits the Mantua
letters (ff. 120v, 142r).

## 14. Open after the second session

1. The key sheet (not found). Ten word lists by mark; the conflicts in section 9 need it or a better image.
2. A second pass of f. 30v lines 11-24 and of all of f. 104r, with attention to marks.
3. More cribs: the rest of f. 26r, the few glossed words of f. 26v, and the mixed lower half of f. 101r.
4. Unread: ff. 26v, 27r, 34r, 36r-v, 104r; ff. 11-16 not fetched.
5. What Spain offered Nevers (f. 30v lines 10-13) is in unresolved figures.

---

# Third session (3 Oct 2026): the lists are alphabetical (coordinator's finding)

## 15. List structure (`lists.tsv`, `interp.tsv`, decoder `lst.py`)

One-part alphabetical nomenclator. Figures 10-99. The mark names the slice of the alphabet:

| list | mark | slice | examples (figure word) |
|---|---|---|---|
| A | none | a – av | 10 a, 16 accettare, 19 accordare, 41 altro, 49 animo, 58 arme, 70 autorità, 72 aviso |
| C | one dot above | b/c – di | 13 cavaliere, 15 certezza, 16 chiaro, 29 con, 63 cosa, 69 da, 70 danaro, 71 danno, 80 detto, 82 di |
| E | two dots above | du – f | 34 dubbio, 60 esperienza, 66 età, 73 fallire, 80 fatto, 87 fermo |
| G | two dots below | g – in | 33 giusto, 39 grande, 50 gusto, 59 honore, 67 il, 83 in, 87 inclinare |
| I | bar below | in – ma | 22 ingegno, 45 intentione, 74 Lega, 79 lettera, 83 libero, 96 maggiore |
| M | one dot below | ma – no | 10 male, 33 medesimo, 54 mio, 72 morte, 78 mutare, 85 necessità, 95 nostro |
| O | circumflex | o – pe | 25 opinione, 57 pari |
| P | caron below | pi – qu | 13 piacere, 52 pretesto, 76 promettere, 81 proposta, 89 prudenza, 96 quale, 99 quello |
| Q | circumflex + caron | qu – r | 11 questo, 23 ragionamento, 52 ricevuta, 76 risolutione, 78 rispetto, 88 rotta |
| S | dot above + bar below | s | 13 sapere, 30 scritto, 34 segno, 42 servitio, 91 stato |
| T | bar above + dot below | su – v | 10, 14 suo, 19 tacere, 22 tanto, 26 tempo, 55 valore, 67 vero, 87 volontà |
| PT | two bars (often only the lower is visible) | particles a – q | 25 assai, 28 che, 30 come, 44 fino, 50 fuori, 63 la, 68 ma, 76 non, 83 per, 87 più, 99 quello |
| BR | round brackets | particles s – v, then auxiliaries, pronouns, titles | (11) se, (14) senza, (15) si, (16) sopra, (20) tanto, (27) essere, (34) io, (50) V.E. |
| N | bar above | persons | 32 Papa, 44 Re di Francia, 47 Re di Spagna, 55 Re, 73 Umena, 78 S. Duca |

Verified on the image for a few key units (f. 30v lines 11-14): the marks agree with the list that the word needs.
NOT verified in general: I did not go back to the images to separate every merged class. The separation above comes
from the alphabetical runs, as the coordinator proposed. The decoder marks with "*" every value that it takes from a
neighbouring list because the mark as I read it does not fit.

The old "conflicts" fall into two lists, as predicted: 70 = autorità (A) and danaro (C); 16 = accettare (A) and chiaro (C);
80 = detto (C, one dot) and fatto (E, two dots); 50 = fuori (PT), gusto (G), istesso (I), Signore (S); 14 = suo (T) and
sapienza/so (S; the clear copy paraphrases it as "bontà" and "so").

Values that break the order and that I dropped or changed (suspect, not rechecked on the image): lodare -> laudare
(71, list I; the gloss reads "laude"); guidare -> governare (34, list G; the clear copy paraphrases); attione -> età (66, E);
bontà -> sapienza (14, S); cercare -> circa (29, PT); protesta/pretesto (52, P); dropped: utile 95, casa 98, successo 12,
alteratione 88, dodici 40 (against due 40), Amb.re 10 with dot (against male 10, list M), (44) V.S. (against S.M.tà).

## 16. Counts

- Glossed values: 153 (`lists.tsv`), 64 of them seen in two independent glosses.
- Interpolated values: 43 (`interp.tsv`), each with its window; 10 of them fit two or more different contexts
  ("confirmed by context": officio, persona, quanto, istesso, mezzo, sicuro, tale, così, parola, A = Francia).
- Order test: inside each list the glossed values are in alphabetical order with no break (12 lists, 121 values) —
  after the changes listed in section 15, so this is not an independent proof for those items.
- Window test (retro, not blind): the 32 values that only f. 101r gives all fall inside the window set by the
  values known before f. 101r. 28 do so with the word of the clear copy; 4 only after I replaced the clear copy's
  paraphrase by a word of the window (governare, età, sapienza, circa).

## 17. Blind test on f. 101r again

A clean blind test is no longer possible: I have read the clear text. What I can state:
- First run (section 10): 130 values proposed, 101 right (78%), all glossed.
- With the lists, 5 of the 29 misses are corrected by window and sense alone, without the clear text
  (50 two bars = fuori, twice; 70 = autorità; (20) = tanto, twice): 106 of 130 = 82% (101 glossed + 5 interpolated).
- The other misses stay: paraphrases in the clear copy (about 10), wrong marks in my transcription, (44).

## 18. Coverage with the lists (decoder `lst.py`; files `*_decode_v3.txt`)

| page | units | glossed | glossed, mark doubtful | interpolated | unresolved |
|---|---|---|---|---|---|
| f. 30r | 121 | 66% | 10% | 6% | 16% |
| f. 30v | 432 | 66% | 6% | 12% | 13% |
| f. 104r | 679 | 61% | 8% | 7% | 22% |

f. 30v now reads as connected prose for lines 1-14 (`reading_f30_1590-01-21.md`, version 3). f. 104r does not:
see `reading_f104r_partial.md`. Not done: second pass of f. 30v lines 15-24 and of f. 104r.

## 19. Open after the third session

1. Go back to the images and settle, unit by unit, the marks of f. 104r and of f. 30v lines 15-24 (dot above / two dots,
   one bar / two bars, dot below). Without this f. 104r stays unread.
2. Recheck on the image the glosses dropped in section 15.
3. Unresolved in f. 30v: [93], (25), (38), the pair [74][80], [89], and lines 20-24.
4. Key sheet not found; unread pages as before (ff. 26v, 27r, 34r, 36r-v; ff. 11-16 not fetched).

## 20. Prior art, third check (3 Oct 2026): Bourdeau CATALOGUE/SOLVED and commits, cipher-lab PROGRESS.tsv, Tomokiyo nevers.htm refetched (prior/recheck/*3_*). Unchanged: only Bourdeau's queue line 78 names fr. 4698; no reading of these letters found.

---

# Fourth session (3 Oct 2026): checks

## 21. The glosses that broke the alphabetical order: verdict for each (crops `sheets/recheck12_1.jpg`, `_2.jpg`)

| # | gloss, figure, place | what the image shows | verdict |
|---|---|---|---|
| 1 | lodare 71 (f. 105) | the gloss word is "laude" | gloss misread by me (laudare; no break) |
| 2 | dodici 40 (f. 22r) | the gloss word is "doue/doe" (= due); figure 40 with two bars | gloss misread by me (due; no break; agrees with f. 101r) |
| 3 | protesta 52 (f. 93r) | the clear word is "pretesta" | gloss misread by me (pretesto; no break) |
| 4 | guidare 34 (f. 101r l. 6) | 34 with ONE dot above | the clear copy is a paraphrase, not a gloss; by mark the unit is in list C (con 29 .. conforme 37): "condurre" (interpolated). I had forced it into list G: withdrawn |
| 5 | attione 66 (f. 101r l. 6) | 66 with two dots, twice in the line | gloss misaligned / paraphrase: the unit is "età" both times |
| 6 | so 14 (f. 101r l. 3) | 14 with bar above and dot below | mark misread by me: it is list T, 14 = suo, used by sound for "so" |
| 7 | bontà 14 (f. 101r l. 8) | 14, no clear mark | undecided; possibly a true break (or a loose paraphrase) |
| 8 | cercare 29 (f. 101r l. 10) | 29 with two bars; "ri-29-ra" | figure and mark confirmed; either "circa" used by sound or a true break |
| 9 | utile 95 (f. 26r) | 95 with a dot below (and a bar above, seen clearly in f. 30v l. 16) | mark misread: it is list T (su – v). u and v are one letter in the order, so "utile" comes after "volontà" 87. No break. (Corrected later in the same session.) |
| 10 | casa 98 (f. 26r) | 98, gloss "casa sua" clear | **true break** (not in list C) |
| 11 | alteratione 88 (f. 21v) | gloss "alterat.e" clear; 88, mark not visible | **true break** as far as I can see |
| 12 | successo 12 (f. 17v) | not rechecked (my crop missed it) | open; by structure it fits list T (sua 10, successo 12, suo 14) |
| 13 | Amb.re 10 (f. 17v, f. 93r) | the 10 with a dot BELOW is "male" (verified, f. 17v l. 2); the 10 glossed "Amb.re" shows no mark I can see | undecided; "Amb.re" cannot be told from "a" on this film |

So, of 13 items: 3 glosses misread by me, 2 marks misread, 2 paraphrase or sound-spelling, 2 true breaks (casa 98, alteratione 88), 4 open (bontà 14, cercare 29, successo 12, Amb.re 10). The order is strong
(about 150 glossed values in order) but not perfect. I do not force it: there may be small extra lists (houses,
persons) or errors in the old key. Also seen: in line 6 of f. 101r my "76 63 66" is "75 63 66" = "ne la età" (figure
misread). **Warning on marks:** the scribes write the figure 1 like a dotted "i". A "dot above" on 10-19 cannot be
trusted on this film (this touches 13, 14, 16, 19 in lists A and C).

## 22. Marks sheet and mark recheck

`sheets/marks.jpg` (captions in `sheets/marks_captions.txt`): seven strips from ff. 17r, 17v, 30v and 101r with the
glossed or read value of each unit, so that a reader can compare the marks. It is not a grid of 3-4 isolated examples
for each list, as asked; it shows 12 of the 14 marks in context. Seen on it: 69 "da" carries a dot above (list C) in
Scipione's hand; I had transcribed it plain.
Recheck of sense-bearing code units in f. 30v: lines 1-10 were re-read in the second session (figures unchanged);
lines 11-18 now. Changes: line 16 "93 51" is one unit, 95 with bar and dot below = utile; line 17 begins with 25
circumflex = opinione (not 21); line 18: 51 with dot = contrario, 24 with circumflex and caron (list Q), 71 with two
dots below = impedimento; line 15: 87 with bar and dot below = volontà/volontieri.

## 23. Blind test: none possible

No glossed text in this cipher is left that I had not seen. ff. 89-96 and 99-100 hold clear text only, except f. 93r
(used). ff. 21v-22r and 26r were used. The five glossed phrases at the top of f. 26v were the only unused gloss; I saw
gloss and cipher together in a locator image, so the test is NOT blind. For the record, the lists give the gloss for
9 of 9 units there: "13 82 (45)" saputa di S.A.; "63 45 82 (36)" la intentione di lei; "13 69 (36)" sapere da lei
(13 with the verb arc; 69 with a dot). One unit, (44), I cannot match to its gloss.

## 24. Second pass of f. 30v lines 15-24, and f. 104r

- Lines 15-18: done (other crops). Lines 19-24: NOT done.
- f. 104r mark-by-mark second pass: NOT done. The sheet stays unread.
- Sense check for f. 104r from Nevers's side: f. 93r is the cipher end of a minute of Nevers (neighbouring pieces are
  dated April 1590; f. 104r is endorsed "R. 9 aprille 1590"). It says: "... il che gli servirà di aviso senza darne
  altro al Amb.re, perché desidero che credi che le sue lettere siano state intercette, sicome il sudetto Balbani lo
  saprà; et però se non farà risposta alla proposta del detto Amb.re, sarà per essere impertinente, ma sotto
  pretesto di non haver ricevuta le lettere di V.S., desiderando di aspettare la risolutione del Patriarca."
  So in April Nevers chose not to answer the ambassador's proposal and to pretend that Scipione's letters were
  intercepted. This fits f. 104r line 1 ("ho ⟨parlato⟩ ... con ⟨l'Amb.re⟩ di Spagna"). I did not find a clear text that
  answers f. 104r point by point.

## 25. State at the end of the fourth session

- Tables: `lists.tsv` 152 glossed values (64 in two glosses); `interp.tsv` 49 interpolated values.
- Coverage (`lst.py`): f. 30v 431 units: 67% glossed, 6% glossed with doubtful mark, 13% interpolated, 12% unresolved.
  f. 104r 679 units: 61 / 8 / 7 / 22% (unchanged: no second pass). f. 30r 121 units: 66 / 10 / 6 / 16%.
- Sense of the letter: one addition (lines 15-19). Scipione thinks the proposal "altretanta utile quanto honore", holds
  "ferma opinione" that the request comes from the King of Spain himself, and says the impediment of {conscience}
  that held "vivente il Re {defunto} {legittimo}" holds no longer.
- `README_draft.md` written for an outside reader.
- Not done in this session: step 2 in full (a grid of isolated examples for each list; mark recheck of every sense unit
  of lines 1-10 against the lists), second pass of f. 30v lines 19-24, second pass and decode of f. 104r.
- Prior art, fourth check: Bourdeau CATALOGUE/SOLVED and commits, cipher-lab PROGRESS.tsv, Tomokiyo nevers.htm
  refetched (`prior/recheck/*4_*`); see the command output of the session. No reading of these letters found.
