# Readings of historical ciphers

Cipher letters from European archives of 1503 to 1653, read or rebuilt in October 2026. Each folder holds one
result, with its reading, its key, its controls and its search for earlier work.

**The work was done by a model** (Claude, by Anthropic, running as Claude Code with subagents), directed by
Paolo Rosson. No palaeographer or historian has checked it yet. Each folder says plainly what is new, what is only
reproduced from a period source, and what stays open. Corrections are welcome: please open an issue.

## The results

| Folder | Document | What is new | State |
|---|---|---|---|
| [oxford-1646](oxford-1646/) | An intercepted letter to King Charles I from besieged Oxford, 13 May 1646 (British Library, Add MS 72438, f. 10) | The first connected reading (an earlier partial reading by A. Aymeloglu had about 45 code values). The key is rebuilt from the printed Titus cipher of 1648, with a shift. | 89 % of the tokens read; the transcription is A. Aymeloglu's, and we did not see the manuscript |
| [cocquet-1616](cocquet-1616/) | Coquet to Mangot, Rome, 13 November 1616 (BnF, Clairambault 369, ff. 316-317) | First reading. Solved from context, then confirmed by the period key sheet (BnF fr. 18009, f. 156). | All cipher passages read |
| [espagnol-318](espagnol-318/) | The viceroy of Sicily to King Ferdinand, Messina, 27 April 1503 (BnF, Espagnol 318, no. 94) | First reading. The key is rebuilt from the letter itself. | Read in large part; 64 code words have no value |
| [dutch-1653](dutch-1653/) | The Dutch deputies in England to Boreel, 1 September 1653 (Thurloe, *State Papers*, i.435) | The key, and the link to the printed Dutch minute. The text itself is reproduced. | 127 of 131 groups fit |
| [espagnol-132](espagnol-132/) | Three letters of Antonio Pérez, one page of Philip II, and a memorial of the Duke of Savoy (BnF, Espagnol 132) | First readings with keys that others published. | Five pieces read |
| [gonzaga-1590](gonzaga-1590/) | Cardinal Scipione Gonzaga to the Duke of Nevers, 1586 to 1590 (BnF, fr. 4698, fr. 4702 and fr. 4696) | The cipher rebuilt with no key sheet; three period decipherments linked to their cipher letters; the rebuilt code tested on a second volume (97.6 % of 463 words right); letters and passages with no decipherment read, and checked against Pastor's history. | A code of 448 values; the new readings have gaps |

Four of these documents are on S. Tomokiyo's list of
[unsolved historical ciphers](https://cryptiana.web.fc2.com/code/unsolved.htm): the letter to Charles I, Cocquet's
cipher, the Dutch ciphers of 1653, and the Spanish letters of 1497 to 1504.

Two earlier results have their own repositories:

- [pangoleen/desportes-1593](https://github.com/pangoleen/desportes-1593): two letters of the Catholic League of
  22 July 1593, read for the first time (BnF fr. 3984).
- [pangoleen/senecey-1594](https://github.com/pangoleen/senecey-1594): two League letters of 1594, read with the
  alphabet that the royal decipherers rebuilt (BnF, Cinq Cents de Colbert 33).

## How the work is done

1. **Find help that nobody linked.** Most results here came from a clear text or a key that already existed
   somewhere: a decipherment in a sister volume, a key sheet in another collection, a minute in a printed book, a
   sister cipher in an edition of 1852. The search of catalogues and printed sources comes first.
2. **Transcribe twice.** Two passes for each cipher line, the second one blind, and a measured rate of agreement.
3. **Control every reading.** A wrong-key or shuffled-key score, period glosses, or an outside source that was
   not used as a crib.
4. **Search for earlier work before any claim.** The lists of S. Tomokiyo, the other projects of 2026, printed
   editions, and the catalogue of the same and the sister volumes. A text that a period source or another
   project already has is called "reproduced".

## What did not work

Three targets of the same days gave no reading: an intercepted list of cover names of 1659 (no key fits), a letter
of Marshal Catinat of 1702 (no key and no clear text; a blind attack failed its own control), and the letters of
Juan Manuel to Charles V of 1522 (no free images). Short texts with no key and no clear text stayed closed.

## Credits

- **Satoshi Tomokiyo** ([Cryptiana](https://cryptiana.web.fc2.com/code/crypto.htm)) described most of these
  ciphers and keeps the list of unsolved ones.
- **Daniel Bourdeau**, **Ari Aymeloglu**, **NoAutopilot/cipher-lab**, **el-descifrador/cabinet-noir** and
  **Satoru** worked on the same lists in 2026. Each folder says what it owes to them.
- **Bibliothèque nationale de France / Gallica**, the **British Library**, the **DECODE** database, the Internet
  Archive and British History Online provide the sources.

## Licence

Code and tables: MIT. Text: CC BY 4.0. Images: under the conditions of their sources. Details are in
[LICENSE.md](LICENSE.md).
