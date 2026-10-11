# The Duke of Nevers to Tommaso Bozio, 1 May 1593: the two cipher passages of the minute read

A draft letter in Italian with two passages in figures. G. Cassiani described the letter in 2014. This folder
reads the two passages.

| Document | Shelfmark | State before | State now |
|---|---|---|---|
| Minute (draft) of Ludovico Gonzaga, Duke of Nevers, to the Oratorian Tommaso Bozio in Rome, La Guierche, 1 May 1593, in Italian | Paris, BnF, ms. français 4700, no. 38, f. 72r (Gallica `btv1b90582908`, view 84) | Described by G. Cassiani in 2014; no reading of the two cipher passages | [reading with an English translation](reading.md): 148 of 149 groups have a value by the key; the first words of passage 1 are not sure |

**Status: 11 October 2026.** The work was done by a model. No palaeographer has checked it. Corrections are
welcome: please open an issue.

## What this is

- A minute is the draft of a letter that the writer keeps. This one fills one page and has many corrections.
- The writer is Ludovico Gonzaga, Duke of Nevers. The addressee is Tommaso Bozio, a priest of the Oratory in Rome.
- The place and the date come from the catalogue of the library: La Guierche, 1 May 1593. G. Cassiani gives the
  same date. We did not see the end of the minute.
- The page is in clear Italian, with two passages in figures. Each passage has four lines.
- The minute answers Bozio's letter of 20 February 1593. That letter told the Duke of the death of Vincenzo
  Badalocchio, his agent in Rome.
- We saw the recto only (f. 72r). We did not see the verso.

## What is new, and what is G. Cassiani's

G. Cassiani's:

- He described this minute in 2014: G. Cassiani, "«Il nostro re, e sua christianissima maestà». Novità su Tommaso
  Bozio dinanzi all'istanza di riconciliazione di Enrico IV", *Rivista di storia della Chiesa in Italia* 68 (2014),
  pp. 387-409, at pp. 394-395. The article is on
  [the site of the journal](https://storiadellachiesainitalia.vitaepensiero.it) and on the author's page at
  academia.edu.
- He identified the addressee: Tommaso Bozio.
- He gave the context: the reconciliation of Henri IV, and the death of Nevers's agent Vincenzo Badalocchio on
  19 February 1593.
- He gives the content of the clear text, with quotations from the leaf.
- Of the cipher he wrote that the Duke "volle crittografare i passaggi più delicati della sua missiva". He gives no
  reading of them.
- His article of 2016 lists the minute among the letters of Bozio and Nevers (footnote 3). It does not speak of
  the cipher of the minute.

Ours:

- **This is the first reading known to us of the two cipher passages of a minute that G. Cassiani described in
  2014; the key is rebuilt from the text.**
- The text has 149 groups and 25 values. The pairs 43 to 49 are the vowels (43 is a second c). The pairs 83 to 89
  and 93 to 99 are the consonants, in the order of the alphabet. The single figures 3, 6 and 7 are vowels, and 0
  is a null.
- We did not find this key on a key sheet.
- "Known to us" has limits. The searches are listed below, with what we did not open.
- The clear text in this folder is our own reading from a small image. It is an aid. Cassiani's quotations are
  from the leaf.

## The cipher

- The cipher text is a row of figures with no gaps between the letters.
- A figure 4, 8 or 9 takes the next figure. The pair is one letter.
- A figure 3, 6 or 7 stands alone. It is a vowel.
- A figure 0 stands alone. It is a null. It follows a vowel in all nine places.

| | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|
| **4x** | 43 c (2) | 44 u (5) | 45 a (13) | 46 e (13) | 47 i (9) | 48 e (12) | 49 o (4) |
| **8x** | 83 b (1) | 84 c (4) | 85 d (6) | 86 f (2) | 87 g (1) | 88 h (3) | 89 l (6) |
| **9x** | 93 m (3) | 94 n (8) | 95 p (5) | 96 r (8) | 97 s (11) | 98 t (11) | 99 q (1) |

Single figures: 3 = a (1), 6 = o (7), 7 = u (3), 0 = null (9). The number in brackets is the count of each value.

- u and v are one letter.
- Five letters have two values: a (45, 3), e (46, 48), o (49, 6), u (44, 7), c (84, 43).
- The cipher has no figures for whole words. It has no sign for a doubled letter: the writer writes "tuto",
  "uenise", "sarebe".
- Two figures have odd forms. The writer's 8 is open at the top. His 5 is an S-shaped sign. The lines have no
  closed 8 and no 5 with a flat bar. With these two values the pairs make a regular table, and the consonants
  stand in the order of the alphabet. So the two values are inferred from the system.
- The key as a table: [key.tsv](key.tsv), with the words that fix each value.

## The reading

The full reading, with notes: [reading.md](reading.md).

| | Passage 1 (after "il salutifero rimedio") | Passage 2 (after "senza spesa alcuna") |
|---|---|---|
| The letters as the cipher gives them | se c pa·[?]pa(?)· uolese mandar a neu·ers un suo· confidente io gli faria saper tu·to che desideraria | di qel tale che u·enise peche sarebe spesato da mi n tuto· e tenu·tolo mo·lt secreto |
| Normalised Italian | se [c] papa(?) volesse mandar a Nevers un suo confidente, io gli faria saper tutto che desideraria. | di quel tale che venisse, pe[r]ché sarebbe spesato da me in tutto, e tenutolo molt[o] secreto. |
| English | if [c] the Pope(?) would send to Nevers a confidant of his, I would let him know all that he would wish. | for the man who came, because I would pay all his costs, and he would be kept very secret. |

A raised dot is the null 0. [?] is a mark that we cannot read.

- **The page does not have "se 'l papa".** The third group of passage 1 is 84, and its value is c. The probable
  sense is "se 'l papa" (if the Pope). That needs 89 in the place of 84. We give the letters as they stand, and
  the probable sense apart from them.
- The clear text goes on after passage 1: this can be done easily, because the town has a college of Jesuits with
  an Italian rector, and a community of Dominican friars. The town is "grande assai", and all would be done
  "senza spesa alcuna". Passage 2 follows these words.
- In short: Nevers asks for a man of trust from Rome, who would come to the town of Nevers. He offers to pay for
  him and to keep him secret. If "papa" is right, the man is to come from the Pope.

## How to check by hand

1. Open the check page: <https://pangoleen.github.io/cipher-readings/nevers-1593.html>. It shows the key and all
   eight cipher lines. Each group stands under the image of its line, with its value.
2. Or take one line yourself. Line 3 of passage 1 is a good one. Its groups are in
   [transcription.txt](transcription.txt), row `B1L3`. Cut the row of figures into groups by the rule above. Look
   up each group in [key.tsv](key.tsv). You get "e io gli faria saper tu·to che d".
3. Compare with the image: `images/f72r_block1.jpg`, third line.
4. Compare the two transcription passes: `pass1.txt` and `pass2_blind.txt`.
5. Run `python3 decode.py`. It decodes the eight lines, counts the groups, compares the two passes, and reads
   passage 2 with the key of passage 1. [decoded_by_key.txt](decoded_by_key.txt) holds its decode.

## The controls

Details: [evidence/worklog.md](evidence/worklog.md).

1. **Two transcription passes.** The first pass came before any decoding. The second pass was blind: a separate
   agent had the names of the signs and the line images only. The passes have the same sign in 288 of 298 places
   (96.6 %). Ten signs differ. Two of them are only the order of one correction. The others are in three
   places, and both passes had marked each of these places as doubtful.
2. **The key of passage 1 reads passage 2.** The values that passage 1 fixes read 61 of the 65 letter groups of
   passage 2 (94 %). Three groups are new in passage 2: 43, 83 and 99. They give c, b and q in "che", "sarebe"
   and "qel".
3. **Shuffled keys.** The letter values of the key were dealt at random to the 24 groups, 5,000 times. No such
   key comes near the score of our key (table below).
4. **Shuffled orders.** The key was kept, and the groups of the text were put in a random order, 5,000 times. No
   such order comes near the score of the true order.
5. **The sense.** Each passage completes the clear sentence in which it stands. The clear sentence between the
   two passages speaks of the same plan.
6. **The structure.** Thirteen consonants stand in the order of the alphabet, in two rows. We tried this order as
   a first guess, so it is not a fully separate control. But a word then confirms each of the thirteen letters.

The score is the mean log10 probability of the groups of four letters, on a table made from Italian prose.

| Measure | First run, 9 October | Second run, 11 October (`control.py`) |
|---|---|---|
| Text that was scored | third group of passage 1 read as l | third group as on the page: c |
| Real Italian of this length, 300 samples | median -4.14, worst -4.61 | median -3.93, worst -4.28 |
| Our key, 139 letters | -4.45 | -4.23 |
| Shuffled keys | mean -7.34, best -5.85; ours is 9.4 sd above the mean | mean -6.60, best -5.49; ours is 9.9 sd above the mean |
| Shuffled orders | mean -6.52, best -5.75; ours is 10.4 sd above the mean | mean -5.99, best -5.41; ours is 11.6 sd above the mean |
| Passage 2 by the key of passage 1 | 61 of 65; score -4.53 | 61 of 65; score -4.24 |
| Shuffled keys of passage 1 on passage 2 | mean -7.00, best -5.11; ours is 5.5 sd above the mean | mean -6.33, best -4.81; ours is 5.9 sd above the mean |
| A free solver on five shuffled orders | -4.60 to -4.73 | -4.40 to -4.68 |
| A free solver on the true order | -4.24 | -4.04 |

- **A four-letter score alone proves nothing at this length.** A free solver knows nothing of our key. On texts
  in a shuffled order it makes strings that are not Italian, and they score almost as well as real Italian. On
  the true order it scores better than our reading. So the score does not prove the reading. The proof is in
  controls 1 to 6 together.
- The two runs do not give the same numbers. The first run used a table of four-letter groups that we did not
  keep. Its scores are lower for every text, for real Italian too. We do not know why. The second run uses the
  script of this folder. Both runs give the same result.
- The Italian text for the table is not in the repository. `control.py` takes any large Italian text.
- The samples of real Italian come from the same text as the table. This makes their scores a little too good.
- In the first run, the free solver gave nonsense on the true order. In the second run, its text has the letter
  of our reading in 106 of 139 places, and the other places are not Italian. This is one run with one seed. We
  do not count it as a control.
- The reading does not come from a solver. It came from the counts, from a trial of the order of the alphabet,
  and then from the words. A first solver with one letter for each group did not find the text.

## A control from outside: the sheet of January 1593

The key of the minute was rebuilt from the minute alone: two short passages, 149 groups. A second text in the same
cipher is in the same volume: BnF fr. 4700 f. 80r (Gallica `btv1b90582908`, view 92). It is a full sheet of
figures, 18 lines, with no clear word and no decipherment. It follows a clear letter of Vincenzo Badalocchio, the
Duke's agent in Rome, that ends on f. 79v. The year 1593 is sure on that page; the month reads as January, with
doubt. This sheet was not used to build the key.

- The key of the minute alone gives a value to 637 of the 1,003 groups of the sheet (63.5 %).
- It reads Italian there at once: *heresia*, *Navara*, *ostinatamente a perseverar*, *pacifico di Francia*,
  *gagliarda rimostranza*, *lo stato di Milano*, *Napoli et Sicilia*.
- Against 3,000 keys with the same letters dealt at random, the true key stands 7.9 standard deviations above the
  mean.
- In *sareb·be* a null stands between the two b. The same habit shows in the minute.

The sheet adds values that the short minute does not have. It is read in long stretches only, and about one line
in four has no connected sense yet. It is not a result of this folder. It is named here as a control, and as open
work.

## Two ciphers of Badalocchio, and the date of the change

The Duke's collection of keys holds an earlier cipher of Badalocchio: BnF fr. 3995, the sheet with the pencil
folio numbers 100-101 (Gallica `btv1b525085665`, canvas 194). S. Tomokiyo lists and describes it as Nevers cipher
no. 56. Its dorse (canvas 195) has this note:

> 1592 / Zifara Bad / no(n) serve piu / p(er) haverne / mandato un'altra / a 9(?) Sett(emb)re 92

"Cipher Bad[alocchio]. It is no longer in use, because another one was sent on 9(?) September 1592." The day is
not sure. We read the note from one image.

The old cipher gives each letter a number from 2 to 25, and each word a number with the sign of its letter list.
The texts of 1593 do not follow it. The minute of 1 May 1593 and the sheet f. 80r use the two-figure numbers 43-49,
83-89 and 93-99 for the letters. So the cipher that we rebuilt is probably the "other one" of September 1592:
the cipher that Badalocchio left to Father Tommaso Bozio, and that the Duke names in the minute as "quella stessa
zifera". No key sheet of this second cipher is known to us.

## Doubts

1. **Passage 1, line 1, third group.** The page has 84 = c. Both passes read 84, and three images show it. "se 'l
   papa" needs 89 = l. So "se 'l papa" is not what is written. Either the writer made a slip, or "c" has a
   meaning that we do not see.
2. **Passage 1, line 1, the mark after the first 0.** We cannot read it. It is not the writer's 8, 5 or 1. It
   stands between "pa·" and "pa·".
3. **Passage 1, line 1, the figure before the second 0.** It is a 3 with a large tail loop, or a 2 in the form of
   a z. We read 3 = a ("papa"). The value 3 = a has this one witness.
4. **Passage 2, line 1, third group.** It is 99, and the first 9 is written over another figure. Its value q
   rests on one word: "di qel tale".
5. **Passage 2, line 2, the correction.** The writer struck some signs and wrote 97 48 95 46 above them ("sepe").
   The 48 is faint. The 95 is a blotted sign and a clear 5: we read it in part from the sense.
6. **The struck first draft is not read.** It has about 15 signs, in line 2 of passage 2. It gives no control.
   Two short struck places fit the key: 96 (r) corrected to 98 (t) in "confident", and a struck 44 (u) that the
   writer wrote again as 7 0.
7. **Four values have one witness each:** 83 = b ("sarebe"), 87 = g ("gli"), 99 = q ("qel"), 3 = a ("papa").
   The order of the alphabet supports 83 and 87. Nothing else supports 99 and 3.
8. **Faint signs.** Three groups are in faint ink (in "neuers" and in "qel"). The text needs them, so we do not
   take them as deletions.
9. **The two odd figures** (8 and 5) are read by the system, not by a clear model of the hand.
10. **The dots.** Dots stand beside some figures. We take them as rests of the pen. They do not divide words in
    a regular way.
11. **The images are small.** Each strip is 610 pixels wide and shows about half of a line. A second set of
    strips of the same scan gave no more detail. The region of one new strip was wrong: it ends just before the
    mark and the figure of doubts 2 and 3.
12. **The clear text** is one pass from a small image. Words with (?) are not sure. The image of the page ends
    at "per amor de Christo".
13. **The key is not on a key sheet that we know.** See "Open work" and "Earlier work".
14. **The numbers of the first run of the controls could not be repeated exactly** (see "The controls").

## Open work: the cipher text from Rome

The minute answers a packet from Rome. One leaf of that packet is in cipher: BnF fr. 4687, f. 89r. By Cassiani,
it is the cipher text of Vincenzo Badalocchio, copied by Bozio. We have not read it. It follows neither the old
cipher of 1592 nor the cipher of the minute: it has the figures 0 to 7 only, in pairs, and capital signs with two
figures after them. It may be a third system or a working notation. We tried both keys, and no Italian word comes
out.

## Earlier work

Searched on 9 and 11 October 2026:

- G. Cassiani's article of 2014 (pp. 393-395 with their notes) and his article of 2016 ("Eclissi e rinascita del
  rex christianissimus nell'epistolario dell'oratoriano Tommaso Bozio con il duca di Nevers ritrovato a Parigi",
  *Rivista di storia e letteratura religiosa* 52, 2016). See above: no reading of the cipher passages.
- D. Bourdeau's [cyphersolver](https://github.com/dbourdeau/cyphersolver) lists fr. 4700 nos. 38-46 among the
  letters to do, with no reading.
- `NoAutopilot/cipher-lab`: no work on fr. 4700.
- S. Tomokiyo's pages, as far as we had them saved (the page on the ciphers of the Duke of Nevers among them):
  none names fr. 4700.
- S. Tomokiyo's descriptions of the Nevers keys in BnF fr. 3995, nos. 35, 44 to 47, 52 and 58: none fits this
  key. In no. 35 the letters are low numbers, and the numbers from 43 up are words and titles. Our text has 45
  thirteen times as the letter a.
- A web search for two phrases of the reading ("salutifero rimedio", "mandar a Nevers un suo confidente"): no hit.

**Not opened:**

- Cassiani's later articles on the same letters (2017, 2018, 2020).
- Most key sheets of fr. 3995 themselves. For the numbers above we compared the descriptions only.
- The verso of the minute, and the pieces nos. 39 to 46 of the same volume.
- The lists of `el-descifrador/cabinet-noir`, of Satoru and of A. Aymeloglu were not checked for this minute.
- A printed edition that is not online can exist.

## Contents

| File | Content |
|---|---|
| `reading.md` | The two passages: the letters as written, a normalised Italian, an English translation, notes |
| `key.tsv` | The key table: group, value, count, and the words that fix the value |
| `transcription.txt` | The settled transcription of the eight cipher lines, with notes on the doubtful places |
| `pass1.txt`, `pass2_blind.txt` | The two transcription passes |
| `decode.py`, `decoded_by_key.txt` | The decoder with the counts, the comparison of the passes and one control; its decode |
| `control.py` | The controls with shuffled keys and shuffled orders (needs an Italian text) |
| `cleartext_f72r.txt` | The clear Italian of the page, as far as we read it. A reading from a small image, not an edition |
| `evidence/worklog.md` | The work log: how the key was found, the controls, the revisions, the search for earlier work |
| `images/` | The page (reduced), the two passages (joined strips), and three detail strips, with the credit "gallica.bnf.fr / BnF" |

## Credits

- **Gennaro Cassiani** described the minute, identified Tommaso Bozio as the addressee, and gave the context
  (2014, 2016).
- **Satoshi Tomokiyo** described the cipher keys of the Duke of Nevers in BnF fr. 3995
  ([Cryptiana, "Ciphers of the Duke of Nevers"](https://cryptiana.web.fc2.com/code/nevers.htm)).
- **Daniel Bourdeau** listed fr. 4700 nos. 38-46 as letters to do.
- **Bibliothèque nationale de France / Gallica** provides the page images.
- **The work was done by a model**: Claude, by Anthropic, running as Claude Code with subagents. Paolo Rosson
  directed it. No palaeographer has checked it.

## Licence

Code and tables: MIT. Text: CC BY 4.0. Images: cut from Gallica, under the BnF's conditions of reuse; the source is
"gallica.bnf.fr / BnF". Details are in [LICENSE.md](../LICENSE.md).
