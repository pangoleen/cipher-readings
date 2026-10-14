# Vincenzo Badalocchio to the Duke of Nevers, Rome, 5 December 1592: the reading of the letter with cipher (f. 85r)

Source: Paris, BnF, ms. français 4700, f. 85r (Gallica `btv1b90582908`, view 97, right page). Key: [../key.tsv](../key.tsv).
Transcription: [transcription.txt](transcription.txt), with its cipher runs cut into groups in [groups.txt](groups.txt).
State: 11 October 2026, after the audit; corrected on 14 October 2026 after a review panel (fills now marked;
line 24 "because"; the count of full sentences; the spaces of lines 10 and 25).

A letter in Badalocchio's own hand: 28 lines and the signature. 17 lines have figures. Clear Italian and cipher alternate
in the same sentences.

**The cipher parts of the letter are read, with gaps.** 361 of the 383 cipher groups that carry text (94 %, a hand
count) stand in words that we translate. All 11 cipher runs join the clear words around them. **Not read:** the seven
name groups (five names: we give numbers), one word in line 11, one group in line 12, the verb of line 13, three short
doubts (line 8, line 23, the sign P of line 25), and the groups 199 and 299 (seven places).

The work was done by a model. No palaeographer has checked it. The clear words are one reading from tiles. They are not
an edition.

Marks:

- In the Italian lines, **bold** = from cipher; plain = clear on the page.
- `·` = a null. `[199]` = a group with no value. `[2]` = a lone 2: open. `[nome 143]` = a name group (the dotted stroke
  and three figures; `.143` in the rows of groups). The key has no value for a name: see the table of names in the
  [README](../README.md).
- `[..]` = a gap in the sense. `(?)` or `[word?]` = doubtful. Square brackets inside a word = letters as the page has
  them, or letters that we supply.
- In the rows "key": a small letter = a group for one letter; CAPITALS = a group for a word or a syllable; a word with
  `?` = a value that is a guess. `python3 ../decode.py` prints the same rows.
- The figures and the clear words are what we saw on the images. The cut into groups, the values and the words are
  inferred.

## What the letter says, in five sentences

1. Cardinal Sforza is expected in Rome in six or eight days. He comes to treat the matters that [name 143] was to treat,
   at the instance of [name 124], who helps the business with great force.
2. The business does not please Spain. The Spaniards want [name 195] as Queen of France and say boldly that the crown
   belongs to her. Badalocchio does not believe that this "claimed right" will find the doors open as it did in Portugal.
3. As he understands it, the business is to make [name 128] King of France. The verb of this sentence is not read.
   Spain dislikes the plan. If the Spaniards could, they would stop the coming of Sforza as they stopped that of
   [name 143].
4. On Sunday 29 November (the first of Advent) he gave the Duke's letter to the Pope. The Pope received him the next day
   and spoke with affection of the Duke, whom he knew from the legation of Cardinal Alessandrino. But the Pope much
   desires that the Duke withdraw from Navarre.
5. Badalocchio answered with the wrongs done to the Duke by the other side, and that there was no clear way to withdraw.
   They spoke of the way that Capilupi proposed. It did not displease. The Pope took time and will call him again.

Sentences 1 to 3 are in lines 4 to 17 (cipher and clear). Sentences 4 and 5 are in lines 17 to 26 (clear, with cipher in
lines 22 to 25). The names are numbers in the cipher. Our guesses are graded in the README: [name 195] is the Infanta
of Spain (settled as a person); [name 143] is probably Cardinal Gondi; [name 124] is probably the Grand Duke of Tuscany;
[name 144] is probably the word "Cardinale"; [name 128] is open.

## The transcription: two passes and the settled text

- [pass_a.txt](pass_a.txt): the first reader. It tried values while it read. So pass A is not blind to the sense.
- [pass_b_blind.txt](pass_b_blind.txt): a separate agent. It had only the tiles and the rules of transcription.
- [transcription.txt](transcription.txt): the settled text. Its base is pass B.

| | Figures and signs | The same as the settled text |
|---|---|---|
| Pass A | 949 | 909 (97.3 %) |
| Pass B (blind) | 920 | 916 (99.6 %) |
| Pass A against pass B | | 906 the same (97.0 %) |

The percent is 2 x the same / the sum of the two counts. `python3 ../decode.py` counts them again. Pass A has 29 figures
too many: the first reader counted a figure two times where two strips of its notes join. Pass B has the right count
in each of these places.

The settled text differs from pass B in four places of figures. We looked at the enlarged tile again for each one:

| Line | Pass B | Settled | What the tile shows | What guided the choice |
|---|---|---|---|---|
| 5 | 3(8)(5)7859 | 38(5)(1)859 | 8, a blot with a long flag (5), a stroke under the flag (1 or 7), 8 5 | The sense: 85 185 gives "ad in-" (a d IN stanze). The stroke is 1 or 7 on the image |
| 13 | 0226 0 239 | 02276 0 239 | after "229 0": two 2, then 7 and 6 (as pass A has it) | The image; then 276 = va |
| 11 | 5797(1) + a word | 5797 + truovi | the stroke after 5797 is the first letter of the clear word "truovi" | The image |
| 22 | 9 `<sign like T, or a 7>` | 97 | a bar with one stem | The sense: 97 = s (ritiras··s·e) |

So **figures were settled by the sense, not by the image alone.** The audit counts all four places so. The notes of the
reader give the sense as the guide in lines 5 and 22, and the image in lines 11 and 13. We also left out a point in
line 10 that is film dirt.

Places where the image stays unsure (kept as seen):

- Line 8: "4 5 8 6 7 9 7". The 86 is clear. The sense asks for 87 ("a gusto").
- Line 11: "4 (8) 6 9 7 9 8 0 5". The 8 is faint. With 43 the word is "costì".
- Line 12: "6 (1) 6 9". A blot is on the 1.
- Line 13: "1 5 2 1 1 6 9". One stroke too many before 169. Lines 8 and 10 have "152 169".
- Line 13: the name "0 i 1 2 8". Pass B saw the dot of the stroke. The first reader does not see it on its enlargement.
- Line 22: "9 4 3 7 4 5 0 3 0" (n a u a · a). The r of "Navara" is not there.
- Line 15: "2 4 7" (pass B) against "2 9 4 4" (pass A). The two forms are close.
- Line 13: the group after "si" is 2 8 9 on the tile. The audit looked at it again.

## The Italian as running text

Bold = from cipher.

Questa settimana per corriero spedito dall'Alt.a di Ferrara, si sa la morte del Car.le Canano in Modena, dove era
Vescovo, con in pochi giorni S. Alt.a ha per morte perduto le due persone, delle quali più si valeva, et nelle quali
più confidava i suoi negotij più importanti, ch'erano questo Car.le et il Vescovo di Reggio morto pure pochi mesi
sono.

Qui si aspetta fra pochi giorni, come fra sei, o vero otto, l'Ill.mo et R.mo S.or Car.le Sforza, quale per quanto
intendo **vien a trattare le cose che dovea trattare il [nome 143], et vien ad instanze del [nome 124], qual aiuta il
negotio gagliardessimamente; il qual negotio, per quello intendo e mi pare verisimile, non è punto a [f u s t] di
Spagna, qual vogli[o]no far la [nome 195] regina di Francia,** ne si spaventano punto [199] di pericolo di morte, di
prigionia, di minaccie, ne di cosa [299] di dire, anzi affermano arditamente **la corona di Francia appartenersi a
detta [nome 195];** ma io non credo che **quel(?) loro pretenso ius** truovi **[e o s t i]** le porte aperte **come
fece in Portogallo [169].** Creda V. Ecc. Ill.ma quello che le piace, [299] che questo negotio, secondo che io lo
intendo, **è che si [289] far [nome 128] re di [1] Francia,** la qual cosa, come ho detto, **non [2] va per la
fantasia punto a Spagna, per la ragione detta;** et se così potessero **impedire la venuta del [nome 144] Sforza, come
hanno impedita quell[a] di [nome 143],** non ci si [199] intende cosa che importi se non [299] risparmiarebbono più(?);
ma bisogna vedere come ci si [199] adoperare tutto quello che si può, per che no[n] si [299] risolveranno dopo.

Diedi domenica prossima passata a N.S. la lettera di V. Ecc. Ill.ma mentre S.S.tà tornava alle sue stanze della
capella, che s'era fatta la prima dell'advento, et mi ordinò che tornasse da lei il giorno seguente doppo mangiare,
come feci, et mostrò molta amorevolezza verso V. Ecc. Ill.ma, con la quale disse esser stata cosa molto amorevolmente,
quando ci fu con l'Ill.mo et R.mo S. Car.le Alessandrino Legato, et perciò le porta affettione: ma **ha [2] molto
disiderio che ella si ritirasse dal Nava[r]a,** sopra di che **risposi [f i] torti et gli aggravi fattoli dall'altra
parte, per che non si vedeva così ben il modo di ritirarsi di q[u]a.** Si parlò **del modo proposto da [segno P]
Capolupo,** che non dispiaque; si tolse tempo a pensarci, et che sarei chiamato, et ordinatomi quello che dovessi
scrivere per risposta: non lasciarò di raccordare destramente il negotio, et di tutto la farò avisata minutamente. Le
bascio humiliss.te le mani, et le prego da N.S. Dio ogni contento, et felicità. In Roma: il dì v. di Dicembre. MDXCII.

## Translation

This week, by a courier of the Duke of Ferrara, we know that Cardinal Canano died at Modena, where he was bishop. In a
few days the Duke has lost the two men whom he used most for his most important affairs: this Cardinal, and the Bishop
of Reggio, who died a few months ago.

Cardinal Sforza is expected here in six or eight days. As far as I hear, he comes to treat the matters that [name 143]
was to treat, and he comes at the instance of [name 124], who helps the business with great force. From what I hear,
and it seems likely to me, this business is not at all to the [taste?] of Spain. The Spaniards want to make [name 195]
Queen of France. They are not afraid of danger of death, of prison, of threats, or of anything that is said. They
assert boldly that the crown of France belongs to the said [name 195]. But I do not believe that this claimed right of
theirs will find the doors open [..] as it did in Portugal [..]. Your Excellency may believe what you please: this
business, as I understand it, is that [the verb is not read] to make [name 128] King of France. As I said, this is not
at all to the liking of Spain, for the reason given. If they could prevent the coming of [name 144] Sforza, as they
prevented that of [name 143], [one clear clause that we do not translate with confidence]. But we must see how to use
all that can be used, because they will not decide later.

Last Sunday I gave Our Lord your letter, while His Holiness went back to his rooms from the chapel for the first
Sunday of Advent. He ordered me to come back the next day after dinner, as I did. He showed much kindness towards Your
Excellency: he said that things were very kind between you when he was there with Cardinal Alessandrino, the Legate,
and for this he has affection for you. But he much desires that you withdraw from Navarre. To this I answered [..] the
wrongs and the injuries done to you by the other side, because one did not see so well the way to withdraw from here. We
spoke of the way that [sign P] Capilupi proposed. It did not displease. He took time to think, [and said] that I would
be called and told what to write in answer. I shall recall the business with tact and tell you all in detail. I most
humbly kiss your hands. Rome, 5 December 1592.

## Line by line

For each line: the page as transcribed; for each cipher run, its groups and the value of each group by the key; our
Italian; English.

### Line 1

- Page: `Questa settimana per corriero spedito dall'Alt.a di Ferrara, si sa la morte del Car.le Canano in Modena, dove era Vescovo, con in`
- Italian: Questa settimana per corriero spedito dall'Alt.a di Ferrara, si sa la morte del Car.le Canano in Modena, dove era Vescovo, con in
- English: This week, by a courier that His Highness of Ferrara sent, we know of the death of Cardinal Canano at Modena, where he was bishop; so in

### Line 2

- Page: `pochi giorni S. Alt.a ha per morte perduto le due persone, delle quali più si valeva, et nelle quali più confidava i suoi`
- Italian: pochi giorni S. Alt.a ha per morte perduto le due persone, delle quali più si valeva, et nelle quali più confidava i suoi
- English: a few days His Highness has lost by death the two persons whom he used most and to whom he most entrusted his

### Line 3

- Page: `negotij più importanti, ch'erano questo Car.le et il Vescovo di Reggio morto pure pochi mesi sono:`
- Italian: negotij più importanti, ch'erano questo Car.le et il Vescovo di Reggio morto pure pochi mesi sono:
- English: most important affairs: this Cardinal, and the Bishop of Reggio, who also died a few months ago.

### Line 4

- Page: `Qui si aspetta fra pochi giorni, come fra sei, o vero otto l'Ill.mo et R.mo S.or Car.le Sforza, quale per quanto intendo`
- Italian: Qui si aspetta fra pochi giorni, come fra sei, o vero otto l'Ill.mo et R.mo S.or Car.le Sforza, quale per quanto intendo
- English: Here we expect in a few days, six or eight, the Most Illustrious and Most Reverend Cardinal Sforza, who, as far as I hear,

### Line 5

- Page: `2780302740294193084697048<0+>14115403<pi>274<lambda>2940184<Cn>i143489827838(5)(1)859798394<triangle>4(8)`
- Run 5.1, groups: `278 0 3 0 274 0 294 193 0 84 6 97 0 48 <0+> 141 154 0 3 <pi> 274 <lambda> 294 0 184 <Cn> .143 48 98 278 3 85 185 97 98 3 94 <triangle> 48`
- Run 5.1, key: `VIEN · a · TRATTA · RE LE · c o s · e · CHE DOVE · a · TRATTA · RE · IL · [.143] e t VIEN a d IN s t a n z e`
- Italian: **vien a trattare le cose che dovea trattare il [nome 143], et vien ad instanze**
- English: comes to treat the matters that [name 143] was to treat, and comes at the instance

### Line 6

- Page: `8546890i124244035798450184<female>2238769856087450(8)708953968546970<Cn>9747934509346949846`
- Run 6.1, groups: `85 46 89 0 .124 244 0 3 5 7 98 45 0 184 <female> 223 87 6 98 5 6 0 87 45 0 87 0 89 5 3 96 85 46 97 0 <Cn> 97 47 93 45 0 93 46 94 98 46`
- Run 6.1, key: `d e l · [.124] QUAL · a i u t a · IL · NE g o t i o · g a · g · l i a r d e s · · s i m a · m e n t e`
- Italian: **del [nome 124], qual aiuta il negotio gagliardessimamente;**
- English: of [name 124], who helps the business with great force;

### Line 7

- Page: `018424409446(8)7698050623924701859828904821409539648<0+>748965974(7)93508946022948`
- Run 7.1, groups: `0 184 244 0 94 46 87 6 98 0 5 0 6 239 247 0 185 98 289 0 48 214 0 95 3 96 48 <0+> 7 48 96 5 97 47 93 5 0 89 46 0 229 48`
- Run 7.1, key: `· IL QUAL · n e g o t · i · o PER QUELLO · IN t ENDO · e MI · p a r e · u e r i s i m i · l e · NON e`
- Italian: **il qual negotio, per quello intendo e mi pare verisimile, non è**
- English: and this business, from what I hear and as seems likely to me, is not

### Line 8

- Page: `<Cn>9579498604586797098<0+>152026402442869460162<female>893i1950964887594301520169 ne si spa=`
- Run 8.1, groups: `<Cn> 95 7 94 98 6 0 45 86 7 97 0 98 <0+> 152 0 264 0 244 286 94 6 0 162 <female> 89 3 .195 0 96 48 87 5 94 3 0 152 0 169`
- Run 8.1, key: `· p u n t o · a f u s · t · DI · SPAGNA · QUAL VOGLI n o · FAR · l a [.195] · r e g i n a · DI · FRANCIA`
- Italian: **punto a [f u s t] di Spagna, qual vogli[o]no far la [nome 195] regina di Francia,** ne si spa-
- English: at all to the [taste?] of Spain: they want to make [name 195] Queen of France, and they are not

### Line 9

- Page: `uentano punto 199 di pericolo di morte, di prigionia, di minaccie, ne di cosa 299 di dire, anzi affer=`
- Italian: ventano punto [199] di pericolo di morte, di prigionia, di minaccie, ne di cosa [299] di dire, anzi affer-
- English: at all afraid of danger of death, of prison, of threats, or of anything that is said; no, they

### Line 10

- Page: `mano arditamente 192084696499431521690395095<female>4596984694489697504501 49i1950 ma io non credo`
- Run 10.1, groups: `192 0 84 6 96 49 94 3 152 169 0 3 95 0 95 <female> 45 96 98 46 94 48 96 97 5 0 45 0 149 .195 0`
- Run 10.1, key: `LA · c o r o n a DI FRANCIA · a p · p · a r t e n e r s i · a · DETTA [.195] ·`
- Italian: mano arditamente **la corona di Francia appartenersi a detta [nome 195];** ma io non credo
- English: assert boldly that the crown of France belongs to the said [name 195]. But I do not believe

### Line 11

- Page: `che 2460896964909596469848094976<0+>5797 truovi 4(8)6979805 le porte aperte 1461641850956(9)60`
- Run 11.1, groups: `246 0 89 6 96 49 0 95 96 46 98 48 0 94 97 6 <0+> 5 7 97`
- Run 11.1, key: `QUEL? · l o r o · p r e t e · n s o · i u s`
- Run 11.2, groups: `48 6 97 98 0 5`
- Run 11.2, key: `e o s t · i`
- Run 11.3, groups: `146 164 185 0 95 6 96 0`
- Run 11.3, key: `COME FECE IN · p o r ·`
- Italian: che **quel(?) loro pretenso ius** truovi **[e o s t i]** le porte aperte **come fece in Por-**
- English: that this claimed right of theirs will find the doors open [..] as it did in Por-

### Line 12

- Page: `98490873890<Cn>89<0+>6(1)69 creda V. Ecc. Ill.ma quello che le piace 299 che questo negotio, secondo che io lo`
- Run 12.1, groups: `98 49 0 87 3 89 0 <Cn> 89 <0+> 6 169`
- Run 12.1, key: `t o · g a l · · l · o FRANCIA`
- Italian: **togallo [169].** Creda V. Ecc. Ill.ma quello che le piace, [299] che questo negotio, secondo che io lo
- English: tugal [..]. Your Excellency may believe what you please: this business, as I

### Line 13

- Page: `intendo 480141025828901620i128<Cn>96481521169 la qual cosa come ho detto 229022760239<0+>19286394`
- Run 13.1, groups: `48 0 141 0 258 289 0 162 0 .128 <Cn> 96 48 152 1 169`
- Run 13.1, key: `e · CHE · SI ENDO · FAR · [.128] · r e DI [1] FRANCIA`
- Run 13.2, groups: `229 0 2 276 0 239 <0+> 192 86 3 94`
- Run 13.2, key: `NON · [2] VA · PER · LA f a n`
- Italian: intendo, **è che si [289] far [nome 128] re di [1] Francia,** la qual cosa, come ho detto, **non [2] va per la fan-**
- English: understand it, is that [the verb is not read] to make [name 128] King of France; and this, as I said, is not at all to the

### Line 14

- Page: `<female>98397530957949860452640239192096387569446149 et se cosi potessero 5(9)3954885509646192<Cn>0`
- Run 14.1, groups: `<female> 98 3 97 5 3 0 95 7 94 98 6 0 45 264 0 239 192 0 96 3 87 5 6 94 46 149`
- Run 14.1, key: `· t a s i a · p u n t o · a SPAGNA · PER LA · r a g i o n e DETTA`
- Run 14.2, groups: `5 93 95 48 85 5 0 96 46 192 <Cn> 0`
- Run 14.2, key: `i m p e d i · r e LA · ·`
- Italian: **tasia punto a Spagna, per la ragione detta;** et se così potessero **impedire la**
- English: liking of Spain, for the reason given. And if in the same way they could prevent the

### Line 15

- Page: `7469479830854689i144097860696<triangle>450146<0+>883940946059395046850598302470152i143 non ci si`
- Run 15.1, groups: `7 46 94 7 98 3 0 85 46 89 .144 0 97 86 0 6 96 <triangle> 45 0 146 <0+> 88 3 94 0 94 6 0 5 93 95 0 46 85 0 5 98 3 0 247 0 152 .143`
- Run 15.1, key: `u e n u t a · d e l [.144] · s f · o r z a · COME · h a n · n o · i m p · e d · i t a · QUELLO · DI [.143]`
- Italian: **venuta del [nome 144] Sforza, come hanno impedita quell[a] di [nome 143],** non ci si
- English: coming of [name 144] Sforza, as they prevented that of [name 143], one does not

### Line 16

- Page: `199 intende cosa che importi se non 299 risparmiarebbono piu(?), ma bisogna uedere come ci si 199`
- Italian: [199] intende cosa che importi se non [299] risparmiarebbono più(?), ma bisogna vedere come ci si [199]
- English: hear of a thing of weight that they would spare(?); but we must see how to

### Line 17

- Page: `adoperare tutto quello, che si può per che no si 299 risolueranno dopo: Diedi domenica prossima passata`
- Italian: adoperare tutto quello, che si può, per che no[n] si [299] risolveranno dopo: Diedi domenica prossima passata
- English: use all that can be used, because they will not decide later. Last Sunday I gave

### Line 18

- Page: `a N.S. la lettera di V. Ecc. Ill.ma mentre S.S.tà tornava alle sue stanze della capella, che s'era fatta la`
- Italian: a N.S. la lettera di V. Ecc. Ill.ma mentre S.S.tà tornava alle sue stanze della capella, che s'era fatta la
- English: Our Lord [the Pope] Your Excellency's letter, while His Holiness went back to his rooms from the chapel that was held for the

### Line 19

- Page: `prima dell'advento, et mi ordinò che tornasse da lei il giorno seguente doppo mangiare, come feci, et`
- Italian: prima dell'advento, et mi ordinò che tornasse da lei il giorno seguente doppo mangiare, come feci, et
- English: first [Sunday] of Advent; and he ordered me to come back to him the next day after dinner, as I did, and

### Line 20

- Page: `mostrò molta amorevolezza verso V. Ecc. Ill.ma con la quale disse esser stata cosa molto amorevol=`
- Italian: mostrò molta amorevolezza verso V. Ecc. Ill.ma con la quale disse esser stata cosa molto amorevol-
- English: he showed much kindness towards Your Excellency, with whom, he said, things were very kind

### Line 21

- Page: `mente, quando ci fu con l'Ill.mo et R.mo S. Car.le Alessandrino Legato, et perciò le porta affettione: ma`
- Italian: mente, quando ci fu con l'Ill.mo et R.mo S. Car.le Alessandrino Legato, et perciò le porta affettione: ma
- English: when he was there with Cardinal Alessandrino, the Legate, and for this he has affection for you: but

### Line 22

- Page: `1772221015225808546960560141<0+>4889089325809659847963970<female>97<Cn>46148890943745030`
- Run 22.1, groups: `177 2 221 0 152 258 0 85 46 96 0 5 6 0 141 <0+> 48 89 0 89 3 258 0 96 5 98 47 96 3 97 0 <female> 97 <Cn> 46 148 89 0 94 3 7 45 0 3 0`
- Run 22.1, key: `HA [2] MOLTO · DI SI · d e r · i o · CHE · e l · l a SI · r i t i r a s · · s · e DA l · n a u a · a ·`
- Italian: **ha [2] molto disiderio che ella si ritirasse dal Nava[r]a,**
- English: he much desires that you withdraw from Navarre;

### Line 23

- Page: `sopra di che 965979560970508650986960980501570878950387<female><0+>8709637501638950148890<female><0+>`
- Run 23.1, groups: `96 5 97 95 6 0 97 0 5 0 86 5 0 98 6 96 0 98 0 5 0 157 0 87 89 5 0 3 87 <female> <0+> 87 0 96 3 7 5 0 163 89 5 0 148 89 0 <female> <0+>`
- Run 23.1, key: `r i s p o · s · i · f i · t o r · t · i · ET · g l i · a g · · g · r a u i · FATTO l i · DA l · · ·`
- Italian: sopra di che **risposi [f i] torti et gli aggravi fattoli dal-**
- English: to which I answered [..] the wrongs and the injuries done to you by

### Line 24

- Page: `389989630238023914122925804446854873084625801350184219152096598479639609750`
- Run 24.1, groups: `3 89 98 96 3 0 238 0 239 141 229 258 0 44 46 85 48 7 3 0 84 6 258 0 135 0 184 219 152 0 96 5 98 47 96 3 96 0 97 5 0`
- Run 24.1, key: `a l t r a · PARTE · PER CHE NON SI · u e d e u a · c o SI · BEN · IL MODO DI · r i t i r a r · s i ·`
- Italian: **l'altra parte, per che non si vedeva così ben il modo di ritirarsi**
- English: the other side, because one did not see so well the way to withdraw

### Line 25

- Page: `15209930 si parlò 854889219<Cn>95960609549979849014 8<P>8439560897095049, che non dispiaque`
- Run 25.1, groups: `152 0 99 3 0`
- Run 25.1, key: `DI · q a ·`
- Run 25.2, groups: `85 48 89 219 <Cn> 95 96 0 6 0 95 49 97 98 49 0 148 <P> 84 3 95 6 0 89 7 0 95 0 49`
- Run 25.2, key: `d e l MODO · p r · o · p o s t o · DA [<P>] c a p o · l u · p · o`
- Italian: **di q[u]a.** Si parlò **del modo proposto da [segno P] Capolupo,** che non dispiaque
- English: from this side. We spoke of the way that [sign P] Capilupi proposed, which did not displease;

### Line 26

- Page: `si tolse tempo a pensarci, et che sarei chiamato, et ordinatomi quello che dovessi scrivere per risposta: non`
- Italian: si tolse tempo a pensarci, et che sarei chiamato, et ordinatomi quello che dovessi scrivere per risposta: non
- English: he took time to think about it, [and said] that I would be called and told what to write in answer. I

### Line 27

- Page: `lasciarò di raccordare destramente il negotio, et di tutto la farò avisata minutamente: le bascio humiliss.te`
- Italian: lasciarò di raccordare destramente il negotio, et di tutto la farò avisata minutamente: le bascio humiliss.te
- English: shall not fail to recall the business with tact, and I shall tell you all in detail. I most humbly kiss

### Line 28

- Page: `le mani, et le prego da N.S. Dio ogni contento, et felicità: In Roma: il dì v. di Dicembre. MDXCII`
- Italian: le mani, et le prego da N.S. Dio ogni contento, et felicità: In Roma: il dì v. di Dicembre. MDXCII
- English: your hands and pray Our Lord God for your every content and happiness. Rome, 5 December 1592.

### Line 29

- Page: `D.V. Ecc.ia Ill.ma / Humiliss.o e devotiss.o S.re / Vincenzio Badalocchio`
- Italian: D.V. Ecc.ia Ill.ma / Humiliss.o e devotiss.o S.re / Vincenzio Badalocchio
- English: Your Excellency's most humble and devoted servant, Vincenzio Badalocchio

## Counts

- The cipher runs have 520 groups. 135 are nulls (the figure 0 and five signs). 2 are a lone 2: open; the count
  takes them as nulls. So 383 groups carry text.
- Of these, 374 have a value by the key, 7 are name groups, and 2 have no value (a lone 1 in line 13, and the sign P).
- **361 of 383 (94.3 %) stand in words that we translate.** This is a hand count by the first reader. The list of the
  22 groups that are out is in `../decode.py` (NOT_IN_SENSE): 7 name groups; "f u s t" (4 groups, line 8); "e o s t i"
  (5, line 11); 169 in line 12; 289 and the lone 1 in line 13; "f i" (2, line 23); the sign P (line 25).
- Seven more groups stand alone between clear words: 199 (three times) and 299 (four times). They have no value. If
  they count as not read, the share is 361 of 390 (92.6 %).
- "Groups with a value" proves little. A shuffled key gives a value to the same groups.

## The cipher runs and their clear sentences

The page has 11 cipher runs between clear words (a run can go over a line end). All 11 join the clear words at both
ends. 8 of the 11 make a full sentence with them (the names stay numbers). One more, in line 13, makes sense, but its
verb is not read ("si [289] far"). 2 do not: the run "e o s t i" in line 11, and the run "come fece in Portogallo
[169]" in lines 11 and 12, where the last group has no place in the sentence. Two of the 8 have a doubt inside:
"f u s t" (line 8) and "f i" (line 23). This is the
judgement of the reader. The key and the cut of the first page gave no complete run on this page.

## What is not read

1. The names: [nome 143] (lines 5 and 15), [nome 124] (line 6), [nome 195] (lines 8 and 10), [nome 128] (line 13),
   [nome 144] (line 15).
2. Line 8: "a f u s t". "a gusto" asks for 87 where the page has 86, and for an o.
3. Line 11: "e o s t i". With 43 for the faint 48 it is "costì".
4. Line 12: the group 169 after "Portogallo". 169 = Francia fits its three other places. Here it makes no sense, and
   a blot is on the figure before it.
5. Line 13: the verb. The page has "si" + 289 + "far". The value "endo" of 289 fits four other places and fails here.
   The sense asks for a verb like "s'intende". A lone 1 stands before 169 in the same line.
6. Line 15: "impedita QUELLO di": the sense asks for "quella". We take 247 as the stem for both.
7. Line 22: "Nava·a" for "Navara"; a lone 2 between "ha" and "molto".
8. Line 23: "f i" before "torti". With 89 for 86 it is "li torti".
9. Line 25: the sign P before "Capolupo". It can be a title. It is not read.
10. The groups 199 and 299 (seven places). A null is our best guess. "come ci si [199] adoperare" speaks against it.
11. Lines 16 and 17 are clear, but our reading of the small words is one reading ("più" or "però"; "adoperare").
12. The sign lambda in line 5: a null by its place.
13. Line 8: the key gives "VOGLI n o", that is "voglino". We read "vogli[o]no". With "voglio" for the group 286 the
    word is exact. That value is not in the key: the group has one place.

## Notes of 14 October 2026

- Lines 10 and 25: the settled rows have a space inside the groups 149 (detta, line 10) and 148 (da, line 25). The
  cut joins the figures across the space. The blind pass B has no space in these places.
- Letters in square brackets are letters that the groups do not give: "vogli[o]no" (line 8), "quell[a]" (line 15,
  the group 247 = quello), "q[u]a" (line 25). "aggravi" (line 23) has one i, as the groups give it.
