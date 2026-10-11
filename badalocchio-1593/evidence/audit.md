# The audit of 11 October 2026: the key, the cut, and the three readings

This file is the public summary of an audit. A separate agent made the audit. It did not make the readings. Its
task was to break the result. It worked from files and images on disk, from book texts on archive.org and from
two catalogue files on GitHub. It did not go back to Gallica.

"Seen" below means: the auditor read it in a file, in a book text, or on an image. "Inferred" means: it is a
conclusion. The auditor is a model. No palaeographer has checked this audit.

## The verdict in short

| Question | Answer |
|---|---|
| Is the key right? | Yes, in the mass. The letters and the two word tables hold in every test. The values with the grade "guess" (245, 246, 269) are not proved. That 199 and 299 are nulls is not proved. No name is proved by the cipher |
| Is the cut right? | Yes: the figure 2 heads a second table of three-figure groups, and a name has three figures. That a lone 2 is a null (6 places) is not proved |
| What had to change in the reading of f. 80r? | The cut rule, the key table, the Italian, the English, the counts, the title, and one sentence that was wrong: "Navara non si mostra prudente" |

## 1. The blind audit of the key: 24 of 24

The files that the reader had are in [blind_audit_2/](blind_audit_2/). Its remarks are in
[blind_audit_2/reader_notes.txt](blind_audit_2/reader_notes.txt), and the score is in
[blind_audit_2/score.txt](blind_audit_2/score.txt).

- The pool: the values that stand 3 times or more on the three letters. Nulls and names are not in the pool. It
  holds 25 letters, 11 words of table 1, 13 words of table 2 and 3 endings: 52 values.
- A random choice with a fixed seed hid 24 of them: 12 letters, 5 words of table 1, 6 words of table 2, 1 ending.
- The reader had eight files only: the three transcriptions, the cut rule as text, the key with "?" for the 24
  values, and the three decodes with a mark at each hidden place.
- The reader was a fresh agent. It worked on a copy of the package in another folder. It reports that it opened
  no other file.

**Result: 24 exact, 0 near, 0 wrong.**

| Group | Kind | Places | Key | Reader | Reader's confidence | Reader's basis |
|---|---|---|---|---|---|---|
| 7 | letter | 44 | u | u | sure | sense |
| 44 | letter | 5 | u | u | sure | sense |
| 45 | letter | 20 | a | a | sure | sense |
| 49 | letter | 15 | o | o | sure | sense |
| 84 | letter | 12 | c | c | sure | sense and order |
| 85 | letter | 21 | d | d | sure | sense and order |
| 87 | letter | 21 | g | g | sure | sense and order |
| 89 | letter | 52 | l | l | sure | sense and order |
| 94 | letter | 56 | n | n | sure | sense and order |
| 96 | letter | 78 | r | r | sure | sense and order |
| 97 | letter | 65 | s | s | sure | sense and order |
| triangle | letter | 4 | z | z | sure | sense |
| 141 | table 1 | 12 | che | che | sure | sense and order |
| 146 | table 1 | 3 | come | come | sure | sense and order |
| 148 | table 1 | 6 | da | da | sure | sense and order |
| 184 | table 1 | 7 | il | il | sure | sense and order |
| 192 | table 1 | 15 | la | la | sure | sense and order |
| 221 | table 2 | 4 | molto | molto | sure | sense and order |
| 223 | table 2 | 6 | ne | ne | sure | sense and order |
| 229 | table 2 | 7 | non | non | sure | sense and order |
| 244 | table 2 | 5 | qual | qual | sure | sense and order |
| 255 | table 2 | 10 | se | se | sure | sense and order |
| 276 | table 2 | 3 | va | va | sure | sense and order |
| 289 | ending | 5 | endo | endo | probable | sense and order |

**The limits of this test:**

1. **The reader is a model of the same family as the first reader.** The two can share a habit.
2. **The cut was given.** The test does not test the cut, and it does not test the figures.
3. **The order of the alphabet helped.** The reader used it for 19 of the 24 values. It fixed 5 values by the
   sense alone. The order cannot be hidden: the group numbers stand in the transcriptions.
4. The pool holds only values with 3 places or more. The weak values of the key are not in it: 125, 129, 149,
   164, 166, 177, 214, 232, 238, 245, 247, 269, 272, 278, 286, 296.
5. The session of the reader held a one-line index of the notes of the project (titles only, no key value). The
   reader says that it did not open the notes.
6. No wrong value came out. So there is no rival value to compare with ours.

**What the fresh reader found against the readings.** These remarks are the useful part of the test. The auditor
checked one of them on the image.

| Place | The reading had | The fresh reader | State |
|---|---|---|---|
| f. 80r line 9 | "con r a SI [145] speranza" | "con quasi": the 96 is a 99 | Inferred, and good: 99 stands for q in "quarto" and "di qua". The image is not checked |
| f. 80r line 10 | "nascesse r e l LA monarchia" | "quella": the 96 is a 99 | The same slip. The image is not checked |
| f. 80r line 17 | "u i u DI o s a" + 245 | "Dio sa quando" | Right. The first count took these groups as not read |
| f. 80r line 18 | "[25?] o NE" | 258: "oc-ca-SI-o-NE" | Right |
| f. 80r line 1 | "[167] r o" | 167 = fosse: "fossero" | A guess. It fits the order (166 fin, 169 Francia) |
| f. 80r line 1 | "potre [8] · · bono" | 83 with its 3 lost | Probable |
| f. 85r line 13 | "si ENDO far" | does not read | Seen on the tile: the figures are 2 8 9. The value "endo" fails here |
| f. 85r line 23 | "risposi f i torti" | 89 5: "li torti" | Probable |
| f. 85r line 15 | "impedita QUELLO di" | the sense asks for "quella" | The key takes 247 for both |
| f. 80r line 7 | "da chi · · · c s SE" | does not read; it also cuts 2 2 284 | Open |

## 2. The order of the alphabet

The test: the rank correlation between the number of a group and the place of its word in the alphabet, against
20,000 shuffles of the same words over the same numbers. `python3 decode.py` repeats it.

**A. All values of the key**

| Table | Words | Rank correlation | Shuffles as high | Best shuffle |
|---|---|---|---|---|
| Table 1 (1xy) | 27 | 1.000 | 0 of 20,000 | 0.664 |
| Table 2 (2xy), words | 24 | 1.000 | 0 of 20,000 | 0.730 |
| Table 2, words and the 4 endings | 28 | 0.598 | 16 of 20,000 | 0.716 |
| Both tables as one list | 51 | 1.000 | 0 of 20,000 | 0.561 |

The four endings (289 endo, 291 ente, 294 re, 296 to) stand after "vogli". They are in order among themselves.
Four values in order prove nothing: the chance is 1 in 24.

**B. Only the values that were fixed before anybody saw the order.** This is the honest form.

| Set | Values | Rank correlation | Shuffles as high | Chance of the full order |
|---|---|---|---|---|
| Table 1: the ten words of the first round (che, chi, ci, di, et, fa, far, il, la, le) | 10 | 1.000 | 0 of 20,000 | 1 in 3.6 million |
| Table 2: the five old two-figure words (12 ma, 29 non, 55 se, 58 si, 66 stato) | 5 | 1.000 | 152 of 20,000 (p = 0.008) | 1 in 120 |
| The same and 239 per | 6 | 1.000 | 37 of 20,000 (p = 0.002) | 1 in 720 |
| The ten and the five as one list | 15 | 1.000 | 0 of 20,000 | 1 in 1.3 million million |

The second row is the key fact. The first page fixed "ma, non, se, si, stato" as groups of two figures. Nobody
knew then that a 2 stands before each of them, and nobody knew of a second table. Put the 2 before them: 212,
229, 255, 258, 266. They are in the order of the alphabet, and the list goes on where table 1 stops (197 lui, then
212 ma). The reader did not choose this.

**C. All values without those that were fixed "with the order in mind".** Table 1: 13 values, in full order, 0 of
20,000 shuffles as high. Table 2: 20 words, the same. **Limit:** set C is not blind. The reader of f. 85r knew that
table 1 was in order before it fixed any new value. Only set B is free of this doubt. Set B is enough.

## 3. The cut rule

**Figures left over, or forced into a group that has no value.** Names and the two framed numbers are not
counted. "Old + T1" is the old rule with the new words of table 1 added to its key: this is fair to the old rule.
Rival A: "2xy" is a word only when 2xy is a listed word; if not, the 2 is a null. Rival B: a 2 always heads three
figures.

| Letter | Figures and signs | Old rule, old key | Old + T1 | New rule | Rival A | Rival B |
|---|---|---|---|---|---|---|
| f. 85r | 899 | 28 groups, 60 figures | 21 groups, 39 figures | **2 groups, 2 figures** | 3 groups, 5 figures | 8 groups, 18 figures |
| f. 65r | 72 | 1 group, 3 figures | 1 group, 3 figures | **0** | 0 | 0 |
| f. 80r | 1,578 | 17 groups, 44 figures | 14 groups, 35 figures | **12 groups, 28 figures** | 13 groups, 31 figures | 15 groups, 39 figures |

**A plain measure of sense.** The share of the letters that stand inside dictionary words of 4 letters or more.
The word list has 20,724 Italian word forms from six printed texts. u and v are one letter. A group with no value
breaks a word. The four-letter score is the mean score of the windows of four letters by a table of Italian. The
word list and the table are not in this repository.

| Rule | f. 85r | f. 65r | f. 80r | Four-letter score (85r / 65r / 80r) |
|---|---|---|---|---|
| Old rule, old key (the first page) | 56.3 % | 36.6 % | 58.0 % | -4.25 / -4.37 / -4.16 |
| Old rule + T1 | 59.3 % | 36.6 % | 57.8 % | -4.23 / -4.37 / -4.17 |
| **New rule, new key** | **71.8 %** | **54.3 %** | **65.6 %** | -4.06 / -3.92 / -4.01 |
| Rival A | 71.5 % | 54.3 % | 65.5 % | -4.06 / -3.92 / -4.00 |
| Rival B | 70.1 % | 54.3 % | 65.6 % | -4.06 / -3.92 / -3.99 |

The scale of the measure: the clear Italian lines of f. 85r, with the spaces removed, give 71.7 %. The period
decipherment of 11 December 1592 gives 67.3 %. The new cut with 200 shuffled keys gives 36 % in the mean and 47 %
at best. So the new cut reads at the level of real Italian of this writer. The old cut is 8 to 18 points below.

**Is the new cut the only one? By form, no. By sense, yes.**

1. The new cut has 119 groups "2xy" with a value on the three letters. At 74 of them the cut "2 = null, then
   letters" is equal by form: it leaves no new group without a value. At 45 of them the null breaks the cut.
2. In the old cut, the two-figure words 12, 55, 58, 66, 91 and 29 made sense only where the figure 2 stood right
   before them. Where no 2 stood before them, the old reading had no sense. A free null does not do this.
3. The old name groups ".17" stood three times, each time before a 6. ".12" stood before a 2. On f. 85r all seven
   strokes have 1xy after them. So a name has three figures.
4. The 74 places of point 1 are settled by the sense: the measure above, and the old gaps that close ("·n" five
   times is "re": sperare, solevare, del Re, un Re, disiderarebbe).

**What the cut does not settle: the lone 2.** The rule takes a lone 2 in 6 places: f. 85r line 13 ("non · · va")
and line 22 ("ha · molto"); f. 80r line 7 (three times) and line 18 (filler). The rival rules differ from the new
rule only at these places and at two doubtful figures. The measure cannot tell them apart. So "a lone 2 is a
null" is a choice of convenience. The places can hold groups without a value, or a slip of the pen.

## 4. The changed readings of f. 80r

The new cut changes the groups or the values in 72 places of f. 80r. The full list is
[changes_f80r.txt](changes_f80r.txt). 28 places change the cut only ("· SI" is now "SI"). 44 change a value. The
table gives every place where the words change. "Right" is judged without the image: by grammar, by the sentence,
and by the two period decipherments (D11 = 11 December 1592, D6 = 6 February 1593; see
[period_decipherments.md](period_decipherments.md)).

| # | Line | The first page | Now | Which is right, and why |
|---|---|---|---|---|
| 1 | 6 | "Navara per[ò?] si mostra prudente come diside-" (English: "Navarre [however?] shows himself prudent") | "Navara **non** si mostra prudente come disiderarebbe" | **New. Sure.** "per si mostra" is not Italian. The same figures 2 2 9 are "non" in 7 more places. The sentence goes on with a reproach: "poi che pure stinatamente persevera nella sua heresia". D11: "nientedimeno persevera heretico" |
| 2 | 5 | "la heresia del ·n [Navara?] et della [117] o r·l no[n?] così belle imprese, per i tr [..] difficili, ma impossi-" | "la heresia del **Re** et della [176] **rendono** così belle imprese **non solo** dificili ma impossibili" | **New. Sure.** A full sentence with subject, verb and "non solo ... ma". The old guess "N[avara]" falls: the word is "Re" |
| 3 | 8 | "[166] ma i[l] quarto [..], ma[..]ente per ·u· [..]; se egli" | "**fin al** quarto **anno, la qual** se egli havesse lasciata" | **New. Sure.** D11, line 1: "Volge il quarto anno che Navara fu chiamato re". "la qual ... lasciata" agrees with "heresia" |
| 4 | 9 | "sarebbe per i tr·n [..] pacifico in Francia" | "sarebbe **non solo re** pacifico in Francia, ma" | **New. Sure.** "non solo ... ma" a second time. D11: "per mettere il regno suo in pace et quiete" |
| 5 | 7-8 | "stinatamente a persevera alla sua heresia" | "stinatamente **persevera nella** sua heresia" | **New. Sure.** Grammar. D11: "persevera heretico" |
| 6 | 7 | "disidera[r]ebbe (the sheet has n for r)" | "disidera-**re**-bbe" | **New. Sure.** No slip of the writer is needed |
| 7 | 2 | "spera[r] ·n di far sole·uo·n lo stato di Milano" | "spera**re** di far sole**vare** lo stato di Milano" | **New. Sure.** Two infinitives |
| 8 | 2 | "malissimo ·i[ente]i· s[odis]fatto(?), di·o [41] ivi(?) impatro-" | "malissimo **sodisfatto di Spagna, et** i impatro-" | **New. Sure.** The clear letter of f. 79 has "male sodisfatti". One i too many stays |
| 9 | 3 | "nirse a facilissimamente" | "nirse**ne** facilissimamente" | **New. Sure** |
| 10 | 3 | 24 groups not read | "hav**endo** [176] uno esserci**to molto** temu**to** in [&] et" | **New. Probable.** It reads. The place of the army (the sign &) is open |
| 11 | 4 | "A u e n ·l· [avenendo?] la morte del [112], con e novi disgusto" | "aven**endo** la morte del [122], con **quel** novi disgusto" | **New.** "avenendo": sure (it was the old guess). "quel": a guess; "quel novi" does not agree |
| 12 | 1 | "bella ·a· che si presentasse Navara, [117] o [167]ro [138]" | "bella **occasione** che si presenta se Navara, [176] [167]ro [.38]" | **New. Probable.** Line 18 ends "così bella occasione" in letters. The three "o" after the old name group were its third figure |
| 13 | 11 | "dovere(?) in ·e·u· [..] nascere, della ·u [quale?] io le scrissi [39] mie lettere" | "dovere in **quel tempo** nascere, della **qual** io le scrissi **per** mie lettere" | **New.** "qual", "per": sure. "quel tempo": probable (both fixed with the order in mind) |
| 14 | 13 | "le·· a deve far una buona et gagliarda rimostranza con e" | "le **ne** deve far una buona et gagliarda rimostranza con **quel**" | "ne": **new, sure.** "con quel così efficaci ragioni" does not agree ("quelle" is wanted): **open** |
| 15 | 14 | "oltra la ·a[ente]i·ta del anima" | "oltra la **perdita** del anima" | **New. Sure.** D11: "per salvar l'anima sua" |
| 16 | 15 | "solevatione allo stato di Milano con l'appogio di un ·n [..] di Francia" | "solevatione **ne** lo stato di Milano con l'appogio di un **Re** di Francia" | **New. Sure** |
| 17 | 16 | "di·o per uolore·ae [..] che Napoli et Sicilia non(?) starebbono a segno" | "di **tanto valore, quando** è che Napoli et Sicilia **non** starebbono a segno" | "valore", "non": **new, sure.** "tanto", "quando": guesses. "di tanto valore quanto è" reads better here; "Dio sa quando" reads better in line 17. One group cannot be both: **open** |
| 18 | 17 | 23 groups not read | "**per li mali trattamenti di Spagna**, u i u Dio sa **quando** si presentarà già mai così bella occasione" | **New. Sure** for "per li mali trattamenti di Spagna". "u i u" is not read |
| 19 | 18 | "occasi[on]e" + filler | "oc·ca[si]o-**ne**" + filler | **New** |
| 20 | 1, 3, 5, 4 | names ".17" + o (three times), ".12" + null | names .176, .122 | **New. Sure** as a cut. The values are open |
| 21 | 1 | "potre[80]·bono" | "potre[8]··bono" | No gain. The figure is in doubt |

**Places where the old reading was better: none found.** Old words that fall: "ivi" (a guess), "N[avara?]" in
line 5, "allo stato", "a persevera alla".

**The five sentences of the first page.** Sentence 3 of its summary already said: "Navarre is not as prudent as his
own good asks". So the summary had the right sense. The Italian line and the English line under it had the wrong
one.

**The count "92 %".** 717 of 778 groups: a hand count. It counts as "in sense" six groups with guessed values
(246 three times, 245 two times, 269) and the words "in [&] et". Without them: 708 of 778, 91 %. "About nine
tenths" is fair. The measure by word list agrees: 65.6 % against 58.0 %, with real Italian at 67 %.

## 5. The facts of the readings

### 5.1 Against the same writer: the two period decipherments and his clear letters

D11 and D6 are period decipherments of two other cipher letters ([period_decipherments.md](period_decipherments.md)).
They had no part in the key. C79 = the clear letter of 9 January 1593 on the same leaf as f. 80r
([clear_letter_f79.md](clear_letter_f79.md)). The quotes are from our transcriptions: one reading by a model.

| # | Fact of the reading | Evidence of the same writer | Verdict |
|---|---|---|---|
| 1 | f. 85r: Cardinal Sforza is expected in 6 or 8 days; he comes to treat what [143] was to treat, at the instance of [124] | C79: "E finalmente venuto a Roma l'Ill.mo et R.mo S. Car.le Sforza"; the public reason is a family contract after a marriage "con una giovane parente del gran Duca di Toscana"; "puo essere che habbia da trattare qualche altra cosa più segreta" | **Fits.** Five weeks later the clear letter reports the coming, a tie to the Grand Duke, and a secret business that the writer cannot name in clear |
| 2 | f. 85r: the Pope wants the Duke to withdraw from Navarre ("che ella si ritirasse dal Navara") | D6: "me rispose che lasci Navara"; "che volesse(?) retirarsi(?) della ... navara" | **Fits.** The same demand, the same verb |
| 3 | f. 85r: Badalocchio answers with "torti et gli aggravii fattoli dall'altra parte, per che non si vedeva così ben il modo di ritirarsi" | D6: "se gli replicavo quello ch'altra volta gli ho detto ch'essendo stato cosi male trattato di quelli della lega non puo assicurarsi di loro" | **Fits, and strongly.** On 31 January he tells the Pope that he repeats what he said "another time". f. 85r is that other time: the audience of 30 November |
| 4 | f. 85r: the coming of [143] was prevented | D6: "non ascoltarebbe ne il Card.le de Gondi ne il Marchese di Pisani" | **Fits** for the matter. The decipherment names two persons |
| 5 | f. 85r: Spain wants a lady as Queen of France; a plan to make [128] King | D11: "nominato che sia un altro re de francia catolico"; D6: "si venisse alla elettione d'un altro re" | **No conflict.** The election of another king is expected. No lady and no Spain in the decipherments |
| 6 | f. 85r: Capilupi's proposal | Not in D11, D6, C79 | **Not found.** G. Cassiani (2014) has Capilupi as the Mantuan agent, and his letter to the Duke of 20 February 1593 (fr. 4700 ff. 89, 100) |
| 7 | f. 80r: Milan "malissimo sodisfatto di Spagna" | C79: the Senate and the nobles of Milan "stanno assai alterati, e male sodisfatti" | **Fits.** The same word |
| 8 | f. 80r: Naples and Sicily "non starebbono a segno" | C79: Messina "sta solevato"; at Naples the nobles are "mezza solevata" | **Fits** |
| 9 | f. 80r: "avenendo la morte del [122]" | C79: the King of Spain "con così poca sanità, che poco si spera della vita sua" | **Fits** if [122] is the King of Spain. C79 also says that the Pope "è risanato": the Pope is the other candidate |
| 10 | f. 80r: Navarre "persevera nella sua heresia fin al quarto anno" | D11: "Volge il quarto anno che Navara fu chiamato re di francia"; "nientedimeno persevera heretico" | **Fits, word for word.** This test is new: the first reading did not have "anno" |
| 11 | f. 80r: "sarebbe non solo re pacifico in Francia" | D11: "per mettere il regno suo in pace et quiete" | **Fits** |
| 12 | f. 80r: "oltra la perdita del anima" | D11: "per salvar l'anima sua" | **Fits** |
| 13 | f. 80r: "la heresia del Re et della [176]" | D11: "la regina d'Inghilterra et gli protestanti"; D6: "quelle de gl'Inglesi"; the clear letter f. 83r: "Reina d'Inghilterra" | **Fits** if [176] is the Queen of England |
| 14 | f. 80r: "la monarchia che predice il Cardano", of which he wrote on [12] December, number [47] | Not in D11 | **Not found.** D11 is the letter of 11 December. The letter of 12 December (fr. 4718 no. 4) is not seen |
| 15 | f. 85r: "Diedi domenica prossima passata ... la prima dell'advento" (clear) | Computed: 29 November 1592 is a Sunday and the first Sunday of Advent. D6: "Domenica ... l'ultima di Genaro": 31 January 1593 is a Sunday | **Fits** |

One more hint for table 1. The clerk of D11 and D6 writes "chi" where the sense wants "che". In the key, 141 che
and 142 chi are neighbours. A slip of one figure gives this fault. It is a hint, not a test.

### 5.2 Against printed history

The book texts are the full texts of archive.org. "Auditor" = the auditor read the passage in the text. "Search
agent" = a second agent read it, and the auditor did not read it again. We give the fact and the page, in our
words.

Books: L. von Pastor, *The History of the Popes*, vol. XXIII (archive.org `historyofpopesfr23past`). H. de
L'Epinois, *La Ligue et les papes*, Paris 1886 (`laligueetlespap00lepgoog`). A. Desjardins, *Négociations
diplomatiques de la France avec la Toscane*, vol. V (`collectiondedocu405unse`). R. Galluzzi, *Istoria del
Granducato di Toscana*, vol. IV (`bub_gb_VzO-HFZbsKYC`). G. Cassiani, 2014 and 2016 (references in
[nevers-1593](../../nevers-1593/)).

| # | Fact of the reading | Verdict | Source and page |
|---|---|---|---|
| 1 | Cardinal Sforza comes to Rome in December 1592 to treat a matter for France | **Not found in print.** No book names a mission of Sforza in these weeks | Related (auditor): Pastor XXIII p. 85 has Sforza among the cardinals who work against Spain in autumn 1593. Search agent: Desjardins V pp. 123 and 137 (letters to and for Sforza in 1590). So the side fits. The evidence of the fact is the clear letter of 9 January 1593 |
| 2 | The coming of [143] was prevented; Spain is against the business | **Fits**, for Cardinal Gondi | Auditor: Pastor XXIII p. 67 (Spain threatens a breach if Gondi comes to Rome); p. 68 note 1 (brief to Gondi, 6 October 1592). L'Epinois p. 573: "en empêchant Gondi de venir à Rome". Cassiani 2014 p. 407 note 86: Gondi reached Florence on 12 October 1592. Search agent: Galluzzi IV p. 163. A contrary voice: Desjardins V p. 244 (1595): the Pope names the League, not Spain |
| 3 | Spain wants a lady as Queen of France and claims the crown for her | **Fits** for the plan and for the date. The words "the crown belongs to her" are not found | Auditor: L'Epinois p. 574 (the Bishop of Lisieux from Rome, 27 October 1592, on "l'élection de l'Infante"). Pastor XXIII p. 71: Philip II proposes his daughter Isabella Clara Eugenia to the Estates in 1593 |
| 4 | "come fece in Portogallo" | **Fits** (Philip II took Portugal in 1580 on a claim of right) | Common knowledge; no page read |
| 5 | A plan to make [128] King of France, which Spain dislikes | **Fits as a frame. The person stays open** | Auditor: L'Epinois p. 574 lists the four ways that were weighed in Rome in October 1592: Navarre converted, another Bourbon prince, the Infanta, a prince of Lorraine. Galluzzi IV p. 165: Gondi must take from the Duke of Lorraine his hope to be king. Search agent: Galluzzi IV p. 167; Desjardins V p. 159 |
| 6 | The Pope knew the Duke "quando ci fu con ... Car.le Alessandrino Legato" | **Fits** | Auditor: Pastor XXIII p. 22: in 1571 Pius V sent the later Clement VIII with Cardinal Bonelli (Alessandrino) on his legation. Cassiani 2014 p. 395 note 44 prints, from the clear letter of the same day (f. 67r), that Tarugi too was in France with Cardinal Alessandrino. In f. 85r the subject of the sentence is the Pope |
| 7 | The Pope wants the Duke to leave Navarre | **Fits** | 5.1 no. 2. Auditor: Pastor XXIII p. 68 note 4: briefs of 1 February 1593 to the Catholic nobles with Navarre. L'Epinois p. 573 names the agent: Nevers charged Badalocchio in October 1592 |
| 8 | Capilupi's proposal | **Not found in print** | Search agent: Cassiani 2014 p. 393 only: Capilupi as the Mantuan agent, and his letters of February 1593 |
| 9 | Milan ill content with Spain | **Not found in print** | The clear letter of the same leaf is the evidence |
| 10 | Naples and Sicily | **Fits in part** | Search agent: Di Blasi, *Storia cronologica dei viceré* (`bub_gb_ZKSpOq2rN3gC`) pp. 258-259: a tumult at Messina in 1593, no month |
| 11 | The King of Spain near death in January 1593 | **Not found in print** | The clear letter is the evidence |
| 12 | Cardano's prophecy of a monarchy | **Not found** | Search agent: Cassiani 2016 pp. 246-247 has another prophecy in Rome in 1592. The reading of the words is sure; the prophecy is not identified |
| 13 | "fin al quarto anno"; the heresy of the King and of [176]; [176] has an army | **Fits** | Computed: Henri IV was king from 2 August 1589; January 1593 is in his fourth year. Auditor: Pastor XXIII p. 68: the Pope, at the end of January 1593, sets Navarre beside the Queen of England. Search agent: La Ferrière (`lanormandiel00lafe`) p. 323: the Queen's forces in Brittany and Normandy, October 1592 |
| 14 | Clear text of f. 85r: Cardinal Canano died; the Bishop of Reggio died some months before | **Fits** | Search agent: Eubel, *Hierarchia catholica* III (`hierarchiacathol0003vari`): Canani died on 27 November 1592; the Bishop of Reggio died in the summer of 1592 |

Not found on archive.org: Paruta's dispatches from Rome in full text; the *Mémoires de Nevers* of 1665. Paruta's
dispatches of December 1592 and January 1593 are the place to look for Sforza.

**No fact of the three readings is against the books.** Three facts stand only on the writer's own clear letter
(Milan, the King's health, Sforza's coming). Two are not found at all (Capilupi's proposal, Cardano).

### 5.3 The names

No name has a proof from the cipher. The order of the numbers does not follow the alphabet of the guesses. The
grade says what the sentence and history allow. **Settled** = history leaves one person. **Probable** = one best
person, with evidence from outside the cipher. **Open** = two persons or more.

| Group | Places | The sentence | Value | Grade | Reason |
|---|---|---|---|---|---|
| .195 | f. 85r lines 8, 10 | "vogliono far la ... regina di Francia"; "la corona di Francia appartenersi a detta ..." | The Infanta of Spain (Isabella Clara Eugenia) | **Settled as a person.** The word of the key is open (Infanta, Infante di Spagna, ...) | Spain proposed no other lady. L'Epinois p. 574 has the plan in Rome on 27 October 1592 |
| .143 | f. 85r lines 5, 15 | "le cose che dovea trattare il ..."; "come hanno impedita quella di ..." | Cardinal Gondi | **Probable (strong)** | The Pope stopped Gondi in October 1592 under a Spanish threat (Pastor p. 67). Pisani was refused in February 1593, after this letter. The decipherment of 6 February names "il Card.le de Gondi". Not settled: the group can be a short form or a title |
| .144 | f. 85r line 15 | "la venuta del ... Sforza" | The word "Cardinale" | **Probable (strong)** | Line 4 has "S.or Car.le Sforza" in clear. .143 and .144 are neighbours: two entries for cardinals fit that |
| .124 | f. 85r line 6 | "vien ad instanze del ..., qual aiuta il negotio gagliardessimamente" | The Grand Duke of Tuscany | **Probable** | Masculine and singular. Gondi asked his mediation at Florence (Pastor p. 67). The clear letter of 9 January ties Sforza's coming to a marriage with a relative of the Grand Duke. Sforza works with Tuscany in 1593 (Pastor p. 85). No book names him for December 1592 |
| .122 | f. 80r line 4 | "avenendo la morte del ..." | The King of Spain | **Probable** | The clear letter of the same day: "poco si spera della vita sua". The sentence is on a rising against Spain. The Pope was ill too, and "è risanato" |
| .176 | f. 80r lines 1, 3, 5 | "se Navara, ... [167]ro [.38]"; "havendo ... uno essercito molto temuto in [&]"; "la heresia del Re et della ..." | The Queen of England, or England | **Probable** | Feminine, a heretic, an ally with an army. The decipherment of 11 December: "la regina d'Inghilterra et gli protestanti". The Pope in January 1593 sets Navarre beside the Queen of England (Pastor p. 68) |
| .128 | f. 85r line 13 | "è che si [..] far ... re di Francia, la qual cosa non va per la fantasia a Spagna" | Open | **Open** | By the books the plan of Gondi and of Tuscany was Navarre, once converted. But the writer spells "Navara" in letters in the same letter (line 22) and on f. 80r. The second candidate is the Cardinal of Bourbon-Vendôme. Lorraine is less probable: Tuscany worked against his claim (Galluzzi IV p. 165) |
| .133 | f. 65r line 1 | "tutto quello che io ho passato col ... per suo conto di lei" | Open | **Open** | History does not help |
| .38, .78 | f. 80r lines 1, 18 | two figures after the stroke | Open | **Open** | .38 can be a word and not a name |

Who was "impedito" before December 1592? Cardinal Gondi: settled by Pastor, L'Epinois and Cassiani. Who wanted to
make whom Queen? Spain, the Infanta: settled. Who was to be made King? Not settled.

## 6. Earlier work for f. 85r and f. 65r (checked on 11 October 2026)

| Source | How read | Result |
|---|---|---|
| `NoAutopilot/cipher-lab`, its catalogue file | Read on 11 October 2026 | No "4700", no "Badalocchio", no letter of 1592 of this agent |
| D. Bourdeau, [cyphersolver](https://github.com/dbourdeau/cyphersolver), its two catalogue files | Read on 11 October 2026; nothing copied | One line lists fr. 4700 nos. 38-46 among the letters to do. No reading |
| S. Tomokiyo, the pages that we had saved | Read | "Badaloc" stands on no page. The saved copies can be old |
| G. Cassiani 2014 | Read | He cites fr. 4700 f. 67r, the clear letter of Badalocchio of 5 December 1592, two times: the news of Tarugi, Avignon and Cavaillon. He cites no f. 85 and no f. 65. He quotes no cipher and no reading of cipher |
| G. Cassiani 2016 | Read | fr. 4700 f. 72r-v only. No cipher of Badalocchio |
| Period decipherments | See [period_decipherments.md](period_decipherments.md) | None found for 5 December. The decipherment of 11 December is of another letter of that day, not of the two runs of f. 65r |

**Result:** no reading of the cipher part of f. 85r or of f. 65r by another hand, as far as the audit found. Not
opened: Cassiani's later articles, the full-text search of Gallica, Google Books, the newest pages of S. Tomokiyo.

## 7. What the key must not claim

| Value | State after the audit |
|---|---|
| 245 | "quando" fits line 17 of f. 80r ("Dio sa quando"). "quanto" fits line 16 ("di tanto valore quanto è"). Open between the two |
| 246 | "quel" fits two places. In two places the sense wants "quei" or "quelle". Accept "quel-" as a stem, as 247 and 244 |
| 269, 272 | One place each. A guess and a probable value |
| 289 | "endo" in four places. It fails in f. 85r line 13 ("si ENDO far"). The figures there are 2 8 9 on the tile |
| 169 | "Francia" in three places. The fourth (after "Portogallo") has a blot and no sense |
| 199, 299 | "Null" is not proved. "come ci si [199] adoperare" speaks against it. They are printed as groups with no value |
| the lone 2 | Not proved as a null |
| 135, 154, 163 | Sure: each has a place on two letters now |
| Names | No value in the key. Grades in 5.3 |

Two slips of transcription on f. 80r are probable (inferred; the image is not checked): 96 for 99 in line 9 ("con
quasi") and in line 10 ("quella monarchia").
