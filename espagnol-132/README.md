# BnF Espagnol 132: five pieces in cipher that had no reading

Paris, BnF, ms. Espagnol 132 holds the secret letters of Philip II and of his secretary Antonio Pérez to Juan de
Vargas Mexía, Spanish ambassador in France, 1577 to 1580 (Gallica `btv1b10032556x`). Other projects read most of
the volume in September and October 2026. This repository reads the five pieces that none of them had.

**Status: 4 October 2026.** The work was done by a model. No palaeographer has checked it. Corrections are welcome:
please open an issue.

## The keys are not ours

J. P. Devos published the ciphers of Vargas Mexía in 1950, and S. Tomokiyo completed and broke the remaining ones in
2020 ([cryptiana, unsolved ciphers, "Secret Letters to Juan de Vargas Mexia"](https://cryptiana.web.fc2.com/code/unsolved.htm)).
The project `el-descifrador/cabinet-noir` published some code values of Pérez's private cipher on 2 October 2026.
We applied these keys and added a few code values, each with its evidence.

## What is read

| Piece | Cipher | What is new | Reading |
|---|---|---|---|
| Antonio Pérez to Vargas Mexía, Madrid, 13 September 1578 (f. 87), 8 December 1578 (f. 157), 26 January 1579 (f. 179) | Pérez's private cipher ("Cipher 4") | The cipher passages. The plain Spanish is in print (S. R. Rubino, 2012), with `[CIFRA]` in place of every cipher passage. | [reading](reading_perez_f87_f157_f179.md) |
| Philip II to Vargas Mexía, March 1578 (f. 26r, first page only) | "Cipher 2" | The whole page | [reading](reading_f26r.md) |
| A memorial in Italian of the Duke of Savoy on the march of 3,000 Spaniards to Flanders (ff. 273-274) | "Cipher 2" | The whole text; it is not a letter of Philip II, and its content dates it to 1573 | [reading](reading_f273_274_savoy_memorial.md) |

Some phrases:

- Pérez: "En lo del quatrumvirato ... que no aya ay Arcauti ni nadie sino solo V.m."; "lo que huviere de ser para
  mi solo venga en la zifra particular".
- Philip II, on Thomas Stukeley at Palamós: "le he mandado proveer de veynte mill escudos en oro, con persona
  propria, secretamente", so as to "desassossegar" the Queen of England.
- The memorial: "chi resterà padrone del mare sarà anco signore della terra".

## How good is it

| Piece | Two transcription passes agree | Wrong-key control (500 shuffled keys as good as the true key) |
|---|---|---|
| Pérez, f. 87 | 91.0 % | 0 |
| Pérez, f. 157 | 91.2 % | 0 |
| Pérez, f. 179 | 90.8 % | 0 |
| f. 26r | 80.0 % | 0 |
| ff. 273-274 | 80.0 to 87.2 % | 0 |

Limits, stated plainly:

- For the Pérez letters the second pass was blind and the first was not: its author had seen a published key file.
- For "Cipher 2" the passes differ in 13 to 20 % of the groups, mostly in the place of a dot. The differences were
  settled by sense and not by a third look at the image.
- f. 26 stops after line 27: ff. 26v to 31r are not in the Gallica scan.
- Eight code words of Pérez's cipher have no value, and two places on f. 87r are not resolved.
- No decipherment is on any of these leaves. The Simancas minutes, Teulet, Marañón and the Turin archives were not
  checked, so a clear text can exist there.

To repeat the control:

```bash
python3 control.py c4 es passes/perez_passA.txt
```

## Earlier work

Checked on 4 October 2026 (12:40 and 13:18 UTC): `el-descifrador/cabinet-noir` (about 30 letters of the volume read;
single decoded phrases of the three Pérez letters in its key file, no reading of them), satoru.net/crypt (three
other letters), `NoAutopilot/cipher-lab` (reading other letters of the volume now), Gachard, Mignet, Rubino, the BnF
record, and five web searches. None has a reading of these five pieces.

## Contents

| File | Content |
|---|---|
| `reading_*.md` | Text in the original language, with the decoded cipher marked, and an English translation |
| `passes/` | The transcription passes |
| `c2.py`, `c4.py` | The key tables and decoders for the two ciphers |
| `cmp2.py`, `cmp4.py`, `control.py`, `corpus/` | The comparison of passes and the wrong-key control |
| `evidence/worklog.md` | The work log: the state of the other projects, the key values added, the search for earlier work |

## Credits

- **J. P. Devos** and **Satoshi Tomokiyo** published and broke the ciphers.
- **el-descifrador/cabinet-noir**, **Satoru** and **NoAutopilot/cipher-lab** read the other letters of the volume.
- **S. R. Rubino** printed the plain Spanish of the Pérez letters.
- **Bibliothèque nationale de France / Gallica** provides the page images.
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code: MIT. Text: CC BY 4.0.
