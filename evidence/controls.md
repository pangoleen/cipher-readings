# The blind test on made-up codes

The question: can a reader who works like a codebreaker by hand turn the first decode of a solver into a reading?
And how often is such a reader right?

## Set-up

- Two made-up codes, P1 and P2, were built with the list lengths of the real cipher: alphabetical lists under
  each initial letter, words and syllables mixed, several numbers for common values, nulls.
- Two Italian texts of 1528 (letters printed by Molini) were put into these codes. Runs of clear words were left
  in the text, in the same share as in the real letter no. 20. Each package had about 3,700 cipher groups.
- Each package held: the groups, 21 values given as known (the same number as for the real text), the list
  lengths, the first decode of the solver, and a list of period words for each letter.
- The answers were kept outside the packages.
- One reader (a model) got one package and a written brief. It was told to use nothing else: no other folder, no
  web. Its record of file access was checked afterwards. Neither reader opened a file outside its package.
- The real text went through the same procedure as a third package, with the same brief.

## Result

| | Solver alone, tokens right | Solver and reader, tokens right | Types right |
|---|---|---|---|
| Control P1 | 50.5 % | 87.6 % | 75.4 % |
| Control P2 | 52.4 % | 93.4 % | 83.7 % |

By the reader's own class of confidence (tokens right; the values given as known are left out):

| Class | P1 | P2 |
|---|---|---|
| sure | 91.7 % | 97.6 % |
| probable | 84.3 % | 90.9 % |
| guess | 53.7 % | 65.3 % |

## What the test shows, and what it does not

- It shows that the method works on a code of this kind, and that the reader's classes mean something: "sure"
  is right nine times in ten or more, "guess" about half of the time.
- It does not measure the reading of the real text. The made-up codes gave each number from 6 to 9 a value that
  begins with the base letter. The real cipher uses these numbers as an alphabet of single letters, and its
  lists hold stems. The readers of the real text had to find this first. Their work was harder than the control.
- All readers are instances of one model.

## The real text

- Reader 1 was cut short: 128 groups with a value.
- Reader 2, alone: 322 groups; it found the alphabet of the numbers 6 to 9 and the date line.
- Of the 101 groups that both valued (the known values left out), 49 agree exactly. Most of the others differ in
  the form of the same word (dicto and detto, present and presente) or belong to the numbers 6 to 9, where
  reader 1 had followed the old idea.
- A third pass merged both, tested the alphabet of 6 to 9 on all contexts, and extended the table to 634
  values: 53 % of the text in connected stretches.

## The check of the transcription on the images

- Every line of the twelve pages was compared with the image; all 114 tokens with base letter g and all 274
  with base letter t were looked at one by one.
- In the "Ranzo" letters (fr. 2988) 57 "g" are s and 63 "t" are r. In letter no. 20 (fr. 3022) the g and the t
  are true. The two volumes are in two hands.
- 11 groups of no. 20 that were read as "e" or "o" are the capital sign Q.
- The readers had corrected 84 tokens by hypothesis before the images were checked. The images confirm 76.
- Blind spot check: 3 lines chosen at random before looking, transcribed again from the image: 43 of 46 groups
  the same, no number different.
- The duplicate of the first "Ranzo" letter (BnF fr. 3019, f. 73, Gallica `btv1b9059994n`, views 114 to 116) is
  a plain copy: the same groups and the same nulls. 807 places agree, 6 are variants. It confirms 41 of the
  corrections and adds 8.
- The corrections alone did not raise the share of text that reads. The first pass had already read most of
  these places through its own hypotheses.

## The last pass and its blind audit

- One reader read the corrected text again with the table of the third pass. Result: 775 values (117 sure, 589
  probable, 69 guesses); 117 connected stretches with 3,377 of 3,914 cipher tokens (86 %).
- Its own check: 40 values chosen at random, hidden, and found again from order and context: 34 the same; 6 fit
  the context and broke the order of the list.
- **Blind audit by a fresh reader.** 80 values were hidden in the table (seed fixed before the draw): 40 of
  class probable that occur once, 30 of class probable that occur more often, 10 of class sure. The auditor saw
  the corrected text, the table without these values, and the general rules of the cipher. It saw no reading
  and no notes. Its record of file access was checked.

  | Hidden values | Exactly the same | Another form of the same word | Different |
  |---|---|---|---|
  | 40 probable, one token | 38 | 1 | 1 |
  | 30 probable, more tokens | 24 | 5 | 1 |
  | 10 sure | 10 | 0 | 0 |
  | all 80 | 72 | 6 | 2 |

  The two that differ: c21 (table "calculo", auditor "caldo") and f15 (table "fato", auditor "fatto").
- What this measures: the table hangs together. A value can be found again from its neighbours in the list and
  from the sentence. What it does not measure: whether the frame is right. For that see the signs listed in the
  README (the reversed alphabet, the date line, the clear runs, the sheet f. 50).
- All readers and the auditor are instances of one model.
