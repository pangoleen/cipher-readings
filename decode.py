import sys, difflib
sys.path.insert(0,'.')
from lib import load
from key import KEY, CODES
def dtok(t):
    if t[0]=='clear': return ' <'+t[1]+'> '
    if t[0]=='code':
        c=t[1]
        if c in ('otto','malz'): return CODES[c][0]
        if c in CODES: return ' '+CODES[c][0].upper()+('?' if CODES[c][1]=='C' else '')+' '
        return ' ['+c+'] '
    s=t[1]
    if s in ('.',',','/','/.'): return ' '+s+' '
    return KEY.get(s,'{'+s+'}')
def dec_line(toks): return ''.join(dtok(t) for t in toks).replace('  ',' ').strip()
def merged(fa,fb):
    A=dict(load(fa)); B=dict(load(fb)); out=[]
    for lab in sorted(A):
        a=[dtok(t) for t in A[lab]]; b=[dtok(t) for t in B.get(lab,[])]
        sm=difflib.SequenceMatcher(None,a,b,autojunk=False); s=''
        for op,i1,i2,j1,j2 in sm.get_opcodes():
            if op=='equal': s+=''.join(a[i1:i2])
            else: s+='('+''.join(a[i1:i2]).strip()+'|'+''.join(b[j1:j2]).strip()+')'
        out.append(lab+': '+s.replace('  ',' ').strip())
    return out
if __name__=='__main__':
    if len(sys.argv)>2:
        print('\n'.join(merged(sys.argv[1],sys.argv[2])))
    else:
        for lab,toks in load(sys.argv[1]): print(lab+': '+dec_line(toks))
