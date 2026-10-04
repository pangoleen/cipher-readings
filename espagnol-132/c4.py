"""Decode Vargas Mexia's Cipher 4 (Antonio Perez's private cipher). Key: J. P. Devos 1950 p.422 as completed by S. Tomokiyo 2020
(table spanish3vargas4.png); code values vo = Su Magestad, xe = V.m., C = ch from Cabinet Noir's cle/cipher4_codes_perez.tsv (CC BY 4.0).
Values marked HERE are proposed in this folder (see NOTES.md). Input notation: passes/PROMPT_c4_blind.md."""
import re, sys, random
ALPHA={12:'a',11:'b',10:'c',9:'d',8:'e',7:'f',6:'g',5:'h',4:'i',3:'l',2:'m',1:'n',23:'o',22:'p',21:'q',20:'r',19:'s',18:'t',17:'u',16:'x',15:'y',14:'z'}
LET={'y':'a','a':'u','o':'o','S':'o','d':'dr','C':'ch','t':'tr','p':'pr','P':'pr','c':'cr','b':'br','g':'gr','f':'fr','B':'bl','G':'gl'}
VOW={'.':'a','+':'e',',':'i','o':'o',"'":'u'}
CODES={'vo':'[S.M.]','xe':'[V.m.]','xi':'[xi]','tu':'[tu]','mo':'[mo]','Ta':'[Ta]','Te':'[te]','te':'[te]','no':'[no]','fa':'[cifra]',
       'ho':'[ho]','si':'[possible]','co':'[carta]','ro':'[para]','ti':'[ti]','du':'[du]','Se':'[Se]','X':'','por^':''}
def dec_group(g, alpha=ALPHA, vow=VOW, codes=CODES):
    g=g.rstrip('?')
    if g in ('/',',','/.','[gutter]'): return {'[gutter]':'[...]'}.get(g,g)
    if g in codes: return codes[g]
    if '^' in g: return ''                     # sign with caret or acute = null
    dbl=g.startswith('='); g=g.lstrip('=')
    m=re.match(r"^(\d+|[A-Za-z])([.+,o']*)$",g)
    if not m: return '<'+g+'>'
    b,marks=m.groups()
    if b.isdigit():
        n=int(b)
        if n not in alpha: return '['+g+']'
        c=alpha[n]
        if n==21 and marks in ('+',','): return 'qu'+vow[marks]
    else:
        if b not in LET: return '<'+g+'>'
        c=LET[b]
    if dbl: c=c+c if len(c)==1 else c
    return c+''.join(vow[x] for x in marks)
def dec(s,**kw):
    s=re.sub(r'\{above:|\}','',s)
    return ' '.join(x for x in (dec_group(g,**kw) for g in s.split()) if x!='')
if __name__=='__main__':
    txt=open(sys.argv[1],encoding='utf-8').read()
    shuffle=len(sys.argv)>2 and sys.argv[2]=='--wrong'
    kw={}
    if shuffle:
        random.seed(132); ks=list(ALPHA); vs=[ALPHA[k] for k in ks]; random.shuffle(vs); kw['alpha']=dict(zip(ks,vs))
    def rep(m): return '«'+dec(m.group(1),**kw)+'»'
    print(re.sub(r'<<(.*?)>>',rep,txt,flags=re.S))
