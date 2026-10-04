KEY = {}
# Evelyn iv 178-179 (page images read by us)
E = {112:'and',121:'be',209:'I',213:'if',234:'left',250:'me',251:'my',269:'no',270:'not',280:'of',281:'or',341:'send',360:'to',
409:'with',412:'where',413:'which',422:'write',429:'you',503:'Earl',550:'Marquis',520:'H[ertford]',141:'de',162:'for',197:'had',200:'hav',
216:'ing',111:'are',147:'ed',356:'South',107:'am',282:'on',361:'the',366:'them',365:'then',148:'el',319:'re',383:'up',122:'by',
56:'s',57:'s',58:'s',59:'s',63:'i',17:'r',18:'r',19:'r',67:'e',70:'e',78:'w',31:'o',81:'d',90:'c',27:'b',40:'i',7:'n',84:'h',43:'t',46:'a',75:'l'}
KEY.update(E)
# nulls / stops
for n in (0,1,2,3,4,20): KEY[n]='_'
R1 = {355:'since',647:'five',681:'May',44:'t',45:'t',68:'e',69:'e',60:'m',117:'able',25:'b',26:'b',49:'a',48:'a',47:'a',77:'l',76:'l',
86:'h',85:'h',72:'p',210:'it',110:'al',80:'w',79:'w',82:'d',83:'d',14:'g',192:'his',11:'u',12:'u',50:'q',296:'pli',109:'at',364:'that',
405:'was',542:'letter',132:'com',106:'an',105:'ad',350:'shall',123:'but',190:'he',193:'him',173:'from',665:'thousand',646:'four',643:'one',
648:'six',644:'two',211:'is',212:'in',108:'as',430:'your',543:'Majesty',370:'tion',367:'they',368:'there',391:'we',153:'end',191:'her',
470:'consider',64:'y',351:'should',528:'Kingdom',583:'copy?'}
KEY.update(R1)
R2 = {35:',',9:'n',8:'n',562:'Oxford',572:'Parliament',512:'garrison',329:'render',382:'us',496:'.',697:'_',555:'[NICHOLAS]',131:'con',
91:'c',10:'u',342:'safe',614:'Sir',629:'[Warwick]',384:'treat',504:'Fairfax',489:'desire',199:'have',36:'f',34:'v',74:'e',73:'l',71:'p',
89:'c',88:'c',537:'London',262:'might',236:'one',120:'also?',6:'_',219:'ish'}
KEY.update(R2)
R3 = {100:'.',101:'.',102:'.',103:'.',87:'.',93:',',94:',',96:',',97:',',99:',',279:'_',126:'being',194:'here',385:'very',256:'many',
201:'hold',284:'out',285:'our',585:'quarter',339:'such',272:'new',667:'day',408:'were?',406:'were',510:'Lords',546:'messenger',
304:'press',597:'refuse',183:'give',330:'reason',402:'why',340:'sent',375:'treat',262:'may',267:'might',172:'free',363:'those',
411:'who',142:'did?',378:'think',259:'most',271:'now',618:'treaty?',196:'hope',150:'est',220:'inter?',258:'more',362:'this',613:'Scot',
175:'faith',166:'ful',596:'receive',569:'Prince Rupert',674:'Sunday',104:'ab',37:'f',39:'i',182:'ge',478:'condition',336:'so'}
KEY.update(R3); KEY[384]='<384>'
R4 = {165:'fall',170:'foot',273:'near',298:'pay',620:'victual',248:'less?',581:'provide',447:'[447:A-word]',204:'hear',568:'Prince [Charles]',
55:'s',571:'Presbyterian',522:'Independent',510:'Governor',583:'print',507:'first',327:'right?',118:'arm?',404:'West',255:'men',224:'keep',
66:'y',431:'yield',335:'[335:run?]',240:'[240:l-word]',215:'il',228:'ly',202:'horse',338:'some?',407:'will',21:'_',274:'next',178:'friend',
231:'[231]',376:'[376]',401:'[401:who?]',264:'[264:my Lord?]',629:'[629:W..=Warwick]',618:'[618:treaty?]',120:'[120]',167:'[167:f-word]',
639:'[639:number?]',691:'[691]',292:'[292]',384:'[384]',219:'ish?',220:'inter?',142:'[142:did?]',236:'[236:one?]'}
KEY.update(R4)
