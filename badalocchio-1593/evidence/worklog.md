# BnF fr. 4700 f. 80r: work log

Work of 11 October 2026, in two rounds. "I" in this log is the model that did the work. The words SEEN and
INFERRED mark what I saw on an image and what I concluded.

The log keeps the order of the work. Parts 3 and 5 give the state of round 1. Round 2 corrects it: parts 4, 6
and 7. Part 13 lists what was corrected when this folder was prepared.

## 1. Result in short

- The sheet is in the cipher of the Duke's minute of 1 May 1593 ([nevers-1593](../../nevers-1593/)). The key of
  the minute reads it at once in many places.
- The sheet adds values that the short minute does not have: the vowel 5 = i, the null 2, six signs, eight groups
  of two figures for syllables and words, and a table of short words with three figures.
- State: the sheet reads for about four fifths. It is not a full edition. Three stretches and all names have no
  reading.
- 919 groups; 894 have a value; 127 of them are nulls. 617 of the 792 other groups (78 %) stand in words that I
  translate. I counted these by hand.

## 2. The leaf, and the images

- SEEN: Gallica `btv1b90582908`, view 92. The left page is f. 79v, the right page is f. 80r. The folio number is
  a pencil "80", with an older "77" struck out.
- SEEN: f. 79r-v is a clear letter in a fair hand, signed "Vincenzio Badalocchio". Date line: "In Roma: il dì
  ix(?) di Gennaro: MDXCIII". My reading of the letter: [clear_letter_f79.md](clear_letter_f79.md).
- SEEN: f. 80r has 18 lines of figures in the same hand. It has no clear word and no decipherment. f. 80v is
  the address, to the Duke of Nevers (small image only).
- The images came from Gallica through a browser, as strips of the IIIF image: twelve tiles of f. 80r (three
  rows of four), three overviews, 13 tiles of the clear letter, and small images of the views 86 to 95. The
  requests went one at a time, with a pause between them.
- Each tile shows 736 by 450 pixels of the scan, inside a black frame. The frame is cut away in every image of
  this folder.
- The scan is from black-and-white film. Blots hide figures in lines 12, 17 and 18. The scan has no larger scale
  than the scale of these tiles.

## 3. Round 1: two passes, and a first cut

- Pass A (`pass_a.txt`): I read the sheet once. For lines 1-8 I had already seen that the key of the minute gave
  words, so this pass is not blind to the key. I wrote the figures as I saw them.
- Pass B (`pass_b_blind.txt`): a separate agent read the tiles blind. It gave a list of every doubtful figure.
- The two passes have the same sign in **1,561 of 1,595 places (97.9 %)**. `decode.py` counts this again.
- The first settled text (`transcription_first.txt`) is pass B, with six places of pass A.
- The first cut took every figure 1 as the head of a pair, like 4, 8 and 9. It gave 1,003 groups. With this cut
  the key of the minute alone covered 637 groups (63.5 %), and the full first key stood 7.9 standard deviations
  above 3,000 shuffled keys. The folder nevers-1593 quotes these numbers. They belong to the first cut.
- The first cut read long stretches, but about one line in four had no connected sense. The four-letter score was
  -4.69, a little worse than real Italian (median -4.14).
- The first key had values that round 2 took back: 14 = c, 18 = d, 19 = l, 15 = di, 12 = "e", and a null 80. It
  had the "open" groups 11, 13, 16, 17, 41, 81 and 82. These were wrong cuts.

## 4. Round 2: the third reading of the figures

I read the weak lines (1-3, 12, 17, 18) again on enlarged strips of the twelve tiles, and every place where the
two passes differ. The rule that I kept: a figure is not changed against a clear image. Where the Italian guided
the choice between two possible figures, the table says "sense".

| Line | First settled text | Third reading | What the image shows | Guided by |
|---|---|---|---|---|
| 6 | 14 8 8 4 6 (pass A) | **1 4 8 4 6** (pass B) | After "1 4" one 8, then 4 6. One 8 only | image; then 148 46 97 2 55 = *da es·se* |
| 6 | 8 7 4 4 4 5 9 6 (pass A) | **8 7 4 4 5 9 6** (pass B) | Two 4 before the 5, on two tiles | image; then 87 44 5 96 = *guir* |
| 7 | 1 4 5 1 4 (pass B) | **1 4 8 1 4** (pass A) | A thin figure with two small loops. 5 is possible | sense: 148 142 = *da chi* |
| 7 | 2 2 after 142 | 2 2 2 | Three 2 | image; nulls, no effect on the text |
| 12 | ? 6 after the frame | **4 6** | A round blot joined to 6. The same form stands in line 18, where *bel* needs 46 | sense |
| 12 | a sign like an epsilon with a dot (pass B) | **6** (with a stray dot) | 9 and an open 6: 96 | sense: 95 96 46 97 2 91 = *pres·ente* |
| 12 | 5 8 9 8 9 6 6 7 3 | the same figures (pass B) | 5, a blotted 8, 9, 8, 9, 6 | cut 58 98 96 6 7 3 = *si trova* |
| 17 | 5 8 9 (7) 9 6 | 5 8 9 **5** 9 6 | Pass B: "(7) joined to the 9 before it; 5 is possible" | sense: 58 95 96 48 = *si pre* |
| 18 | 83 ? 6 | 83 **4** 6 | A blot joined to 6, as in line 12 | sense: *bel* |
| 18 | ? 43 after the arch | **8** 4 3 (pass A) | A blot with two bows and a tail | sense: 84 3 = *c a* |
| 18 | 5 ? 6 | 5 ? 6 (not settled) | A large blot. 8 would give 58 6 = *si o* (occa·sio) | open |
| 3 | a sign like a theta (pass B) | the sign & (a large "et" form, pass A) | | image |
| 11 | frame "?ii" / "xiij" | frame: one blotted sign, then i and j, each with a dot | xij (12) or xxij (22) | open. 12 December 1592 is a Saturday, the day of the post |
| 11 | a dot above 188 | a round blot above the line, not the dotted stroke | | image; 188 = *io* |

Places that I checked and did not change: line 1 (all four tiles: as the passes); line 2 (as the passes); the start
of line 3, "1 5 (8) 1 4 3 (8) 9 5 9 7" (blotted; pass B kept: 158 143 89 5 97 = *fa ci l i s*); line 8, "9 7 7 3"
(two 7, pass B); line 9, "5 8 6 9 6" (pass A, as in the first settled text); the end of line 13, "3 8 4 4 9 9 4 2
4 6" (pass B is right: *con·e*); line 14, "3 9 1 5 2 9 8 3" (clear; the place has no sense yet); line 16, "2 2 9 9
7 9 8 3" (clear).

**The dotted stroke.** The sign is a short stroke with a heavy dot. A plain 1 follows it in lines 1 (first
place), 3, 4 and 5. A 3 follows it in line 1 (second place). Line 18 is damaged. INFERRED: it is the figure 1 with
a dot, and it heads a group of three figures of another table, a table of names: 117 (three times), 112, 138 and
178(?). The rows of groups write these `.17`, `.12`, `.38`, `.78`.

## 5. Round 1: the system as I first saw it

These points of round 1 stay:

- The figures 3, 5, 6 and 7 stand alone: the vowels a, i, o, u. The minute has 3, 6 and 7. It has no 5.
- 2 and 0 stand alone and are nulls. 2 is very frequent. It stands between words, before the group for "-ente",
  and between the two halves of a doubled sound (*haves·se*, *nasces·se*).
- A doubled consonant is written with nulls between the two letters: *sareb··be*, *sareb··bono*, *ef··ficaci*,
  *ap··pogio*.
- The signs (gate, C-n, arch, ring with a cross, ring on a cross) are nulls. Three of them close a passage at
  the end of line 3.
- Numbers in clear stand in a drawn frame: *segnate col numero di [frame]*.
- The older key sheet of Badalocchio (BnF fr. 3995; see nevers-1593) asks for no doubled letters and for
  nulls at the end. I read these words of the old sheet from one image, and I did not check them again. I name
  them only as a possible link of habit between the two ciphers.

## 6. Round 2: the cut rule and the key

**What was wrong.** A group that starts with 1 has THREE figures. These groups are a table of short words in the
order of the alphabet (141 che ... 197 lui). Only 12 (= ma) has two figures. 58 = si is a regular group (12
places). 29 and 39 are groups. With the new cut the four-letter score goes from -4.69 to -4.18 (real Italian:
median -4.14).

**The system (INFERRED; each rule has many places).**

- 3 5 6 7 alone = a i o u. 4x, 8x, 9x = letters (the key of the minute). 2 and 0 = nulls. Five signs = nulls.
  The triangle = z.
- 1xy = one word or syllable of a table in the order of the alphabet. The writer also uses these groups as parts
  of words: bel-LE, LA-sciata, pre-DI-ce, monar-CHI-a, FA-CI-lissimamente, DOVE-re(?), DI-cembre.
- Groups of two figures for syllables and words: 12 ma, 55 se, 58 si, 66 stato, 91 ente, 92 per; 29 (non?),
  39 (open).
- A null stands between the two halves of a doubled sound: es·se-guirsi, impos·si·bili, sareb··bono, ef··ficaci,
  ap··pogio.
- The figure 1 with a dot + two figures = a name (another table). No name is read.
- **The cut is not free of doubt in two cases:** 5 before 8 (58, or i + 8x), and 2 or 3 before 9 (29, 39, or a
  null / the letter a + 9x). `decode.py` lists each choice: four places where "5 8" is i + 8x (Milano two times,
  "cosi bel-", Sicilia), and two places where 29 and 39 are groups.
- The group 80 of round 1 is gone in line 5 (58 0). It stands once, in line 1: *potre[80]·bono*.

**The key.** The table with the places and the witness words is [`../key.tsv`](../key.tsv).

- No value: 132, 133, 138, 145, 166, 167, 181, 194, 198, 199, 100; 41, 80, 39; the names 117, 112, 138, 178; the
  sign &.
- Guesses that the order of the alphabet allows, NOT in the key: 132 al.. (altra?), 138 bene, 166 fin, 167 fosse.
- Guesses for two names, NOT in the key: 112 = the King of Spain (the clear letter says of him "poco si spera
  della vita sua"; the cipher has "la morte del [112]"); 117 = a power with "heresia" and the article "la"
  (England?).

**The order of the alphabet is a control of its own.** The 17 sure words stand in the order of their numbers:
141 che < 142 chi < 143 ci < 146 come < 148 da < 152 di < 156 egli < 157 et < 158 fa < 162 far < 175 giorno <
184 il < 185 in < 188 io < 192 la < 193 le < 197 lui. Ten of them (che, chi, ci, di, et, fa, far, il, la, le) I
fixed from the sense before I saw the order. The chance that ten values fall in order is 1 in 3.6 million. Seven
(come, da, egli, giorno, in, io, lui) I fixed with the order in mind: they are not independent.

## 7. Round 2: the controls

| Test | Result |
|---|---|
| Blind audit | A fresh agent had the cut text, the key with ten values hidden (87, 83, 93, 98, 5, 152, 141, 192, 58, 12) and the masked decode. It gave g, b, m, t, i, di, che, la, si, ma: **10 of 10**. Limit: the same family of model; the cut was given. See [blind_audit.md](blind_audit.md) |
| Groups with a value | 894 of 919 (97.3 %); 127 of them are nulls. This number proves little |
| Connected sense | 617 of the 792 groups that are not nulls (78 %) stand in words that I can translate. Without the 28 groups at the end of line 18 (probably filler): 81 %. Counted by hand, line by line (the table is in `../reading.md`) |
| Halves | The key of the minute + the values fixed in lines 1-9, on lines 10-18: 421 of 443 groups (95.0 %), score -4.07; seven values are missing (z, et, far, io, lui, dove, non). The key of the minute + the values fixed in lines 10-18, on lines 1-9: 445 of 476 (93.5 %), score -4.18; missing: per, ci, come, egli, fa, in, ben, fatto, and two signs that are nulls. Limit: I made the key on the whole sheet; "fixed in a half" means that a clear word of that half fixes the value |
| Four-letter score | Full key: -4.183 on 880 groups of four letters (real Italian: median -4.14, worst of 300 samples -4.61) |
| 3,000 shuffled keys | mean -5.96, best -5.29; the key is 8.3 sd above the mean. The letters were dealt among the 26 letter groups, the words among the 27 word groups |
| 3,000 shuffled orders | mean -5.42, best -5.21; the true order is 21.2 sd above |
| The order of the word table | 17 of 17 in order (part 6) |
| Held-out text, f. 83r (6 February 1593) | 33 groups, key unchanged: 32 with a value; "il .. di Pavia" and "co·se di Navara" read (18 of the 29 groups that are not nulls); both names stand in the clear text of that letter. "ENTE m" (two places) and "s c i u e" do not read. See [heldout_f83r.md](heldout_f83r.md) |
| Content | Part 8 |

- The score is the mean log10 probability of the groups of four letters, on a table made from Italian prose. The
  table is not in the repository. So the three rows with scores cannot be run from the repository.
- `decode.py` counts again: the groups, the agreement of the passes, the two halves (without the scores), the
  order of the word table, and the held-out passage.
- With the new cut, the key of the minute alone covers 608 of the 919 groups (66.2 %).

## 8. The content against the clear letter and against history

Fits (SEEN in the clear letter of the same bifolium):

- **Milan.** Clear: "il senato, e tutta la nobiltà stanno assai alterati, e male sodisfatti". Cipher: "lo stato di
  Milano malissimo .. s[odis]fatto", "solevatione allo stato di Milano".
- **Naples and Sicily.** Clear: unrest at Messina; the nobles of Naples "mezza solevata". Cipher: "Napoli et
  Sicilia non(?) starebbono a segno".
- **A death.** Clear: the King of Spain "con così poca sanità, che poco si spera della vita sua". Cipher: "la morte
  del [name 112]".
- **Navarre.** Clear: "detto Navara sia per farsi cattolico". Cipher: "Navara ... pure stinatamente a persevera
  alla sua heresia", "se egli havesse lasciata il primo giorno del suo regno, sarebbe ... pacifico in Francia".
- **The addressee is with the king and has standing.** Cipher: "Ella che si trova presente et con autorità ... deve
  far una buona et gagliarda rimostranza". This is the work that G. Cassiani describes: Badalocchio was the Duke's
  agent for the reconciliation of Henri IV until his death on 19 February 1593.
- "il primo giorno del suo regno" and "il quarto" (if "year" is meant): Henri IV was king from August 1589.
  January 1593 is in his fourth year.
- Standard history: the Constable of Castile came to Milan as governor at the end of 1592; Olivares was viceroy
  of Sicily; Henri IV abjured on 25 July 1593. **These three facts are from memory. I did not check them against
  a book.**

Does not fit, or is not checked:

- "la monarchia che predice il Cardano": the reading of the words is sure (groups of three figures, and letters).
  I did not find the prediction of Girolamo Cardano that is meant. G. Cassiani (2016) shows that prophecies of a
  new monarchy of Henri IV were current in Rome in 1592.
- No word "Papa", "impresa" (singular) or "conversione" stands on the sheet. "imprese" (plural) does.
- The names 117, 112 and 138 are not read. "King of Spain" and "England" are guesses.

## 9. Which piece of the volume is f. 80?

- The printed catalogue (Ancien fonds, vol. 4): "39 à 46. Lettres de Vincenzio Badalocchio au duc de Nevers. 1590,
  1592 et 1593. En italien. Chiffre. (Fol. 73 et suiv.) La seconde de ces lettres, adressée au Sr Capilupi ...".
  No. 47 starts on f. 89.
- SEEN on small images (views 86 to 95): ff. 73-88 are bifolia. Each one is a letter with its address on the last
  page: 73-74; 75-76 (the salutation is "Molt'Ill.re et R.mo Mons.r", so it is the second letter, to Capilupi);
  77-78 (16 January 1593); 79-80; 81-82; 83-84 (6 February 1593). Eight bifolia for eight numbers.
- **INFERRED by this count: ff. 79-80 is no. 42.** The catalogue gives no folio for each number.
- Views 96 to 100 are not seen.

## 10. Earlier work, checked on 11 October 2026

- D. Bourdeau's [cyphersolver](https://github.com/dbourdeau/cyphersolver): one line of its catalogue names
  fr. 4700 nos. 38-46 among the letters to do, and names Nevers key no. 35 as a key to try. Its list of solved
  letters, its catalogue data and its site index have no entry for fr. 4700 or for Badalocchio. No reading. I
  read these pages and copied nothing. Key no. 35 is not this cipher: its letters are low numbers (see
  nevers-1593).
- NoAutopilot/cipher-lab, its catalogue and its progress table: no fr. 4700, no Badalocchio.
- S. Tomokiyo: the pages that I had saved, with the page on the ciphers of the Duke of Nevers: no fr. 4700, no
  reading of a text of Badalocchio. His blog feed (the 25 newest posts, up to 11 October 2026): nothing on this.
- G. Cassiani 2014 and 2016: he cites fr. 4700 f. 67r (5 December 1592), f. 72r-v (the minute), ff. 89r-v and
  100r (Capilupi), f. 109r-v (Badalocchio, 2 January 1593). He does not cite ff. 79-80. Of Badalocchio's cipher
  he names only the draft that Bozio copied (fr. 4687 f. 89r), and he does not decode it.
- So: no reading of f. 80r by another hand, as far as I found.
- Not opened: Cassiani's later articles (2017, 2018, 2020); the lists of el-descifrador/cabinet-noir, of Satoru
  and of A. Aymeloglu; the full-text search of Gallica and of Google Books. A printed edition that is not online
  can exist.

## 11. What stays open

1. Line 3, the second half; line 17, the first half; line 18 after "occasi[on]e" (probably filler); short gaps in
   lines 1, 2, 4, 5, 8, 9, 11, 14 and 16.
2. The values 132, 133, 138, 145, 166, 167, 181, 194, 198, 199, 100, 41, 39; the four names; and the letter "n"
   after a null (five places: "·n et", "tr·n", "un·n", "spera·n", "uo·n").
3. 92 = per fits "persevera", but not "per si mostra" and "per i tr".
4. What would settle it:
   - a second pass of the held-out passage, and the other cipher sheets of Badalocchio (fr. 4700 views 96-100,
     not seen; fr. 4718 nos. 3-5; fr. 4700 nos. 32-35, of which the catalogue says "la troisième a deux parties
     en chiffre"). Each new text gives more places for the word table;
   - the key sheet of the cipher that Badalocchio sent on 9(?) September 1592, if it is in fr. 3995 or with
     Bozio's papers;
   - a colour scan of f. 80r, for the blots of lines 12, 17 and 18.

## 12. The line images of this folder

- I joined the twelve tiles into one image of the sheet. The place of each tile comes from the correlation of the
  parts that two tiles share (0.92 to 0.996).
- Each line image (`../images/line01.jpg` to `line18.jpg`) is a band of 66 pixels along one written line, made
  level. The scale is the scale of the tiles. No pixel is drawn or cleaned.
- `../images/f80r_sheet.jpg` is the joined image, reduced. It shows the written part of the sheet, not the whole
  page.
- `../images/f83r_cipher.jpg` is joined from five strips of f. 83r. The last strip had another scale and was
  reduced to fit.

## 13. Corrections made when this folder was prepared

The folder was prepared from the working notes on the same day. Three things in the notes did not agree with the
data. They are corrected or marked here, and none of them makes the result stronger.

1. **The count of line 3.** The table of counts has 19 groups "in sense" for line 3. The text of the line says
   that 24 of its 39 groups are not read, which leaves 15. The table stands as the reader made it. With 15, the
   total is 613 of 792 (77 %), not 617 (78 %).
2. **The count of the held-out passage.** The notes gave 31 groups, 30 with a value, and 18 of 27 groups in
   words (67 %). The row of groups has 33 groups, 32 with a value, and 29 that are not nulls. So the words that
   read are 18 of 29 (62 %).
3. **Sentence 3 of the summary.** The notes say that sentences 1, 2 and 4 hold gaps. Sentence 3 holds two gaps
   too, and its sense ("not as prudent as his own good asks") is a view of the reader, not the plain sense of the
   words "si mostra prudente".
