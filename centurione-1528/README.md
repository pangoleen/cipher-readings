# The "Garbino" cipher of 1528: read for the greater part

Paris, BnF, ms. français 3022, no. 20 (a letter dated Madrid, 11 April 1528, to "Garbino") and the letters signed
"Hieronimo Ranzo" in BnF fr. 2988 and fr. 3019 are written in a cipher of letters with small numbers above them.
It is on S. Tomokiyo's list of unsolved historical ciphers as "Venetian? Cipher with Superscript Digits (1528)".

**Status: 5 October 2026. The cipher is read for the greater part.** 86 % of the cipher text lies in stretches
that read as connected sense ([reading/islands.md](reading/islands.md), 117 stretches). The rest has gaps and
guesses. The work was done by a model. No palaeographer has checked it. The transcription is D. Bourdeau's; we
checked it on the page images and list our corrections; it is not copied here.

## What is new

1. **The build of the cipher.** It is a code of stems, with a small alphabet of single letters for the endings.
2. **A key table of 775 values** ([key/table.tsv](key/table.tsv)): 117 sure, 589 probable, 69 guesses.
3. **The dates.** Both "Ranzo" letters are of Madrid, March 1528. The catalogue has them without a date.
4. **The writer.** The "Ranzo" letters are letters of a father to his son. The father is Martino Centurione,
   envoy of Genoa at the court of Charles V. "Hieronimo Ranzo" is the name under which he gets his mail.
5. **The content**, in summary: [reading/contents.md](reading/contents.md).

## The cipher

A group is a base letter and a number.

| Numbers | What they are |
|---|---|
| 0 to 5 | Nulls. They stand between words, in a different place each time. |
| 6 to 9 | One alphabet of single letters. The base letter is the cipher letter; 6, 7, 8 and 9 are four signs for the same letter. |
| 10 and above | The list of the base letter. The value begins with the base letter. The list runs in alphabetical order, by word family (altro, altra, altre). |

- The lists hold many **stems**. The writer adds the ending with a single letter: `present-e`, `cos-a`,
  `script-o`, `have-n-do`, `pot-u-ta`. A word that is not in the list is spelled from syllables and letters:
  `ma-d-r-d` (Madrid), `re-ce-vu-to`, `carta-ge-ni-a`.
- **The alphabet of the numbers 6 to 9**, from the contexts:

  | Cipher letter | z | s | f | e | c | v | t | d | q | h | m | n | l | o | i |
  |---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
  | Plain letter | a | e | r | s | u | c | d | t | g | n | o | i | m | l | p |

  The first nine pairs are the alphabet of 21 letters read backwards (a-z, b-x, c-u, d-t, e-s, f-r, g-q). Three
  more pairs of the same rule turned up later, each at one or two places: cipher r = f, a = z, x = b. The last
  six pairs of the table are the middle of the alphabet in another order; we do not know its rule. The values
  t, d, q, o, i rest on few places.
- The y-groups read "et" (112 of 113 places). The sign Q, a capital letter, reads "con" (46 places).
- Before this was seen, the numbers 6 to 9 were taken for one value of the base letter, and z6 to z9 for nulls.
  That is why solvers gave no sense.

## How it was read, and how far to trust it

1. A solver that uses the alphabetical order gives a first decode. On made-up codes of the same build it has
   about half of the tokens right.
2. A reader then works like a codebreaker by hand: propose a word from the context, check that it keeps the
   order of the list, read all places of the group, accept or drop. The reader is a model.
3. **A blind control.** Two made-up codes with hidden answers went through the same procedure. The readers saw
   only their own package. Result: 87.6 % and 93.4 % of the tokens right (the solver alone: 50.5 % and 52.4 %).
   Details: [evidence/controls.md](evidence/controls.md).
4. Two readers then read the real text, each alone. A third pass merged them and tested the alphabet of 6 to 9.
   This gave 53 % of the text in connected stretches.
5. **The transcription was checked on the images.** Every line was compared with the page. 144 groups were
   corrected ([evidence/transcription_corrections.tsv](evidence/transcription_corrections.tsv)). The cause of
   most errors: two hands. In the "Ranzo" letters the s is a plain 8 and was often read as g, and the r was read
   as t. In no. 20 the same 8-like sign is a true g. A blind check of three random lines agreed with the
   transcription in 43 of 46 groups, and no number differed. The duplicate of the first "Ranzo" letter (fr. 3019,
   f. 73) is a plain copy with the same groups; it confirmed 41 of the corrections and fills three damaged places.
6. A last pass read the corrected text again, weakest pages first. It gave 86 %.
7. **A blind audit of the last pass.** 80 values of the table were hidden: 40 that occur once, 30 that occur
   more often, 10 of class sure. A fresh reader saw only the text and the rest of the table. It restored 72 of
   the 80 exactly (38 of the 40 that occur once), and 6 more as another form of the same word (quel and quelle,
   secur and securo). Two differed.

**The limits, stated plainly.**

- The real cipher has features that the made-up codes did not have (the stems and the alphabet of 6 to 9). So
  the control proves the method, and it does not measure the real reading. The share of right tokens on the real
  text is an estimate: about 85 % overall, about 92 % inside the stretches of `reading/islands.md`.
- The audit shows that the values hang together: the context and the order of the list force each one. It
  cannot show that the whole is right.
- The last pass was one reader. It raised about 100 earlier guesses to "probable" because their sentence now
  reads, and most of its 155 new values occur once. The class "probable" is the main risk.
- All readers are instances of one model. Agreement between them shows that a value is repeatable. It does not
  prove it.
- 17 places are read through a guess about one wrong digit or letter. They are marked.
- Some pairs of values break the order of their list. They are flagged in the table. In the audit, 6 of 40
  values fit their context and broke the order.
- 86 groups (83 tokens) have no value. The weakest page is fr. 3022 f. 46v (66 %).
- The writer made slips himself: the first copy of the first "Ranzo" letter has t41 where the cipher needs r41,
  and the duplicate has r41.

**Signs that the reading is real.** None of them was used as a crib by the reader who found it.

- The alphabet of 6 to 9. A reader found z = a, s = e, c = u, f = r, e = s, t = d from the contexts alone. These
  six pairs are a reversed alphabet. Nobody had told the reader to expect a rule.
- The date line. Both "Ranzo" letters hold the same four groups in the same order, m176 c193 v152 o66, with
  different nulls between them: "mille cinquecento vinti octo". The group v152 stands in the day and in the
  year ("vinti sette de marzo ... vinti octo"). The place before it is spelled `ma-d-r-d` in one letter and
  `ma-d-i-d` in the other. All these values keep the order of their lists (ma 10, marzo 82, mille 176).
- The clear runs of no. 20 go on into the cipher runs without a break of sense: "DAPOI DE HAVERVI SCRIPTO PER
  PIU LETTERE a genoa per man de hieronimo".
- The words that the sheet f. 50 adds to the lists (cosa, suo, stato, the future endings) are the words that the
  letters spell out piece by piece. And the letter itself announces the sheet: "mandoti una altra adicione del
  zifra presente". (The last pass knew the sheet; the first two readers did not.)

## Who wrote to whom

- **The "Ranzo" letters (fr. 2988; fr. 3019 f. 73 is a duplicate of the first one) are from a father to his son.** They say "tu". They
  close "Vale. Tuo padre ti saluta". The father says that his secret letters begin "Fili dilectissime", "where I
  usually put Amantissime fili". He forbids the son to speak of one matter "con persona del mondo altra che con
  toa madre".
- **The father is Martino Centurione.** His clear letter to his son Girolamo (fr. 3022, f. 58, Burgos, 16-17
  January 1528, printed by Molini in 1837) begins "Amantissime fili", sends additions to this same cipher
  ("a la littera r agiongeraili recevut. r336 ... garbino g215"; the same values stand on the sheet f. 50), and
  names the same persons and matters: Cattaneo, Savona, the "Unione", the way of Lyon.
- **"Hieronimo Ranzo" is a name for the mail.** The father orders the son to send his letters "qua a Hieronimo
  Ranzo". A Girolamo Ranzo was chamberlain of the Grand Chancellor Gattinara. The signature "V.o Hieronimo
  Ranzo" under the father's letters is then a cover. (The name is read through a corrected base letter.)
- **No. 20 (fr. 3022, Madrid, 11 April 1528) is by the same hand of the network, to another person.** The writer
  says "voi". He writes "all the time to Hieronimo" at Genoa, and has ordered him to send the addressee a copy,
  with "our cipher". So he is probably Martino again, and the Hieronimo at Genoa is his son. The addressee is
  not the son. "Garbino" at Lucca is a cover address: the clear letter of January says that the son wrote "in
  zifra in nome del Garbino de Luca".

**The history of our own statements, for the record.** On 5 October in the morning this page said that no. 20
is a letter of Martino to his son. At noon we withdrew that, because no. 20 says "voi", and we named Ranzo as
the probable writer, as D. Bourdeau had done before us. The reading now shows a third picture: the father and
son letters are the "Ranzo" letters, and no. 20 is probably Martino to somebody else. Each step followed the
evidence of its hour. The present one rests on a part reading and can change again.

## What the letters say, in short

- **To the son (March 1528).** Letters written "with milk" could mostly not be read: leave more room between the
  ink lines. Report more, and day by day, above all on Savona. Send what the Emperor must see in separate
  letters, in the large cipher, in a disguised hand, under another name. Keep the ciphers and copies hidden. The
  father hopes for a presidency in the "Camera de la Sumaria" of Naples, with the favour of the Grand
  Chancellor. He sends "una altra adicione" to the cipher.
- **No. 20 (April 1528).** A Duke, probably of Milan, must stay in the Emperor's grace: his acts against the
  Emperor "non siano voluntarie salvo violente". His ambassador is "the cavalier Bilia". Money for Italy: a plan
  to take "oro et argenti superflui de le giesie" as a loan. The worst thing at court is "la inresolucione": "if
  God had not helped them, they would be in a fine state". Who will govern Naples: "at times there was talk of
  the Grand Chancellor, at times of ..., at times of the Archbishop of Toledo". The court sounded the Venetian
  orator in secret, "ma lui non ha voluto prestare orechie". The Emperor leaves for Valencia "a li vinti del
  presente".

More, with the doubtful points marked: [reading/contents.md](reading/contents.md).

## To check it

1. Take a transcription of the letters (D. Bourdeau's: `dbourdeau/cyphersolver`, `targets/vasto1527`).
2. Run `python3 decode.py FILE`. It applies our corrections and then `key/table.tsv`. A value with `?` is
   probable, with `??` a guess.
3. Compare with [reading/islands.md](reading/islands.md).

A quick test by hand: the last line of the second "Ranzo" letter (fr. 2988, Gallica `btv1b9059908w`, view 20)
has the groups m176, c193, v152, o66 with small numbers between them. They read "mille cinquecento vinti octo".

## Earlier work, and what this folder owes

- **Satoshi Tomokiyo** listed the cipher, saw that the base letter is the initial of the word, and guessed that
  the code is alphabetical.
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`, target `vasto1527`) transcribed the letters. All readings here
  rest on his transcription. He found that the copy in Clairambault 327 has its original in fr. 3022, he named
  Hieronimo Ranzo, "Gattinara's man", in connection with no. 20, and he described ff. 48-50 as the kit of an
  agent. His catalogue lists the cipher as open (26 September 2026).
- **NoAutopilot/cipher-lab** checked the editions and the clear postscript, tested the g/s relabelling, and
  compared the two copies of the first "Ranzo" letter (fr. 2988 and fr. 3019) on 3 October 2026. Our comparison
  reproduces theirs. Its notes list the cipher as open (3 October 2026).
- **G. Molini** (1837) printed the clear letter of January 1528.
- We found no earlier reading (search of 5 October 2026, 12:00 UTC).

## Contents

| File | Content |
|---|---|
| `key/table.tsv` | The key: group, value, class (sure, probable, guess, null), number of tokens, note |
| `reading/islands.md` | The 117 stretches that read as connected sense, with an English gloss |
| `reading/contents.md` | What each letter is about; the dates; what stays open |
| `evidence/controls.md` | The blind test on made-up codes, the check on the images, the blind audit |
| `evidence/transcription_corrections.tsv` | Our 144 corrections to the transcription: file, line, position, old group, new group |
| `evidence/worklog.md` | The earlier search for a clear text and the tests of the order |
| `decode.py` | Applies the key to a transcription |
| `images/` | The passage of f. 58 with the cipher values, and the addition sheet f. 50 (reduced; "gallica.bnf.fr / BnF") |

Code: MIT. Text: CC BY 4.0. Details are in [LICENSE.md](../LICENSE.md).
