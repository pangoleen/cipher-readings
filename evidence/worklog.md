# Cocquet to Mangot, Rome, 13 November 1616 — NOTES (4 October 2026)

Result: the cipher is read. The key is a period document: BnF Français 18009, f. 156, "Double du chiffre baillé à
monsieur le marquis de Treinel". Coquet was the secretary of Tresnel, ambassador in Rome.

## Log

1. Read `scout2/AGENT_RULES.md`, the row in `open_items.tsv`, Bourdeau's `targets/cocquet/NOTES.md` (copy in
   `scout2/src/bd/`), Tomokiyo's paragraph (`scout2/src/tomo/louisxiii.txt`).
2. Fetched Clair 369 canvases 328, 329, 330 (IIIF, full size, saved in `img/`). f. 316r starts the letter
   ("Monseigneur, Je vous escrivis de Thurin…"), f. 317r has the cipher in its lower half, f. 317v has the end,
   the date "a Rome ce 13e novembre 1616" and the signature "Coquet".
3. Deskewed the cipher block (2.9 degrees) and cut line strips (`img/s2/`) and zoom tiles (`img/z/`).
4. Pass 1 (mine) on the tiles. Then a solution from context, before any key was known:
   - L05 "del J mu s $ g J ep mu" has the pattern of "a don pedro" (clear text: "mande force choses … qui le
     poussent"). This gave 7 values.
   - L11 "ep mu 6" = "roy", L10 = "aneantir la uctorite", L01 = "que le duc de montaleon auoit mande que sa
     maieste", L02-L03 = "… un sy grand desuoyement … croyoit que elle ne pouuoit passer".
   - 43 sign values came from context. 5 stayed open or wrong (see Controls).
5. A sub-agent searched the catalogues (files in `src/`). It found the notice of fr. 18009 with f. 156, the Tresnel
   cipher. I fetched reduced images of canvases 166, 178, 185, 181, 182 to find the folio, then canvas 181 in full
   size (`img/fr18009/c181.jpg`).
6. A second sub-agent made the blind pass 2 (sign names and images only): `pass2_blind.txt`.
7. `decode.py` applies the key, counts the agreement and runs the shuffled-key control.

## Cipher system

Homophonic letter substitution with a small nomenclator, as on the key sheet:
- 21 plain letters (A B C D E F G H I L M N O P Q R S T V X Y Z; no J, K, U, W), 2 to 4 signs each.
- Underlined letters and the numbers 1-99 for words and names (popes, princes, places, common words).
- Nulls: ä ë ï ö ü. "Ce qui est entre ces deux caracteres [two signs] est nul."
- "Ces deux caracteres [tall cross with three bars] [two stems with two bars] doublent chacun leur precedent."
- "Chacun de ces deux [two signs] l'annullera" (cancels the sign before it). Not used in this letter.
- The writer leaves gaps between words in most places. A dot on the line stands before some words.

## Key table (signs that occur in the letter; value read on fr. 18009 f. 156)

| Sign name | Shape | Value | Key position | Count |
|---|---|---|---|---|
| f | f with crossbar | a | A row 1 | 3 |
| del | delta | a | A row 2 | 17 |
| delx | o with a cross on top | a | A row 3 | 2 |
| c | small c | b | B row 2 | 1 |
| 3 | ezh / h-like | c | C row 1 | 1 |
| z, Z | z with a short bar; large Z (L07, doubtful) | c | C row 3 | 3+1 |
| J | tall hook | d | D row 1 | 7 |
| 5 | 5 with top bar | d | D row 2 | 1 |
| L | L / looped l | e | E row 1 | 8 |
| t | small cross, two bars | e | E row 2 | 4 |
| g | g with looped tail | e | E row 3 | 6 |
| pi | plain pi | e | E row 4 | 1 |
| C | C with inner hook | g | G row 1 | 1 |
| dd | tall Latin d | h | H row 3 | 1 |
| q | q | i | I row 1 | 8 |
| ub | two legs on a bar | i | I row 3 | 1 |
| x | small x/r with dot or base stroke | l | L row 1 | 3 |
| PI | pi with top and bottom bar | l | L row 3 | 1 |
| 2 | 2 with tail | m | M row 1 | 4 |
| ff | double f with bar | m | M row 2 | 1 |
| s, S | s | n | N row 1 | 8 |
| xi | xi / barred 6 | n | N row 3 | 4 |
| sl | long s | o | O row 1 | 2 |
| ss | double long s | o | O row 2 | 1 |
| mu | mu | o | O row 3 | 12 |
| Zb | z with bar | p | P row 1 | 1 |
| $ | long s with strokes | p | P row 2 | 6 |
| o | plain o | q | Q row 1 | 1 |
| ep | epsilon / open 8 | r | R row 1 | 10 |
| nb | n with base stroke | s | S row 2 | 2 |
| th | o with a bar through | s | S row 3 | 9 |
| ob | o with a bar to the right | t | T row 3 | 1 |
| ot | o joined to t | t | T row 2 | 9 |
| gam | gamma / y | t | T row 1 | 4 |
| eta | eta | u | V row 1 | 2 |
| w | omega | u | V row 2 | 9 |
| H | small H | u | V row 3 | 1 |
| 6 | 6 | y | Y row 1 | 5 |
| n_ | underlined n | Le | nomenclator | 6 |
| c_ | underlined c | La | nomenclator | 2 |
| y_ | underlined y | Il | nomenclator | 3 |
| 86 | number | que | nomenclator | 3 |
| 89 | number | quil | nomenclator | 1 |
| T | tall cross | doubles the letter before | note on the key | 2 (+1 as end mark) |
| DBL | two stems, two bars | doubles the letter before | note on the key | 1 |
| oo | o with two dots | null | "Nulles" | 4 |

Counts are from the consensus transcription (189 signs with 8, 6 and 9 counted as figures).

## Controls (numbers)

1. Two transcription passes, the second blind: 189 signs, 179 the same (94.7 %); 184 (97.4 %) if an "A/B" answer
   of pass 2 counts as agreement. The 10 differences are listed in `transcription.txt`. None changes a word.
2. Outside source: 43 sign values that I found from context before I saw the key are all the same in the key
   (0 conflicts). The key corrected or settled 5 points: 89 = "quil" (I had "qu'on"), dd = h ("hault", I had
   "d'ault"), plain o = q ("quant", I had "avant"), y_ = "Il" (a guess before), DBL = doubling sign (I had s).
   The proof of the order (context first, key second) is only this session's log; `pass1.txt` was saved before the
   key image was opened.
3. Shuffled key: French 4-gram score per 4-gram (`corpus/fr_4.npy`, modern French) of the text with the true key
   -10.47; 2000 keys with the same letter values shuffled over the signs: mean -15.42, sd 0.65, best -13.13.
   z = 7.6. No shuffled key comes near.
4. Sense: one consistent table gives sound French of 1616 in all nine cipher lines, and the cipher text joins the
   clear text on both sides ("… ne pouuoit passer | deux heures"; "mande force choses | a don Pedro | qui le
   poussent"). The duke of Monteleone was the ambassador of Spain in France in 1616.

## Prior-art and novelty checks (4 October 2026)

- Tomokiyo, "Ciphers during the Reign of Louis XIII", https://cryptiana.web.fc2.com/code/louisxiii.htm : "It is
  not deciphered". Unsolved list https://cryptiana.web.fc2.com/code/unsolved.htm (modified 4 Oct 2026): still listed.
  Blog search: no post.
- Bourdeau, cyphersolver `targets/cocquet/NOTES.md` (16 Sept 2026): gate check, "not solvable with what is online";
  sister search "not checked". No change found today.
- Aymeloglu, unsolved-ciphers TARGETS.md (pushed 28 Sept 2026): "blocked, parked 16 Sept 2026".
- NoAutopilot/cipher-lab CATALOG.md (pushed 4 Oct 2026): "Open". el-descifrador/cabinet-noir (pushed 2 Oct 2026):
  no Cocquet entry; its Brèves key (fr. 3462) is a different key.
- Period decipherment: the BnF notices of Clairambault 362-376 (Lauer's item lists) name Cocquet once (369 f. 316)
  and no "déchiffrement" for it. Avenel t. I, VII, VIII: no letter to Cocquet; t. VII p. 921 (king to Tresnel,
  28 Feb 1617) names "Coquet". No printed text of this letter found.
- Web search for "Cocquet Mangot Monteleon" and for the title of the key: no decipherment, no use of the key.
- Details and URLs: `src/novelty_check_2026-10-04.txt` and the other files in `src/`.
- Wording: the text is new (both checks clean as far as searched). The key is not ours: it is a period key. So the
  right words are "first reading, with the period key of the Rome embassy, which we identified in fr. 18009 f. 156".
- Not reached: Lauer's printed catalogue itself, Poncet 2011, AAE Rome 23-24, BnF fr. 18010 f. 380 and NAF 461
  (Tresnel's letter book; not digitised). A clear copy of this dispatch can be there.

## Who and what

- "Coquet": secretary of François Juvénal des Ursins, marquis de Tresnel (source: richelieuletters.hypotheses.org/74945,
  copy in `src/`; first name not found). The letter says "arrivé à Rome auprès de mon M[aist]re".
- The letter reports his journey Turin - Béthune's quarters - Florence - Rome, then the Milan rumour of the King's death.

## Open points

- See "Not resolved" in `reading.md` ("son frere", "car", some clear words).
- Shape problems: th/ob (s/t) and xi/ep (n/r) are hard to tell apart; the g of "pedro" and "aneantir" has a short
  tail like the key's B sign, but only e gives sense. Context decides these.
- The clear text of the letter has one pass only.
- Lead for other work: the same key should read Tresnel's own ciphered letters (Clair 369 ff. 68, 70, 252, 321, 323;
  fr. 18009-18012; Clair 370, 372). Not tested.
- Leftover: `img/lines/` holds a first, badly centred set of strips. A safety check blocked its removal. It is not used.

## Files

`transcription.txt`, `pass1.txt`, `pass2_blind.txt`, `reading.md`, `decode.py`, `decoded_by_key.txt`, `src/`
(catalogue and novelty texts, fr. 18009 manifest), `img/` (c328-c330 of Clair 369; `fr18009/c181.jpg` = the key;
`s2/`, `z/`, `clear/` crops).
