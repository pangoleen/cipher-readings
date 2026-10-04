# The cipher of the Dutch deputies in England, 1653: the key rebuilt

In 1653 the deputies of the States General in England (Beverningk, Nieupoort, van de Perre, Jongestal) wrote in
cipher to Willem Boreel, the Dutch ambassador in France. Cromwell's government intercepted the letters. Thurloe's
*State Papers* (1742) print them with their number groups. The cipher is on S. Tomokiyo's list of unsolved
historical ciphers ("Dutch ciphers (1653)").

**Status: 4 October 2026.** The work was done by a model. Corrections are welcome: please open an issue.

## What is new and what is not

| | Item |
|---|---|
| Reproduced | The text of the letter of 1 September 1653 (Thurloe i.435). The Dutch minute of this letter is in print: *Verbael gehouden door de Heeren H. van Beverningk ...* (1725), pp. 97-99, No. 6. |
| New | The link between the two printed books, and the key of the cipher. We found no earlier reconstruction of it. |
| New, small | A reading of 12 cipher groups in Boreel's letter to the deputies of 13 September 1653 (Thurloe i.454): "[general Cromwell] in iames p[a]rc". The deputies' printed reply names the conference in St James's Park, so the fact itself is known. |
| Not ours | The letters to De Witt in the same volume use another cipher. R. Fruin printed its key in 1906. |

## The system

1. **A ring of 24 numbers**, 10 to 33, in this order:
   `32 30 28 26 24 22 20 18 16 14 12 10 11 13 15 17 19 21 23 25 27 29 31 33`. Even numbers go down, odd numbers go up.
2. **24 letters** follow the ring: `a b c d e f g h i k l m n o p q r s t v w x y z` (i = j, v = u).
3. **An indicator digit** k, from 1 to 5, sets the letter `a` on the k-th number of the ring.
4. **A group of three digits** is the indicator and the first letter: `222` is alphabet 2 and the number 22, which is `e`.
   The groups of two digits that follow stay in that alphabet until the next group of three digits.

There are no nulls and no syllables. The whole table is 5 x 24 = 120 values from this one rule ([key.tsv](key.tsv)).
Numbers above 100 that are not indicators are words of a general code (168 is "general Cromwell" by Thurloe's own gloss).

## How well it fits

All 136 groups were checked on the page image of the 1742 edition ([alignment.tsv](alignment.tsv)).

| Measure | Value |
|---|---|
| Groups that fit the minute | 124, and 2 more if "6" is a misprint of "16" |
| Spelling differences between the letter and the minute | 3 |
| Conflicts | 6 |
| Open | 1 (the group 117, probably a code word) |
| Alphabets 1 and 3 predicted from alphabets 2 and 5 | 41 of 43 groups right |
| Best of 5,000 random rings, with a free shift for each alphabet | 60 of 131 groups; the ring above gives 127 |

The conflicts are of the kind that Birch's edition has elsewhere: in a letter with a known key it prints 12 wrong
groups in 207.

To repeat the check:

```bash
python3 align.py && python3 control.py
```

## How it was found

Two other projects tried this cipher in September 2026 and noted that it needs a clear text from the Dutch side.
The Dutch minute is in the printed *Verbael* of the embassy. Its first sentence agrees word for word with the clear
text in Thurloe. The alignment of the cipher runs with the minute gave the values of two alphabets; the ring and the
indicator rule came from their structure; the other two alphabets were then predicted and tested.

## The life of the cipher, and a search for more text

The printed *Verbael* dates the cipher. The deputies asked Boreel for it on 18 August 1653 and used it on
1 September. On 29 September they wrote that the English could have it "by copye". By 20 October they had a new
cipher. So the cipher lived about five weeks.

All seven volumes of Thurloe were scanned twice for more runs in this cipher (the text of British History Online,
and the OCR text of the 1742 edition). Both scans find the two letters of this folder and nothing else
([evidence/thurloe_scan.md](evidence/thurloe_scan.md)). More text can only come from the manuscripts.

The numbers above 100 belong to the older general cipher of the States General ([codewords.tsv](codewords.tsv)).
One value is now certain: 128 is "den Koningh van Denemarcken", by a second minute in the *Verbael* (p. 16) beside
Thurloe i.316. The others (168 general Cromwell, 117 the fleet of the States) rest on one place or on an English
gloss.

## Earlier work

Searched on 4 October 2026: D. Bourdeau's `cyphersolver`, A. Aymeloglu's `unsolved-ciphers` (he names the *Verbael*
for another target), `NoAutopilot/cipher-lab`, S. Tomokiyo's pages and blog, K. de Leeuw's thesis *Cryptology and
statecraft in the Dutch Republic* (2000), and the web. None has this key. Thurloe's volume 6 and the manuscripts
were not seen.

## Open points

- Three groups that give "xxd" where the minute has "eene". No shift explains them; the print probably has wrong
  digits there.
- The code group 117.
- The manuscript of the intercepted letter (Bodleian, Rawlinson A) can settle the printed groups that conflict.

## Contents

| File | Content |
|---|---|
| `thurloe_groups.txt` | The cipher groups of Thurloe i.435, read from the page image |
| `verbael_no6.txt` | Our transcription of the Dutch minute |
| `alignment.tsv`, `key.tsv` | The alignment and the key table |
| `model.py`, `align.py`, `control.py` | The rule, the alignment and the controls |
| `reading_boreel_to_deputies_1653-09-13.txt` | The 12 groups of Thurloe i.454 |
| `reading_dewitt_cipher_letters_1653.txt` | The De Witt letters, read with Fruin's printed key (reproduced) |
| `evidence/worklog.md`, `evidence/thurloe_scan.md` | The work log, and the scan of all volumes of Thurloe |
| `codewords.tsv`, `letters.tsv` | The code words above 100 with their evidence, and the letters found by the scan |
| `images/` | Reduced page images of Thurloe i.435 and of the *Verbael* p. 97 (both books are in the public domain) |

## Credits

- **Satoshi Tomokiyo** lists the cipher as unsolved ([cryptiana](https://cryptiana.web.fc2.com/code/unsolved.htm)).
- **Daniel Bourdeau** and **Ari Aymeloglu** analysed it in September 2026 and stated what was missing.
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code: MIT. Text: CC BY 4.0. Details are in [LICENSE.md](../LICENSE.md).
