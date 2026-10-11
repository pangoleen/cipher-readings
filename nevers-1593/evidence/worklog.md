# BnF fr. 4700 no. 38, f. 72r: work log

Work of 9 and 11 October 2026. "I" in this log is the model that did the work. The words SEEN and INFERRED mark
what I saw on an image and what I concluded.

The log keeps the order of the work. Parts 1 to 9 are the state of 9 October. Parts 10 to 12 are the revisions
of 11 October. Where a later part corrects an earlier one, the earlier part says so.

## 1. Result in short

- The cipher is a small letter cipher. A figure 4, 8 or 9 takes the next figure: the pair is one letter. The
  figures 3, 6 and 7 stand alone and are the vowels a, o and u. The figure 0 is a null.
- I read both passages. 148 of 149 groups have a value by the key. One mark is not read.
- Passage 1 (letters as written): *se c pa·[?]pa(?)· uolese mandar a neuers un suo confidente io gli faria saper
  tuto che desideraria.* On 9 October I gave the start as *se 'l papa*. The page does not have this (part 10).
- Passage 2 (letters as written): *di qel tale che uenise peche sarebe spesato da mi n tuto e tenutolo molt
  secreto.*
- The key is rebuilt from the text. I did not find it on a key sheet.
- G. Cassiani described the minute in 2014 and gave no reading of its cipher passages (part 11). So this is a
  first reading of the two passages, as far as we found.

## 2. Material, and what I saw

- The images came from Gallica through a browser, as strips of the IIIF image of view 84. Two strips for each
  passage (left half and right half), each 610 by about 200 pixels of picture. One small image of the whole page.
- I joined the left and the right strip of each passage. The overlap is 31 pixels, with no vertical shift
  (found by correlation). The joined strips are `images/f72r_block1.jpg` and `images/f72r_block2.jpg`.
- For each pass the lines were cut into enlarged pieces, with other cut points and another scale for each pass.
- SEEN: passage 1 has four lines. The first starts after *il salutifero rimedio*. The last ends before *Il che
  si potra*.
- SEEN: passage 2 has four lines. The first starts after *senza spesa alcuna*. The last ends before *Pero degno*.
  The first strips cut the tops of the first line: all its signs show, but the tops of three "8" and of the
  two "9" of the third group are missing. A later strip shows them (`images/f72r_block2_top.jpg`).
- SEEN: the last line of passage 2 has clear gaps between the pairs (`98. 97 48 43 96 46. 98 6.`). The other
  lines have no gaps.
- SEEN: the writer corrects in cipher. He strikes `96` and writes `98` above it (passage 1, line 2). He strikes
  about 15 signs in passage 2, line 2, and writes `97`, a faint `48`, `95`, `46` above them. He strikes `44 8` at
  the end of passage 2, line 1.
- SEEN: some signs are faint: `(4)6 (44)` in passage 1, line 2, and `(48)` in passage 2, line 1. INFERRED: the
  text needs them, so they are not deletions.

### The sign like an 8 that is open at the top

It is the figure 8. How I decided:

- The lines use eight signs only: 0, 3, 4, 6, 7, 9, the open-top sign, and an S-shaped sign with a small flag.
  No line has a closed 8 or a 5 with a flat bar. Pass 2 says the same. So the two odd signs are the writer's 8
  and 5. The S-shape with a flag is a normal 5 of the time. The loop with two horns is an 8 that the pen does not
  close.
- With these two values the pairs make a regular table: 43 to 49, 83 to 89, 93 to 99, and nothing else. The
  second figure of a pair is always 3 to 9.
- The table then gives the consonants in the order of the alphabet (part 4). With the two signs changed round,
  this order breaks.
- Pass 2 found two forms of the sign: a closed loop with a hook, and an open cup with an arch. Both stand in the
  same places of the same words (`48` = e in both forms). So they are one sign.

## 3. Two transcription passes

- Pass 1: `pass1.txt`. I made it before any decoding.
- Pass 2: `pass2_blind.txt`. A separate agent made it blind. It had the names of the signs and its line images
  only. It did not see pass 1.
- Agreement (`decode.py`): 288 of 298 signs (96.6 %). Two of the ten differences are only the order in which the
  passes write `[96]` and `^98^`. The real differences are in three places. Both passes had marked all three as
  doubtful:
  1. Passage 1, line 1, the sign after the first `0`. Pass 1 read "8". Pass 2 read "s" and a tall stroke ("1?").
     On the image: a small curl and a thick stroke that comes down from above the line. It is not a normal 8, 5
     or 1. I leave it as `{?}`.
  2. Passage 2, line 1, the last struck sign. Pass 1 "8", pass 2 "5". It is in a blot or a strike. It is not part
     of the text.
  3. Passage 2, line 2, the correction. Pass 1 read a struck `89` with `95` above. Pass 2 read one large blotted
     sign, a clear `5` above, and a struck `9`. Both give `?5` above the line. The text needs `95` (p).
- One more doubt, where the passes agree: passage 1, line 1, third group. Both passes read `84`. On 9 October I
  preferred `89`, because the second figure has a long stem and because the sense asks for l. **This was a
  reading from the sense. Part 10 takes it back.**
- Settled text: `transcription.txt`.

Counts, for the text as the writer corrected it: **149 groups** = 128 pairs + 21 single figures. **25 different
values**: 21 pairs, and 0, 3, 6, 7. (277 signs stand on the lines, without the struck signs.)

Dots: they stand at mid height before or after some signs, most of them beside a 4 or a 6. They do not divide
words or pairs in a regular way. I take them as rests of the pen. The two pass files have them.

## 4. The key (rebuilt)

| | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| **4x** | 43 c (2) | 44 u (5) | 45 a (13) | 46 e (13) | 47 i (9) | 48 e (12) | 49 o (4) |
| **8x** | 83 b (1) | 84 c (4) | 85 d (6) | 86 f (2) | 87 g (1) | 88 h (3) | 89 l (6) |
| **9x** | 93 m (3) | 94 n (8) | 95 p (5) | 96 r (8) | 97 s (11) | 98 t (11) | 99 q (1) |

Single figures: 3 = a (1), 6 = o (7), 7 = u (3), 0 = null (9). The number in brackets is the count of each value.
The counts are those of the settled text of 11 October (on 9 October the table had 84 three times and 89 seven
times).

- The consonants b c d f g h l m n p r s t are 83 to 89 and 93 to 98, in the order of the alphabet. The vowels
  are in the row 4x.
- Two values for one letter: e = 46, 48; o = 49, 6; u = 44, 7; a = 45, 3; c = 84, 43.
- The null 0 follows a vowel in all nine places: after 6 three times, after 7 three times, after 3, 44 and 45
  once each. 7 never stands without 0.
- Values with one witness: 83 b (*sarebe*), 87 g (*gli*), 99 q (*qel*), 3 a (*papa*). The order of the alphabet
  supports 83 and 87. The values 99 and 3 rest on one word each.
- No figures for whole words. No sign for a doubled letter: the writer writes single letters (*tuto, uenise,
  sarebe*).

## 5. How I solved it

1. Counts and contacts showed that the values 4x behave as vowels (Sukhotin's test gives 44 to 49).
2. A hill-climb with a table of Italian four-letter groups did NOT find the text. A key with one letter for each
   group cannot fit the double values, and a free key fits 139 letters too easily. I say this plainly: the solver
   is not the source of the reading.
3. The counts of the values 8x and 9x fit the Italian consonants in the order of the alphabet. I tried this
   order. It gave `ch.` twice and `t . c h . d . s . d . r . r . .` at the end of passage 1: *che desideraria*.
   The vowels followed from the words: *confidente* gave 6 = o; *saper tu·to che* gave 7 = u; *secreto* and
   *tale che* gave 43 = c.

## 6. The reading, line by line

| Line | Letters (· = the null 0) |
|---|---|
| B1L1 | s e c p a · [?] p a(?) · u o l e s e m a n |
| B1L2 | d a r a n e u · e r s u n s u o · c o n f i d e n t |
| B1L3 | e i o g l i f a r i a s a p e r t u · t o c h e d |
| B1L4 | e s i d e r a r i a |
| B2L1 | d i q e l t a l e c h e |
| B2L2 | u · e n i s e p e c h e s a r e b e s |
| B2L3 | p e s a t o d a m i n t u t o · e t e n u · t o l o m o · l |
| B2L4 | t s e c r e t o |

The reading with its clear context and the English translation: `reading.md`.

Forms of the writer: *uolese*, *uenise*, *sarebe*, *tuto* (single consonants); *qel* for *quel*; *peche* for
*perche* (r left out); *da mi n tuto* (one i for *mi in*); *molt secreto* (no o).

Context, from the clear text (`cleartext_f72r.txt`): the minute answers a letter of 20 February. It mourns a
"S.r Badalochio(?)", through whom Nevers hoped to reach the Pope. It asks the Father to use "la Zifera" that the
dead man left. On 9 October I INFERRED the persons: Vincenzo Badalocchio, and his confessor Tommaso Bozio. I did
not see a name of the Father on f. 72r. Cassiani's article confirms both (part 11).

## 7. Controls

(a) Sense. The two passages are Italian sentences. Each one completes the clear sentence in which it stands:
*il salutifero rimedio* + "if ... would send a confidant to Nevers"; *senza spesa alcuna* + "of the man who came,
because I would pay for him". The clear sentence between them (*Il che si potra fare facilmente*, Jesuits,
Dominicans, a large town) is about the same plan.

(b) Numbers, first run, 9 October. Score = mean log10 probability of the groups of four letters, on a table made
from Italian prose. Real Italian of this length: median -4.14, worst of 300 samples -4.61. The text that was
scored had l as the third letter (*selpapa...*).

| Test | Result of the first run |
|---|---|
| Our key, 139 letters | -4.45 |
| C1: the letter values of the key, dealt at random to the 24 groups, 5,000 keys | mean -7.34, best -5.85; our key is 9.4 sd above the mean |
| C2: our key, the groups in a shuffled order, 5,000 times | mean -6.52, best -5.75; the true order is 10.4 sd above the mean |
| C3: the key of passage 1 only, applied to passage 2 | 61 of 65 letter groups read (94 %); the text is *di?eltale?heuenisepechesare?espesatodamintutoetenutolomoltse?reto*; score -4.53; 5,000 shuffled keys of passage 1: mean -7.00, best -5.11 (5.5 sd) |
| C4: a free solver (two groups can have one letter) on 5 shuffled orders | -4.60 to -4.73. On the true order the same solver reached -4.24, with nonsense |

C4 is a warning. For 139 letters, a free key can make nonsense that scores almost as well as real Italian. The
four-letter score alone does not prove the reading. The proof is C3 (passage 2 reads with the key of passage 1,
and the three new values are b, c, q in sensible words), C1 and C2, the sense, and the structure of the key.

(c) Structure. Thirteen consonant values stand in the order of the alphabet, in two rows. I took this order as a
first trial, so it is not a fully separate control. But a word then confirms each of the thirteen letters
(*sarebe, che, mandar, faria, gli, che, uolese, molt, un, saper, secreto, spesato, tuto*).

(d) Share that has a value: 148 of 149 groups (99.3 %): 139 letters and 9 nulls. One mark is not read.

## 8. Earlier work, state of 9 October

- D. Bourdeau's `cyphersolver` lists fr. 4700 nos. 38-46 among the letters to do. No reading there.
- `NoAutopilot/cipher-lab`: no work on fr. 4700 in its table of progress.
- S. Tomokiyo's pages, as far as they were saved on disk: no page names fr. 4700.
- S. Tomokiyo's descriptions of the Nevers key sheets in BnF fr. 3995. By the description, no. 35 is not the key
  of f. 72r: there the letters are low numbers (11 to 40), and the numbers from 43 up are words and titles. Our
  text has 45 thirteen times as the letter a. The descriptions of nos. 44 to 47, 52 and 58 do not fit either.
  I could NOT look at these sheets themselves on that day. So: by description no known sheet has this key; this
  is not checked on the sheets.
- The clear text says that the cipher came from Badalocchio. A sheet for it can exist in fr. 3995 or in another
  volume.
- Web search for *"salutifero rimedio"* and *"mandar a Nevers un suo confidente"*: no hit.
- Not known to me on 9 October: G. Cassiani's articles. See part 11.

## 9. What was doubtful on 9 October

1. Passage 1, line 1, third group: `89` (l) or `84` (c).
2. Passage 1, line 1, the mark after the first 0 (`{?}`), and the group `3 0` after `95`: the 3 has a large tail
   loop, and the 0 is small and high. *pa·pa·* is the reading; 3 = a has this one witness.
3. Passage 2, line 1, third group `99`: the tops are cut, and the first 9 has an odd head. *qel* needs q.
4. Passage 2, line 2: the correction. `95` above the line is read from a blotted sign and a clear 5.
5. The struck first drafts are not read.
6. The clear text is from a small image, one pass. Words with (?) are not sure. The page ends at "per amor de
   Christo". I did not see the verso.
7. The names (Badalocchio, Bozio) were inferred.

## 10. Revision of 11 October: three new strips of f. 72r

The new strips have the same pixel size as the first strips. The scan gives no more detail.

| Place | Result | State |
|---|---|---|
| Passage 1, line 1, third group | The new strip shows **84** again. The stem of the second figure rises above its hook and has a crossbar: it is a 4 with a long tail, not a 9. Three images and both passes now say 84 = c. | Settled as SEEN: 84. The sense is open: *se c pa·...* is not clear Italian; *se 'l papa* needs 89. Either the writer made a slip (he made others), or *c* means something that I do not see. |
| Passage 1, line 1, the mark after the first 0 | The new strip ends just before the mark. Only its left edge shows. The half-size image shows a hook at the top of the mark, so it belongs to this line. | Open. |
| Passage 1, line 1, "3 0" | Not on the new strip. The figure can be a 3 with a tail loop or a 2 in the form of a z. | Open. My region for this strip was wrong. A strip of the same scan will not show more. |
| Passage 2, line 1, 99 | The tops show two 9. The first has one more hook at its upper left: a correction over another figure. | Settled: 99. Its value q rests on one word (*di qel tale*). |
| Passage 2, line 2, the correction | No gain. Above the line: 97, a faint 4 with a faint oval, a blotted sign with a clear 5, then 46. | As before: 97 48 95 46 (*s e p e*), with 95 in part inferred. |
| The struck first draft | Struck on the line: `79 . 74 {8/?}9 4 6 0 48 84 6 9`. If 79 and 74 are 97 and 47 with the figures changed round, the draft is *s i l e · e c o* and a broken pair. I see no sure sentence in it. | Not read. It gives no control. The other struck places are short: `[96]` = r, corrected to t (*confidenr* to *confident*), and `[44 8]` = *u* and a broken pair, written again as `7 0` on the next line. These two fit the key. |

Effect on the reading. The subject of *volese* is less sure than I said on 9 October. The signs are
`84 95 45 0 {?} 95 {3/2} 0` = *c p a · ? p a(?) ·*. "The Pope" (*papa*) is still the probable sense: the clear
text before it speaks of *Sua Santità*, and *pa·pa·* fits the signs if the mark is not a letter. But *se 'l* is
not what the page shows. The sentence is to be written as: *se [c] pa·[?]pa(?)· volese mandar a Nevers un suo
confidente ...*

## 11. Revision of 11 October: the articles of G. Cassiani

- Read: G. Cassiani, "«Il nostro re, e sua christianissima maestà». Novità su Tommaso Bozio dinanzi all'istanza
  di riconciliazione di Enrico IV", *Rivista di storia della Chiesa in Italia* 68 (2014), pp. 387-409: pp. 393-395
  with their notes. And his article of 2016 in the *Rivista di storia e letteratura religiosa* 52: footnote 3, and
  a search of the whole text for the words for "cipher".
- 2014, pp. 394-395: he describes this minute and cites it as f. 72r-v, minute of L. Gonzaga to T. Bozio, 1 May
  1593. He gives its content from the clear text, with quotations from the leaf. Of the cipher he says only that
  the Duke "volle crittografare i passaggi più delicati della sua missiva". He does not decode them.
- 2016, footnote 3: he lists the pieces of the correspondence, this minute among them. The article has no
  number, no decipherment, and no word on a cipher passage.
- The addressee is Tommaso Bozio, rector of the Roman Oratory. This confirms the inference of part 6.
- The dead man is Vincenzo Badalocchio, secretary of the French ambassadors in Rome and agent of Nevers. He died
  on 19 February 1593. This confirms the "Badalochio(?)" of my clear text.
- Where my clear text differs from his quotations, his are from the leaf. Mine is one pass from a small image.
- He reports that Nevers asked for two copies of the answer, by way of Lucca and by way of Mantua. I did not read
  this on the recto. It is probably on the verso, which I did not see.
- What is ours: the two cipher passages. They give the plan that the clear text only points to: Nevers asks for a
  secret envoy to the town of Nevers, and offers to pay for him.
- The minute tells Bozio to use the cipher that Badalocchio left. The leaf from Rome that the minute answers
  (BnF fr. 4687, f. 89r) is in a cipher of another look. It is not read. See the README, "Open work".
- NOT read: Cassiani's later articles on the same letters (2017, 2018, 2020).
- Words to use: **a first reading, as far as we found, of the two cipher passages of a minute that G. Cassiani
  described in 2014; the key is rebuilt from the text.** Not "an unknown letter". Not "with a known key".

## 12. Check for publication, 11 October: the controls again

- I ran the controls again with the script of this folder (`control.py`) and a table made anew from 2.5 million
  letters of Italian prose. The text that was scored is the settled text, with c as the third letter.
- **The numbers of the first run did not come back exactly.** The table of the first run was not kept. Its scores
  are lower for every text, for real Italian too. I do not know why.

| Test | Second run |
|---|---|
| Real Italian of this length, 300 samples from the text of the table | median -3.93, worst -4.28 |
| Our key, 139 letters | -4.23 |
| C1, 5,000 shuffled keys | mean -6.60, best -5.49; ours is 9.9 sd above the mean |
| C2, 5,000 shuffled orders | mean -5.99, best -5.41; ours is 11.6 sd above the mean |
| C3, passage 2 by the key of passage 1 | 61 of 65 letter groups; score -4.24; 5,000 shuffled keys of passage 1: mean -6.33, best -4.81 (5.9 sd) |
| C4, free solver on five shuffled orders | -4.68, -4.40, -4.66, -4.58, -4.53 |
| C4, free solver on the true order | -4.04 |

- The result is the same as in the first run. The warning of C4 stands: the best string from a shuffled order
  (-4.40) is near the worst sample of real Italian (-4.28) and near our reading (-4.23).
- One point differs. In the first run the free solver gave nonsense on the true order. In the second run its
  text has the letter of our reading in 106 of 139 places (*...mandaraneuerrunruocontidenteio...
  tutochederiderariadi...*), and the other places are not Italian. It is one run with one seed and another
  table. I do not count it as a control.
- The pass agreement (288 of 298) and C3 (61 of 65) need no table. `decode.py` prints them.
