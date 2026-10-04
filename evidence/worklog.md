# BnF Espagnol 318 nos. 94 and 93 - notes (4 October 2026)

## Result

- **No. 94 (ff. 120r-121r, Juan de Lanuza, viceroy of Sicily, to Ferdinand, Messina, 27 April 1503): key rebuilt, letter read in large part.**
  Three pages, 98 lines, about 2,540 cipher signs and 680 code-word tokens. All sign types that matter have a letter (2,521 of 2,537 sign tokens). 36 of 100 code words have a value (570 of 677 tokens).
- **No. 93 (f. 118, Lorenzo Suárez, Venice, 24 February 1504): not attempted.** I opened the image only. Other hand, other sign set (+, ÷, ʒ, ıı, #, π), wholly in cipher. It shares the group "otto" and three-letter code words with no. 94. The key of no. 94 does not carry over by sign shape. The method used here (two blind passes, then the solver) should work on it: it has about 50 lines.

## Cipher system of no. 94

- Homophonic sign alphabet: 44 sign types for 20 letters (table: `KEY_TABLE.md`, source: `key.py`). Vowels have 2-4 signs each (a: `p 3 o-`; e: `x tb tbo`; i: `& :. Z`; o: `R al X`; u/v: `a ß`).
- The letter c has a sign (`F`) and also the joined group **"otto"** (79 times): *prin-otto-ipales, ne-otto-esidad, otto-apitanes, otto-ardona*. Before `8` (h) it gives ch (*sospecha, dicho, aprovechados*). The other projects took "otto" for a code word.
- **"malz" = ll** (*acuchilladas, castillo, cavalleros, Vintemilla, hallan*).
- Code words (two to four letters, joined): raz = que, muy = de, qa = y, qaq = se, mub/nob = la, mas = el, mys = en, nyb = lo, pif = no, lue = a, nar = los, qik = su, muz = gente, qaz = V. Al., mog = del, mok = dar, nas = mas, pet = para, lik = buena, and others with grades in `KEY_TABLE.md`.
- Nulls or markers: `H qo` at the start, `H qo QQ . tz .` at paragraph ends and before the date.
- Spelling of the plain text is Aragonese: *conpanya, senyaladamente, danyo, punyaladas, screvia, anyma*.

### Relation to the published keys of the family

| key | source | fit |
|---|---|---|
| Gran cifra of the Gran Capitán (Bergenroth, BNE MSS 20.211/52; CNI 2018) | Quirantes's photograph, ABC table (`src/keyimg/`) | Code words: raz = que and muy = de are the same; uob = la matches our mub/nob; "tt" (their anulante) is inside our "otto". Sign alphabet: different (their 7 = a, 6 = l; ours 7 = s, 6 = t). Their moc = con is our mon; our mok = dar. |
| Estrada's cipher 1502-04 (Tomokiyo; Bergenroth PRO 31/11/11) | `src/keyimg/Estrada.jpg` | ra = que is near raz. Sign x (a "4" shape) = e in both. Other signs differ. |
| Cifra general de los RRCC (Galende Díaz 1994) | Bourdeau's `cifra_general.txt` | No fit: code initials v, x, y, z, b, c. |
| Escrivà no. 1, Vich 1508, Charles/Vich 1519 (Tomokiyo, Parisi) | `scout2/src/tomo/spanish.txt` | No fit. |
| "Cifra del visorrey", RAH 9/15 ff. 1-6 (Galende Díaz 1994, described only) | not online | Not tested. Our rebuilt key is the natural candidate for it. A copy from the RAH can confirm or correct the code values. |

So the letter uses a key of the same office and build as the Gran cifra, with partly the same code words and another sign alphabet. cipher-lab tested the Gran cifra alphabet on a 37 % transcription and got a non-test; with a 93 % transcription the test is clear: codes fit in part, signs do not.

## How the key was found

1. Line strips from the IIIF full images (`cut_lines.py`, three overlapping strips per line).
2. Sign names by shape (`tr/SIGNS.md`). Pass A of f. 120r by me; pass B by a blind agent. Two blind agents each for f. 120v and f. 121r.
3. Sukhotin's test split vowels from consonants (p, x, R, tb, o-, al came out as vowels).
4. A hill climber over the sign-to-letter map (`solve3.py`: 5-gram Spanish model built from the Crónicas del Gran Capitán and the project corpus, letter-frequency term, vowel and consonant classes, the codes que, de, y as known words). 3 of 8 starts gave the same best key.
5. That key gave *a don Joan de Cardona*, *fortaleza*, *presoneros principales*, *capitanes*. I then fixed every sign by reading words in context (`kwic.py`) and set the code words from context.
- Dead ends before that: the crib "galea" from the clear text, and the Gran cifra alphabet. A climber on one page alone (840 signs) gave false Spanish; three pages (2,540 signs) converged.

## Measured rates

| measure | f. 120r | f. 120v | f. 121r |
|---|---|---|---|
| lines, passes per line | 31, 2 | 37, 2 | 30, 2 |
| token agreement of the two passes | 93.2 % | 96.0 % | 92.9 % |
| - cipher signs | 95.5 % | 97.6 % | 93.9 % |
| - code words | 86.0 % | 93.7 % | 90.2 % |
| decoded characters that agree between passes | 93.5 % | 94.6 % | 94.2 % |
| key score, log-probability per 5-gram (pass A / pass B) | -12.42 / -12.52 | -12.14 / -12.17 | -12.34 / -12.32 |
| 200 shuffled keys: mean, best | -18.53, -17.40 | -18.53, -17.33 | -18.58, -17.47 |

Real Spanish scores -10.8 on the same model; shuffled Spanish -17.9. No shuffled key reached the true key on any page (0 of 200, `control.py`). cipher-lab's two passes agreed on 37 % of f. 120r.

Main confusions between passes: `&` / `Z8` / `R` (loop signs), `5` / `G`, `ff` / `4f`, and the last letter of code words (mog / moz, nar / nae, malz / mals).

## Outside control

The names and facts read from the cipher match the Crónicas del Gran Capitán (ed. Rodríguez Villa 1908, text in `src/cronicas_gc.txt`): the battle near Joya (Gioia), Aubigny ("monsiur de Aubegni") shut in the "Roca de Anguito", don Fernando de Andrada and don Hugo de Cardona, Manuel de Benavides, Alonso de Carvajal, the death of Portocarrero and the choice of Andrada as general. The letter's own clear text names "la roqua de Angito", Andrada, Benavides, Caravajal and "Puerto Carrero". The chronicle did not serve as a crib; the solver found the names.

## Prior-art checks (all on 4 October 2026)

- Tomokiyo, https://cryptiana.web.fc2.com/code/unsolved.htm (page dated 4 Oct 2026): no. 94 and no. 93 listed under "unknown ciphers". His article spanish.htm lists both as undeciphered.
- Bourdeau, https://raw.githubusercontent.com/dbourdeau/cyphersolver/main/targets/esp318/NOTES.md (fetched today, `src/bourdeau_esp318_NOTES.md`): "No. 94 ... not-attempted; never transcribed"; no file for f. 120-121 in his folder listing.
- cipher-lab, PROGRESS.tsv and `ciphers/esp318-sicilia-1503` (last commit for this folder 3 Oct 2026 01:37 UTC): open, blocked on transcription.
- Cabinet Noir README: no "318". Aymeloglu catalogue: no "318". Satoru index: no entry.
- Web searches: `"Lanuza" virrey de Sicilia carta al Rey Católico Mesina "27 de abril de 1503" Salazar y Castro`; `"Juan de Lanuza" ... "roca de Anguito" ... carta cifrada descifrada`; `"Lanuza" 1503 Joya saqueo fortaleza "Aubeni" ... "Vintemilla"`. No decipherment and no printed text of this letter.
- Bergenroth's Calendar vol. 1 and Supplement: no entry (cipher-lab's full-text search, 26 Sept 2026; not repeated by me).
- **Not checked:** RAH, Colección Salazar y Castro (letters to Ferdinand of 1503, where a period decipherment could be); AGS; A. de la Torre, Documentos sobre relaciones internacionales vol. VI; Zurita, Historia del rey don Hernando, book V. The volume itself has no decipherment (Bourdeau and cipher-lab looked at the neighbouring leaves).
- Wording to use: **first reading, key rebuilt from the letter** ("new" only with the caveat on the RAH and Simancas copies).

## Open points

- 64 code words with no value; 6 guessed. The RAH key (9/15 ff. 1-6) or more letters of Lanuza in this cipher can settle them.
- The f sign must be split from the a sign in the transcription (third pass on every `p`).
- Loop signs `&`, `Z8`, `R`: a third pass on the places where the passes differ.
- The clear Spanish on f. 120v needs a palaeographer's eye. f. 121v (address) was not transcribed by me.
- No. 93: not attempted.
- A note on line strips: on ff. 120v and 121r the first strip of many lines shows two lines; both agents took the lower one and checked it against the overlap.

## Files

- `img/` six IIIF full images (canvases 446, 447, 452-455; f453 came from Bourdeau's copy after a Gallica HTTP 500). `lines/` line strips.
- `tr/SIGNS.md` sign names; `tr/f120r_passA.txt`, `..._passB.txt`, and the same for f120v, f121r: the transcriptions.
- `key.py`, `KEY_TABLE.md` the key. `DECODE_RAW.md` both passes decoded line by line. `READING.md` edited Spanish reading and English summary.
- `solve.py`, `solve2.py`, `solve3.py` solvers; `agree.py` pass agreement; `control.py` shuffled-key control; `kwic.py`, `decode.py`, `show.py` tools.
- `src/` sources fetched: Tomokiyo pages and key images, Quirantes's photographs of the Gran cifra, the ABC table of the CNI, Bourdeau's notes and key files, the Crónicas text, `lm5.npy` (5-gram model).

## Log (4 October 2026)

1. Read AGENT_RULES, the scout notes, cipher-lab's and Bourdeau's notes.
2. Fetched Tomokiyo's index, Bergenroth page, key images; the Gran cifra photographs.
3. Six Gallica IIIF requests, 12 s apart; one HTTP 500, not retried.
4. Pass A of f. 120r by eye; pass B by a blind agent: 93.2 %.
5. Key tests and cribs failed on one page. Four more blind agents for ff. 120v, 121r.
6. Solver on three pages converged; key fixed by context; controls run; files written.
