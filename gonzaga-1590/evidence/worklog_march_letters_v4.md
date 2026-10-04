# Notes, version 4 — the two letters of March 1590 with no period decipherment (BnF fr. 4698 ff. 26v-27r, ff. 36r-36v)

4 October 2026. Work of one agent (a model) with one blind sub-agent. No palaeographer has checked it. Nothing was
committed, pushed or published. All files are in `gonzaga1590/v4/`. No file outside this folder was changed.

## 1. Log

1. Read `scout2/AGENT_RULES.md`, the README of `gonzaga-1590`, the two readings of version 3, the two
   transcriptions, `lists_v4.tsv`, `fr4696/worklog.md`.
2. Decoded both transcriptions again with `lists_v4.tsv` and the rules of `v2work/dec3.py` (`v4/dec5.py`).
3. Started a blind third pass for f. 36 (`v4/blind_f36_passC.txt`): an agent with the brief, the mark sheet and the
   two images only.
4. Cut every cipher line of the four pages into enlarged crops (`lc_*.jpg`, four parts for each line, 1.7 to 2 times
   the film size; zooms `z_*.jpg` at 2 to 5 times) and looked at each line. This look is not blind.
5. Only after that, read Pastor, History of the Popes, vol. 21 (archive.org) for the control.
6. Wrote the transcriptions of version 4, the proposals, the readings and these notes.

No new image was fetched. Gallica requests: none. archive.org: three requests for the text of Pastor.

## 2. Numbers

### Coverage

| letter | class | version 3 | lists_v4, same transcription | version 4 |
|---|---|---|---|---|
| 24 March | glossed, in the list that the mark names | 492 (84 %) | 518 (88 %) | 509 (87 %) |
| | window proposal | 31 | 20 | 41 (7 %) |
| | value of another list (suspect mark) | 22 | 18 | 1 |
| | gloss value that does not fit, kept with (?) | - | - | 14 |
| | number, not a code word | - | - | 2 |
| | unresolved | 41 | 30 | 17 (3 %) |
| | units | 586 | 586 | 584 |
| 31 March | glossed, in the list that the mark names | 199 (86 %) | 204 (88 %) | 189 (81 %) |
| | window proposal | 14 | 11 | 28 (12 %) |
| | value of another list (suspect mark) | 7 | 7 | 3 |
| | gloss value that does not fit, kept with (?) | - | - | 5 |
| | number, not a code word | - | - | 1 |
| | unresolved | 12 | 10 | 6 (3 %) |
| | units | 232 | 232 | 232 |

How to read this table:
- The middle column is the pure effect of the larger table. Eight proposals of version 3 became glossed values; one
  (C 33 "concorrere") is contradicted and was removed.
- Version 4 is stricter than version 3 in two ways. A value from a near list is accepted only when I name the unit as
  a suspect mark (4 units in all). A glossed word that gives no sense is counted apart (19 units). So the glossed
  count of version 4 is lower than the middle column.
- "Glossed" is still an upper bound. In 23 units of the first letter and 8 of the second the mark cannot tell list A
  from list C or from a plain name, and the word decides (`@A`, `@C`, `@N` in the transcriptions).
- Raw outputs: `raw_f26_v4_step1.txt`, `raw_f36_v4_step1.txt` (middle column); `decode_f26_v4.txt`,
  `decode_f36_v4.txt` (version 4). To make them again, from `gonzaga1590/`:
  `python3 v4/dec5.py f26v-27r_transcription_v3.txt` (set NOFIX=1 and move `interp_v4.tsv` away for the middle column),
  `python3 v4/dec5.py v4/f26v-27r_transcription_v4.txt`, and the same for f36.

### Agreement of the passes on f. 36 (`v4/agree.py`)

| pair | same figure | same mark, where the figure agrees |
|---|---|---|
| pass A (not blind) with pass B (version 3) | 211 of 234 (90 %) | 152 of 211 (72 %) |
| pass B (blind) with pass C (blind) | 213 of 228 (93 %) | 202 of 213 (95 %) |
| consensus of version 3 with pass C | 206 of 229 (90 %) | 165 of 206 (80 %) |
| transcription of version 4 with pass C | 218 of 228 (96 %) | 211 of 218 (97 %) |
| transcription of version 4 with pass B | 216 of 227 (95 %) | 204 of 216 (94 %) |

The arc and the question marks are not counted. The low number of version 3 came from pass A. Two blind passes agree
on the mark for 95 % of the units on these two pages; the film of f. 36 is not worse than that of f. 26v.

For ff. 26v-27r the two blind passes of version 3 stand: same figure 556 of 586 (95 %), same mark 502 of 556 (90 %).

## 3. Changes of marks, figures and signs

### 24 March (ff. 26v-27r): 15 marks, 7 figures, 14 signs or clear words

The full list, with the list choices and the flags, is `changes_f26.tsv` (102 rows). The rows below are the units
where what is read on the film changed (a row that only drops a question mark is in the list too).

| line | version 3 | version 4 | reason |
|---|---|---|---|
| L04 | `30^:_-` | `30^._-` | the period gloss above the line reads "scrivere": list S (dot above, bar below), not two dots |
| L06 | `62~?` | `62~^^` | the stroke above is the circumflex of list O, with the verb arc; the same figure in L08 has a clear circumflex |
| L06 | `81?` | `81^.?` | dot above seen (pass B) |
| L06 | `62~` | `62^^` | wavy stroke above = circumflex, as in L08 |
| L07 | `x9^.?` | `19^.?@A` | blot; a short stem with its dot and a 9 are seen: 19. A 19 accordare |
| L08 | `10` | `10` | Amb.re |
| L08 | `82?` | `82^.` | dot seen |
| L08 | `ll'?` | `ll'` | the Spagna sign is clear |
| L08 | `10?` | `10` | no mark |
| L08 | `SP{#}` | `[del]` | the sign is a crossed-out figure, not a letter |
| L09 | `82^.?` | `82^.` | dot seen |
| L09 | `65^-_.?` | `65^-_.?` | as pass A: stroke above, dot below (list T) |
| L09 | `ll'?` | `ll'` | Spagna sign with a tick; both passes |
| L09 | `83_v?` | `83~_v!` | arc above and caron below (list P, verb); no value |
| L09 | `30~^._.?` | `50~^._.?` | pass B read 50; the first digit has the round top of this hand's 5. M 50 minaccia + arc. Pass A: 30 |
| L09 | `90_v` | `90_v?` | caron below seen |
| L10 | `73^._-?` | `73^._-` | dot above and bar below (list S), figure 73 as pass A |
| L11 | `20` | `20n` | plain figure after "di" and before "cardinali": the number 20, not a code word |
| L11 | `66^-_.` | `66^-_.@A` | the same word as L10 "questo atto" (66 with a dot above); here a dot below and a stroke above are seen. Suspect mark |
| L11 | `67_:?` | `67_:` | two dots below seen |
| L11 | `29~^._-` | `28~^._-?` | the second digit has no tail below the line; a 9 of this hand always has one. Both passes read 29. S 28 scomunica + arc |
| L12 | `59=?` | `59_v?%` | a caron below is seen, no bars: P 59 primo; the word does not fit well |
| L12 | `(13)?` | `(13)` | (13) as pass A |
| L13 | `55=?` | `65=?` | the first digit has the tall stroke of a 6 (pass B: 65; pass A: 55) |
| L14 | `80^.` | `80^:?` | two dots above are seen: E 80 fatto, not C 80 detto |
| L16 | `"il duca"` | `"il dar"` | clear word read again: "il dar", not "il duca" |
| L17 | `82^.?` | `42^.?%` | 42 as pass B (pass A: 82); A 42 ambasciata / C 42 conscienza do not fit |
| L17 | `(93)` | `(43)?` | (93) has no value and the bracket list ends near 50; the first digit can be a closed 4: (43) S.S.tà |
| L17 | `SP{K a gl? L E E3? om L #? v dd    phi}` | `SP{K a gl L E xi om L xx v dd qo om phi}` | read again on the image: 14 signs, HAGIUSTIFICATO (pass B has xi for the sixth sign; the ninth is the double x, f) |
| L18 | `10?` | `10` | no mark |
| L18 | `28^-?` | `28^.?%` | a dot above, not a bar (C 28 commune does not fit); a figure 87 is written above the line before it |
| L18 | `"lodando"` | `"domandò"` | clear word read again: "domando", not "lodando" |
| L18 | `46?` | `46` | 46 as pass A |
| L18 | `2x` | `2n` | a single 2: the number 2 ("sopra 2 punti") |
| L19 | `SP{y ca}` | `SP{y L}` | second sign = Lambda (i), as pass B: RI |
| L21 | `x0?` | `0?` | a single 0 after 58; not explained |
| L21 | `10?` | `10` | no mark |
| L21 | `91_-?` | `91^._-?` | dot above the 1 and bar below: list S (stato) or list I (luogo); the dot of the digit 1 cannot be told from a mark. The word decides |
| R02 | `10?` | `10` | no mark |
| R02 | `69^:?` | `69^.?` | one dot (C 69 da); the second dot is a blot |
| R02 | `32^.` | `32^.@N` | no bar is seen above 32; the sense wants Papa (32 with a bar). Suspect mark |
| R04 | `ll'?` | `"li(?)"` | a clear word, not the Spagna sign (pass B) |
| R04 | `10` | `10` | no mark |
| R05 | `10?` | `10` | no mark |
| R05 | `xi` | `SP{xi phi}` | two signs: SO |
| R06 | `10?` | `10` | no mark |
| R06 | `x8^._.` | `88^._.` | a blot (a cancelled figure), then 88 with a dot above and a dot below: M 88 negotio |
| R06 | `76^^_v?` | `76~_v?` | the stroke above is the verb arc, not a circumflex: P 76 promettere |
| R06 | `10?` | `10` | no mark |
| R07 | `10?` | `10` | no mark |
| R07 | `(4x)?` | `(44)` | (44) as pass B, with a correction above |
| R07 | `50^.` | `50^.?%` | no bar is seen; "Navarra" (50 with a bar) does not fit |
| R07 | `SP{# sig}` | `SP{xx a}` | first sign = double x (f): FA |
| R08 | `28^-_.` | `28^-_.?` | bar above and dot below (list T) |
| R08 | `SP{#  r t? v}` | `SP{xx qo r t v}` | first sign = double x (f): FAREI |

The most important ones for the sense:
- L07 `19`: "si fosse accordato con Re di Spagna" (version 3: an unread blot).
- L11 `28~^._-`: "scomunicava" (both passes: 29). The second digit has no tail below the line. This reading was looked
  for after the table showed S 28 "scomunica" next to the window; see section 5.
- L11 `20` and L18 `2`: numbers.
- L17: the spelled group is HAGIUSTIFICATO; (93) is (43) S.S.tà.
- L18: the clear word is "domandò", not "lodando".
- L19: RI + 41 with the verb arc = "RI-conosce".
- L21 `91`: S 91 "stato" against I 91 "luogo". The dot above a digit 1 cannot be told from a mark; the word decides.
- R06 `88^._.`: "negotio"; `76~_v`: "promesso".

### 31 March (ff. 36r-36v): 38 marks, 11 figures, 3 new units

Rule: where the blind passes B and C agree, their reading is taken, unless my look at the crop is clearly against it.
`changes_f36.tsv` has the same rows.

| line | consensus of version 3 | pass B | pass C | version 4 | kind |
|---|---|---|---|---|---|
| L01 | `14_:?` | `14~_.` | `44~^._.?` | `44~^._.?%` | figure |
| L01 | `32^^?` | `82^-?` | `32^-` | `32^-` | mark |
| L01 | `45?` | `45^.` | `45^.` | `45^.` | mark |
| L02 | `76=?` | `76_-` | `76_-` | `76_-` | mark |
| L02 | `33^^?` | `33~^:` | `33~^:?` | `33~^:` | mark |
| L02 | `53~?` | `53^-_.` | `53^-_.` | `53^-_.` | mark |
| L02 | `96_.?` | `90_-` | `96_-` | `96_-` | mark |
| L02 | `33?` | `33^.` | `33^.` | `33^.@A` | mark |
| L02 | `82?` | `82^.` | `82^.` | `82^.` | mark |
| L02 | `70?` | `70^:` | `70^:` | `70^:@C` | mark |
| L03 | `58?` | `58^.` | `58^.?` | `58^.` | mark |
| L03 | `68_-?` | `68=` | `68=` | `68=` | mark |
| L03 | `11^^_v?` | `15^^_v` | `15^^_v?` | `15^^_v?!` | figure |
| L03 | `68_-?` | `68=` | `68=` | `68=` | mark |
| L03 | `(15)?` | `(21)` | `(11)` | `(11)` | figure |
| L04 | `50^-?` | `70=` | `70=` | `70=` | figure |
| L04 | `70?` | `70^.` | `70^.` | `70^.` | mark |
| L04 | `44_.?` | `84=` | `94=?` | `84=?` | figure |
| L04 | `20^.?` | `20^._.` | `20^._.` | `20^._.` | mark |
| L04 | `87?` | `87_:` | `87_:?` | `87_:` | mark |
| L04 | `13_-?` | `93=` | `93=` | `93=` | figure |
| L04 | `59?` | `59^.` | `59^.` | `59^.@A` | mark |
| L04 | `98^.` | `98^.` | `98^:` | `98^:` | mark |
| L04 | `76=?` | `76_-` | `76_-` | `76_-` | mark |
| L04 | `61_:?` | `61^:` | `61^.?` | `61^:?` | mark |
| R01 | `65~_.?` | `65~^-_.` | `65~^-_.` | `65~^-_.` | mark |
| R01 | `(44)?` | `(14)` | `(14)` | `(14)` | figure |
| R01 | `47_.?` | `42^-_.` | `42^-_.` | `42^-_.?` | figure |
| R02 | `34^:?` | `34^.` | `34^.` | `34^.@A` | mark |
| R02 | `30=?` | `30^._-` | `30^._-` | `30^._-` | mark |
| R02 | `75=?` | `95=` | `95=` | `95=` | figure |
| R02 | `83=?` | `83~_-` | `83~_-` | `83~_-` | mark |
| R02 | `87~_.?` | `87^-_:?` | `87~^-_:?` | `87~^-_.?` | mark |
| R02 | `72^.?` | `72^._.` | `72^._.` | `72^._.` | mark |
| R03 | `76=?` | `76_-?` | `26_-` | `76_-?` | mark |
| R03 | `62_-?` | `62=` | `62=` | `62=` | mark |
| R03 | `-` | `24` | `2?` | `2n` | new unit |
| R03 | `-` | `6x?` | `46` | `46` | new unit |
| R04 | `-` | `29~?` | `19~?` | `29^.?` | new unit |
| R04 | `32=?` | `32^-` | `32^-` | `32^-` | mark |
| R04 | `13_-?` | `93=` | `93=` | `93=` | figure |
| R04 | `83_-?` | `83=` | `83=` | `83=` | mark |
| R04 | `73~_.?` | `73~^._.` | `73~^._.` | `73~^._.` | mark |
| R04 | `69` | `69?` | `69^.?` | `69^.` | mark |
| R05 | `28=?` | `28^-` | `28^-_.?` | `28^-_.?` | mark |
| R05 | `9x=?` | `98=` | `98=?` | `98=?%` | figure |
| R05 | `69` | `69` | `69^.` | `69^.` | mark |
| R05 | `69` | `69` | `69^.` | `69^.` | mark |
| R06 | `90_.?` | `90^._.` | `90^._.` | `90^._.` | mark |
| R06 | `71_.?` | `71^-_.` | `71^-_.` | `71^-_.!` | mark |
| R07 | `79_-?` | `79=` | `79=` | `79=` | mark |
| R07 | `79~^.?` | `79~?` | `79~^._-?` | `79~^._-?` | mark |

The most important ones for the sense: L02 `76_-` and `96_-` ("il {legato}", "la maggiore parte"); L03 `68=` twice
("ma"), `(11)` ("non se ne FARÀ"); L04 `93=` ("{pure}"), `98^: 82^. 76_-` with no figure 88 between; R01 the
spelled word begins with the sign for d (DARIA, not SARIA); R02 `83~_-` and `72^._.` ("liberarà", "morte"); R05
`28^-_.` (list T).

## 4. Window proposals

`interp_v4.tsv`: 16 kept from version 3, 31 new. Each row gives the window in lists_v4 and the contexts. A proposal
with (?) has a rival word in the same window.

Kept: {legato}, {richiamare}, {secondo}, {dovere}, {partire}, {esercito}, {esempio}, {giorno},
{radunare}, {preciso}, {restare}, {devotione}, {fama}, {ritorno}, {principio}; {dire} (C 90) is replaced
by {cacciare} (A 90) and {concorrere} (C 33) by {aiutare} (A 33).

New, with two or more contexts: {cacciare} (3), {pure} (3), {via} (2), {venire} (2), {spavento} (2), {tentare} (2),
{è} (2). New, one context: {audienza}, {vano}, {romore}, {publico}, {fatica}, {modo}, {procurare},
{in somma}, {mattina}, {a pena}, {confine}, {chiesa}, {ciascuno}, {offerire}, {ritrarre}, {piacevole},
{manifesto}, {arrivo}, {fratello}, {espettare}, {breve}, {incertezza}, {aiutare}.

Windows where I give no word, with the words that fit, are named in the readings and in the decode files:
E 11, PT 24, PT 49, PT 52, G 88, P 60, P 83, P 41, P 42, M 17, M 55, M 59, S 65, T 45, T 71, Q 15, Q 30, O 72,
(26), and the name 28 with a bar.

Notes for the keeper of the table (`table_notes_v4.tsv`; the table itself is not changed):
- N 28 "Cardinale d'Este" (1586) cannot be the person of March 1590.
- O 83: the clerk of fr. 4702 wrote "perdono", and "perdono" keeps the order after "perdita" 82. It fits L08
  "domandò perdono a Papa".
- BR (25): "volta" (the clerk, f. 108r) keeps the order after "verso" 23, and fits twice here ("per questa volta",
  "più di [una] volta"). The four "si" of f. 30 can be (15) read as (25).
- C 36 "confusione" is weak; "confine" keeps the order.
- M 44 and M 46 both have "mezzo". On f. 36r L01 the figure 44 carries the verb arc: one of the two can be "messo".
- A 84 "buono" and A 89 "bontà" break the order; A 86 falls between them.

## 5. History check

Source: L. von Pastor, The History of the Popes, vol. 21 (London 1932), pp. 343-362, full text on archive.org
(`historyofpopesf21past`), read on 4 October 2026. Pastor uses the reports of the envoys of Venice, Florence and
Mantua (Badoer, Niccolini, Brumani). L'Épinois was not read; Pastor cites him for the same events.

### Letter of 24 March

| statement of the reading | kind of words | Pastor |
|---|---|---|
| A person left Rome 18 days before, "per una sua {devotione}" | proposals | confirmed: Luxembourg left on 7 March "on the pretext of a pilgrimage to Loreto" (p. 350-351) |
| At once the report rose that the Pope had come to terms with Spain | glossed, one figure under a blot | confirmed: "It was thought in Rome that ... the Pope intended to yield to Spain" (p. 351) |
| The King of Spain had asked this with much insistence | glossed | confirmed (pp. 348-349) |
| The ambassador, in the first audience after the departure, asked pardon of the Pope | glossed and {audienza} | confirmed: audience of 10 March "to ask the Pope's pardon" (p. 350) |
| The rumour proved vain; sure news of the return of [O] | proposals | confirmed in substance: "But they were mistaken"; Luxembourg came back on 20 March (pp. 351, 356) |
| The ambassador threatened again to carry out the p[..] | partly read | confirmed: threat of the protest on 10 and 17 March (pp. 351, 353) |
| The Pope called a meeting of 20 cardinals at the instance of cardinals | glossed, a number, {radunanza} | confirmed: congregation of 19 March "by the advice of Cardinals Gesualdo and Galli"; 23 were called, Santori, Carafa and Castagna did not come (p. 354). 23 less 3 is 20 |
| He was threatened if he did not drive [O] away and excommunicate the princes who follow Navarre | {cacciare} {via}, one digit read again | confirmed: the demands were the expulsion of Luxembourg and the excommunication of the Catholic followers of Navarre (pp. 348-349, 354) |
| He told how he had acted in the affair of France, always with the King of Spain | glossed, {modo}, {procurato} | confirmed (pp. 354, 357) |
| Almost all held that the Pope should do none of the things asked, except in due time and after Navarre's answer on the freeing of the Cardinal of Bourbon | glossed | confirmed: only four cardinals voted for the Spanish demands; a delay for Navarre's reply "concerning the liberation of Cardinal Bourbon" (p. 354) |
| The act was not to be accepted | glossed | confirmed: the protest "could not be admitted" (p. 357) |
| The ambassador was not quieted | glossed | confirmed (p. 356) |
| The Pope, with the cardinals on Wednesday, ordered another meeting for the next morning | clear word, {radunanza}, {mattina} | confirmed: consistory of 21 March (a Wednesday: 17 March was a Saturday), all cardinals called "on the following day, March 22nd" (p. 356) |
| There he showed letters of good understanding with the King of Spain and JUSTIFIED his cause | spelled, glossed | confirmed: "He proved by documents, which were read by the secretary Caligari, that he had tried ... to act in union with Philip" (p. 357) |
| He asked the cardinals on 2 points. One: whether to drive out the ambassador | a number, {cacciare} | confirmed: "He therefore proposed the expulsion and excommunication of Olivares" (p. 357) |
| The Pope sees the ambassador as the source of the evil and can hardly believe that the order comes from the King | spelled RI, glossed, {a pena} | confirmed in part: some held "that Philip II. knew nothing of the provocative behaviour of Olivares" (p. 357); Pastor gives this as the view of cardinals |
| The second: whether to arm, Spanish soldiers being gathered at the borders of the State of the Church, more to frighten than for anything else | {confini}, {Chiesa}, {radunati}, {spaventare}; "stato" by a mark choice | confirmed: "the defence of the frontiers of the Papal States against the Spaniards"; Olivares had "written to Naples to withdraw the troops from the frontier" (pp. 357-358). "To frighten" is not in Pastor as the Pope's view |
| On the first, everyone held that he should not be driven out before two Spanish cardinals tried to draw him back | glossed, plain name 60, {ciascuno} | confirmed: "Most of them were opposed to the use of extreme measures until further negotiations with Olivares had been held"; Cardinals Deza and Mendoza were sent to him (p. 357) |
| "non però come ministri di Papa o vero di cardinali, ma da loro medesimi" | glossed, two doubtful units | Pastor has these words for Colonna and Sforza on 19-20 March ("not in the name of the Pope or of the congregation, but only in their own name", p. 356), not for Deza and Mendoza |
| They got a promise that nothing else will be done; out of danger for some days | glossed, {ritratto} | confirmed: Olivares "had yielded so far as to defer his protest for fourteen days" (p. 358) |
| The point is the freeing of the Cardinal of Bourbon | glossed | confirmed (pp. 352, 358) |
| The Pope more than once promised the King of Spain to accept no King of France who is not Catholic and trusted by the King of Spain | spelled, glossed, {pure} | not in Pastor in these words; he names the Pope's "proposals of December, 1589" to Philip (pp. 347, 357) |
| The identity of [N28] di [O] | not read | Pastor: the Duke of Luxembourg-Piney |

### Letter of 31 March

| statement of the reading | kind of words | Pastor |
|---|---|---|
| The Pope told the general Congregation "hieri mattina" | clear | confirmed: news on 29 March, congregation "on the following day" (p. 359) |
| He put the question whether to recall the Legate; all judged no | {richiamare}, {legato}, glossed | confirmed: he "proposed the immediate recall of the legate. But all the Cardinals were opposed to this" (p. 359) |
| The greater part wanted help with money first and then arms, with the King of Spain | glossed, {aiutare} | confirmed: "the majority ... were therefore in favour of strong intervention in union with Spain" (p. 359). Money and arms are not named there |
| The second question was referred to a particular meeting of cardinals | spelled FU RIMESSO | confirmed: the decision was left to the Pope with five cardinals of the French Congregation and five others (p. 359) |
| "per giudicio mio non se ne FARÀ niente ... tale si vede la inclinatione di S.S.tà" | spelled, glossed | confirmed by the outcome: "No decision was arrived at"; "the Pope wished to gain time" (p. 360) |
| Something is awaited from the Legate; in clear, the Patriarch Caetano is expected | chain of proposals; clear | confirmed in substance: "the brother of Cardinal Caetani, who had come to Rome to justify his conduct" (p. 360) |
| The Legate, before the rout of Mayenne, sent something to 2 cardinals who are with Navarre | {legato}, glossed, a number | confirmed in part: "the monitorium which he had sent to the Catholic adherents of Navarre" (p. 359); his harsh treatment of Cardinals Vendôme and Lenoncourt (pp. 346-347) |
| The order was perhaps to try the gentle way first; the Spaniards or Mayenne hindered it | {tentasse}, {via}, {piacevole}, glossed | confirmed: "the legate had orders first of all to try milder means" (p. 348); he acted "more in accordance with the wishes of the Spaniards than with the instructions of the Pope" (p. 347) |
| An army from Rome into France; "io ne credo poco" | proposals, glossed | background only: Philip's plan of an expedition of 50,000 men with a commander named by the Pope (p. 347) |
| Navarre wrote to Rome that he will free the Cardinal of Bourbon, with a reserve | glossed | not mentioned |
| Volta and the danger of letters | name, proposals | not mentioned |

### Where the reading was shaped by knowledge of the events

- Before I read Pastor I knew what the task brief says (Luxembourg, Olivares, the threat of a public protest, the
  congregations, the demand to free the Cardinal of Bourbon, Ivry) and I had a general memory of the quarrel.
- I looked at all the lines and wrote down the proposals before I read Pastor. The proposal file was typed after.
- Shaped by that knowledge: {cacciare} (the window allows other words; the three contexts carry it);
  "scomunicava" (I looked at the last digit again because S 28 "scomunica" stands next to S 29; the shape of the
  digit is the argument); {publico} (weak; from the words "public protest" of the brief); {fratello} (I knew that
  the Patriarch Caetano of the clear text was the Legate's brother).
- Decided after I read Pastor: that the plain 20 in L11 is the number of cardinals (before, I had it as "[20?]").
  Pastor's 23 less 3 gave the reason. "accordato" (19 under the blot) was my first idea from the sentence; I zoomed
  on the blot after I read Pastor, and the stem with its dot is seen.
- Not shaped, and confirmed after: {devotione}, {richiamare} il {legato}, {ritorno} (all three are proposals of
  version 3, made with no comparison), "Mercordì ... per la {mattina} dopo", "2 punti", {confini} di Stato di
  {Chiesa}, {via} {piacevole}, "i due cardinali Spagnoli", "per qualche {giorno}".
- No word was taken from Pastor into the text.

## 6. Controls

- Outside source: section 5. Of 22 statements of the first letter, Pastor confirms 19, confirms 2 in part, and
  does not have 1. Of 11 of the second letter: 7 confirmed, 1 in part, 3 not mentioned or background only.
  The count is mine; a statement that holds a proposal counts as confirmed in sense, not word by word.
- Two blind passes: section 2.
- Proposals of version 3 tested by a later source: fr. 4696 confirmed 8 and contradicted 1; Pastor now supports the
  sense of 3 more.
- The shuffled-table control of the earlier work (2 of 572) was not run again; the table did not change.

## 7. Prior art, checked again on 4 October 2026, 18:29 UTC

- D. Bourdeau, `cyphersolver` CATALOGUE.md: fr. 4698 is still in the queue, with key no. 35 named
  ("Nevers–Mantua letters ... BnF fr. 4698 nos. 2–5, 47, 92 ... catalogue 331"); no reading. SOLVED_CATALOGUE.md: no
  row for fr. 4698, fr. 4696 or fr. 4702.
  (https://raw.githubusercontent.com/dbourdeau/cyphersolver/main/CATALOGUE.md, .../SOLVED_CATALOGUE.md)
- NoAutopilot/cipher-lab PROGRESS.tsv: no row for these volumes.
  (https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/PROGRESS.tsv)
- One web search for phrases of the plain text with the shelfmark: nothing found.
- Not checked again: cabinet-noir, satoru.net, Tomokiyo's pages (checked on 3 October by the earlier work).
- Pastor does not cite these letters of Scipione Gonzaga; his Mantuan source is Brumani's reports in the Gonzaga
  Archives. A printed edition that is not online can exist.
Words to use: "first reading with the rebuilt key, with gaps, not checked by a palaeographer".

## 8. Open

1. The name [N28] di [O], and the oval sign.
2. Line 9 end ("p" and the drawn head after it), line 17 first half, f. 27r line 4 and line 8.
3. f. 36v line 1 (the army) and the word that the Legate "sent" to the two cardinals (P 42).
4. The windows of section 4 with no word.
5. The 19 glossed values that do not fit: each can be a wrong mark, a wrong figure or a wrong gloss.
6. My look at the film is not blind. A blind third pass for ff. 26v-27r was not made.
7. L'Épinois, and the reports of Brumani to Mantua (Pastor, App. nos. 31-33), were not read. Brumani wrote on the
   same day (24 March 1590) from the same city to the same family; his report is the best outside control.

## 9. Files in `v4/`

`reading_f26v-27r_v4.md`, `reading_f36_v4.md`, `NOTES.md`; `f26v-27r_transcription_v4.txt`,
`f36_transcription_v4.txt`; `changes_f26.tsv`, `changes_f36.tsv`, `edits_f26.py`; `interp_v4.tsv`,
`table_notes_v4.tsv`; `decode_f26_v4.txt`, `decode_f36_v4.txt`, `raw_f26_v4_step1.txt`, `raw_f36_v4_step1.txt`;
`blind_f36_passC.txt` and its crops `pC_*.jpg`; scripts `dec5.py`, `apply_edits.py`, `agree.py`, `linecrop.py`,
`linecrop2.py`, `zoom.py`, `lines.py`; crops `lc_*.jpg`, `z_*.jpg`, overviews `ov_*.jpg`.
