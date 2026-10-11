# BnF Espagnol 318 no. 93: machine decode, line by line

Made by `decode.py` with `key.py` (state of 11 October 2026). Nothing is edited. The edited reading with the English
translation is in `READING.md`.

- CAPITALS = code word with a value. A `?` after it = grade C (a guess, or a doubtful value).
- `[xxx]` = code word with no value. `{x}` = sign with no value. `[..]` = a sign that is struck out.
- `,` = the small pause mark of the cipher. `.` = the strong pause mark.
- `<...>` = clear Spanish on the page.
- The decoder puts no spaces between the letters of one run of signs. A code word can be a syllable inside a word
  (`gra DE ci EN` = "gradecien-").

## The settled transcription

This is the text that the reading uses (`transcription/f118r_final.txt`, `transcription/f118v_final.txt`).

### f. 118 recto

```
r01: a , yerllegoaqui [..] a VENECIANOS letra COMO EMBAXADOR QUE tienen EN FRANCIA
r02: . COMO ENTRE V.AL. y EL REYDEFRANCIA , SE auyaasentadotregua POR TRES a
r03: nos , po SE dendocada UN DELAS? PARTES lo QUE tiene , ESTA so
r04: LA particu LA ridadles DE zia , . EN biaronlu
r05: ego POR mi PARA NO tificarmelo , mostraron
r06: MUCHO? plazer DE llo . y YO? lesdia EN tender QUE lo
r07: creya , AUNQUE? muy MAS CON [gab] , QUE EL? alegria ESTA va ENEL
r08: rostro , y EL dolor ENEL coracon , hasta SE
r09: DE V.AL. lo QUE YO? do NO DAR vi NO replicalles , AUNQUE? SE
r10: alo QUE {h}cre QUE LA tregua ESTA BIEN DE QUAL quier MANERA
r11: QUE SE a . y POR ELLO? SE pue DE BIEN DEZIR , QUE qui EN a DIO s
r12: tiene TODO tiene , afirmoa V.AL. QUE POR EL ES
r13: pi [..] ri EN cia DE lo QUE ve EN YA? NOS , MAS caso HA zen
r14: DE [rie~] [mut] , QUE DE SU poder , .
r15: ESTOS y EL PAPA ESTA nmuy MAL? SE gune [gag] , y DE ayer ACA
r16: an SI nifycado , QUE rer QUE nvie SE algu NO , QUE
r17: SE ynterpud SI e SE EN MEDIO , PARA HA blar EN CON cor
r18: dia , LA QUAL BIEN CREO QUE NO SE ra , QUE ri EN doresti
r19: tuyr . afa EN ca , niarimy NO , AUNQUE? anauido
r20: LOS? castillos DE lo DE SE sena . y CREO QUE CON ESTO?
r21: QUE riancunplir , y DE sestir SE DE lo DE MAS
r22: , . EL PAPA me ES crivio UN breve , gra DE ci EN
r23: domealgo DE lo QUE aquiauia HA blado , y
r24: LAS mesmasgraciasmedan VENECIANOS . NO SE SI an
r25: bas PARTES QUE ran QUE meynterpongaenello , lo
r26: QUAL acetare SI me CON bidan , yhasta VER man
r27: dami EN to DE V.AL. , NO apretaria EL NEGOCIO ,
r28: a CON cordallos , POR QUE meparece QUE NO HA ze EN
r29: SU SERVICIO? . anteome HA ganmedianeroo NO
r30: EN ti EN do POR vias ES qui SI tas , DE tra
r31: bajar QUE ES ten COMO ESTA n , POR QUE hecha LA tegua
r32: . yteni EN do ESTA diferencia , PAPA y VENECIANOS . CREO
r33: QUE SE ES triniran ESTOS ajuntar SE os ,
```

### f. 118 verso

```
v01: , POR QUE realmente POR [hue] SE manify ESTA , y POR [nae] [meq]
v02: QUE EL PAPA SE DE clinaa LA PARTE DE FRANCIA , y EN MUCHAS? yn SI
v03: nias SE leco NO ce ,
v04: DEL reame NO SE sabeaoraaqui , SI NO COMO a
v05: quelluys DAR ce ESTA SI tiado EN ve NO sa ,
v06: LA EMBAXADA? DEL soldan , DE QUE SE avia ES critoo QUE ve
v07: nian , diz QUE LA asobre SE ydo , PIENSAN? algu NOS
v08: QUE SE lea CON SE jado DE aqui , POR NO mostrar
v09: QUE HA zetantocaso , hasta VER SI SE toma
v10: algun MEDIO , me NOS preciando EL NEGOCIO DE POR to
v11: gal , COMO COSA QUE PIENSAN? NO poderdurar , ESTOS DE s DE
v12: nos SE mu ES tran POR VENECIANOS , POR ES forcaral
v13: pueblo , EL QUAL ESTA EN gran CON fu SI on ,
v14: enesto DEL ES pecieria , y EN [roo] ES UN muy
v15: gran NEGOCIO EN existencia . ,
v16: . gofernandez ESTA YA? BUENO? a DIO sgracias , SE
v17: gun V.AL. avransabido , <de Venecia xx iiii de febrero>
```

## The two transcription passes

Pass A and pass B, decoded with the same key. `(a|b)` = the two passes differ: pass A before the bar, pass B after
it. Pass B often wrote `pie~` (with a stroke) where pass A wrote `pie` (que); the key has no entry for `pie~`, so
it shows as `[pie~]`.

### f. 118 recto

```
r01: a , yerllegoaqui [..] a VENECIANOS letra COMO EMBAXADOR QUE tienen EN FRANCIA
r02: . COMO ENTRE V.AL. y EL REYDEFRANCIA , SE auyaasentadotregua POR TRES a
r03: nos , po SE dendrcada (UN CON|[rig] DELAS?) PARTES lo QUE tiene , ESTA so
r04: LA particu LA ridadles DE zia , . EN biaronlu
r05: ego POR mi PARA NO tificarmelo , mostraron
r06: MUCHO? plazer DE llr . y YO? lendia EN tender QUE lo
r07: creya , AUNQUE? muy MAS CON [gab] , (QUE|[pie~]) EL? alegria ESTA va ENEL
r08: rostro , y EL dolor ENEL coracon , hasta SE
r09: DE V.AL. lo (QUE|[pie~]) YO? do NO DAR (u|v) i NO replicallen , AUNQUE? SE
r10: alo QUE {h}cre (QUE|[pie~]) LA tregua ESTA (BIEN|[fau]) DE QUAL quier MANERA
r11: (QUE|[pie~]) SE a . y POR (ELLO?|[hig~]) SE pue DE (BIEN|[fau]) DEZIR , (QUE|[pie~]) qui EN a DIO s
r12: tiene (TODO|[ruh]) tiene , afirmoa V.AL. (QUE|[pie~]) POR EL ES
r13: pi ([..]|r) ri EN cia DE lo (QUE|[pie~]) ve EN (YA?|V.AL.) NOS , MAS caso HA zen
r14: DE [rie~] [mut] , QUE DE SU poder , .
r15: ESTOS y EL PAPA ESTA nmuy MAL? SE gune ([gag]|[gaq]) , y DE ayer ACA
r16: an SI nifycado , (QUE|[pie~]) rer (QUE|[pie~]) n (v|u) ie SE algu NO , QUE
r17: SE ynterpud SI e SE EN MEDIO , PARA HA {tt}plar EN CON cor
r18: dia , LA QUAL BIEN [gab] (QUE|[pie~]) NO SE (r|i) a , (QUE r|[pie~] i) i EN doresti
r19: tuyr . afa EN ca , niarimy NO , AUNQUE? anauido
r20: LOS? castillos DE lo DE SE sena . y [gab] (QUE|[pie~]) CON ESTO?
r21: (QUE|[pie~]) riancunplir , y DE sestir SE DE lo DE MAS
r22: , . EL PAPA me ES crivio (UN|YA?) breve , gra DE ci EN
r23: domealgo DE lo (QUE|[pie~]) aquiauia HA blado , y
r24: LAS mesmasgraciasmedan VENECIANOS . NO SE SI an
r25: bas PARTES (QUE|[pie~]) ran (QUE|[pie~]) meynterpongaenello , lo
r26: QUAL acetare SI me CON bidan , yhanta VER man
r27: dami EN to DE V.AL. , NO apretaria EL NEGOCIO ,
r28: a CON cordallos , POR (QUE|[pie~]) meparece (QUE|[pie~]) NO HA ze EN
r29: SU SERVICIO? . anteome HA ganmedianeroo NO
r30: EN ti EN do POR vias ES qui SI tas , DE t (r|i) a
r31: bajar QUE ES ten COMO ESTA n , POR QUE hecha LA tegua
r32: . yteni EN do ESTA diferencia , PAPA y VENECIANOS . [gab]
r33: QUE SE ES triniran ESTOS ajuntar SE os ,
```

### f. 118 verso

```
v01: , POR QUE realmente POR [hue] SE manif (y|m) ESTA , y POR [nae] [meq]
v02: (QUE|[pie~]) EL (PAPA|[nam]) SE DE clinaa LA (PARTE|ez) DE FRANCIA , y EN MUCHAS? yn SI (|[|])
v03: nias SE leco NO ce ,
v04: DEL reame NO SE sabeao (r|i) aaqui , SI NO COMO a
v05: quelluys DAR ce ESTA SI tiado EN ve NO sa ,
v06: (LA|[mye]) EMBAXADA? DEL soldan , DE (QUE|[pie~]) SE a (vi|ll) a ES crito (|o) QUE ve
v07: nian , diz (QUE LA|[pie~] [mye]) asobre SE ydo , (PIENSAN?|[goot]) algu (NOS|[me])
v08: (QUE|[pie~]) SE lea CON SE jado DE aqui , POR NO mostra (r|m)
v09: QUE HA zetantocaso , ha (s|o) ta (VER|VENECIANOS) SI SE toma
v10: algun MEDIO , me NOS preciando EL NEGOCIO DE POR to
v11: gal , COMO COSA QUE PIENSAN? NO poderdu (r|i) ar , ESTOS DE s DE
v12: nos SE mu ES tran POR VENECIANOS , POR ES forcaral
v13: pueblo , EL QUAL ESTA EN gran (CON|DAR) fu SI on ,
v14: enesto DEL ES pecieria , y EN [roo] ES (UN|[rao]) muy
v15: gran NEGOCIO EN elistencia . ,
v16: . gofernandez ESTA (YA? BUENO?|[rac] e [fin~]) a (DIO|[gce]) sgracias , SE
v17: gun V.AL. avransa (p|b) ido , (<de Venecia xx iiii de febrero>|<de benecia? xxiiij? de febrero>)
```
