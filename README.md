# Cocquet to Mangot, Rome, 13 November 1616: the cipher read

A first reading of the cipher passages in a letter from Coquet, secretary of the French ambassador in Rome, to
Claude Mangot, secretary of state. The letter is on S. Tomokiyo's list of unsolved historical ciphers
("Cocquet's Cipher (1616)").

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| Coquet to Mangot, Rome, 13 November 1616 | Paris, BnF, Clairambault 369, ff. 316-317 (Gallica `btv1b9000782k`, views 328-330) | Not deciphered; no key known | [reading and translation](reading.md) |

**Status: 4 October 2026.** The work was done by a model. No palaeographer has checked it. Corrections are welcome:
please open an issue.

## The key is a period document

The cipher is the cipher of the French embassy in Rome. Its key sheet survives: Paris, BnF, ms. français 18009,
f. 156, "Double du chiffre baillé à monsieur le marquis de Treinel" (Gallica `btv1b90638776`, view 181;
[image](images/fr18009_f156_key.jpg)). The marquis de Tresnel was the ambassador, and Coquet was his secretary.
We found no earlier use of this sheet for this letter.

The order of work matters for the proof. The cipher was first solved from context, with the crib "a don pedro".
The key sheet was found afterwards. All 43 sign values of the solution agree with the sheet, with no conflict. The
sheet then corrected five points (the code 89 = "qu'il", the words "hault" and "quant", the sign for "il", and the
doubling sign).

## What the cipher says

The letter reports a rumour in Milan that Louis XIII was dead. The cipher passages name the source:

- "que le duc de Montaleon auoit mande que sa maieste auoit un sy grand desuoyement hault et bas qu'il croyoit
  qu'elle ne pouuoit passer" [deux heures]
- [cest homme ... mande force choses] "a don Pedro"
- "quant il les a veu mal aller il a porte" ... "il le dispose a la pais"
- [ses intentions ne tendent qu'à] "aneantir l'auctorite du roy en ce pays"

The duke of Monteleone was the Spanish ambassador in France. Don Pedro de Toledo was governor of Milan. Louis XIII
was gravely ill at the end of October 1616.

## How good is it

| Measure | Value |
|---|---|
| Cipher signs | 189, in nine runs inside clear French |
| Signs identical in the two transcription passes (the second blind) | 179 (94.7 %); no difference changes a word |
| Sign values of the context solution that agree with the key sheet | 43 of 43 |
| Four-letter-group score of the reading | -10.47; 2,000 shuffled keys: mean -15.42, best -13.13 |

Limits: the clear French around the cipher had one pass only, and some clear words are doubtful ("son frere"
among them). The first sign of the word read "car" has no exact match on the key sheet. Two pairs of signs are close
in shape, and the context decides between them.

To repeat the decoding and the control:

```bash
python3 decode.py
```

## Earlier work

Searched on 4 October 2026: S. Tomokiyo's pages on the ciphers of Louis XIII's reign and on unsolved ciphers (the
letter is given as not deciphered), D. Bourdeau's `cyphersolver` (a first look only, September 2026),
A. Aymeloglu's `unsolved-ciphers` (parked), `NoAutopilot/cipher-lab` (open), `el-descifrador/cabinet-noir` (no
entry), the BnF notices of Clairambault 362 to 376, and Avenel's edition of Richelieu's letters. No reading and no
printed text of the letter was found.

## Open points

- The same key should read the cipher letters of the ambassador Tresnel in the same volume. This is in work.
- A second pass on the clear text.

## Contents

| File | Content |
|---|---|
| `reading.md` | French text with the cipher passages in bold, English translation, notes |
| `transcription.txt`, `pass1.txt`, `pass2_blind.txt` | The signs of each cipher line, and the two passes |
| `decode.py`, `decoded_by_key.txt` | The decoder with the key table, the comparison of the passes, and the control |
| `evidence/worklog.md` | The work log, with the search for sister letters and for the key |
| `images/` | The key sheet and the cipher page, reduced, with the credit "gallica.bnf.fr / BnF" |

## Credits

- **Satoshi Tomokiyo** listed the letter as unsolved and described its cipher.
- **Daniel Bourdeau** and **Ari Aymeloglu** looked at it in September 2026 and noted what was missing.
- **Bibliothèque nationale de France / Gallica** provides the page images.
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code: MIT. Text: CC BY 4.0. Images: reduced images from Gallica, under the BnF's conditions of reuse.
