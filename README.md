# The "Garbino" cipher of 1528: whose it is, and how it is built

Paris, BnF, ms. français 3022, no. 20 (a letter dated Madrid, 11 April 1528, to "Garbino") and the letters signed
"Hieronimo Ranzo" in BnF fr. 2988 and fr. 3019 are written in a cipher of letters with small numbers above them.
It is on S. Tomokiyo's list of unsolved historical ciphers as "Venetian? Cipher with Superscript Digits (1528)".

**Status: 5 October 2026. The cipher is NOT read.** This folder gives two findings on the way: the owner of the
cipher, and its structure. The work was done by a model. No palaeographer has checked it.

## Finding 1: Martino Centurione used this cipher, and "Garbino" is a name in it

Martino Centurione, the envoy of Genoa at the court of Charles V, used this cipher with his son Girolamo
(Hieronimo) in Genoa.

- A clear letter of Martino to his son, Burgos, 16-17 January 1528, is in the same volume (fr. 3022, f. 58).
  G. Molini printed it in 1837 (*Documenti di storia italiana*, ii, no. CLXIV). So the text is reproduced; the
  link to the cipher is the new part.
- In its postscript the father gives additions to the cipher ([image](images/fr3022_f58_cipher_values.jpg)):
  "Poi che vedo havere tu receputo el zifra mandato per via de Roma ... a la l[itte]ra r agiongeraili recevut.
  r336 et receu. r337 / & a la l[itte]ra G garbino g215".
- The same three values stand on the sheet "Aditione nel zifra" in the volume (f. 50;
  [image](images/fr3022_f50_aditione.jpg)).
- The old docket of the letter says that the letters "sono a nome del Garbino".
- The list of cover names in the volume (ff. 48-49) has the persons that the clear letter names (Jacobo and
  Stephano Centurione, Ansaldo Grimaldo, the secretary Perez).
- No. 20 and a leaf of the "Ranzo" letters (fr. 2988, f. 11v) carry the same cover address, "Garbino" at Lucca.

So the cipher is not Venetian: a Genoese envoy at the Emperor's court used it.

**Correction of 5 October 2026.** An earlier version of this page said that no. 20 is a letter of Martino to his
son. The clear passages of no. 20 do not support that. Martino writes "tu" to his son in the letter of January.
The writer of no. 20 writes "voi" and signs "v[ost]ro": "io non saperia consigliarvi la venuta v[ost]ra qua"
(f. 44v), "a voi ... mi offero" (f. 46v). He gives the addressee's letters to the Grand Chancellor (Gattinara),
reports the Chancellor's gout and lack of money, advises the addressee not to come to court yet, and works for
"il S[ign]or prior de Barleta". This is a man near the Chancellor who writes to a client or friend. It can be the
"Hieronimo Ranzo" of the other letters: a Girolamo Ranzo of Vercelli was Gattinara's kinsman and chamberlain.
No. 20 has no name in its signature, so this is a hypothesis. Who "Garbino" at Lucca was is open.

What holds: the cipher of no. 20 and of the "Ranzo" letters is the cipher that Martino shared with his son. Why a
man of the Chancellor's household and a Genoese envoy used the same code is not known.

## Finding 2: the structure

- A group is a base letter and a number. The base letter is the first letter of the word. The father's own words
  above prove it: "recevut." goes under r, "garbino" under g.
- The addition sheet gives the length of each list before the additions (a 326, b 156, c 326, d 307, and so on).
- **The numbers run in alphabetical order.** The frequency profile of the numbers, in number order, was set against
  the profile of Italian units in alphabetical order, with the order kept and the spacing free. Against 2,000
  shuffles the real order ranks first (z = 4.1; the letter no. 20 alone 4.5; the "Ranzo" letters alone 3.9). A code
  made up in alphabetical order gives z of about 7 in the same test, and the same code shuffled gives 0.
- The lists hold syllables, stems and endings beside words, and several numbers in a row can stand for one value
  (d34 to d37 all stand before "la, le, li").

An earlier test by another project found the numbering "not alphabetical". That test used ten fixed bins and a
list of whole words; the same kind of test gives only z = 1.7 here.

## What is read: fragments only

The letter no. 20 and the "Ranzo" letters do not use the additions of f. 50: no group has a number above the old
length of its list. So the additions give no certain value in these texts.

About 25 values are probable, by context and by their place in the alphabet. None has an outside proof. They give
fragments such as "non ho pero (?) voluto", "in Italia", "del presente (?) & del seguente farete avisato"
([fragments.md](fragments.md)). A solver that uses the alphabetical order gets 51 to 56 % of the tokens right on
a made-up code of the same kind. On the real text it gives a skeleton and no sense.

A second, stronger solver (5 October) gave the same answer. On made-up codes with the real list lengths it gets
54 % of the tokens right with 20 known values, and it needs about 400 known values (about 20 for each letter) to
reach 85 %. We have about 20 probable values and no certain one. So the method cannot read the letter now.

## What would open it

Girolamo's own cipher letter of 10 December 1527, the base table of the cipher, or a decipherment. The places to
look are the Archivio di Stato of Genoa (letters of the ministers in Spain) and Simancas. We found none in print:
Sanuto's diaries (vols. 44-49), Bornate, the Calendar of State Papers, Spain, and the printed catalogue of the
three BnF volumes were searched.

## Earlier work, and what this folder owes

- **Satoshi Tomokiyo** listed the cipher and saw that the base letter is the initial of the word.
- **Daniel Bourdeau** (`dbourdeau/cyphersolver`, target `vasto1527`) transcribed the letters and found that the
  copy in Clairambault 327 has its original in fr. 3022. His transcription was used here and is not copied.
- **NoAutopilot/cipher-lab** checked the edition and the clear postscript.
- None of them names Centurione (checked on 5 October 2026).
- **G. Molini** (1837) printed the clear letter.

## Contents

| File | Content |
|---|---|
| `fragments.md` | The few phrases that the probable values give, and the clear passage on the cipher |
| `evidence/worklog.md` | The search for a clear text, the tests of the order, the table of probable values, the earlier work |
| `images/` | The passage of f. 58 with the cipher values, and the addition sheet f. 50 (reduced; "gallica.bnf.fr / BnF") |

Code: MIT. Text: CC BY 4.0. Details are in [LICENSE.md](../LICENSE.md).
