# Key of BnF Espagnol 318 no. 93 (Lorenzo Suarez, Venice, 24 February 1504), rebuilt from the letter itself.
# Corrected after the audit of 11 October 2026 (evidence/audit.md lists each change).
# Sign names: transcription/SIGNS.md.
# Grades: A = firm (fixed by three or more clear words); B = probable (fits every place, but few places; or one
# place, with the sense confirmed by an outside source); C = guess, or a value that the alphabet rule puts in doubt.
KEY={
 # a
 'p':('a','A'),'p+':('a','A'),'+':('a','A'),
 # b / v
 '2=':('b','A'),'c':('b','B'),'ttc':('b','C'),'pq':('v','A'),
 # c
 'dl':('c','A'),
 # d
 'n-':('d','A'),'tb':('d','A'),'=8':('d','B'),
 # e
 '^':('e','A'),'.ll.':('e','A'),'gt':('e','A'),'4':('e','A'),
 # f g h
 'X':('f','A'),'m4':('g','A'),'2~':('h','A'),'7':('h','B'),
 # i / y
 'm':('i','A'),'5':('i','A'),'u_':('y','A'),'y':('y','A'),
 # j
 'P':('j','A'),
 # l, ll
 'e':('l','A'),'cf':('l','A'),'qpi':('ll','A'),
 # m n
 'Y':('m','A'),'Y=':('m','B'),'pi':('m','A'),'fs':('n','A'),'ff':('n','A'),'otto':('n','A'),
 # o
 'oo':('o','A'),'tto':('o','A'),'ir':('o','A'),'#3':('o','B'),
 # p q r
 'C.':('p','A'),'tb2':('p','B'),'h4':('q','A'),'tri':('q','B'),'III':('r','A'),'psi':('r','A'),'Xo':('r','A'),
 # s
 ':/':('s','A'),'O.':('s','A'),'tf':('s','A'),'y-':('s','B'),
 # t u x z
 'gto':('t','A'),'X:':('t','A'),'qp':('u','A'),'E':('x','C'),'u3':('z','B'),'Z=':('z','A'),'o':('o','C'),
}
CODES={
 'pie':('que','A'),'gad':('de','A'),'heg':('en','A'),'mat':('no','A'),'roc':('se','A'),'roe':('se','A'),
 'me~':('por','A'),'hug':('esta','A'),'hif':('es','A'),'pet':('si','A'),'hoe':('el','A'),'gue':('con','A'),
 'mae':('la','A'),'luq':('ha','A'),'gee':('dio','A'),'pif':('qual','A'),
 'gie':('como','A'),'gie~':('del','B'),'rup':('v.al.','B'),'ren':('venecianos','B'),'hog':('estos','B'),
 'nan':('papa','B'),'gib':('creo','B'),'ris':('un','B'),'muy':('aunque','C'),'myl':('mas','B'),'met':('nos','A'),
 'fam':('bien','B'),'fan':('bien','B'),'mez':('medio','B'),'rer':('ver','B'),'hie':('enel','B'),'lo':('francia','B'),
 'noe':('para','B'),'rel':('tres','B'),'rih':('todo','B'),'muq':('manera','B'),'fok':('aca','B'),'fij':('esto','C'),
 'mee':('las','B'),'nez':('partes','B'),'nuz':('parte','B'),
 'mud':('negocio','B'),'mie':('la','B'),'hab':('embaxada','C'),'hu':('embaxador','B'),'got':('piensan','C'),
 'ged':('cosa','B'),'poz':('reydefrancia','B'),'hac':('entre','B'),'fab':('yo','C'),'maq':('mucho','C'),
 'gut':('dezir','B'),'gae':('dar','B'),'gue~':('delas','C'),'pot':('el','C'),'gaf':('los','C'),'moq':('muchas','C'),
 'fin':('bueno','C'),'rus':('ya','C'),'ree':('su','B'),'hig':('ello','C'),
 'rud':('servicio','C'),'mul':('mal','C'),
}
OPEN=['gab','gag','rie~','mut','hue','nae','meq','roo']
WORDS={'Z':',','÷':'.'}   # Z = small pause (comma); ÷ = strong pause (stop, new sentence)
# The code list follows the alphabet: the first letter of a code word gives the first letters that its value can have.
BAND={'f':'ab','g':'cd','h':'e','l':'fgh','m':'lmn','n':'p','p':'qrs','r':'stuvxy'}
# The ten values that lay outside their band at the audit, and what was done with each.
OUTSIDE={
 'hog':'was "venecianos"; swapped with ren; now "estos", in its band',
 'ren':'was "estos"; swapped with hog; now "venecianos", in its band',
 'noe':'was "a"; now "para", in its band; both places read well',
 'got':'doubtful: the band asks for c or d (creen? dizen?)',
 'fij':'doubtful: the band asks for a or b (aquello?)',
 'gaf':'doubtful: the band asks for c or d (dos? ciertos?)',
 'fab':'doubtful: the band asks for a or b; no other value found',
 'pot':'doubtful: the band asks for q, r or s; the blind reader gave "su", but "su" is ree',
 'muy':'doubtful: the band asks for l, m or n; no other value found; the sense "though" fits all three places',
 'me~':'outside its band, but firm: POR-to-gal, POR QUE, 14 places; the words with a stroke may be a list of their own',
}
# Guesses for open code words (not used by the decoder): roo = verdad (both blind readers; fits the band).
