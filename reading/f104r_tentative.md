# f. 104r: reading by the checker (BnF fr. 4698, `img/v107_R.jpg`)

Heading on the sheet, in clear, by another hand: "[..] di 16 feb. 1590 / R. 9 aprile 1590 da Parigi" (the first agent reads
"Con la lettera di 16 febraro 1590. R. 9 aprille 1590"). 21 cipher lines, no gloss. Italian.

## Method and limits

- Transcription: `f104r_transcription_checker.txt`. I read every unit on my own crops (`work/Q_LL_S.jpg`) with the first
  agent's transcription open, and corrected figures and marks. This is one pass by me; it is the second pass of the sheet.
- Decode: `work/dec104.py`. The mark alone names the list. I do not let a neighbour list supply a word (the first agent's
  decoder did). Tables: `lists.tsv` (glossed), `interp.tsv` (first agent's interpolations), `checker_candidates.tsv` (mine).
- Three kinds of words, and one more:
  - CAPITALS = spelled with the symbol alphabet. “quotes” = written in clear on the sheet. “A” = a clear capital used as a code name (the first agent takes it as Francia; I follow, as an inference).
  - plain lower case = **glossed** value. (v) = the figure has the verb arc: read the verb.
  - {braces} = **interpolated** value from the first agent's `interp.tsv` (no gloss).
  - {{double braces}} = **my candidate** (no gloss): a word in the alphabetical window of the list that the mark names, chosen for sense. It is an inference.
  - [figure and mark] = unresolved.
- Count: code units 643: glossed 416 (64%), first agent's interpolations 40 (6%), checker's candidates 40 (6%), unresolved 147 (22%); spelled groups 24; null groups 4
- What I changed most against the first transcription: many "bar below" are two bars; "dot below" is often "bar above and dot below" (list T)
  or "dot above and dot below" (list M); several arcs carry a second mark; `60 69 09` (line 6) and `50 52 02` (line 21) are
  null groups of the pattern a0 ab 0b, not words ("60 69 90 97" and "50 52 02?" in the first transcription).

## Passages that read as sentences

Quotations keep the marks of the three kinds. I give the Italian in the grammatical form; the code gives dictionary forms.

| lines | reading | how far it is safe |
|---|---|---|
| 1-2 | "ho {parlato} di [10^^] con [a] di Spagna, et per risolutione? di {{domanda}} di V.E. “dico che” il [74] di proposta che [83] LE FECI in {{nome}} di lui {{nacque}} da {{poca}} inclinatione che fino hora HA mostrato [il] Papa {verso} la {persona} di lei" | glossed: ho, con, Spagna, proposta, lui, inclinare, che fino hora, mostrare, Papa, la, lei. "a di Spagna" = the Spanish ambassador by sense only (figure 10, no mark seen) |
| 2 | "da {{la quale}} mala {{dispositione}} [36] per necessità che S.S.tà non si [..]" | male, necessità, S.S.tà glossed; the rest inferred |
| 3 | "il che si {{conosce}} {quanto} [..] può {{importare}} a [..] {successo} di cose di “A”" | potere glossed (39 with caron and arc) |
| 4 | "et in questo si ferma: non potere {tale} {{effetto}} essere {opera} di altra {{mano}} che di quella di Re di Spagna, il quale [(33)] in {sommo} grado [..]" | glossed: questo, si, fermo, non, potere, essere, altro, che, quello, Re di Spagna, il quale, grado |
| 5-6 | "si come può con autorità et grandezza sua COLLOCAR [63] {persona} di lei in quello [91: stato?] di honore et di {sicurezza} che lei {merita} et {{deve}} desiderare" | glossed: si, come, potere, con, autorità, grande, sua, lei, in, quello, honore, desiderare. 91 has a bar below; "stato" needs the dot of the 1 as a mark |
| 6 | "{Così} non vuole né [14] da lei né {{disporre}} di lei se non {quanto} SARÀ giusto et {{espediente}} a quale di {{uno}} et di altro" | glossed: non, volontà (verb), ne, da lei, di lei, se non, giusto, quale, altro |
| 6-7 | "Non “sarà” {{dunque}} per hora il {{fine}} di Re di Spagna il servirsi di V.E. fuori di “A”, ma sì il VALLERSI di {opera} sua et di suo [76]" | glossed: non, per, hora, il, Re di Spagna, servire (42 with dot, underbar and arc), si, V.E., fuori, ma, sua, suo |
| 8-9 | "ma {{pensa}} {{anco}} di con-CEDERLE di quelle {{gratie}} che a lei SIANO più {{honeste}} A ricevere che A {{domandare}}" | glossed: ma, di, con (used as a syllable), quello, che, a, lei, più, ricevuta (verb), che |
| 13 | "“intendendo” {però} questo, et senza PRE-{{giudicio}} di necessità di ..." | glossed: questo, senza, necessità |
| 14 | "et per quello tempo che le cose di “A” “saranno” ..." | all glossed (26 with bar above and dot below = tempo) |
| 17 | "et che non HA per {{fine}} di essere Re di “A”, ma questo di [N 50] non È {sicuro}" | glossed: che, non, per, essere, Re, ma, questo. [N 50] is a person (bar above); {{Navarra}} is a weak guess |
| 18 | "se lui non desidera da vero [35], di che fino hora non si {{vede}} {{molto}} [84] segno, se non in [59 arc] [16] di [32]" | glossed: se, lui, non, desiderare, da, vero, che fino hora, non, si, segno, se non, in |
| 21 | "... a V.E. che, “facendo” {condurre} deliberare, può [42] con [a] di Spagna [41] {{costì}}, il quale ..." | weak |

## What the sheet is about (only as far as the words carry)

- It continues the business of the letter of 21 January (f. 30v). Scipione has spoken again with a person "di Spagna"
  (the figure is 10 = "a"; "Amb.re" is by sense only).
- He explains the proposal that he made to Nevers in that person's name: it came from the small inclination that the Pope
  has shown up to now toward Nevers (glossed words: Papa, inclinare, mostrare, "che fino hora"; "poca" and "nacque" are mine).
- The argument: the desired result cannot be the work of any other than the King of Spain, who can, with his authority and
  greatness, "COLLOCAR ... {persona} di lei in quello [stato] di honore et di {sicurezza}" that Nevers merits.
- For now the King of Spain does not aim to use Nevers "fuori di “A”" but "il VALLERSI di {opera} sua" (line 7). The nouns "fine" and "dunque" are my candidates; "servire ... fuori di A, ma si il VALLERSI" is glossed and spelled.
- Line 17 says of someone "che non HA per {{fine}} di essere Re di “A”". By position this is the King of Spain; the subject is not in the line. I do not claim more.
- Lines 8-12, 15-16 and 19-21 do not read as connected text. I do not say what they hold.
- The sheet names no sum and no office that I can read.

## Line by line (decoder output, strict marks)

```
L01 ho {parola(v)} di [10^^] con a di Spagna et per risolutione? di {{domanda (verb: domandare)}} di V.E. “dico che” il? [74^._.] di proposta che [83^-_.?] LE FECI in {{nome}} di lui {{nascita (verb: nascere)(v)}} da
L02 {{poco}} inclinare che fino hora HA mostrare Papa {verso} la {persona} di lei da? {{la quale}} male {{dispositione (verb: disporre)}} [36~_-] per necessità che S.S.tà non si A per {opera(v)} [14_:] ne per il honore di lei
L03 ne per L accordare suo con [98] di [71] il che si {{conoscere(v)}} {quanto} [83] potentia (verb: potere)(v) {{importanza (verb: importare)}} a [84^.?] {successo} di cosa di “A” ne “potendo” questo essere [88^._.] se non di {(a prince; Principe?)} di {{la quale}}
L04 danaro [68~_.?] {{honesto?}} a in {{pensiero (verb: pensare)}} et in questo si fermo non potentia (verb: potere)(v) {tale} {{effetto}} essere {opera} di altro {{mano}} che di quello di Re di Spagna il quale [(33)] in {singolarmente/sommamente} grado [63_:] quale che io [38~^-_.?]
L05 [10^-] V.E. di {(a prince; Principe?)} et di cavaliere si come potentia (verb: potere)(v) con autorità et grande sua COLLOCAR [63_.] {persona} di lei in quello [91_-] di honore et di {sicuro} che lei {merito(v)} et
L06 {{debito (verb: dovere)(v)}} desiderio/desiderare(v) {così} non volontà (also volontieri)(v) ne [14~^^_v] da lei ne {{dispositione (verb: disporre)(v)}} di lei se non {quanto} SARÀ giusto et {{espediente}} a quale di {{uno}} et di altro [60 69 09] non “sarà” {{dunque}} per
L07 hora il {{fine}} di Re di Spagna il servitio / servire(v) si di V.E. fuori di “A” ma si il VALLERSI di {opera} sua et di suo [76^.?] come il {Signore} [86] di {lungo} mostrare? [13=]
L08 in quello [32^^_v] non [11~^-] [34^._.] [55=] [15_:?] che altro [44_-] non [65~_v] hora Re di Spagna in “A” et in questo havere non [66^._-] {ogni} {{debito (verb: dovere)}} [45^.?] a honore di V.E. ma {{pensiero (verb: pensare)}} {{anco}} di con CEDERLE
L09 di quello {{gratia}} che a lei SIANO più {{honesto}} A ricevuta(v) che A {{domanda (verb: domandare)(v)}} [66=] a quale [61^-?] [(33)] io [36_v] [62=] [63_:] [86^:] di [37_:] di O [81_-] a V.E. da {Signore} di [71] [79=] la
L10 altro [18^^] manco circa (used for "cerca") [63_:] [94^.?] di {Signore} [87] sua [88^:] come circa (used for "cerca") [63_:] [15^^] di {condurre} sua [31_.] [79~^^_v] L a {quanto} a questo [83^-_.] cosa che [53^-_.] “haverà” danno [66^^_v] [94_-] si città(v) il [92_v] [61_v] di volontà (also volontieri)
L11 {quanto} [90=] a [59_v] di [37_:] DICE hora essere [24^._.] se quello {Signore} L [50~^.] [15^^] perché FU DATO a lei in [16^^] di [98] [(37)] ne [(47)] {{pensiero (verb: pensare)(v)}} essere [12^^] a [36~^._-]
L12 [63_:] [63_.] {ordine} da [55] morte [91_-] da medesimo FU [88^._v?] [(37)] la di in [91_-] per ma {ragione?} non {{giudicio (verb: giudicare)(v)}} detto (dire) [(46)] il {{domanda (verb: domandare)(v)}} in [55=] questo [37_:] in quale [56~] più [51] la [66^.] [(37)] ma si
L13 [49~^.] di altro cosa {{la quale}} si a per essere di non [52^._.] [62^._-] et si a non a [78^-_.] ma [91^^] in {quanto} sua “intendendo” {però} questo et senza PRE {{giudicio (verb: giudicare)}} di necessità di
L14 [57^.] et per quello tempo che la cosa di “A” “saranno” {però} che a hora convenire(v) [48~_v] quello che “haveranno” servitio / servire a {così} giusto [78_:] [80 08?] che [90=] la cosa di {{Navarra ?}}
L15 [83~_v] [67_-?] medesimo [67_.] si intendere(v) da più [74^.] ma L a credere(v) che non “andaranno” [43^:] maggiore Re di Spagna [52^.] L CI SARÀ [51] si come [64~] {{anco}} che {{Navarra ?}} non [40^^] a
L16 V.E. cosa che hora promettere(v) per havere lei da [74^.] sua {però} [(41~)] in prudenza di lei il [45~^.] quale di questo [63~] {{debito (verb: dovere)}} [88=] essere accettare a [59=?] [15] arme(v) quello di Re di Spagna
L17 fermo et [86^._-] et [blot=] non potentia (verb: potere)(v) essere [67^^_v] di [42^.] [39~^.] V.E. con Re tanto [64] et che non HA per {{fine}} di essere Re di “A” ma questo di {{Navarra ?}} non È {sicuro} et potentia (verb: potere)(v)
L18 essere con grande [18^^] di {Iddio} et [90^.?] et [25^:] di [32^^_v] se lui non desiderio/desiderare(v) da vero(v) [35^^_v] di che fino hora non si {{vista (verb: vedere)(v)}} {{molto}} [84^.] segno se non in [59~] [16=] di [32~^^_v]
L19 et da questo io [93~^:] [86_.] [31] che [27=] lui si [70~_v] [64^^] non il “facendo” per sua quello ma [16=] per suo [24^.] et {interesse} [67_.] non “sarà” [69_-] [67^._.] [64] perché
L20 [60=] la di È [30^:] di {Iddio} non cosa che si [23~^.] per [94^:] [83_.] et {Iddio} per {ordine} non da(v) il [14_:] [30^:] a quello che non il volontà (also volontieri)(v) et si ne “fanno” [(13)] più
L21 [96_:] con [54_-] [50 52 02] potentia (verb: potere)(v) a V.E. che “facendo” {condurre} deliberare potentia (verb: potere)(v) [42~^-_.] con a di Spagna [41^^_v] {{costì}} il quale di [53^-_.] È {{debito (verb: dovere)}} et [20=]
```

## Unresolved units (list named by the mark, glossed window)

```
  	L01	10^^	O	start .. 25 opinione
  	L01	74^._.	M	73 mostrare .. 75 muovere
  	L01	83^-_.?	T	67 vero .. 87 volontà (also volontieri)
  	L02	36~_-	I	22 ingegno .. 43 intendere
  	L02	14_:	G	start .. 33 giusto
  	L03	98	A	72 aviso .. end
  	L03	71	A	70 autorità .. 72 aviso
  	L03	83	A	72 aviso .. end
  	L03	84^.?	C	82 di .. end
  	L03	88^._.	M	85 necessità .. 92 nocumento
  	L04	68~_.?	M	65 molto .. 72 morte
  	L04	(33)	BR	32 havere .. 34 io
  	L04	63_:	G	59 honore .. 67 il
  	L04	38~^-_.?	T	26 tempo .. 55 valore
  	L05	10^-	N	start .. 26 legato
  	L05	63_.	M	54 mio .. 65 molto
  	L05	91_-	I	83 libero .. 96 maggiore
  	L06	14~^^_v	Q	11 questo .. 23 ragionamento
  	L07	76^.?	C	75 deliberare .. 78 desiderio/desiderare
  	L07	86	A	72 aviso .. end
  	L07	13=	PT	start .. 25 assai
  	L08	32^^_v	Q	29 replica / risposta .. 52 ricevuta
  	L08	11~^-	N	start .. 26 legato
  	L08	34^._.	M	33 medesimo .. 54 mio
  	L08	55=	PT	51 già .. 56 hora
  	L08	15_:?	G	start .. 33 giusto
  	L08	44_-	I	43 intendere .. 45 intentione
  	L08	65~_v	P	52 pretesto .. 76 promettere
  	L08	66^._-	S	42 servitio / servire .. 91 stato
  	L08	45^.?	C	44 consenso/consentire .. 47 conservare
  	L09	66=	PT	63 la .. 68 ma
  	L09	61^-?	N	59 V.S.Ill.ma (Card. Gonzaga) .. 73 Umena (Mayenne)
  	L09	(33)	BR	32 havere .. 34 io
  	L09	36_v	P	13 piacere .. 39 potentia (verb: potere)
  	L09	62=	PT	56 hora .. 63 la
  	L09	63_:	G	59 honore .. 67 il
  	L09	86^:	E	80 fatto (fare) .. 87 fermo
  	L09	37_:	G	33 giusto .. 38 grado
  	L09	81_-	I	79 lettera .. 83 libero
  	L09	71	A	70 autorità .. 72 aviso
  	L09	79=	PT	77 nondimeno .. 82 o vero
  	L10	18^^	O	start .. 25 opinione
  	L10	63_:	G	59 honore .. 67 il
  	L10	94^.?	C	82 di .. end
  	L10	87	A	72 aviso .. end
  	L10	88^:	E	87 fermo .. end
  	L10	63_:	G	59 honore .. 67 il
  	L10	15^^	O	start .. 25 opinione
  	L10	31_.	M	10 male .. 33 medesimo
  	L10	79~^^_v	Q	78 rispetto .. 88 rotta
  	L10	83^-_.	T	67 vero .. 87 volontà (also volontieri)
  	L10	53^-_.	T	26 tempo .. 55 valore
  	L10	66^^_v	Q	52 ricevuta .. 76 risolutione
  	L10	94_-	I	83 libero .. 96 maggiore
  	L10	92_v	P	89 prudenza .. 96 quale
  	L10	61_v	P	52 pretesto .. 76 promettere
  	L11	90=	PT	87 più .. 97 qualche
  	L11	59_v	P	52 pretesto .. 76 promettere
  	L11	37_:	G	33 giusto .. 38 grado
  	L11	24^._.	M	10 male .. 33 medesimo
  	L11	50~^.	C	47 conservare .. 51 contrario
  	L11	15^^	O	start .. 25 opinione
  	L11	16^^	O	start .. 25 opinione
  	L11	98	A	72 aviso .. end
  	L11	(37)	BR	36 lei .. 39 sono
  	L11	(47)	BR	45 S.A. .. 50 V.E.
  	L11	12^^	O	start .. 25 opinione
  	L11	36~^._-	S	34 segno .. 42 servitio / servire
  	L12	63_:	G	59 honore .. 67 il
  	L12	63_.	M	54 mio .. 65 molto
  	L12	55	A	49 animo .. 57 ardire
  	L12	91_-	I	83 libero .. 96 maggiore
  	L12	88^._v?	None	mark not in the table
  	L12	(37)	BR	36 lei .. 39 sono
  	L12	91_-	I	83 libero .. 96 maggiore
  	L12	(46)	BR	45 S.A. .. 50 V.E.
  	L12	55=	PT	51 già .. 56 hora
  	L12	37_:	G	33 giusto .. 38 grado
  	L12	56~	A	49 animo .. 57 ardire
  	L12	51	A	49 animo .. 57 ardire
  	L12	66^.	C	64 credere .. 69 da
  	L12	(37)	BR	36 lei .. 39 sono
  	L13	49~^.	C	47 conservare .. 51 contrario
  	L13	52^._.	M	33 medesimo .. 54 mio
  	L13	62^._-	S	42 servitio / servire .. 91 stato
  	L13	78^-_.	T	67 vero .. 87 volontà (also volontieri)
  	L13	91^^	O	57 pari .. end
  	L14	57^.	C	53 convenire .. 59 corrivo
  	L14	48~_v	P	39 potentia (verb: potere) .. 52 pretesto
  	L14	78_:	G	73 impertinente .. 83 in
  	L14	90=	PT	87 più .. 97 qualche
  	L15	83~_v	P	81 proposta .. 84 protesta
  	L15	67_-?	I	63 la .. 71 laudare
  	L15	67_.	M	65 molto .. 72 morte
  	L15	74^.	C	71 danno .. 75 deliberare
  	L15	43^:	E	34 dubbio .. 60 esperienza
  	L15	52^.	C	51 contrario .. 53 convenire
  	L15	51	A	49 animo .. 57 ardire
  	L15	64~	A	58 arme .. 70 autorità
  	L15	40^^	O	25 opinione .. 57 pari
  	L16	74^.	C	71 danno .. 75 deliberare
  	L16	(41~)	BR	39 sono .. 43 S.S.tà
  	L16	45~^.	C	44 consenso/consentire .. 47 conservare
  	L16	63~	A	58 arme .. 70 autorità
  	L16	88=	PT	87 più .. 97 qualche
  	L16	59=?	PT	56 hora .. 63 la
  	L16	15	A	10 a .. 16 accettare
  	L17	86^._-	S	42 servitio / servire .. 91 stato
  	L17	67^^_v	Q	52 ricevuta .. 76 risolutione
  	L17	42^.	C	37 conforme .. 44 consenso/consentire
  	L17	39~^.	C	37 conforme .. 44 consenso/consentire
  	L17	64	A	58 arme .. 70 autorità
  	L18	18^^	O	start .. 25 opinione
  	L18	90^.?	C	82 di .. end
  	L18	25^:	E	start .. 34 dubbio
  	L18	32^^_v	Q	29 replica / risposta .. 52 ricevuta
  	L18	35^^_v	Q	29 replica / risposta .. 52 ricevuta
  	L18	84^.	C	82 di .. end
  	L18	59~	A	58 arme .. 70 autorità
  	L18	16=	PT	start .. 25 assai
  	L18	32~^^_v	Q	29 replica / risposta .. 52 ricevuta
  	L19	93~^:	E	87 fermo .. end
  	L19	86_.	M	85 necessità .. 92 nocumento
  	L19	31	A	19 accordare .. 41 altro
  	L19	27=	PT	25 assai .. 28 che
  	L19	70~_v	P	52 pretesto .. 76 promettere
  	L19	64^^	O	57 pari .. end
  	L19	16=	PT	start .. 25 assai
  	L19	24^.	C	19 città .. 29 con
  	L19	67_.	M	65 molto .. 72 morte
  	L19	69_-	I	63 la .. 71 laudare
  	L19	67^._.	M	65 molto .. 72 morte
  	L19	64	A	58 arme .. 70 autorità
  	L20	60=	PT	56 hora .. 63 la
  	L20	30^:	E	start .. 34 dubbio
  	L20	23~^.	C	19 città .. 29 con
  	L20	94^:	E	87 fermo .. end
  	L20	83_.	M	78 mutare .. 85 necessità
  	L20	14_:	G	start .. 33 giusto
  	L20	30^:	E	start .. 34 dubbio
  	L20	(13)	BR	11 se .. 14 senza
  	L21	96_:	G	87 inclinare .. end
  	L21	54_-	I	45 intentione .. 63 la
  	L21	42~^-_.	T	26 tempo .. 55 valore
  	L21	41^^_v	Q	29 replica / risposta .. 52 ricevuta
  	L21	53^-_.	T	26 tempo .. 55 valore
  	L21	20=	PT	start .. 25 assai
```

## Open

1. A second, independent pass of the marks of lines 8-21. My pass was made with the first transcription open.
2. The brackets (33), (37), (46), (47), (13), (23), (41): no value.
3. Plain figures above 72 (98, 71?, 86, 87, 55, 64): the plain list seems to hold names after "aviso" 72 (73 Umena, 75 Savoia, 78 S. Duca, 99 Parigi).
4. My candidates need a gloss or a third context. Those with two contexts: dispositione (E 16), domanda (E 27), fine (E 89), mano (M 21), uno (T 86), molto (PT 74), anco (PT 19).
5. List Q figures 32, 35, 41, 66, 67, 79 and list O figures 10, 12, 15, 16, 18, 40: no value.
