# The cipher of Cardinal Scipione Gonzaga and the Duke of Nevers, 1590

**Claim: a reconstruction of the cipher system and a partial reading of one unread letter. No key sheet was found.
This is not a full decipherment.**

**Status: 3 October 2026.** The work was done by a model. An independent blind check of the marks was made (see
below). No palaeographer has checked the reading. Corrections are welcome: please open an issue.

## The documents

Paris, BnF, ms. français 4698 (Gallica `btv1b9058291p`, black-and-white microfilm). Letters in Italian from Cardinal
Scipione Gonzaga in Rome to Louis de Gonzague, Duke of Nevers, in 1590, with passages in cipher, and minutes of the
Duke's letters to the Cardinal in the same cipher. The printed BnF catalogue calls the Cardinal's letters at
ff. 30-39 "Chiffre", with no decipherment.

Pages used here: ff. 17r-v (cipher) with f. 105r (period decipherment); ff. 21v, 22r, 26r, 26v (cipher with words
written above); ff. 93r and 101r (the Duke's minutes, cipher and clear together) with ff. 97r-98r (clear copy headed
"Cif. dicifrata della mia di 31 gen. 90"); ff. 30r-31r (letter of 21 January 1590, no decipherment); f. 104r (a
cipher sheet endorsed "Con la lettera di 16 febraro 1590. R. 9 aprille 1590. Da Parigi", no decipherment).

## The system

Three layers.

1. **A word code.** A two-digit figure, 10 to 99, stands for one word in its dictionary form. A mark on the figure
   says which list the figure belongs to. Each list is a slice of one alphabetical word list (a one-part
   nomenclator). The order is by the first letters, loosely; u and v count as one letter.

| mark on the figure | slice | examples |
|---|---|---|
| none | a – av | 10 a, 16 accettare, 19 accordare, 41 altro, 49 animo, 58 arme, 70 autorità, 72 aviso |
| one dot above | c – di | 13 cavaliere, 15 certezza, 29 con, 63 cosa, 69 da, 70 danaro, 71 danno, 80 detto, 82 di |
| two dots above | du – f | 34 dubbio, 60 esperienza, 66 età, 73 fallire, 80 fatto, 87 fermo |
| two dots below | g – in | 33 giusto, 39 grande, 59 honore, 67 il, 71 impedimento, 83 in, 87 inclinare |
| bar below | in – ma | 22 ingegno, 45 intentione, 74 Lega, 79 lettera, 83 libero, 96 maggiore |
| one dot below | ma – no | 10 male, 33 medesimo, 54 mio, 72 morte, 78 mutare, 85 necessità |
| circumflex above | o – pe | 25 opinione, 57 pari |
| caron below | pi – qu | 13 piacere, 76 promettere, 81 proposta, 89 prudenza, 96 quale, 99 quello |
| circumflex above and caron below | qu – r | 11 questo, 23 ragionamento, 76 risolutione, 78 rispetto, 88 rotta |
| dot above and bar below | s | 13 sapere, 30 scritto, 34 segno, 42 servitio, 91 stato |
| bar above and dot below | su – v | 10 sua, 14 suo, 19 tacere, 26 tempo, 55 valore, 67 vero, 87 volontà, 95 utile |
| bar above and bar below | particles, a – q | 25 assai, 28 che, 30 come, 44 fino, 63 la, 68 ma, 76 non, 83 per, 87 più |
| round brackets | particles s – v, then auxiliaries, pronouns, titles | (11) se, (15) si, (16) sopra, (27) essere, (34) io, (36) lei, (50) V.E. |
| bar above | persons | 32 Papa, 44 Re di Francia, 47 Re di Spagna, 73 Umena (Mayenne) |

2. **A symbol alphabet** of about 45 signs, with several signs for each common letter, for words that are not in
   the lists. A diamond with a dot is "et".
3. **A verb sign.** An arc above a figure means: the word in the list is a noun; read the verb. The Cardinal states
   this rule in clear on f. 17v, and promises to make a new cipher when he has time.

Clear words can stand inside a cipher line. [images/marks.jpg](images/marks.jpg) shows the marks in context.
The tables are in [tables/](tables/): `lists.tsv` (glossed values by list), `interp.tsv` (interpolated values with
their windows) and `secure.tsv` (the symbol alphabet).

## How it was found

- f. 105r gives one clear word for each unit of the cipher on f. 17r-v. The words written above the cipher on
  ff. 21v, 22r, 26r and 26v, and the Duke's minutes with their clear copy, give more. Total: 152 values with a
  period gloss; 64 of them occur in two independent glosses.
- The symbol alphabet came from "habia" and "dire" on f. 105r and then from long spelled words in the unread letter.
- With about 200 values in hand, the values of each mark, sorted by figure, turned out to be in alphabetical order.
  This gives a "window" for every figure that has no gloss: its word lies between its two nearest known neighbours.

## Measured rates and their limits

- Symbol alphabet, on pages not used to build it: 23 of 26 spelled groups read as Italian words without change.
- Word code, blind: the Duke's minute f. 101r was decoded before its clear copy was read. 190 code units; the table
  of that moment proposed a value for 130; 101 of the 130 were right (78%). The clear copy is a paraphrase, so
  about 10 of the 29 misses cannot be judged.
- The alphabetical order: the 32 values learned only from f. 101r all fall in the window set by the earlier values
  (4 of them only after a paraphrase in the clear copy was replaced by a word of the window; this check is not blind).
- Order breaks. Thirteen glosses did not fit the order at first. On the images: 3 were misread glosses, 2 misread
  marks, 2 paraphrase or spelling by sound, 2 are true breaks (casa 98, alteratione 88), 4 are open.
- No further blind test was possible: every glossed page had been seen.
- Limits. The marks are small and the film is poor. The figure 1 is written like a dotted i, so a dot above 10-19
  cannot be trusted. A wrong mark gives a wrong list and a wrong word that looks real. An interpolated word is a
  choice inside a window, by sense; it is weaker than a glossed word.

## Independent blind check of the marks

A second agent read the figures and marks of 26 cipher lines (f. 30v lines 1-14 and f. 30r) without access to the
first transcription, the lists or the reading. Its two passes were saved before it opened those files. The full
report is [evidence/blind_check/phase2_report.md](evidence/blind_check/phase2_report.md).

| Measure | Value |
|---|---|
| Code units compared | 345 (330 of them blind) |
| Same figure | 332 of 345 (96 %) |
| Same mark, where the figure is the same | 273 of 332 (82 %) |
| The checker's mark names the list that the reading used | 252 of 297 (85 %) |
| ... for units with a glossed value | 92 % |
| ... for units placed by alphabetical order only | 48 of 76 (63 %) |

What this shows:

- **The rule "the mark names the list" holds.** It is well supported for nine lists: brackets 45/45, two dots
  below 22/22, plain 12/12, bar above and dot below 11/11, circumflex and caron 8/8, persons 7/7, dot above 58/64,
  two bars 54/64, dot below 6/7.
- **It is weak for four lists** on this film: two dots above 2/10, bar below 4/12, the s-list 5/11, circumflex 6/9.
  One dot against two dots, and a dot on a figure that contains a 1, cannot be decided.
- **The interpolated words are much less safe than the glossed words.** Where the first reading took a word from a
  neighbour list because the sense asked for it, the checker's mark often points elsewhere. Read strictly, the
  checker's mark gives a better word in at least 8 places (for example 87 with bar above and dot below =
  "volontieri", not {necessario}).
- Three groups of figures with the pattern a0 ab 0b look like null groups.

So: trust the spelled words and the glossed values; treat every word in {braces} as a proposal.

## The letter of 21 January 1590 (ff. 30r-31r): partial reading

Dated on f. 31r "Di Roma a xxi di Gen.o 1590". Of 431 code units on f. 30v, 67% have a glossed value, 6% a glossed
value with a doubtful mark, 13% an interpolated value, 12% none. All 67 spelled groups are read. Lines 1-18 were
read twice, lines 19-24 once.

Three kinds of words: CAPITALS = spelled in the symbol alphabet; plain = glossed code value; {braces} = interpolated.
⟨angle⟩ = supplied for sense. [..] = not read.

- "... ha dato {occasione} a {l'istesso} ⟨Amb.re⟩ di Spagna [..] di VENIRE A TROVARMI, et {dopo} {lungo} ragionamento ..."
- "... O RICHIEDERMI [..] che io PRIEGHI V.E. con {ogni} {efficacia} ... S.S.tà O RITIRARSI O INTEPIDIRSI in quello che
  lei CONOSCE essere servitio di {Iddio} ..."
- "... SO CHE BASTA a prudenza di V.E. LO ACCENNARLO ..."
- "... si ANDÒ TOCCANDO di {difficoltà} che POSSONO essere {fra} lei et Umena ..."
- "Lui VEDREBE {necessario} che V.E. FACESSE promessa di APPOGGIARSI a [..] di Re di Spagna ..."
- "... {così} PROMETTE a V.E. {quanto} {però} PUÒ PROMETTERE [..] senza {ordine} di suo {Signore}, REPLICANDOMI DUE O TRE
  VOLTE queste parole ..."
- "... È [..] cavaliere et SA PESARE E DISTINGUERE il {merito} di {persona}."
- "CONCLUSE [..] che, VOLENDO V.E. APPIGLIARSI A questo {espediente}, POTEVA TRATTARNE {sicuramente} con ⟨l'Amb.re⟩ di
  Re di Spagna che SI TROVA in Parigi ..."
- "Io ho accettato volontieri di FAR questo {officio}, PARENDOMI che la proposta POSSA TORNARE AD ALTRETANTA utile
  {quanto} honore di V.E., et tanto più la STIMO HONOREVOLE {quanto} io {porto} ferma opinione che il [..] di
  RICHIEDERLA di questo VENGA da Re di Spagna medesimo ..."
- "Né già da [..] di V.E. MILITA hora quella {ragione} di impedimento che POTEVA essere in {conscienza} VIVENTE il Re
  {defunto} {legittimo}."

**Summary.** The Spanish ambassador in Rome came to the Cardinal and asked him to press Nevers to lean on the King of
Spain. He spoke of the difficulties between Nevers and Mayenne. He promised what he could promise without an order
from his master, and repeated it two or three times; the words support general assurances only, no office and no
sum. He said that Nevers could treat of it safely with the Spanish ambassador in Paris. The Cardinal says he took
the errand willingly: he thinks the proposal as useful as it is honourable, he is sure that it comes from the King
of Spain himself, and the scruple of conscience that held while the late king lived holds no longer. He ends with
instructions on how to send letters safely (not read).

**Independent check.** The Duke's answer of 31 January 1590 survives in clear (ff. 97r-98r): "desidero essere chiaro
in qual modo intende l'Amb.re di Spagna che debba servire il Re Catt.co, sia fuor di questo Regno et in qual grado,
o vero in questo Regno et con qual intentione et carica". A later minute (f. 93r) says that he will give no answer
to "la proposta del detto Amb.re", under the pretext that the Cardinal's letters were intercepted.

## Not read

- f. 104r (21 lines, almost all word code): two single passes; the marks are not safe; no connected text.
  The checker's tentative decoding is in [reading/f104r_tentative.md](reading/f104r_tentative.md). It seems to
  continue the January business ("il servir(si) di V.E. fuori di A, ma si il VALLERSI di {opera} sua"; "A" is a sign that is not resolved).
- f. 30v line 24 and f. 30r lines 1-5, except their spelled words. A second pass of f. 30v lines 19-24 is in
  [reading/f30v_lines19-24_second_pass.md](reading/f30v_lines19-24_second_pass.md); it changes about 25 marks.
- ff. 26v, 27r, 34r, 36r-v: not started. ff. 11-16: not examined.
- The key sheet. Five candidate sheets in BnF fr. 3995 were compared (Tomokiyo's nos. 5, 32, 33, 34, 37); none
  is this cipher.

## Earlier work

Searched on 3 October 2026: D. Bourdeau's `cyphersolver` catalogue (the volume is in his queue, with another key
named; no reading), `NoAutopilot/cipher-lab`, `el-descifrador/cabinet-noir`, satoru.net/crypt, S. Tomokiyo's
Cryptiana pages on the Nevers ciphers and on unsolved ciphers, and a web search for distinctive phrases of the
reading and for a printed edition of the Cardinal's letters. No reading of these passages was found. The search
was short; a printed edition that is not online can exist. The decipherment on f. 105r is of the period; it is
reproduced here, not new.

## Contents

| Path | Content |
|---|---|
| `reading/f30_1590-01-21.md` | The partial reading of the letter of 21 January 1590, line by line, with an English summary |
| `reading/f30v_lines19-24_second_pass.md`, `reading/f104r_tentative.md` | The checker's second pass and its tentative decoding of f. 104r |
| `tables/` | The word lists, the interpolated values, the symbol alphabet, and the checker's candidate values |
| `transcription/` | The cipher transcriptions, the period decipherment of f. 105r, and the glosses of f. 26r |
| `evidence/worklog.md` | The work log, as written during the work. It names folders of the working machines; those folders are not part of this repository |
| `evidence/blind_check/` | The checker's blind passes, its report, and one row for each compared unit |
| `evidence/blind_f101r_decode.txt` | The decoding of f. 101r that was made before its clear copy was read |
| `images/` | Reduced images of f. 17v, f. 30v and f. 105r, and the sheet of marks |

## Credits

- **Satoshi Tomokiyo** catalogued the cipher keys of the Duke of Nevers in BnF fr. 3995
  ([cryptiana, "Ciphers of the Duke of Nevers"](https://cryptiana.web.fc2.com/code/nevers.htm)). We compared his
  entries with this cipher; none is its key.
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`) listed the volume as a candidate in September 2026.
- **Bibliothèque nationale de France / Gallica** provides the page images. Images here are reduced, with the
  credit "gallica.bnf.fr / BnF".
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code and tables: MIT. Text: CC BY 4.0. Images: reduced images from Gallica, under the BnF's conditions of reuse,
with the credit "gallica.bnf.fr / BnF". Details are in [LICENSE.md](LICENSE.md).
