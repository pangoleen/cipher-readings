# Blind audit of the key, 11 October 2026: summary

The question of this test: do the values of the key follow from the text, or only from the first reader?

## What was done

- A second run of the model, with a new context, was the auditor.
- It had three files only. They are in [blind_audit/](blind_audit/): `groups.txt` (the text, cut into groups),
  `masked_key.txt` (the key with ten values hidden) and `masked_decode.txt` (the decode with the ten groups
  shown as gaps).
- It did not have the notes, the full key or the images.
- The ten hidden groups were 87, 83, 93, 98, 5, 152, 141, 192, 58 and 12.

## Result

| Group | Places | Hidden value | Value of the auditor | Auditor's confidence | Result |
|---|---|---|---|---|---|
| 87 | 10 | g | g | sure | right |
| 83 | 14 | b | b | sure | right |
| 93 | 18 | m | m | sure | right |
| 98 | 25 | t | t | sure | right |
| 5 | 53 | i | i | sure | right |
| 152 | 17 | di | di | sure | right |
| 141 | 8 | che | che | sure | right |
| 192 | 10 | la | la | sure | right |
| 58 | 12 | si | si | sure | right |
| 12 | 10 | ma | ma | sure | right |

**Score: 10 of 10.**

The words that the auditor gave as witnesses: disgusto, esseguirsi, segnate, gagliarda, ragioni; impossibili,
sarebbe, dicembre, buona; Milano, morte, monarchia, numero; presenta, autorità, sollevatione; heresia, Francia,
Sicilia, primo; stato di Milano, predice; che si presenta, speranza che da lui nascesse, poi che pure; bella,
della monarchia, alla sua heresia, lasciata; facilissimamente, scrissi, si trova; malissimo, ma impossibili,
già mai.

- The auditor saw without help that the word groups 141 to 148 and 192 to 193 stand in the order of the alphabet.
- It named one rough place: line 2 reads "sperandi far", where "sperando" is expected. This place is open in the
  reading too.

## Limits of this test

- **The auditor is a language model of the same family as the reader.** The two can share a wrong habit.
- **The cut into groups was given to the auditor.** The test does not test the cut rule.
- The test does not test the figures. The auditor did not see the images.
- The ten hidden groups all stand 8 times or more. The test does not touch the values that stand once.
- The test shows one thing: the hidden values follow from the other values and from the Italian.
- Nobody can prove that the auditor opened no other file. We report what it was given.

## The state of the package

The three files show the work as it stood at the time of the audit. Two things changed after it:

- The groups 29 and 39 were not yet cut. Line 11 has `2 3 99 3 5`, and line 16 has `2 2 99 7`. The held-out passage
  of f. 83r gave the new cut ([heldout_f83r.md](heldout_f83r.md)).
- The values 29 (non), 135 (ben), 154 (dove) and 163 (fatto) were not yet in the key. All four are "probable"
  in the key table of today.
