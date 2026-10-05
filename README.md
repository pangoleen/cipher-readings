# The viceroy of Sicily to King Ferdinand, Messina, 27 April 1503: the cipher rebuilt and read in large part

A first reading of a cipher letter of the Italian wars, written six days after the French defeat in Calabria.

| Letter | Shelfmark | State before | State now |
|---|---|---|---|
| Juan de Lanuza, viceroy of Sicily, to King Ferdinand, Messina, 27 April 1503 | Paris, BnF, ms. Espagnol 318, no. 94, ff. 120r-121v (Gallica `btv1b52503046q`, views 452-455) | Not transcribed; no key | [reading](READING.md): the sign alphabet is solved; 36 of 100 code words have a value |

**Status: 4 October 2026.** The work was done by a model. No palaeographer has checked it. The reading has gaps.
Corrections are welcome: please open an issue.

## What this is

- **The key is rebuilt from the letter itself.** The original key ("Cifra del visorrey", Real Academia de la
  Historia, 9/15 ff. 1-6) is not online and was not seen. The published keys of the Catholic Monarchs do not fit:
  the "Gran cifra" shares a few code words (raz = que, muy = de), and its sign alphabet is another one.
- **It is a reading in large part, not a full one.** 64 code words have no value. They stand mostly in the
  stretches that the reading marks with "...".
- We found no earlier reading and no printed text. Another project had tried the transcription and stopped there.

## The cipher

A symbol alphabet with several signs for each letter (44 signs for 20 letters), and code words of three letters
for common words and names. Two code words stand for letters: "otto" is c, and "malz" is ll. The key is in
[KEY_TABLE.md](KEY_TABLE.md) and `key.py`.

## What the letter says

The parts that rest on words read letter by letter:

- The viceroy wrote "luego depues del desbarate", the rout of the French near Gioia on 21 April 1503.
The quotations below are the edited reading. Where the two transcription passes confuse look-alike signs, the
raw decode differs by a letter (for example "clmara de mosae de Aubeni" for "camara de mosse de Aubeni");
`DECODE_RAW.md` shows the raw text of both passes.

- The fortress gave itself up. Three captains were put in it for an inventory: "puestos en la fortaleza a don
  Joan de Cardona ... Antonyo de Leyva ... Caravajal". Before the inventory men went in; they found "la camara de
  mosse de Aubeni" empty, and "assi se saqueo la fortaleza".
- "enbio don Ferando de Andrada tres presoneros principales aqui". They are lodged in the castle of Messina.
- A hard report on don Hugo de Cardona: "en vida de Puertocarero se sintio de ir debaxo de nadi". Some captains
  "stuvieron para darle de punyaladas". The viceroy names "el conde Joan de Vintemilla".

The names agree with the chronicles of the Great Captain. They were not used as a crib.

A search of the printed sources after the reading ([evidence/print_check.md](evidence/print_check.md)) found no
clear text of the letter. Zurita (*Historia del rey don Hernando*, book 5, ch. 25 and 29) used the same matter:
he has "Hernando de Valencia", "Alonso Guerrero", the anger of the Cardonas, and Gioia "puesto a saco, y
quemado". He does not have the sack of the fortress by night, the inquiry, or the threat to stab don Hugo. The
probable cover letter survives: Lanuza to Almazán, Messina, 26 April 1503 (Real Academia de la Historia,
Salazar A-11, f. 373), asking him to pass a letter to the King.

## How good is it

| Measure | Value |
|---|---|
| Cipher lines | 98, on three pages |
| Tokens identical in two blind transcription passes | 93.2 %, 96.0 % and 92.9 % for the three pages |
| Sign tokens with a letter value | 2,521 of 2,537 |
| Code-word tokens with a value | 570 of 677 |
| Five-letter-group score of the key | -12.1 to -12.4; 200 shuffled keys: mean -18.5, best -17.5; real Spanish: -10.8 |

Limits, stated plainly:

- The transcription does not separate the sign for f from one sign for a. The letter f was restored by context.
- Three signs that look alike were confused by the passes. A third pass can change single words.
- Three of the eight points of the summary rest on code words with no value. The reading file says which.
- The clear Spanish on f. 120v is in a fast hand and was not checked on the image.
- Not reached in the search for a clear text: de la Torre's edition (vol. 6), Simancas. The catalogue of the BnF
  Spanish manuscripts (Morel-Fatio, no. 172) and the index of the Salazar collection note no decipherment.

`control.py` needs a five-letter-group table of Spanish that is too large for this repository (47 MB).

## Earlier work

Checked on 4 October 2026: S. Tomokiyo's list of unsolved ciphers ("Spanish Letters (1497-1504)"),
`NoAutopilot/cipher-lab` (two machine transcription passes of f. 120r that differ in 63 %; no reading),
D. Bourdeau's `cyphersolver` (not transcribed), `el-descifrador/cabinet-noir`, A. Aymeloglu's list, and three web
searches. No reading and no printed text was found.

## Contents

| File | Content |
|---|---|
| `READING.md` | The edited reading in Spanish, an English summary, and what is not resolved |
| `DECODE_RAW.md` | The machine decode of both transcription passes, line by line |
| `KEY_TABLE.md`, `key.py` | The key: signs, code words, and the basis of each value |
| `transcription/` | The two passes for each page and the names of the signs |
| `decode.py`, `agree.py`, `control.py`, `lib.py` | The decoder, the comparison of passes, the control |
| `evidence/worklog.md` | The work log |
| `images/f120r.jpg` | The first page, reduced, with the credit "gallica.bnf.fr / BnF" |

## Credits

- **Satoshi Tomokiyo** described the ciphers of the Catholic Monarchs and listed these letters as unsolved.
- **G. A. Bergenroth** printed the keys that were tested.
- **NoAutopilot/cipher-lab** and **Daniel Bourdeau** identified the cipher family and stated what was missing.
- **Bibliothèque nationale de France / Gallica** provides the page images.
- The work was done by Paolo Rosson with Claude (Anthropic), running as Claude Code with subagents.

## Licence

Code: MIT. Text: CC BY 4.0. Image: reduced from Gallica, under the BnF's conditions of reuse.
