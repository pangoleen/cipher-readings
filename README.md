# A lost letter to Charles I from besieged Oxford, 13 May 1646: the cipher read

The first connected reading of an intercepted cipher letter to King Charles I, written in Oxford during the siege and taken by
Fairfax's army. The letter is on S. Tomokiyo's list of unsolved historical ciphers ("An Intercepted Letter to
Charles I (1646)").

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| [Sir Edward Nicholas, Secretary of State,] to Charles I, Oxford, 13 May 1646 | London, British Library, Add MS 72438, f. 10 (DECODE record R8624) | Partly read: about 45 code values from Nicholas's glosses in Evelyn (A. Aymeloglu, September 2026), which give about a quarter of the tokens | [reading and translation](reading_f10.txt): 89 % of the tokens read |

**Status: 4 October 2026.** The work was done by a model. **We did not see the manuscript.** The cipher text is the
transcription of A. Aymeloglu (`aaymeloglu/unsolved-ciphers`, folder `royalist-1646`), made in one pass from the
DECODE image. It is not copied here. No palaeographer has checked the reading. Corrections are welcome: please open
an issue.

## The help that nobody had linked

The word list of this cipher is the list of the King's cipher with Captain Titus of 1648. George Hillier printed the
Titus letters with their figures and a decipherment in 1852 (*Narrative of the Attempted Escapes of Charles the
First*, pp. 153-161). The numbers of 1646 are the Titus numbers with a small shift:

| Words | Shift from Titus 1648 to the cipher of 1646 |
|---|---|
| a to h (an, and, be, for ...) | +4 |
| i to n (I, if, in, it, me, my, not ...) | 0 |
| o to t (of, or, send, so, the, to ...) | +1 |
| w (was, where, which, with ...) | +8 |
| write, you, numbers, days and months | +9 |
| second list of names and nouns | +10 |

74 words are in both tables. 67 of them fall in the band of their first letter. Seven have another shift (but,
give, may, re, us, up, we); they can be slips in one of the two reconstructions, or real differences. The 20 words that Nicholas himself glossed in
two letters of the King of 1646 (Evelyn's *Diary and Correspondence*, iv. 178-179) fit the same shifts. The letter
alphabets of the two keys differ, and the one of 1646 was solved from context. The key is
[key1646.tsv](key1646.tsv): 261 codes, each with its basis.

## What the letter says

The writer reports the state of Oxford to the King, who had left the town on 27 April:

- "Since mine of ye fift of May I have herewith sent quadruplicate (?)".
- Fairfax has finished "his bridge at Marston" and runs lines from the hill; shot has come into Oxford from
  "Heddington hil" "but done noe great hurt".
- Fairfax summoned the town "to render Oxford to him for the use of ye Parliament", with "honorable terms for
  himselve and all within ye garrison".
- The governor "desired a safe conduct for Sir Io. Munson and Mr [Warwick]"; they asked to send a messenger to the
  King, "but he absolutely refuses to give it".
- "since your departure, we have not received a word from your Majesty".
- "the differences there betwene the Presbyterian and Independents".
- Prince Rupert, "picquering with some of Fairfax horse", received a flesh wound.

## Outside checks

- **Printed papers of 11 May 1646.** Fairfax's summons says: "honourable termes for your selfe, and all within the
  Garrison, if you seasonably accept thereof". The governor's answer asks "a safe conduct for Sir Iohn Mounson, &
  Master Philip Warwick". The decipher gives both.
- **The King's reply.** On 2 June 1646 the King wrote to Nicholas that he had received "but one letter from you,
  w^ch was of the 5th of May". Our letter begins "Since mine of ye fift of May". So this letter of 13 May never
  reached him.
- **The House of Commons.** On 25 May 1646 Fairfax sent "several intercepted Letters ... in Characters".
- **Place names** that the cipher spells: Marston, Headington hill, St Bartholomew's Hospital.

## How good is it

| Measure | Value |
|---|---|
| Tokens in the transcription | 735, of which 20 are illegible there |
| Tokens read with no doubt mark | 652 (89 %) |
| Tokens read with a doubt mark | 43 |
| Tokens not read | 20 (17 codes) |
| Glossed words of 1646 that fit the Titus list with the shifts | 20 of 20; with the Titus values shuffled 20,000 times: 5 at most |

Limits, stated plainly:

- **One transcription pass, and it is not ours.** A second, blind pass needs the image, and the image needs a
  DECODE account with image rights.
- One pass for the decipherment.
- 130 of the 261 code values rest on context only. They are marked in the key table.
- The name of the writer is our inference: the code 555 stands in the signature, between M and O in the list.

## Earlier work

Checked on 4 October 2026: S. Tomokiyo's list and his pages on the ciphers of Charles I, A. Aymeloglu's
`unsolved-ciphers` (transcription and a first analysis of 16 September 2026), `NoAutopilot/cipher-lab`,
D. Bourdeau's `cyphersolver`, Evelyn iv, the House of Lords papers in the 6th Report of the Historical Manuscripts
Commission, the Commons Journal, and a full-text search of archive.org. No full reading of the letter and no link to the
Titus cipher was found. The state of the others on 4 October 2026 (18:35 UTC): A. Aymeloglu calls the letter
"open, partial", with about 45 values fixed; `NoAutopilot/cipher-lab` reproduces that partial reading (164 to 192
of 735 tokens) and notes that no full decipherment exists. Not checked: Bodleian MS e Mus. 203 (John Wallis's deciphered letters), BL Egerton MS 1533
and 2550.

## By-products

- [evelyn_16aug1646.txt](evelyn_16aug1646.txt): the end of the King's letter of 16 August 1646, which the edition
  leaves in figures: "by yielding up my seales and sword to the rebels".
- Proposed corrections to Hillier's decipherment of the Titus letters, from the order of the list (in the work log).
- [survey.tsv](survey.tsv): the state of the other open Charles I entries. None of them reads with either key.

## Contents

| File | Content |
|---|---|
| `reading_f10.txt` | The reading in words, with doubt marks, and an English version |
| `key1646.tsv`, `titus_key.tsv` | The key of 1646 with the basis of each value, and the Titus key rebuilt from Hillier |
| `code/` | The scripts. They read the transcription from A. Aymeloglu's repository, which you must fetch yourself |
| `evidence/worklog.md` | The work log: the survey, the sources, the controls, the search for earlier work |

## Credits

- **Ari Aymeloglu** transcribed the cipher text and identified the glossed words in Evelyn.
- **Satoshi Tomokiyo** listed the letter as unsolved and described the ciphers of Charles I.
- **George Hillier** (1852) printed the Titus letters with their figures.
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code: MIT. Text: CC BY 4.0.
