# Blind test: the earlier reading against the period decipherments of BnF fr. 4702

Date: 3 October 2026. The earlier reading and its tables were frozen before anyone saw fr. 4702 ff. 94-97
(`gonzaga-1590/`, local commit; working copies `lists.tsv`, `interp.tsv`, `check/checker_candidates.tsv`, `lst.py`,
all unchanged since 13:54). Nothing in those files was changed for this test.

## Method

1. **Mechanical score.** The old decoder (`lst.py`, with the old tables) decodes every code unit of the old
   transcriptions. `v2work/score.py` compares each unit with the alignment (`alignment_f30.tsv`,
   `alignment_f104.tsv`). Each unit has two reference words: the word that the clerk wrote, and the "alignment value".
   The two differ in 49 units, where the clerk's word does not fit the mark on the film and the sense (see the last
   section). One row for each unit: `v2work/blind_units.tsv`.
2. **Hand score of the printed reading** (`gonzaga-1590/reading/f30_1590-01-21.md`): the words in {braces} and the
   spelled words, counted by me against the clerk's text.

Classes of the old decoder: *glossed* = the mark names a list that has a period gloss for the figure. *Glossed, other
list* = no value in that list; the decoder took a glossed value from a list with a similar mark (shown with `*`).
*Interpolated* = no gloss; a word chosen inside an alphabetical window (`interp.tsv`). *Candidate* = the checker's
window candidates for f. 104r. A word counts as right when it is the same dictionary word.

## Result 1: letter of 21 January 1590, ff. 30r-v (549 code units)

| class | units | right against the alignment | right against the clerk |
|---|---|---|---|
| glossed | 371 | 344 (93 %) | 330 (89 %) |
| glossed, other list | 39 | 20 (51 %) | 19 |
| interpolated | 64 | 42 (66 %) | 39 (61 %) |
| unresolved | 64 | – | – |
| null figures | 9 | 8 recognised as no word | |
| units of the first pass that do not exist | 2 | – | |

- Wrong glossed values: 27. In 22 of them the transcribed mark names another list than the word needs (for example
  `80` with a dot = "bene", list a-ca, not "detto"; `74` = "molto", not "Lega"; `76` = "risolutione", not
  "promettere"). In 5 the figure 10 is "Ambasciatore", not "a"; the printed reading supplied ⟨Amb.re⟩ there.
- Wrong interpolated values: 22. 8 are near misses (the true word is in the same window: "differenza" for
  {difficoltà}, "riserva" for {rifiuto}, "consideratione" for {conscienza}, "primo" for {parola}, "principale" for
  {passo}, "poi" for {lungo}, "portare" for {ordine}). 14 are wrong because the list was wrong.
- The mechanical score includes f. 30r lines 1-5, which the printed reading left unread.

**Spelled words** (old symbol alphabet, applied by the decoder, against the clerk's words): f. 30r 17 groups, 16 exact,
1 with one or two letters wrong (126 letters, 2 errors). f. 30v 69 groups, 50 exact, 16 with one or two letters
wrong, 3 with three (665 letters, 28 errors = 96 % of letters right). The printed reading corrected these by sense:
of its 67 spelled groups on f. 30v, 62 are the clerk's words; in 3 the clerk misread the spelling
(INTEPIDIRSI / "intermidirsi", SPERAR / "sprezar", PUÒ / "poco"); 2 are open (O or A RICHIEDERMI; APPIGLIARSI or
"apuggiarsi"). One sign was not read: a single sign that the clerk gives as "Lione".

## Result 2: the printed reading, words in {braces} (58 words)

| | count | words |
|---|---|---|
| right | 41 | occasione, dopo, lungo, persona (4), efficacia, esaltatione, fede, officio (2), fra (2), principe (2), così (3), confidenza, quanto (4), però, Signore, tale (2), interesse, merito, sicuro (3), porto, forse, ragione, proposito, pericolo, mezzo (3), and ogni, Iddio, ordine (see below) |
| near miss (same window, other word) | 5 | {singolarmente} for sommamente (given as second choice), {difficoltà} for differenza, {contenti} for consolatione (second choice), {rifiuto} for riserva, {conscienza} for consideratione |
| wrong | 11 | {istesso} twice (Signore), {errore} (conveniente), {parte} (honore), {necessario} (volontieri), the second {però} (uno), {espediente} (consiglio), {defunto} (morto: same sense, other list), {legittimo} (onde), {passi} (particolarmente), {confusione} (alteratione) |
| cannot be judged | 1 | {santa}: the clerk writes "inetitud.e" before SEDE and nothing before "fede" |

Three of the 41 stand **against the clerk**: "{ogni} efficacia" (clerk: "pieno efficatia"), "servitio di {Iddio}"
(clerk: "ser.tio di Catolici") and "senza {ordine} di suo Signore" (clerk: "senza agiotam.te"). I looked at the three
units on the film (`v2work/zc1.jpg`, `zc2.jpg`, `zc3.jpg`): `21` has its mark above (circumflex = list o-pe), and the
clerk himself writes "ogni" for the same unit on f. 97r line 19; `64` has two dots below (list g-in), and the clerk
writes "Iddio" for it four times on f. 97v; for `32` the clerk writes "ordine" on f. 97v line 12. Counted strictly
against the clerk's text, the right words are 38 of 58.

Plain (glossed) words of the printed reading that were wrong: "detto" (bene), "servitio" in line 10 (integro),
"altro" in line 7 (merito), "promessa" given before "risolutione" in lines 9 and 19, "in con⟨to⟩" (in materia),
"la" in line 24 (no such unit). The summary of the letter in the README holds, with one correction: the Ambassador
did not say that Nevers must "promise"; he "would gladly see that V.E. made the resolution to lean on the favour of
the King of Spain".

## Result 3: the alphabetical window (the prediction for units with no gloss)

For each unit with no glossed value in the list that its mark names, does the true word lie between the two nearest
glossed words of that list?

| folios | units tested | inside the window | outside |
|---|---|---|---|
| ff. 30r-v, interpolated only | 61 | 47 (77 %) | 14 |
| ff. 30r-v, all units with no gloss | 148 | 89 (60 %) | 59 |
| f. 104r, interpolated and candidates | 80 | 69 (86 %) | 11 |
| f. 104r, all units with no gloss | 200 | 143 (72 %) | 57 |

Why the prediction failed: of the 116 failures, 102 have a transcribed mark that names the wrong list, 4 a wrong
figure, and 10 are something else (particles of the two-bar list that the old tables did not have in order, and the
true breaks listed in `SUMMARY_v2.md`). So the rule "one alphabetical list for each mark" is right; the reading of
the marks on the microfilm is the weak point, as the earlier report said. In the rebuilt alignment the transcribed
mark names the right list for 1,061 of 1,219 code units (87 %).

## Result 4: the cipher sheet of 16 February 1590, f. 104r (643 code units)

| class | units | right against the alignment | right against the clerk |
|---|---|---|---|
| glossed | 420 | 394 (94 %) | 383 |
| glossed, other list | 28 | 5 | 5 |
| interpolated | 50 | 36 (72 %) | 33 |
| checker's candidates | 37 | 32 (86 %) | 33 |
| unresolved | 108 | – | – |

The checker's tentative decoding (`gonzaga-1590/reading/f104r_tentative.md`) gave no connected text. Its candidates
were mostly right (nome, nascere, poco, dispositione, domanda, effetto, mano, conoscere, importare, debito, uno,
fine, honesto, gratia, giudicio, molto, vista, la quale, pensiero, Navarra, uso, ministro, costì). Wrong: {espediente}
(conveniente), "A" was read rightly as France. It missed the subject of the sheet (Champagne, the Guises,
Navarre's conversion) because the key nouns had no value.

## Where the clerk and the cipher disagree

49 units (26 on ff. 30r-v, 23 on f. 104r). Kinds:

- The clerk took the figure in another list: "benche" for `(27)` essere (twice), "così" for `(32)` havere (twice),
  "pieno" for ogni, "Catolici" for Iddio, "primo" for parola, "agiotam.te" for ordine, "curiosità" for sommo,
  "edificio" for grande, "eternamente" for il, "oscuro" for potere, "debitore" for avisato, "amicitia" for altro and for alcuno.
- He wrote "lui" for `(36)` lei four times, and "quanto" for `99` quello twice.
- He left out short words (in, che, con, per, ma, hora, non: 12 units). Once this changes the sense: f. 97v line 5
  "questo di Navarra è sicuro"; the cipher has "non È sicuro".
- He wrote "huomo" (list g-in, 63) eight times where the sense asks for "la". Here I keep his word in the tables,
  because the film shows the same mark that he read.

These judgements are mine. They rest on the film and on the sense, and a second reader should check them.
