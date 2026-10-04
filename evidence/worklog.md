# charles1 — the open ciphers of Charles I and his circle (4 October 2026)

Agent run of 4 Oct 2026, 13:45-14:30. Rules: `scout2/AGENT_RULES.md`. Work folder: `charles1/`.

## Result in one paragraph

The scout verdict ("number codes with no key and no crib") is wrong for one entry. The largest text, the
intercepted letter to Charles I of 13 May 1646 (BL Add MS 72438 f.10, 735 tokens), has a sister key in print that no
team linked: the King's cipher with Captain Titus of 1648, which Hillier printed with a decipherment in 1852. The
word list of 1646 is the Titus list with a small shift (+4 for a-h, 0 for i-n, +1 for o-t, +8 to +10 for w-y and
the second list). With this key the letter reads: it is the lost letter of Secretary Nicholas from besieged
Oxford. About 89% of the tokens are read. The text repeats Fairfax's summons of 11 May 1646 and Glemham's answer,
which are in print. This is an outside control. We did not see the manuscript: the cipher text is the
transcription of A. Aymeloglu (one pass).

## Part 1 — survey

See `survey.tsv` (one row for each open entry: text and source, size, system, what each team tried, our view).
Short form:

| entry | size | state on 4 Oct 2026 | our verdict |
|---|---|---|---|
| Charles I - Henrietta, private cipher, 8 Apr 1645 | 21 groups | no team has a folder | too short; no help found |
| Charles I to Worsley, 22 May 1648 | 112 groups | Bourdeau: two keys excluded | 1646 key and Titus key do not read it (tested here) |
| Charles I to the Prince, 1 Aug 1648 | 88 groups | Bourdeau: needs the key | 1646 key and Titus key do not read it (tested here) |
| Maurice to Rupert, 7 July 1645 | 93 groups | cipher-lab tested 6 sister keys, parked | no new help; not attacked |
| Royalist letter, 21 May 1646 (f.9) | 151 tokens | not attacked | another key (1646 key and Titus key give no words) |
| Letter to Charles I, 13 May 1646 (f.10) | 735 tokens | Aymeloglu about 45 values; cipher-lab 164-192 tokens, "not reading ready" | **READ, see below** |
| Craven to Rupert, 6 Nov 1648 | unknown | no public transcription | blocked (DECODE login) |
| Charles II to Hamilton, 1650 | 102 groups | key located at NRS GD406/1/2197, not online | blocked on Edinburgh |
| Ormond to Arran, 24 Jan 1678 | 24 groups | cipher-lab: no key | too short |
| Hyde, 1 Nov 1659 | | another agent | skipped |

## Part 2 — the help found for f.10

1. **Sister key in print.** George Hillier, *Narrative of the Attempted Escapes of Charles the First* (1852),
   pp.153-161, 210, 240, prints letters XI-XV of the King to Titus with figures and a free decipherment
   (archive.org `narrativeofattem00hilluoft`; OCR text in `src/hillier_uoft.txt`; p.155 checked on the page image
   `src/img/hillier_n180.jpg`, figures equal the OCR). We aligned the figures one by one: `titus_key.tsv`
   (about 150 words, 48 letter values).
2. **Same list, shifted.** The 20 words that Nicholas glossed in the King's letters of 24 June and 16 Aug 1646
   (Evelyn iv.178-179, page images `src/img/evelyn4_n185.jpg`, `_n186.jpg`) are all in the Titus list:

   | word | 1646 | Titus 1648 | shift |
   |---|---|---|---|
   | and, be, de, for, had | 112, 121, 141, 162, 197 | 108, 117, 137, 158, 193 | +4 |
   | I, if, me, my, no, not | 209, 213, 250, 251, 269, 270 | same | 0 |
   | of, or, send, to (the, that, then) | 280, 281, 341, 360 (361, 364, 365) | 279, 280, 340, 359 (360, 363, 364) | +1 |
   | with, where, which | 409, 412, 413 | 401, 404, 405 | +8 |
   | write, you | 422, 429 | 413, 420 | +9 |
   | second list: desire, provide (letter?) | 489, 581 (542) | 479, 571 (532) | +10 |
   | numbers, days, months: one, five, Sunday, May (thousand?) | 643, 647, 674, 681 (665) | 634, 638, 665, 672 (656) | +9 |

   The first five rows are the 20 Evelyn words (found without Titus). The last two rows are values that we set in
   f.10 from the Titus value plus the shift, and that the context then confirmed. Read the other way, the 1646 list
   gives Titus 512 = Independent and 493 = Earl (see "Cross-check back to Titus").

   The cause of the +4: the 1646 list starts with four stop signs (100-103); Titus has its stops at 200-202.
   The letter alphabets of the two keys are different (1646: n 7-9, u 10-12, r 17-19, b 25-27, t 43-45, a 46-49,
   s 55-59, e 67-70, l 75-77, w 78-80, d 81-83, h 84-86, c 88-91).
3. **The reply.** The King to Nicholas, Newcastle, 2 June 1646 (Evelyn iv.177): "since I saw you, I receaued but
   one letter from you, w^ch was of the 5th of May". Our letter starts "Since mine of ye fift of May" (647 43 280
   681). So the letter of 13 May never came to the King: Fairfax took it. Commons Journal, 25 May 1646: Fairfax
   sends "several intercepted Letters ... in Characters", five go to Sir Walter Erle; 30 May: Erle reports one,
   Nicholas to Ashburnham of 15 May, "intercepted going out of Oxford"
   (https://www.british-history.ac.uk/commons-jrnl/vol4/pp553-555 and pp558-559, read 4 Oct 2026).
4. **The clear text of what the letter reports.** *Sir Thomas Fairfax his summons sent into Oxford and the
   governours answer* (London, 14 May 1646; EEBO-TCP A60305, `src/tcp_A60305.txt`), and *Orders and instructions
   from the Lords ...* (23 May 1646; A83934).
5. **Not found:** a period decipherment or a printed clear text of the letter itself (searched: Evelyn iv; HMC 6th
   Report, House of Lords papers; Commons Journal 25-30 May 1646; archive.org full text for "bridge at Marston",
   "Nicholas to the King" "13 May 1646"; all 4 Oct 2026). Leads not followed: Bodleian MS e Mus. 203 (Wallis's
   deciphered letters; "one from the king, p.34, from Newcastle, 1646", with the cipher attached); the King's
   letter of 2 June 1646 sold at Sotheby's in 2018 (cipher with interlinear decipherment, mostly cancelled);
   BL Egerton MS 1533 (Titus originals); Egerton MS 2550 (Nicholas keys); BL Add MS 72438 f.11.

## Part 3 — the reading

Files: `key1646.tsv` (261 codes with grade, count, basis), `reading_f10_tokens.txt` (token by token),
`reading_f10.txt` (words, (?) marks, English), `transcription_f10_aymeloglu.txt` (cipher text, his),
`evelyn_16aug1646.txt` (by-product), `titus_key.tsv`.

### System

One-part numeric nomenclator. 0-4, 6, 20, 21: nulls. 5-99: letters, 3 or 4 numbers in a row for each letter,
letters not in ABC order. 100-103: stops. 104-431: syllables and words, ABC by first letter (ab 104 ... yield
431). 447-629: second list, names and nouns in ABC order (A 447, consider 470, condition 478, desire 489, Earl
503, Fairfax 504, first 507, Governor 510, garrison 512, Hertford 520, Independent 522, Kingdom 528, London 537,
letter 542, Majesty 543, messenger 546, Marquis 550, N[icholas] 555, Oxford 562, Prince 568, Prince Rupert 569,
Presbyterian 571, Parliament 572, provide 581, print 583, quarter 585, receive 596, refuse 597, Scot 613, Sir 614,
victual 620, W[arwick] 629). 639-681: numbers, day, days of the week, months. 691, 697: not clear.
The writer also uses words as syllables: "t-here be-t-we-n-e" (there betwene), "h-o-s-p-it-al", "to-ge-her".

### What the letter says (quotes from the decipher)

- "Since my-n-e of ye five-t of May I hav here-with sent q-u-a-d-r-u-pli-c-at-e"
- "his b-r-i-d-g-e at M-a-r-s-t-on"; "he is ...ing of severall ly-n-e-s from that hil"; "St B-a-r-t-h-o-l
  h-o-s-p-it-al"; "H-e-d-d-ing-t-on h-il ... made divers s-h-o-t in to Oxford but done noe great hurt"
- "to render Oxford to him for the us-e of ye Parliament, and expressing that he may hav h-on-or-able t-e-r-m-s
  for him-s-e-l-v-e and al within ye garrison if he ... a-c-c-e-p-t"
- "desire-d a safe con-d-u-c-t for Sir I-o M-u-n-s-on and Mr [629]"; "to send a messenger to your Majesty, for
  which they hav press-d Fairfax, but he absolute-ly refuse-s to give it"
- "since your depart-u-r-e we hav not receive-d a w-or-d from your Majesty"
- "the difference-s t-here be-t-we-n-e the Presbyterian and Independent-s"
- "Prince Rupert p-i-c-q-u-e-r-ing with some of Fairfax horse receive-d ... but thanks be to God ... noe ... in it"

### Rates

735 tokens in the transcription. 20 are "?" there (illegible). 715 figures: 652 read without mark (89% of 735),
43 read with (?), 20 not read (17 codes). Grades of the 261 codes: E 41 (gloss in Evelyn), E2 21 (our reading of
the unglossed part of the 16 Aug letter), T 52 (Titus sister key + shift + context), C 130 (context; this
includes the letters and the stops), U 17. Passes: decipher 1 (ours, no blind second pass); transcription 1
(Aymeloglu's, not ours). The rule of two transcription passes is NOT met: images need a DECODE login.

### Controls

1. **Outside source (the best control).** The decipher gives the content of two printed papers of 11 May 1646:
   - Fairfax's summons: "I doe by these, summon you to deliver up the Citie of Oxford into my hands, for the use
     of the Parliament ... You may have honourable termes for your selfe, and all within the Garrison, if you
     seasonably accept thereof." Decipher: "to render Oxford to him for the use of ye Parliament ... he may have
     honorable terms for himselve and all within ye garrison if he ... accept". (So the clear word that Aymeloglu
     read "reasonably" is probably "seasonably".)
   - Glemham's answer: "send a safe conduct for Sir Iohn Mounson, & Master Philip Warwick, to repaire unto you".
     Decipher: "desired a safe conduct for Sir Io. Munson and Mr [629]".
   - The King's letter of 2 June ("of the 5th of May") against "five-t of May": the values five (647) and May
     (681) come from the Titus numbers 638 and 672 plus the shift of 9 that "write" and "you" give.
   - Place names of the siege that the letters spell: Marston, Headington hill, St Bartholomew's Hospital,
     Dover (Pier).
2. **Shuffled sister key** (`work/control.py`). Evelyn words that are also in our Titus list: 20. With a shift of
   0 to 9: 20 of 20. Titus values shuffled over the Titus codes, 20,000 times: mean 0.59, max 5, none reaches 20.
3. **Shuffled letter values** (`work/control.py`). Share of letters in spelled runs of 4 or more that make a word
   or the start of a word (word list from Evelyn iv and Hillier): 0.66. Letter values shuffled 2,000 times: mean
   0.020, max 0.168. Limit of this control: we fitted the letter values on the same runs, so it shows that a
   consistent alphabet exists, not more.
4. **Cross-check back to Titus.** 522 = Independent comes from f.10 ("differences ... betwene the 571 and 522s")
   and the ABC order. Titus 512 (= 522 - 10) stands in "any ... made me by the 512 298", where Hillier guessed
   "Parliament party". "Independent party" is the better sense for May 1648.

### Corrections to other teams

- Aymeloglu (16 Sept 2026) and cipher-lab name the cipher "Digby key no. 129" and read 562 = Davenant, 568 =
  Madame Dona, 569 = Madame de Brederode, 571 = Madame Vantelet, 572 = Mylord from the key page f.77. In our
  reading 562 = Oxford (twice), 568 = Prince, 569 = Prince Rupert, 571 = Presbyterian, 572 = Parliament. The page
  f.77 is another key. Their Evelyn values are right and we use them.
- cipher-lab's "111 = were": it is "are" (Titus 107 ar + 4); Nicholas wrote "were" as a free gloss.

### By-products

- `evelyn_16aug1646.txt`: the part of the King's letter of 16 Aug 1646 that Evelyn's editor left in figures:
  "for having more care of themselves than of my honnor, by yielding up my seales and sword to the rebels".
- Hillier's free decipherment of 1852 can be corrected with the order of the 1646 list (all (?)): Titus 512 =
  Independent (not Parliament); 493 = Earl and 493 509 = Earl Holland (not "Rogers' papers"; letter of 10 July
  1648, three days after Holland's rising failed); 541 = Monsieur (before c-on = Con); 264 = make (not have);
  379 = though; 656 = thousand; 102 289 14 210 = "an-other h-it" (not "accomplish it"); 483 11 382 = "danger-o-us",
  279 643 = "of-ten".

### Negative tests (this run)

- Worsley letter (22 May 1648) and the letter to the Prince (1 Aug 1648) with the Titus key and with the 1646
  key: no words (`work/`, output in the log). These two use other keys, as Bourdeau said.
- f.9 (21 May 1646) with both keys: no words.

## Prior-art checks (all 4 Oct 2026)

- Tomokiyo, https://cryptiana.web.fc2.com/code/unsolved.htm (last modified 4 Oct 2026, fetched 14:21): f.10
  "I believe is not deciphered". His charlesi.htm gives the Titus cipher and the 1646 values 17, 18 = r, 280 = of,
  360 = to, with no link between them.
- Aymeloglu, `royalist-1646/` (last commit 18 Sept 2026): partial, about 45 values, "needs the contemporary
  decipher or the rest of the key". No word "Titus" or "Hillier" in README, key129.txt, solve.py.
- cipher-lab, `ciphers/intercepted-royalist-1646/` (last commit 4 Oct 2026 03:00 UTC): NOTES, AUDIT, HYPOTHESES:
  no "Titus", no "Hillier"; PROGRESS.tsv: "no full decipherment located".
- Bourdeau: CATALOGUE.md and SOLVED_CATALOGUE.md (fetched 13:56): no entry for Add MS 72438 ff.9-10; his
  `rupert/NOTES.md` has it as "offline-only". His `charlesi/NOTES.md` rebuilt 35 Titus passages (251 my, 209 I,
  270 not ...) to test the Worsley letter, and did not compare them with the 1646 letters.
- Web: exa search "Nicholas letter to King Charles I 13 May 1646 intercepted cipher deciphered" (no solution
  found); archive.org full-text search (see Part 2, point 5).
- Words to use: f.10 = "first reading, with a key that we rebuilt from a printed sister key (Hillier 1852) and
  from Evelyn's glosses". The summons and the answer inside it are "reproduced" (print of 14 May 1646). The
  transcription is Aymeloglu's.

## Open points

1. No image seen. A second, blind transcription pass of DECODE R8624 is needed (login). It would settle: the 20
   "?"; "q I ing finishd" (line 1); "Peee"; "f ward"; "Iersem"; "{reasonably}" against "seasonably"; "{me from}".
2. 17 codes not read (list in `reading_f10.txt`). 691 (three times) and 292 (twice) are the most useful to get.
3. The sense of the stop signs (100-103, 87, 93-99, 279, 496, 697) is a guess: they stand at breaks of the sense.
4. 555 = Nicholas: from the place in the ABC list (after Marquis 550, before Oxford 562), the closing formula, the
   King's letter of 2 June and the Commons Journal. No signature in clear.
5. Hillier's figures: OCR, one page checked on the image. Titus values with ? in `titus_key.tsv` are our split of
   a free decipherment.
6. Rupert's wound ("his right(?) arm(?)"): the two codes 327 and 118 occur once; the known fact (a shot in the
   shoulder at Oxford in May 1646) is from memory, not checked in a source today.

## Log

- 13:45 rules, scout notes, Tomokiyo charlesi/charlesii, Bourdeau charlesi/rupert/hamilton, cipher-lab and
  Aymeloglu folders on the 1646 letters fetched to `src/`.
- 13:52 Hillier fetched for the Isle of Wight letters. Seen: Titus 209 I, 251 my, 270 not = the Evelyn values of 1646.
- 13:56 `survey.tsv` saved.
- 13:58 Evelyn page images read; tail of 16 Aug 1646 read ("seales and sword to the rebels").
- 14:00-14:15 f.10 solved line by line (`work/key1646.py`, `show.py`, `ctx.py`); summons text fetched (EEBO-TCP).
- 14:17 controls; negative tests on f.9, Worsley, 1 Aug.
- 14:20 files written. Nothing committed, posted or sent.
