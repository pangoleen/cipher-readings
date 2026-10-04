# Titus cipher 1648, values read by us from Hillier (1852) pp.153-161, 210, 240 (OCR text of archive.org narrativeofattem00hilluoft,
# aligned by hand; Hillier's own decipherment is free, so each value below is our alignment, not his).
TITUS = {
102:'an',103:'am',104:'as',105:'at',106:'al',107:'ar',108:'and',109:'any',112:'after',113:'able',115:'about',116:'but',
117:'be',118:'by',126:'can',127:'con',128:'com',131:'cause',132:'could',133:'course',135:'do',136:'dis',137:'de',140:'did',
141:'dar',143:'ed',144:'el',149:'end',150:'endeavour?',151:'ever',152:'en?',158:'for',159:'fit',164:'fail',165:'find',169:'from',
174:'friend',176:'God',177:'go',179:'get',181:'good',182:'give',184:'great',185:'help',186:'he',187:'her',189:'him',193:'had',
194:'hath',198:'horse',200:'(stop)',201:'(stop)',202:'(stop)',203:'here',209:'I',210:'it',211:'is',212:'in',213:'if',215:'il',216:'ing',
218:'just',226:'know',228:'ly',230:'like',231:'leave',232:'life',250:'me',251:'my',253:'may',254:'made',255:'men',257:'much',
263:'must',264:'make',269:'no',270:'not',271:'now?',274:'next',275:'nigh',279:'of',280:'or',281:'on',282:'ow',284:'our',289:'other',
292:'pre',296:'put',298:'p??',302:'place',313:'re',315:'Queen',335:'so',337:'some',338:'such',340:'send',343:'sure',344:'soon',349:'shall',
356:'ship',359:'to',360:'the',361:'this',363:'that',364:'then',367:'there',369:'trust',371:'time',375:'t??',376:'try',377:'thing',379:'though',
381:'un',382:'us',383:'up',389:'w??',391:'we',392:'window',397:'was',399:'will',401:'with',404:'where',405:'which',411:'wise',413:'write',420:'you',
437:'assist',453:'business',457:'Lady Carlisle',463:'answer',465:'confide',468:'contents',478:'design',479:'desire',483:'danger',493:'Rogers?',
505:'affair?',509:'paper',512:'Parliament',531:'land',532:'letter?',541:'?(Con)',546:'??',557:'order',563:'certain',564:'treaty',571:'provid',577:'??',
599:'service',608:'trouble',631:'first',634:'one',635:'two',636:'three',637:'four',638:'five',639:'six',643:'ten',644:'eleven',647:'twenty',651:'week',
656:'thousand',659:'Monday',660:'Tuesday',662:'Wednesday',665:'Sunday',672:'May',680:'wife',686:'escape',689:'??name',705:'boat',708:'Col. Legge',
714:'Dr Fraizer',715:'Mrs Whorwood'}
TITUS_LET = {7:'p',10:'o',11:'o',14:'h',15:'h',16:'h',20:'a',21:'a',22:'a',23:'a',31:'u',32:'u',33:'u',35:'b',36:'b',38:'g',39:'g',40:'g',
41:'k',42:'k',46:'y',47:'y',50:'r',51:'r',52:'r',53:'w',54:'w',55:'w',60:'l',63:'s',64:'s',65:'s',66:'s',67:'d',68:'d',71:'n',72:'n',73:'n',
78:'t',79:'t',80:'t',84:'j',91:'e',92:'e',93:'e',94:'e',96:'c',97:'c',98:'c',99:'c'}
def shift(n):
    """1646 code -> Titus code (first guess)"""
    if n < 100: return None
    if n <= 207: return n-4
    if n <= 279: return n
    if n <= 400: return n-1
    if n <= 420: return n-8
    return n-9
