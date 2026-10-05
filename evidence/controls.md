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
- The third pass merged both, tested the alphabet of 6 to 9 on all contexts, and extended the table to 634
  values. Its own estimate: about 75 % of the tokens right, and about 93 % inside the stretches of
  `reading/islands.md`. These are estimates, not measurements.
