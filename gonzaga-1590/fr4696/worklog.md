# BnF fr. 4696 — notes (letters of Scipione Gonzaga to Nevers, Rome, 1585-1589)

Session of 4 October 2026. Gallica `btv1b9059540q`, black-and-white film, 250 views, ONE page for each view
(about 3950 x 5700 px). View = 2 x folio + 1 at the start (f. 12r = view 25) and 2 x folio + 3 at the end
(f. 122r = view 247). "Seen" = on a page image. "Inferred" = not seen.

## Log

- 13:53 manifest; fetch daemon (`fetchd.py`, then `fetchd2.py`: one request, 11 s apart, retry after an error).
  One HTTP 429 at 13:59 (several agents on Gallica); none after the pause was raised.
- Overviews of all views at 900 px in `ov/`; full pages of the cipher pages in `img/`.
- Survey: `survey_coordinator.tsv` (my own rows), `survey_*.tsv` (survey agents).
- Transcriptions in `tr/`. Briefs for the agents: `BRIEF.md`, `SURVEY_BRIEF.md`.

## What the Cardinal says about the cipher (seen, my reading of his hand)

- f. 3v, 18 Nov 1585: "Rivedendo io la cifra mi sono avveduto d'haver fatto un errore alla l[ette]ra S, che è, di
  non haver posto numero alla parola Suizzeri. Però parendo così a V. Ecc. potrà ordinare, che vi sia posto il
  num.o 57, che è posto alla seguente, et a questa il 58, et così di mano in mano, sì che finisca nel num.o 68,
  dove prima finiva nel 67. Alla cifra delle clausule ancora ho notato, che due volte si replica Mi rallegro ...
  dove si leggono queste parole al num.o 90 si può mettere in luogo loro, Sto con buona speranza".
  So in November 1585 the cipher was new, the Cardinal made it, and it had a numbered word list by letter and
  a numbered list of phrases ("clausule").
- f. 12r, February 1586: "Ho inteso la parola aggiunta alla cifra ... Sarà necessario aggiungere molti nomi".
- f. 15v, March 1586: "Ho aggiunto alla cifra i due nomi, che V. Ecc. mi ha scritto, et io mando a lei molte
  altre parole per fare il medesimo, se così le parerà, poi che lodando ella che si scrivano le cose di maggior
  importanza senza alcuna interpositione di parole fuori di cifra, così la fatica riuscirà molto minore."
- f. 120r, 18 Nov 1589: he got "una lettera di V. Ecc. con un lungo foglio di cifra sotto il dì ... 8 d'ottobre"
  and "la fatica fatta nel dicifrare" hurt his back, so he writes "compendiosamente".
- fr. 4698 f. 17v, February 1590 (earlier project): he promises "una nuova cifra" when he has time.
- fr. 4698 f. 179r, Nevers, 9 July 1590: Nevers describes a way to dictate figures with "ponti" and says that he
  sent "uno novo alfabeto" that he will not use before he knows that it arrived.

## Question 1: is the cipher of 1585-1589 the cipher of 1590? (answer written 18:05, 4 Oct 2026)

**Yes. It is one cipher. The Cardinal made it in 1585 and it grew. No change of cipher was found inside the volume
(in the pages seen so far; the survey of views 40 to 119 is not finished).**

Evidence (all seen on page images; the values of 1590 are those of `gonzaga-1590/tables/lists_v3.tsv`):

1. **The symbol alphabet is the same from the first cipher page to the last.** f. 5r (December 1585), f. 12r
   (February 1586), f. 82r (October 1588), f. 113r (September 1589) and f. 122r-v (18 November 1589) use the signs
   of fr. 4698: T / inverted T = e, small v / Lambda = i, Sigma / 3 = s, lambda / y = r, Omega / small omega = t,
   pi = m, K = h, F = l, two bars / two uprights = d, hash = c, phi = o, diamond / q-circle = a, reversed R = p,
   inverted triangle = b, round E = u, circle with cross = n, box or diamond with a dot = "et".
   The glosses above the cipher prove each value (for example f. 122r "pensiero", "adherir", "buonissimo fine").
2. **The names list (bar above) of 1590 is already there in 1585-1586 with the same figures.** f. 5r (Dec 1585):
   47 = Re di Spagna. f. 12r (Feb 1586): 32 with a bar above = Papa; 71 = Duca di Guisa. In 1590: N 47 Re di Spagna,
   N 32 Papa, N 71 Guisa. In 1586 other persons are plain figures (28 = C. d'Este, 31 = Card. Farnese; f. 15v:
   42, 12, 95 = three persons).
3. **The word code of 1590 is in full use in 1588-1589.** f. 82r (30 October 1588): 88 with two bars "più tosto",
   28 with two bars "che", 76 with two bars "non", 83 "per", 27 = Card. di Gioiosa. f. 100v-101r (10 July 1589):
   half of the cipher is figures with dots, bars, roofs, small v and brackets. f. 113r (September 1589): five lines,
   64 figures with all the marks of 1590. f. 122r-v (18 November 1589): 101 figures; 85 have the value of lists_v3
   under the list that the mark names (first agent pass, before corrections; see the agreement test below).
4. **How it grew.** 1585-1586: alphabet, a list of names, a list of "clausule"; small words are spelled
   ("che" = hash K e). March 1586: the Cardinal sends "molte altre parole" to add. 1587: short runs of signs.
   October 1588: small words by figure with two bars. July 1589: content words by figure with dots. 1590 (fr. 4698):
   nearly all figures. The exact month in which the lists with marks begin lies between April 1587 (f. 65) and
   October 1588 (f. 82); the pages between them hold almost no cipher.
5. The Cardinal's own words agree (see above): he made the cipher in 1585, added words in 1586, and in February
   1590 he still only promises a new one.

So fr. 4696 is an answer key for the cipher of fr. 4698. The limit: most letters of the volume are clear; the cipher
pages are few (see the survey), and before 1588 the glosses give letters of the alphabet and names, not code words.

## Two-pass agreement on runs with no gloss (measured 18:15)

f. 113r (September 1589), pass 1 = coordinator (`tr/f113r_pass1.txt`, knew lists_v3), pass B = blind agent
(`tr/unglossed_passB.tsv`, saw no table): 64 figures. Same figure: 63 of 64 (98 %; the one difference is 67 / 61 in
line 5). Same mark among those: 56 of 63 (89 %; the differences: 10 plain / dot twice, 83 two bars / bar below,
78 bar+caron / roof+caron, 54 dot below / dot above and below, 21 one dot / two dots, 83 plain / two dots below).
Spelled words: the same words in both passes, except three stretches (line 2 "GLI PUO"?, line 4 "SOPRA CIO"?,
line 5 last word).

## Which Nevers letters are online (question 4)

SRU on 4 Oct 2026, 17:10 UTC, query `(dc.source all "NNNN") and (dc.type all "manuscrit")`, records listed in
`prior/sru_*.xml`: no record with source "Français 3612", "Français 3375", "Français 4697" or "Français 4701"
(the hits are Latin, Arabe, Pelliot, NAF). The scout's three other query forms gave the same (scout3/sru.tsv).
cipher-lab says "fr.3612 not digitised" (NEVERS-VEIN.tsv, row 20). So fr. 3612 f. 149, fr. 3375 ff. 143, 145,
fr. 4697 nos. 16-17, 23, 26 and fr. 4701 nos. 9, 22 are BLOCKED: no images. What unblocks them: a BnF
digitisation order, or the reading room.
Online: fr. 4698 no. 47 (f. 108r, 28 Feb 1590) and no. 93 (f. 179r, 9 July 1590). Seen and transcribed (below).
No period decipherment of these two was found: not in fr. 4698 (catalogue rows), not in fr. 4702 ff. 90-110
(survey of the earlier project). fr. 4702 beyond ff. 90-110 was not searched page by page.

## Prior art (4 Oct 2026, 13:17 UTC, copies in `prior/`)

No "4696" and no "Scipione" in: Bourdeau CATALOGUE.md and SOLVED_CATALOGUE.md, cipher-lab PROGRESS.tsv and
NEVERS-VEIN.tsv, cabinet-noir README, aaymeloglu README. Bourdeau CATALOGUE.md line 78 lists "BnF fr. 4698
nos. 2-5, 47, 92" as queued with key no. 35 (no reading). Tomokiyo (nevers.htm, copy of scout3) names only
fr. 3612 no. 80 as "undeciphered". Not done: a web search for phrases of the plain text.

## Question 1, second part: where the cipher changes (added 18:25 from the survey of views 40-119; quotes read by the survey agent on 900-px images, NOT yet checked by me at full size)

The ALPHABET does not change. The WORD CODE was replaced once, in summer 1586:
- f. 22v (19 May 1586): "Ho veduto la correttione che V. Ecc. ha fatto all'augumentatione della Cifra che ultimamente
  le mandai ... ho trasportato molte voci semplici ch'erano nella prima in questa seconda cifra".
- f. 28r-v (28 July 1586): "preso a rinovar la Cifra delle parole ... mi è riuscita un mezo Calepino volgare ...
  ridotta a ordine seguitato d'Alfabeto".
- f. 32v (11? August 1586): "appresento a V. Ecc. la Cifra de' nomi ... un mezo Dittionario ... nell'Alfabeto si è
  servato quel più esquisito ordine che si poteva. ... si dovranno cassar le due prime, cioè quella delle clausule,
  che si scrisse in presenza di lei, et quella de' nomi, che poi le si mandò."
- f. 39r (6 October 1586): Nevers finds it difficult. f. 44r (17 Nov 1586): Nevers "havesse già stracciata la prima Cifra".
- f. 49v (15 December 1586): "usar più tosto quella dell'Alfabeto, che quella de' nomi, fuor che in cose di
  grandissima importanza".
So: the alphabetical "half dictionary" of August 1586 is the word code that we rebuilt for 1590 (to be tested on the
glossed pages of October to December 1586: ff. 38v-39v, 44v, 46v). Brackets and bars on figures begin on f. 38v
(6 October 1586). Before August 1586 the figures (plain, often in groups of four digits) belong to the two first
lists, which were cancelled. The order of December 1586 explains why most cipher of 1587-1589 is spelled with the
alphabet and why the word code comes back for the grave matters of July and September 1589 and of 1590.
ff. 54-55 (no date): a separate piece in ANOTHER cipher (one unbroken string of digits, another hand, with gloss):
it says that the letters in cipher are read "sapendosi la zifra" and that the Duke should change it.

## Runs with no gloss (question 3), state at 18:27

| Folio | Letter | Run | Passes | Agreement |
|---|---|---|---|---|
| f. 113r | [end of Sept 1589] | 5 lines, 64 figures + 10 spelled words | 2 (coordinator; blind agent) | figure 98 %, mark 89 % |
| ff. 62r, 62v | March 1587 | 27 short runs, 343 signs, 3 name figures | 2 blind agents | letters 99.7 % (378 of 379 with f. 65r) |
| f. 65r | 5 April 1587 | 3 runs, 36 signs, 1 name figure | 2 blind agents | as above |
| ff. 42v, 43r | 3 Nov 1586 | 5 runs, figures with marks | 2 agents (running) | |
| ff. 48v, 51r, 51v | Dec 1586 | short runs and lone figures | 2 agents (running) | |
| ff. 30r-32r, 34r, 36v-37v | Aug-Sept 1586 | short rows of plain figures, partly glossed | not transcribed | the survey (900 px) lists them |

fr. 4698 f. 108r lines 1-2 (Nevers, 28 Feb 1590): coordinator pass against blind pass B: figure 35 of 38 (92 %),
mark 26 of 35 (74 %). My pass was at low zoom; a third look at line 1 at high zoom agrees with pass B (8 written as
loop + stroke: "80", not "10"). Lines 3-5: pass B only, with a partial look by me. This letter needs a third pass.

## Question 1, test (added 18:45): the word code of October 1586 is the word code of 1590

The glossed pages of 6 October, 17 November and 1 December 1586 (ff. 38v, 39r, 39v, 44v, 46v) were transcribed by
agents that saw no table. 239 figures: for the units whose figure and list are in lists_v3, the gloss gives the
lists_v3 word at the same rate as the pages of 1589 (see the table). So the "mezo Dittionario" that the Cardinal
sent on 11 August 1586 is the code of fr. 4698. The cipher did NOT change between October 1586 and 1590.
Before August 1586: the same alphabet, with two older lists (plain figures, often in groups of four digits), which
he cancelled. Names changed with them: 31 = Card. Farnese in February 1586 (f. 12r), 31 = Nuncio in October 1586.

## Question 2: harvest and agreement test

Pages harvested (first pass by blind agents; one pass each; `tr/*_passA.tsv`): f. 122r-v (18 Nov 1589), f. 100v-101r
(10 July 1589), f. 82r (30 Oct 1588), f. 76v (10 Aug 1587), f. 46v (1 Dec 1586), f. 44v (17 Nov 1586), ff. 38v-39v
(6 Oct 1586). 587 figure units; 572 with a gloss. Files: `harvest_units.tsv` (automatic score), `manual.tsv` (my
verdict for each unit that did not agree at once; I knew lists_v3, so this step is not blind), `harvest_judged.tsv`.

Result (`agreement_table.md`): 463 units have a figure whose word is in lists_v3.
- The gloss is the lists_v3 word: 452 of 463 = 97.6 %.
- The gloss is the lists_v3 word AND the mark that the agent read names that list: 408 of 463 = 88.1 %
  (the earlier project measured 87 % for the mark on fr. 4698).
- Near misses 10 (the clerk wrote "di" for C 69 "da" five times; a figure one off; "qualità" for "quale").
- One conflict: O 87 "perfidia" (f. 100v) against "pericolo" (lists_v3, from one place in fr. 4702). They are
  neighbours in the alphabet; the figure of one of them is one off, or lists_v3 is wrong there.
- Left out: 25 units where the gloss or its alignment is not safe (listed with ALIGN in `harvest_judged.tsv`),
  15 with no gloss.
By list: see the table. Lists A and C share the dot, so the mark cannot separate them: "agree" there means one of the two.
Marks that the agents often read as another list: G (two dots below read as none: 9 of 24), T (bar above and dot
below read as bar above: 11 of 28), PT (two bars read as brackets or as one bar: 11 of 131).
Control: with the words of lists_v3 shuffled over the figures, the automatic score falls from 373 of 572 to a mean
of 2.1 (200 shuffles; one shuffle reached 46 because "che" fell on a frequent figure).

lists_v4.tsv: 448 values = 378 of lists_v3 + 70 new, each with its folio. 152 values of lists_v3 now carry a
confirmation from fr. 4696. New values by kind: names 11 (plain figures with a point: 30 Card. Gonzaga, 23 Card. di
Borbone, 24 Card. di Vendôme, 27 Card. di Gioiosa, 28 Card. d'Este, 31 Nuncio, 37 Principe di Mantova, 60 Spagnoli,
99 Parigi, 12 "Ab.", 49 "cap."), the rest words in the alphabetical lists.
Window proposals of interp_v3 that a gloss now confirms (8): T 44 travaglio, Q 12 quiete (proposal: quietare),
(10) quasi, I 40 instanza, I 44 intelligenza, PT 70 massimamente (proposal: massime), T 30 termine, C 34 condurre.
One that a gloss contradicts: C 33 "concorrere" (C 32 = condannagione, so C 33 lies between condann- and condu-).
Not tested: the other 18 proposals.

Alphabetical order (`order_breaks.txt`): 18 neighbour pairs out of order in lists_v4. 10 were in lists_v3. 8 come with
the new values: buono 84 / bruttezza 88 / bontà 89 (lists_v3 has buono and bontà the wrong way round, or one figure is
wrong); comporre 27 / commune 28; confusione 36 / conforme 37; intendere 43 / intelligenza 44; perdita 82 / perdere 83;
pretesto 52 / prestito 53; proprio 78 / proposito 80. All are swaps of close neighbours ("loose" order by the first
three or four letters). No new value lies far from its place: 50 of the 57 new values of the alphabetical lists stand in order between
their neighbours of lists_v3; 7 are one place off. That is itself a test of the reconstruction.

## Controls and limits

- The harvest pages had ONE transcription pass each (blind to the table). Only the runs with no gloss had two passes.
- The clerk's gloss is the answer key, and the clerk also errs (he writes "di" for "da", "il Re" for the King of France).
- Clear-text quotes from the survey agents were read at 900 px and were not checked at full size, except ff. 3v,
  12r, 15v, 82r, 120r, which I read myself.
- f. 108r (Nevers, 28 Feb 1590): lines 3-5 one pass; marks agree for 74 % in lines 1-2. The reading is a word list.
- A web search for phrases of the plain text was not done. No reading of fr. 4696 was found in the index files of
  the other projects (13:17 UTC). "New" is not claimed; use "first reading with the rebuilt key, not checked".

## Open

1. Second pass for the harvest pages; a third pass for fr. 4698 f. 108r.
2. The glossed pages of May and June 1586 (ff. 20r-27r) and the rows of plain figures of August and September 1586
   (ff. 30r-37v): they belong to the two older lists. Not harvested.
3. ff. 54-55: another cipher (digits in one string) with its decipherment; it warns that the cipher is known.
4. The 18 window proposals of interp_v3 that no gloss met. The names 13, 34, 45 (bar above) and the code letters A, H, Z.
5. The Nevers minutes of 1586 (fr. 3612 f. 149, fr. 3375, fr. 4697, fr. 4701) need images. They date from March to
   November 1586, so those before August use the older lists; fr. 4696 ff. 20r-27r hold glosses for them.

## Files

`lists_v4.tsv`, `agreement_table.md`, `order_breaks.txt`, `harvest_units.tsv`, `harvest_judged.tsv`, `manual.tsv`,
`READING.md`, `tr/` (transcriptions and passes), `survey_*.tsv` (all 250 views), `BRIEF.md`, `SURVEY_BRIEF.md`,
`ov/` (250 overviews), `img/` (full pages), `crops/`, `prior/`, scripts (`fetchd2.py`, `harvest.py`, `build_v4.py`,
`dec4.py`, `linecrop.py`, `strips.py`, `sheet.py`). Nothing was committed, pushed or published.
Gallica requests: about 300 (250 overviews, 37 full pages of fr. 4696, 10 of fr. 4698), one at a time, 11 s apart;
one HTTP 429 at 13:59, then none.
