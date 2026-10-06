# Guide: where everything is

This file is a map of the repository. It is for a person who is new here, and for an AI model that a person
points at the repository ("read GUIDE.md in pangoleen/cipher-readings and tell me about the 1528 cipher").

## In one paragraph

In September and October 2026, Paolo Rosson directed Claude (by Anthropic, running as Claude Code with subagents)
to read old cipher letters from European archives, 1503 to 1653. Nine results came out of it. Seven are in this
repository, and two earlier ones have their own repositories. Each result has its key, its reading, its
transcription, its controls, and a page where a person can check the decoding by hand.

- Pages to check by hand: <https://pangoleen.github.io/cipher-readings/>
- All files: <https://github.com/pangoleen/cipher-readings>
- A raw file: `https://raw.githubusercontent.com/pangoleen/cipher-readings/main/<path>`

## The results, one line each

| Year | Folder | The story | State |
|---|---|---|---|
| 1503 | [espagnol-318](espagnol-318/) | The viceroy of Sicily writes to King Ferdinand from Messina. The key is rebuilt from the letter alone. | Read in large part; 64 code words are open |
| 1528 | [centurione-1528](centurione-1528/) | Martino Centurione, envoy of Genoa in Madrid, writes to his son under the cover name "Hieronimo Ranzo". He tells him to show the letter to nobody "except your mother". | 86 % reads as connected sense; 779 values |
| 1577-80 | [espagnol-132](espagnol-132/) | Three letters of Antonio Pérez, one page of Philip II, and a memorial of the Duke of Savoy, from the secret letters to the Spanish ambassador in France. Read with keys that other people published. | Five pieces read |
| 1586-90 | [gonzaga-1590](gonzaga-1590/) | Cardinal Scipione Gonzaga writes to the Duke of Nevers. The word code is rebuilt with no key sheet. | 448 values; 97.6 % right on a second volume |
| 1593 | [pangoleen/desportes-1593](https://github.com/pangoleen/desportes-1593) | Two intercepted letters of the Catholic League, Paris, 22 July 1593: "and on Sunday he is to go to Mass". Henri IV did so three days later. | Read in full |
| 1594 | [pangoleen/senecey-1594](https://github.com/pangoleen/senecey-1594) | Two League letters, read with the alphabet that the royal decipherers rebuilt. | Read |
| 1616 | [cocquet-1616](cocquet-1616/) | The secretary of the French ambassador in Rome writes to the secretary of state. First solved from context. Then the period key sheet was found in another volume, and it agrees. | All cipher passages read |
| 1646 | [oxford-1646](oxford-1646/) | An intercepted letter to King Charles I from besieged Oxford. The key comes from a printed sister cipher, with a shift. | 89 % of the tokens read |
| 1653 | [dutch-1653](dutch-1653/) | The Dutch deputies in England write to the Dutch ambassador in France. Cromwell's government intercepted the letters. The key is rebuilt from a minute printed in 1725. | 127 of 131 groups fit |

## Where each kind of file is

| You want | Look here |
|---|---|
| The summary of one result, with its limits | `<folder>/README.md` |
| The key | `centurione-1528/key/table.tsv`, `cocquet-1616/key_fr18009_f156.tsv`, `espagnol-318/KEY_TABLE.md`, `dutch-1653/key.tsv`, `oxford-1646/key1646.tsv`; for Gonzaga, the folder `gonzaga-1590/alignment/` |
| The reading (decoded text) | `centurione-1528/reading/`, `cocquet-1616/reading.md`, `espagnol-318/READING.md`, `espagnol-132/reading_*.md`, `gonzaga-1590/editions/` and `gonzaga-1590/fr4696/readings.md`, `oxford-1646/reading_f10.txt`, `dutch-1653/reading_*.txt` |
| The transcription of the cipher | `<folder>/transcription/`, `<folder>/passes/`, or `pass1.txt` and `pass2_blind.txt` |
| The controls and the search for earlier work | `<folder>/evidence/` (each has a `worklog.md`) |
| Images of the manuscripts | `<folder>/images/` (page images), `docs/img/<folder>/` (lines cut for the check pages) |
| Images made to share | [`share/`](share/) |
| The code that decodes | `<folder>/decode.py` or the `.py` files of the folder |

## Images made to share

- [`share/centurione-1528-dateline.png`](share/centurione-1528-dateline.png): the date line of the second "Ranzo"
  letter of 1528 (BnF fr. 2988), with the reading at each sign: "Madrid ... de marzo mille cinquecento vinti octo".

## Who checked what

- **Satoshi Tomokiyo** ([Cryptiana](https://cryptiana.web.fc2.com/code/crypto.htm)) keeps the list of unsolved
  historical ciphers. He wrote an article on two of the results:
  - the 1528 cipher: ["A Cipher with Superscripts for Word Elements ('Hieronimo Ranzo') Solved by AI"](https://cryptiana.web.fc2.com/code/ranzo.htm),
    6 October 2026. One day earlier, his article ["Codebreaking with AI"](https://cryptiana.web.fc2.com/code/ai.htm)
    had named this cipher as one that stayed out of reach of AI.
  - the letters of 1593: ["An Intercepted Report of Henry IV's Upcoming Attendance at Mass in a Polyphonic Cipher"](https://cryptiana.web.fc2.com/code/polyphonic1593.htm).
- **Paolo Rosson** is Italian. He read the decoded Italian of the 1528 letters himself, and he proposed or confirmed
  seven open words.
- **No palaeographer or historian has checked the other results yet.** Each folder says so.

## How to judge a result yourself

1. Open its page at <https://pangoleen.github.io/cipher-readings/>. It shows the key and a few lines of cipher,
   decoded sign by sign beside the image.
2. Read "What is new" and "What stays open" in the folder's `README.md`. Some results are a first reading. Some are
   only a key for a text that was already in print. The README says which.
3. Read `evidence/`. Each reading has a control: a score with a wrong or shuffled key, a blind second
   transcription, a blind test on a made-up code with hidden answers, or an outside source that was not used as a
   crib.

## What did not work

The root [README](README.md) lists the targets that gave no reading. A failed attempt is reported as failed.

## Credits and licence

The root [README](README.md) names the people whose transcriptions and lists this work rests on. Code and tables:
MIT. Text: CC BY 4.0. Images: under the conditions of their sources ([LICENSE.md](LICENSE.md)).
