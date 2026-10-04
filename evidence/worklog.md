# BnF Espagnol 132 (Gallica btv1b10032556x): the letters that nobody had read — notes of 4 October 2026

Work folder `es132/`. Rules: `scout2/AGENT_RULES.md`. All times BST on 4 Oct 2026.

## 1. State of the others (fetched 13:36-13:40 BST = 12:36-12:40 UTC)

Sources: `src/cl_*` (NoAutopilot/cipher-lab `ciphers/es132-vargas-mexia-1578/`, last es132 commit 4f50697d, 4 Oct 11:48 UTC; last repo commit
dc4db821, 12:36 UTC), `src/cn_*` (el-descifrador/cabinet-noir, last commit 47b6db9a, 2 Oct 14:15 UTC, v1.2.1), `src/satoru_now.html`
(satoru.net/crypt, same bytes as the scout's copy of 13:13), `src/bd_*` (D. Bourdeau: no Espagnol 132 target; last commit 3 Oct 06:07 UTC),
Aymeloglu (no row).

| Folio (first leaf) | Cipher | Read by | Date |
|---|---|---|---|
| 3-4 | 1 | S. Tomokiyo (with D. Martín Vilela) | 2020 |
| 11-12, 17-25 (+dup. 22), 34 | 2 | Cabinet Noir (results 6, 16, 15) | 29 Sept 2026 |
| 198-199 | 4 | Cabinet Noir (result 7); Satoru (`perez1579`) | 29 Sept; 2 Oct 2026 |
| 123 | 4 | Cabinet Noir (17); Satoru (`es132-f123`) | 29 Sept; 2 Oct 2026 |
| 154-155 | 4 | Cabinet Noir (19) | 29 Sept 2026 |
| 32, 44, 46, 58, 71, 73, 81, 105, 113, 134, 138, 142, 161, 165(+167), 195, 200, 211, 215, 220, 222, 228, 233, 245, 255 | 3 (Cp.30) | Cabinet Noir (24 letters) | 29 Sept - 1 Oct 2026 |
| 37 | 3 | Satoru (`es132-f37`) | 2 Oct 2026 |
| 89-91 (+dup. 93-95), 119-120 | 3 | cipher-lab (Teulet prints one paragraph of each, "Déchiffr. officiel") | 3-4 Oct 2026 |
| 41, 50-51 | 3 | cipher-lab | 4 Oct 2026 |
| 169, 177 | - | period clear copies in the volume | 1579 |
| other Cipher 3 letters (39, 54, 62, 79, 85, 129, 146, 150, 171, 181, 185, 202, 206, 208, 213, 218, 235, 237, 251, 253, 257, 267, 269, 271, 275) | 3 | nobody found; cipher-lab is on this pool | - |
| **87, 157, 179** (A. Pérez) | 4 | nobody (Cabinet Noir: single phrases in its key file; Rubino 2012: plain text only) | - |
| **26** | 2 | nobody (Cabinet Noir names it "lettre E, non comptée") | - |
| **273-274** | 2 | nobody (BnF: "chiffre"; Tomokiyo: "Philip II to Vargas, Cipher 2") | - |
| 136, 148 (A. Pérez) | none | plain letters (Rubino 2012 prints both) | - |

I took the five pieces in bold. cipher-lab had not reached any of them at 12:40 UTC (its NOTES list f.87/157/179 as "not attempted").

## 2. Images

IIIF only, one request at a time, files kept in `img/` (`c<N>.jpg` = canvas N, full size, 6500-6900 x 5452, bitonal microfilm scan).
Each canvas is an opening. Folio to canvas: from f.32 on, f.Nr = right page of canvas N-3 and f.Nv = left page of canvas N-2; before
the gap, f.Nr = right page of canvas N+2. Canvases used: 84, 85 (f.87r, 87v-88r); 154, 155, 156 (f.157r; blank; f.158v-159r);
176, 177, 178 (f.179r, 179v-180r, address); 270, 271, 272 (f.273r, 273v-274r, 274v); 28, 29 (f.26r; then the address leaf before
f.32). Canvases 22, 23, 24 were fetched by mistake (f.19v-22r). Three requests failed (no file or an HTTP 500 page) and were
repeated once: canvases 155, 24, 156, 29. `img/c29_error.html` is the saved error page.
**The scan has no f.26v-31r.** `img/tiles/` holds a first, faulty cut of the line tiles; `img/t2/` is the good one (a safety check
refused the removal of the old folder; it can be deleted by hand).

## 3. Cipher 4 (Antonio Pérez's private cipher) — f.87, 157, 179

System: numerals 1-23 = letters in reverse order (a=12, b=11, c=10, d=9, e=8, f=7, g=6, h=5, i=4, l=3, m=2, n=1, o=23, p=22,
q=21, r=20, s=19, t=18, u=17, x=16, y=15, z=14); a mark after the numeral adds a vowel: dot right = a, plus = e, dot below = i,
6-shaped hook = o, dot above = u; letter signs y = a, a = u/v, o = o; cluster letters t = tr, p/P = pr, c = cr, b = br; a plus above
doubles (rr, ll, ss). **Key: J. P. Devos 1950, p.422; completed by S. Tomokiyo 2020** (`src/tomo_spanish3vargas4.png`).
From Cabinet Noir (`src/cn_cipher4_codes_perez.tsv`, CC BY 4.0): vo = Su Magestad, xe = V.m., C = ch, a with dot below = vi.

What this folder adds (hypotheses; each with its evidence):

| Sign | Value | Evidence |
|---|---|---|
| any sign with a caret or an acute above (7^, 5^, 2^, 9^, P^, y^, 6^, 3^, 19o^, por^) | null | 14 places; each word reads only without it (a-[7^]-cudido, ar-[7^]-cauti, ar-[5^]-cauti, ce-[2^]-saran, me [6^] guardare) |
| the looped H-like sign (Cabinet Noir's "H?") | null | 7 places, always beside other nulls or between words |
| d (letter) | dr | pa-dre (f.179v), 1 context |
| t with dot above | tru | qua-tru-m-vi-ra-to (f.157r) |
| si | possible | 2 contexts in one sentence: "si fuesse [si] aver a las manos", "con el mayor recato que sea [si]" |
| co | carta | "recognoscer todas las [co]s" (Tomokiyo had co = carta from f.123) |
| fa | cifra | "se les pediran las [fa]s", 1 context; same letter spells "zif[ra] particular" |
| ro | para (?) | "lo que huviere de ser [ro] mi solo", 1 context; pass B read "vo" |
| xi | don Juan de Austria (?) | 4 contexts, all in the letter of 13 Sept 1578 (don Juan died on 1 Oct): he wrote to Vargas; he wants no [mo] but one placed by his own hand; he is disliked "in those parts"; he honours Arcauti, his own paymaster in Paris (Mignet 1846: "Pedro Arcant[i], contador … de son armée"). Cabinet Noir gave this value 0.45-0.5 |
| tu | señor (?) | gloss "tu xi" over a struck name, 1 context |
| mo, Ta, Te/te, no, ho, ti, du, Se | not resolved | Ta: feminine, "tomara S.M. la [Ta]", "la [Ta] que se ha tomado" (traça? resolucion?); ho: a coin ("doze mill [ho]s"); du: perhaps a null |

Not resolved in the text: f.87r, the group after "recoge-" (`10 2+` or `10 21+`; both passes); f.87r, "X 1? P^ 1?" before "y Lalain"
(two short strokes that can be the numeral 1 or slashes); f.87v, the last sign (read `[Te]` by pass B, `xe` by pass A); f.157r,
"quitar la leche de las amas" is what the cipher says (C+ = che), its sense is a figure that I do not understand for certain;
f.179v, four line ends in the binding.

Passes: A = the solver, on bands at 0.75 scale and full-size crops (`passes/perez_passA.txt`); B = blind agents, sign names and
images only (`passes/f87_passB.txt`, `f157_passB.txt`, `f179_passB.txt`; prompt `passes/PROMPT_c4_blind.md`). Pass A saw Cabinet
Noir's key file first (it quotes about 20 groups of these letters), so pass A is not blind; pass B is.
`python3 cmp4.py passes/perez_passA.txt passes/f87_passB.txt f87r f87v` → 81/89 = **0.910**;
`… f157_passB.txt f157r f158v f159r` → 322/353 = **0.912**; `… f179_passB.txt f179v f180r` → 128/141 = **0.908**.
After the comparison I took four readings from pass B (procurar for "q cunple", a verme, [Te], 9 with acute).

Control (`python3 control.py c4 es passes/perez_passA.txt`, Spanish letter-trigram model from `corpus/es_3.npy`, 876 decoded
letters, codes left out): real key −7.576; 500 shuffled alphabets (vowel marks kept) mean −11.046, sd 0.680, best −9.442, z = 5.1,
0/500 as good; alphabets and vowel marks shuffled: mean −11.653, best −9.704, 0/500. Inside control: "don Alonso de Sotomayor" in
cipher on f.87r stands in plain letters on f.88r and f.159r; "Curiel" in cipher on f.158v stands in plain letters two lines below.

## 4. Cipher 2 — f.26r and f.273-274

System: numerals 2-23 = a-z in order (a=2 … z=23); marks: rho-hook = a, plus = e, dot below = i, dot above = o, dot right = u;
overlined groups = nulls. **Key: S. Tomokiyo, broken on 1 Aug 2020** (`src/tomo_spanish3vargas2.png`). From Cabinet Noir's notes:
lone rho = y, V = ll, 0+ = ss, f = cr, n = pr, p = tr, R = rr, C = ch, 98 = Rey, 99 = Reyno, 48 = Duque.
This folder adds: 0 without a mark = a (acertado, avisarme, a Inglaterra: 6 places); **du = the King of France** (f.273v L28,
f.274r L7; it also fits Cabinet Noir's open "oficio con [du]" in f.34); **42 = the Duke of Savoy** (heading and docket of f.273-274);
the g-like sign with a crossed tail = z (Cruz, zelo, sforzo).

Passes: two blind agents per page on 4-line tiles (`img/t2/`, prompt `passes/PROMPT_c2_blind.md`); A = default model, B = Sonnet.
`python3 cmp2.py passes/<page>_passA.tsv passes/<page>_passB.tsv`: f.26r 436/545 = **0.800**; f.273v 609/698 = **0.872**;
f.274r 610/702 = **0.869**; f.274v 299/345 = **0.867**; f.273r 640/778 = **0.823**. The reading follows pass A.
Control (`python3 control.py c2 it|es <pass file>`): f.26r (Spanish model) −7.728 against shuffled mean −11.444, best −9.644, 0/500;
f.273v (Italian model) −7.667 against −11.817, best −10.085, 0/500 (the same page under the Spanish model: −8.425, so the text is
Italian); f.274r −7.608 against −11.855, 0/500; f.274v −7.684 against −11.831, 0/500; f.273r −7.702 against −11.703, best −9.951, 0/500.

## 5. What the pieces are

- **f.87, f.157, f.179**: three private letters of Antonio Pérez to Vargas Mexía (13 Sept 1578, 8 Dec 1578, 26 Jan 1579). Plain
  Spanish with cipher passages (87, 353 and 141 groups). File `reading_perez_f87_f157_f179.md`.
- **f.26r**: first page of a letter of Philip II to Vargas, March 1578 (Stukeley at Palamós; 20,000 escudos in gold, in secret).
  File `reading_f26r.md`. Blocked after line 27: f.26v-31r are not in the Gallica scan.
- **f.273r-274v**: not a letter of Philip II. Heading in cipher: "Copia del escrito que ha dado Mos de la Cruz a Su Magestad de
  parte del [42]"; text in **Italian**: a memorial of the Duke of Savoy (Emanuele Filiberto) to Philip II on the march of 3,000
  Spaniards to Flanders with the "Commendator maggiore" (Requesens). It names the camp before La Rochelle and the Huguenots of
  Languedoc and Nîmes, so it is of **spring-summer 1573**, when Vargas Mexía was ambassador in Turin. Docket on f.274v: "dupp.do /
  Para embiar a Juan de Vargas Mexia" and the same heading in cipher. So Cipher 2 was Vargas's cipher already in 1573, five years
  before the Paris letters. File `reading_f273_274_savoy_memorial.md`.

## 6. Prior art (searched 4 Oct 2026)

- S. R. Rubino, "The Secrets of Antonio Pérez Decoded", OSU honors thesis 2012 (kb.osu.edu/handle/1811/51582; text read through
  exa.ai/library/publication/k9gwns7mnk0, saved as `src/rubino2012_exa.txt`): prints the plain text of f.66, 87, 136, 148, 157, 179,
  198 with `[CIFRA]` for every cipher passage, and says the cipher was not broken. **So the plain text of f.87, 157, 179 is reproduced;
  only the cipher passages are a first reading.**
- L.-P. Gachard, La Bibliothèque nationale à Paris, i (1875), pp.415-424 (`src/ia_labibliothque01gach.txt`): one sentence of f.87
  ("Yo estava con desseo de recobrar a heredero …"); knows only three Pérez letters (f.66, 87, 198); nothing on f.157, 179, 26, 273.
- F. Mignet, Antonio Perez et Philippe II (`src/ia_antonioperezetph00mign.txt`): names Arcanti and Sotomayor; none of these texts.
- BnF record cc34747q (`src/bnf_cc34747q.html`): f.87, 157, 179 "en partie chiffrée"; f.273 and 275 "Deux chiffres de Philippe II
  pour Juan de Vargas Mexia"; art. 10-16 on f.17, 22, 26, 28, 30, 32, 34, art. 13 the duplicate of art. 12.
- Web: Exa and WebSearch, 5 queries (Pérez + Arcauti/Capelo/quatrumvirato; Savoy memorial 1573 + "padrone del mare"; Stukeley +
  Palamós + 20,000 escudos; CSP Simancas 1578). No text of f.26, f.273 or of the cipher passages found.
- Not done: Teulet v (archive.org answered HTTP 500); Marañón, "Antonio Pérez" (not online); CODOIN; Calendar of State Papers,
  Simancas, March 1578, page by page; AGS minutes (Estado K 1544-1558 and the Savoy series, not online); Archivio di Stato di Torino.
- On the leaves: no period decipherment, no margin gloss, no clear copy on the next leaf, for any of the five pieces (all the
  canvases above were seen). One period gloss only: "tu xi" on f.87r.

Words to use: plain text of the three Pérez letters = **reproduced** (Rubino 2012); cipher passages of f.87, 157, 179, the page
f.26r and the memorial f.273-274 = **first reading with the known key** (keys: Devos, Tomokiyo; code values partly Cabinet Noir).
Nothing here is "new" in the strict sense of the rules: the Simancas minutes were not checked.

## 7. Open points

1. The two passes of the Cipher 2 pages were not reconciled group by group on the image: the reading follows pass A, and the 13-20 % of groups where B differs were settled by the sense of the word, not by a third look. A third pass on the disagreements would raise the confidence.
2. Code words of Cipher 4 without a proved value: mo, Ta, Te, no, ho, ti, du, Se, and xi/tu (probable only).
3. f.87r "recoge-c-me/que"; the two strokes before "y Lalain".
4. f.26: the rest of the letter needs images of f.26v-31r (ask the BnF, or microfilm MF 8506).
5. "Mos de la Cruz": the Savoy ambassador in Madrid in 1573 is not identified by me.
6. The Italian of f.273-274 is edited from one pass with a second pass as a check; the dots (o / i / u) are the weak point.

## 8. Files

`reading_perez_f87_f157_f179.md`, `reading_f26r.md`, `reading_f273_274_savoy_memorial.md` (text, (?) marks, English).
Transcriptions: `passes/perez_passA.txt`, `passes/f87_passB.txt`, `passes/f157_passB.txt`, `passes/f179_passB.txt`,
`passes/<page>_passA.tsv` and `_passB.tsv` for f26r, f273r, f273v, f274r, f274v. Scripts: `c4.py`, `c2.py` (decoders; `c4.py … --wrong`
prints a wrong-key decode), `cmp4.py`, `cmp2.py` (agreement), `control.py` (wrong-key control), `tiles.py`, `bands.py`, `linecut.py`.
Passes per line: every cipher line had two passes (one blind for the Pérez letters, two blind for the Cipher 2 pages); the plain
Spanish of the Pérez letters had two passes and a comparison with Rubino's print.

## 9. Last check of the others (13:18 UTC, 4 Oct 2026)

cipher-lab: last es132 commit 13:14 UTC, still on the Cipher 3 letter f.50-52 (f.51v, f.52r). Cabinet Noir: no commit after
2 Oct 14:15 UTC. Neither has f.87, 157, 179, 26 or 273.
