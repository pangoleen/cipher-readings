"""Decode Vargas Mexia's Cipher 2 (key: S. Tomokiyo 2020; complements read from Cabinet Noir's notes: lone rho = y, V = ll,
0+ = ss?, b = br, n = pr, f = cr, p = tr, R = rr, C = ch, Z = z, overlined groups = nulls, codes 98 = Rey, 99 = Reyno, 48 = Duque).
Input: pass files in the notation of passes/PROMPT_c2_blind.md."""
import re, sys, random
ALPHA={2:'a',3:'b',4:'c',5:'d',6:'e',7:'f',8:'g',9:'h',10:'i',11:'l',12:'m',13:'n',14:'o',15:'p',16:'q',17:'r',18:'s',19:'t',20:'u',21:'x',22:'y',23:'z'}
LET={'f':'cr','n':'pr','p':'tr','pp':'tr','R':'rr','C':'ch','V':'ll','v':'ll','b':'br','P':'pl','Z':'z','m':'m','du':'[du]','rho':'y','g':'gr'}
VOW={'p':'a','+':'e',',':'i',"'":'o','.':'u'}
CODES={'98':'[Rey]','99':'[Reyno]','48':'[Duque]','42':'[42]'}
def dec_group(g, alpha=ALPHA, vow=VOW):
    q=g.endswith('?'); g=g.rstrip('?')
    if g in ('/','(',')',',','/.','(empty)','[gutter]'): return g if g!='(empty)' else ''
    if g.startswith('{') or g.startswith('['): return g
    if g.startswith('~') or g.startswith('^~'): return ''          # overlined = null
    dbl=g.startswith('^'); g=g.lstrip('^')
    m=re.match(r'^(\d+|rho|pp|du|[A-Za-z])([p+,\'.]*)$',g)
    if not m: return '<'+g+'>'
    b,marks=m.groups()
    if b.isdigit():
        if b in CODES and not marks: return CODES[b]
        n=int(b)
        if n==0: c='ss' if marks.startswith('+') else 'a'; marks=marks[1:] if marks.startswith('+') else marks
        elif n in alpha: c=alpha[n]
        else: return '['+b+marks+']'
        if b=='16' and marks=='+': return 'que'
        if b=='16' and marks==',': return 'qui'
    else:
        c=LET.get(b,'<'+b+'>')
    if dbl: c=c+c if len(c)==1 else c
    return c+''.join(vow[x] for x in marks)
def dec_line(s,**kw): return ''.join((dec_group(g,**kw) or '') if True else '' for g in s.split()) if False else ' '.join(x for x in (dec_group(g,**kw) for g in s.split()))
if __name__=='__main__':
    for f in [a for a in sys.argv[1:] if not a.startswith('--')]:
        print('#',f)
        for line in open(f,encoding='utf-8'):
            line=line.rstrip('\n')
            if not line.strip(): continue
            if '\t' in line: lab,txt=line.split('\t',1)
            else: lab,txt=line.split(' ',1) if ' ' in line else (line,'')
            print(lab, dec_line(txt).replace(' ','') if '--join' in sys.argv else dec_line(txt))
