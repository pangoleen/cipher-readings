# Reader for the transcription files of BnF Espagnol 318 no. 93. One line of a file = one line of the page.
# A token is a cipher sign (names in transcription/SIGNS.md), a joined group that stands for one letter
# (gto, gt, otto, tto), or a code word in small letters. "?" after a token = doubt of the transcriber.
import re, collections
SIGNS=set("E o tf ttc c #3 m4 + ÷ Z ^ p p+ P pq qp III m 4 h4 oo e C. :/ .ll. ir pi qpi u_ n- u3 dl 5 7 tb tb2 ff fs cf X Xo X: Y Y= y y- psi O. 2= 2~ =8 Z= tri tt h o".split())
GROUPS={'gto','gt','otto','tto'}
FINAL=('transcription/f118r_final.txt','transcription/f118v_final.txt')
PASS_A=('transcription/f118r_passA.txt','transcription/f118v_passA.txt')
PASS_B=('transcription/f118r_passB.txt','transcription/f118v_passB.txt')
def load(path):
    """[(line label, [(kind, token, doubt)])]; kind = sign, group, code, unk or clear"""
    lines=[]
    for ln in open(path,encoding='utf-8'):
        ln=ln.strip()
        if not re.match(r'^[rv]\d+:',ln): continue
        lab,rest=ln.split(':',1); toks=[]
        for p in re.split(r'(<[^>]*>)',rest):
            if p.startswith('<'): toks.append(('clear',p[1:-1],False)); continue
            for t in p.split():
                q=t.endswith('?') and t!='??'
                base=t[:-1] if q else t
                kind='sign' if base in SIGNS else 'group' if base in GROUPS else 'unk' if base in ('??','[del]') else 'code'
                toks.append((kind,base,q))
        lines.append((lab,toks))
    return lines
def merge(toks):
    """the sign "m" followed by the sign "4" is one sign, m4 (= g)"""
    out=[]; i=0
    while i<len(toks):
        if toks[i][1]=='m' and i+1<len(toks) and toks[i+1][1]=='4': out.append(('sign','m4',False)); i+=2
        else: out.append(toks[i]); i+=1
    return out
def toks(files=FINAL):
    """[(line label, kind, token)] for all lines of the files, with m4 merged"""
    return [(lab,k,b) for f in files for lab,t in load(f) for k,b,q in merge(t)]
