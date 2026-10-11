# Vincenzo Badalocchio to the Duke of Nevers, Rome, 9(?) January 1593: the reading of the cipher sheet

Source: Paris, BnF, ms. français 4700, f. 80r (Gallica `btv1b90582908`, view 92, right page). Key: [key.tsv](key.tsv).
Transcription: [transcription.txt](transcription.txt), cut into groups in [groups.txt](groups.txt). State: 11 October 2026.

**This is a partial reading.** 617 of the 792 groups that are not nulls (78 %) stand in words that we translate.
Three stretches have no reading: the end of line 3, the first half of line 17, and line 18 after its first two
words. No name is read. Nothing is forced: a gap is a gap.

The work was done by a model. No palaeographer has checked it.

Marks:

- `·` = a null. `[132]` = a group with no value. `[name 117]` = a name group (the figure 1 with a dot, and two more
  figures; `.17` in the rows of groups).
- `[..]` = a gap in the sense. `(?)` or `[word?]` = doubtful. Square brackets inside a word = letters that we supply.
- In the rows "Key": a small letter = a group for one letter; CAPITALS = a group for a word or a syllable.
  `python3 decode.py` prints the same rows from the transcription and the key table.
- The figures are what we saw on the images, after three readings. The cut into groups, the values and the words
  are inferred.

## What Badalocchio tells the Duke, in five sentences

1. The troubles of the Spanish lands in Italy make an opening: the State of Milan is very ill content, and Navarre with
   two other powers (the names are not read) could hope to raise it and to take it with ease.
2. The death of a prince (name not read; the clear letter says that the King of Spain is near death) would add to this,
   but the heresy of Navarre and of another power makes such enterprises hard or impossible to carry out.
3. Navarre is not as prudent as his own good asks, because he still perseveres stubbornly in his heresy: if he had left it on
   the first day of his reign, he would now be at peace in France, with the hope of the monarchy that Cardano foretells, of
   which Badalocchio wrote in his letters of December, number 47.
4. The Duke is on the spot and has authority, so he must make the king a good and vigorous remonstrance, with reasons
   beyond those of the soul: a rising in Milan with French support, and Naples and Sicily would not(?) stay in line.
5. So fine an occasion will never come again.

Read these sentences with their limits:

- Sentences 1, 2 and 4 hold gaps. Their general sense is inferred from the words around the gaps and from the
  clear letter.
- Sentence 3 holds two gaps too ("c[..]sse", and the group 138). The words that we read are "si mostra prudente
  come disidera[r]ebbe": "shows himself prudent as one would wish". The summary takes the sentence as a reproach,
  because of the words that follow ("he still stubbornly perseveres in his heresy"). This is our view of the
  sense. The words alone do not prove it.
- The names of sentences 1 and 2 are not read.

## The Italian as running text

Ecco [132] bella ·a· che si presentasse Navara, [name 117] o [167]ro [name 138], che potrebbono spera[r] [..] di far
sole·uo·n [sollevatione?] [nel]lo stato di Milano, malissimo [..] s[odis]fatto(?), di·o [41] ivi(?) impatronirse a
facilissimamente. [.. 24 groups ..] ···

A u e n ·l· [avenendo?] la morte del [name 112], con e novi disgusto; ma la heresia del ·n [Navara?] et della [name 117]
o r·l no[n?] così belle imprese, per i tr [..] difficili, ma impossibili da esseguirsi veramente. Navara per[ò?] si mostra
prudente come disidera[r]ebbe da chi c[..]sse il ben suo, se [138] poi che pure stinatamente a persevera alla sua heresia
[166] ma i[l] quarto [..], ma[..]ente per ·u· [..]; se egli havesse lasciata il primo giorno del suo regno, sarebbe per i
tr·n [..] pacifico in Francia, ma con ra·si[145] [..] speranza che da lui nascesse rella [quella?] monarchia che predice il
Cardano dovere(?) in ·e·u· [..] nascere, della ·u [quale?] io le scrissi [39] mie lettere del giorno [xij?] di dicembre
segnate col numero di [47?].

Ella che si trova presente et con autorità, le·· a deve far una buona et gagliarda rimostranza con e così efficaci
ragioni, oltra la [..]ita del anima; et se si vedesse solevatione allo stato di Milano con l'appogio di un ·n [..] di
Francia, di·o per uolore·ae [..] che Napoli et Sicilia non(?) starebbono a segno. [.. 23 groups ..] si presentarà già mai
così bella occasi[on]e. [28 groups without sense: probably filler]

## Translation

Here is [..] a fine [occasion?], should Navarre, [name 117] or [..] [name 138] come forward, who could hope [..] to raise
[a revolt?] in the State of Milan, which is very ill [satisfied?], [..] and to make themselves masters there very easily.
[About one third of a line is not read.]

[If] the death of [name 112] [comes?], with new displeasure [..]; but the heresy of N[avarre?] and of [name 117] [..] not
such fine enterprises, [..] hard, nay impossible to carry out in truth. Navarre [however?] shows himself prudent in the way
that one would wish of a man who [knew?] his own good, [..] since he still stubbornly perseveres in his heresy, [now the
fourth (year)?] [..]. If he had left it on the first day of his reign, he would be [..] at peace in France, and with [..]
hope that from him would be born that(?) monarchy which Cardano foretells must(?) be born in [..], of which(?) I wrote to
you [in] my letters of the [12th?] day of December, marked with the number [47?].

You, who are on the spot and with authority, must make [him] a good and vigorous remonstrance with [..] reasons so
effective, beyond the [..] of the soul; and if a rising were seen in the State of Milan with the support of a [..] of
France, [..] that Naples and Sicily would not(?) stay in line. [Half a line is not read.] Never again will so fine an
occasion come.

## Line by line

For each line: the groups, the value of each group by the key, our Italian with the gaps, and English.

### Line 1

- Groups: `48 43 0 <arch> 43 6 132 83 46 89 <pi> 0 192 2 3 2 141 2 58 95 96 46 97 48 94 98 3 2 55 94 3 7 45 96 3 .17 6 167 96 6 .38 141 95 6 98 96 46 80 <pi> 83 6 94 49`
- Key: `e c · · c o [132] b e l · · LA · a · CHE · SI p r e s e n t a · SE n a u a r a [.17] o [167] r o [.38] CHE p o t r e [80] · b o n o`
- Italian: Ecco [132] bella ·a· che si presentasse Navara, [name 117] o [167]ro [name 138], che potre(b)bono
- English: Here is [..] a fine [occasion?], if Navarre, [name 117] or [..] [name 138] should come forward, who could

### Line 2

- Groups: `97 95 46 96 3 2 94 152 162 97 6 193 2 7 6 2 94 89 6 2 66 152 93 5 89 3 94 6 2 12 89 5 97 2 58 93 6 2 5 91 5 2 97 163 152 2 6 41 5 7 47 47 93 95 3 98 96 49`
- Key: `s p e r a · n DI FAR s o LE · u o · n l o · STATO DI m i l a n o · MA l i s · SI m o · i ENTE i · s FATTO DI · o [41] i u i i m p a t r o`
- Italian: spera[r?] ·n di far sole·uo·n [sollevatione?] lo stato di Milano, malissimo ·i[ente]i· s[odis]fatto [?], di·o [41] ivi [?] impatro-
- English: hope [..] to make [a rising?] in the State of Milan, [which is] very ill [satisfied?], [..] to make themselves masters there

### Line 3

- Groups: `94 5 96 97 48 2 2 3 158 143 89 5 97 2 58 2 12 93 2 91 88 3 7 2 89 .17 6 7 94 6 48 97 <0+> 0 97 46 96 143 2 96 2 2 198 48 93 7 2 96 185 <et> 157 <arch> 0 <Cn>`
- Key: `n i r s e · · a FA CI l i s · SI · MA m · ENTE h a u · l [.17] o u n o e s · · s e r CI · r · · [198] e m u · r IN [<et>] ET · · ·`
- Italian: nirse a facilissimamente. [Ha u·l [name 117] o uno esser ci·r·· [198] e m u·r in [&] et] ···
- English: very easily. [Not read: 24 groups; the passage ends with three nulls.]

### Line 4

- Groups: `3 7 46 94 2 89 0 89 45 93 6 96 98 46 85 46 89 .12 2 43 6 94 2 46 94 6 7 5 152 97 87 44 97 98 49 2 12 192 88 46 96 48 97 5 3 85 46 89`
- Key: `a u e n · l · l a m o r t e d e l [.12] · c o n · e n o u i DI s g u s t o · MA LA h e r e s i a d e l`
- Italian: A u e n ·l· [avenendo?] la morte del [name 112], con e novi disgusto; ma la heresia del
- English: [If] the death of [name 112] [comes?], with new displeasure [..]; but the heresy of

### Line 5

- Groups: `2 94 157 85 46 89 192 .17 6 96 2 89 94 6 43 6 97 5 83 48 89 193 47 93 95 96 46 97 48 2 2 92 5 98 96 152 86 5 43 47 89 5 2 12 5 93 95 6 97 2 58 0 <pi>`
- Key: `· n ET d e l LA [.17] o r · l n o c o s i b e l LE i m p r e s e · · PER i t r DI f i c i l i · MA i m p o s · SI · ·`
- Italian: ·n [Navara?] et della [name 117] o r·l no[n?] così belle imprese, per i tr [..] difficili, ma impossi-
- English: N[avarre?] and of [name 117] [..] not such fine enterprises, [..] hard, nay impossible

### Line 6

- Groups: `83 47 89 5 148 46 97 2 55 87 44 5 96 2 58 44 46 96 3 93 2 91 94 3 7 45 96 3 2 2 92 58 93 6 97 98 96 3 95 96 7 85 2 91 146 152 2 58 85 48`
- Key: `b i l i DA e s · SE g u i r · SI u e r a m · ENTE n a u a r a · · PER SI m o s t r a p r u d · ENTE COME DI · SI d e`
- Italian: bili da esseguirsi veramente. Navara per[ò?] si mostra prudente come diside-
- English: to carry out in truth. Navarre [however?] shows himself prudent as one would wish

### Line 7

- Groups: `96 3 2 94 83 <female> <pi> 83 48 148 142 2 2 2 84 97 2 55 184 135 97 7 6 2 55 138 95 6 5 141 95 7 96 48 97 98 5 94 3 98 45 93 2 91 2 3 92 55 7 46 96 3 2 2 3 89`
- Key: `r a · n b · · b e DA CHI · · · c s · SE IL BEN s u o · SE [138] p o i CHE p u r e s t i n a t a m · ENTE · a PER SE u e r a · · a l`
- Italian: ra[r]ebbe (the sheet has n for r) da chi c[..]sse il ben suo, se [138] poi che pure stinatamente a persevera al-
- English: of a man who [knew?] his own good, [..] since he still stubbornly perseveres in

### Line 8

- Groups: `192 97 7 3 88 46 96 48 97 5 3 166 12 5 99 3 96 98 6 12 91 92 2 44 2 55 156 88 3 7 46 97 2 55 192 97 43 5 3 98 45 184 95 96 5 93 6 175 152 89 97 7 6`
- Key: `LA s u a h e r e s i a [166] MA i q a r t o MA ENTE PER · u · SE EGLI h a u e s · SE LA s c i a t a IL p r i m o GIORNO DI l s u o`
- Italian: la sua heresia [166] ma i[l] quarto [anno?], ma[..]ente per ·u· [..]; se egli havesse lasciata il primo giorno del suo
- English: his heresy, [now the fourth (year)?] [..]; if he had left it on the first day of his

### Line 9

- Groups: `96 46 87 94 6 97 3 96 46 83 <Cn> 0 83 46 2 2 92 5 98 96 2 94 95 3 43 47 86 47 84 6 185 86 96 45 94 43 5 3 2 12 43 6 94 96 3 2 58 145 97 95 46`
- Key: `r e g n o s a r e b · · b e · · PER i t r · n p a c i f i c o IN f r a n c i a · MA c o n r a · SI [145] s p e`
- Italian: regno, sarebbe per i tr·n [..] pacifico in Francia, ma con ra·si[145] [..] spe-
- English: reign, he would be [..] at peace in France, and with [..] hope

### Line 10

- Groups: `96 3 94 <triangle> 3 141 148 197 94 3 97 84 46 97 2 55 96 46 89 192 93 6 94 3 96 142 3 141 95 96 46 152 43 46 184 43 45 96 85 3 94 6 154 96 46 185`
- Key: `r a n z a CHE DA LUI n a s c e s · SE r e l LA m o n a r CHI a CHE p r e DI c e IL c a r d a n o DOVE r e IN`
- Italian: ranza che da lui nascesse rella [quella?] monarchia che predice il Cardano dovere [?] in
- English: that from him would be born that(?) monarchy which Cardano foretells must(?)

### Line 11

- Groups: `2 46 2 7 2 94 3 97 43 46 96 48 85 46 89 192 2 44 188 193 97 43 96 5 97 2 58 2 39 93 5 48 193 98 48 96 46 85 46 89 175 <frame_?ij> 152 152 43 46`
- Key: `· e · u · n a s c e r e d e l LA · u IO LE s c r i s · SI · [39] m i e LE t e r e d e l GIORNO [<frame_?ij>] DI DI c e`
- Italian: ·e·u· [..] nascere, della ·u [quale?] io le scrissi [39] mie lettere del giorno [xij? or xxij] di dice-
- English: be born in [..], of which(?) I wrote to you [in/with] my letters of the [12th? or 22nd] day of Decem-

### Line 12

- Groups: `93 83 96 48 97 46 87 94 3 98 46 43 6 89 94 7 93 46 96 6 152 <frame_47> 46 89 192 141 2 58 98 96 6 7 3 95 96 46 97 2 91 157 43 6 94 <Cn> 0`
- Key: `m b r e s e g n a t e c o l n u m e r o DI [<frame_47>] e l LA CHE · SI t r o u a p r e s · ENTE ET c o n · ·`
- Italian: mbre segnate col numero di [47?]. Ella che si trova presente et con
- English: ber, marked with the number [47?]. You, who are on the spot and with

### Line 13

- Groups: `45 7 98 6 96 5 98 3 193 2 2 3 85 46 7 48 162 7 94 3 83 7 6 94 45 157 87 3 87 89 5 3 96 85 3 96 5 93 6 97 98 96 3 94 <triangle> 3 84 49 94 2 46`
- Key: `a u t o r i t a LE · · a d e u e FAR u n a b u o n a ET g a g l i a r d a r i m o s t r a n z a c o n · e`
- Italian: autorità, le·· a [gliela?] deve far una buona et gagliarda rimostranza con e [?]
- English: authority, must make [him] a good and vigorous remonstrance, with

### Line 14

- Groups: `43 6 97 5 46 86 0 <pi> 86 5 43 45 84 5 96 3 87 47 6 94 5 49 89 98 96 3 192 2 3 91 5 2 98 3 85 46 89 3 94 5 93 3 157 2 55 2 58 7 46 85 48`
- Key: `c o s i e f · · f i c a c i r a g i o n i o l t r a LA · a ENTE i · t a d e l a n i m a ET · SE · SI u e d e`
- Italian: così efficaci ragioni, oltra la ·a[ente]i·ta [..] del anima; et se si vede-
- English: reasons so effective, beyond the [..] of the soul; and if one saw

### Line 15

- Groups: `97 2 55 97 6 89 46 7 3 98 5 6 94 46 2 2 3 89 6 2 66 152 93 5 89 3 94 6 43 6 94 89 3 95 0 <0+> 95 6 87 5 6 152 7 94 2 94 152 86 96 3 94 43 5 3 0 <Cn>`
- Key: `s · SE s o l e u a t i o n e · · a l o · STATO DI m i l a n o c o n l a p · · p o g i o DI u n · n DI f r a n c i a · ·`
- Italian: sse solevatione allo stato di Milano con l'appogio di un ·n [..] di Francia,
- English: a rising in the State of Milan with the support of a [..] of France,

### Line 16

- Groups: `152 2 6 92 7 6 89 6 96 46 2 45 48 141 94 3 95 6 89 5 157 97 5 84 47 89 5 3 2 29 97 98 3 96 46 83 0 <pi> 83 6 94 49 3 97 48 87 94 6`
- Key: `DI · o PER u o l o r e · a e CHE n a p o l i ET s i c i l i a · NON s t a r e b · · b o n o a s e g n o`
- Italian: di·o per uolore·ae [..] che Napoli et Sicilia non [?] starebbono a segno.
- English: [..] that Naples and Sicily would not(?) stay in line.

### Line 17

- Groups: `2 3 98 95 2 12 89 5 2 7 49 3 48 94 98 5 152 2 6 47 5 7 152 6 97 3 2 45 2 58 95 96 48 97 46 94 98 3 96 45 87 5 3 2 12 5 43 49 97 47`
- Key: `· a t p · MA l i · u o a e n t i DI · o i i u DI o s a · a · SI p r e s e n t a r a g i a · MA i c o s i`
- Italian: [·atp· ma li·uoaenti di·o iiu di osa·a·] si presentarà già mai così
- English: [Not read: 23 groups] ... will never again so

### Line 18

- Groups: `83 46 89 192 6 43 <Cn> 0 <arch> 84 3 2 5 ? 6 2 2 3 199 141 7 199 0 7 0 100 0 12 2 133 49 5 7 7 194 92 83 6 5 181 5 3 5 7 3 95 5 .78 43 0`
- Key: `b e l LA o c · · · c a · i [?] o · · a [199] CHE u [199] · u · [100] · MA · [133] o i u u [194] PER b o i [181] i a i u a p i [.78] c ·`
- Italian: bella occasi[on]e. [·· a [199] che u [199] ·u· [100] · ma · [133] o i u u [194] per b o i [181] i a i u a p i [name 178] c ·]
- English: fine an occasion come. [28 groups without sense to the end of the sheet: probably filler.]

## Counts, line by line

"Groups" = the groups that are not nulls. "In sense" = the groups in words that we translate. We counted them by
hand.

| Line | Groups | In sense | | Line | Groups | In sense |
|---|---|---|---|---|---|---|
| 1 | 44 | 36 | | 10 | 45 | 38 |
| 2 | 49 | 31 | | 11 | 40 | 35 |
| 3 | 39 | 19 | | 12 | 41 | 40 |
| 4 | 43 | 36 | | 13 | 48 | 45 |
| 5 | 45 | 34 | | 14 | 45 | 40 |
| 6 | 43 | 42 | | 15 | 47 | 46 |
| 7 | 44 | 40 | | 16 | 43 | 32 |
| 8 | 50 | 38 | | 17 | 43 | 20 |
| 9 | 44 | 35 | | 18 | 39 | 10 |

All: 919 groups; 127 nulls; 792 other groups; 894 groups have a value (97.3 %); 25 groups have no value.
**617 of 792 (78 %) stand in words that we translate.** Without the 28 groups at the end of line 18, which are
probably filler, it is 81 %.

One count does not agree with the text above. The table has 19 groups "in sense" for line 3. The text of line 3
says that 24 of its 39 groups are not read, and this leaves 15. We give the table as the reader made it. With 15
for line 3, the total is 613 of 792 (77 %).

## What is not read

- Line 3 after "facilissimamente": 24 groups, and three nulls that end the passage.
- Line 17, the first half: 23 groups.
- Line 18 after "bella occasi[on]e": 28 groups without sense, to the end of the sheet. They are probably filler.
- Short gaps in lines 1, 2, 4, 5, 8, 9, 11, 14 and 16.
- The four names: 117 (three times), 112, 138 and 178.
- The letter n after a null, in five places: "spera·n", "uo·n", "·n et", "tr·n", "un ·n".
- The number in the frame of line 11 (xij or xxij), and the first figure of the number in the frame of line 12
  (47, with a blotted 4).
