"""Agreement of two passes on the cipher groups of the Perez letters (notation of PROMPT_c4_blind.md)."""
import re, sys, difflib
def groups(path, pages):
    txt=open(path,encoding='utf-8').read()
    out={}
    for m in re.finditer(r'== (f\d+[rv])\n(.*?)(?=\n== |\Z)',txt,re.S):
        pg,body=m.groups()
        if pg not in pages: continue
        gs=[]
        for c in re.findall(r'<<(.*?)>>',body,re.S):
            c=re.sub(r'\{above:|\}|\[gutter\]','',c)
            c=re.sub(r'\[(looped|U-like)[^\]]*\]','X',c); c=re.sub(r'\[the letters "por"[^\]]*\]','por^',c); c=re.sub(r'\{struck:[^}]*\}?','',c); c=c.replace('[comma]','').replace('15o','15 o').replace('(?)','')
            for g in c.split():
                g=g.rstrip('?')
                g={"5'":'5^',"9'":"9'",'16':'1o','P^':'P^'}.get(g,g); g=g.replace('P','p') if re.match(r'^P[,+o.]',g) else g
                if g in ('/',',','/.','??',''): continue
                gs.append(g)
        out[pg]=gs
    return out
A=groups(sys.argv[1],sys.argv[3:]); B=groups(sys.argv[2],sys.argv[3:])
ta=tb=tm=0
for pg in sys.argv[3:]:
    a,b=A.get(pg,[]),B.get(pg,[])
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
    m=sum(x.size for x in sm.get_matching_blocks())
    ta+=len(a); tb+=len(b); tm+=m
    print(pg,'A',len(a),'B',len(b),'match',m)
    for op,i1,i2,j1,j2 in sm.get_opcodes():
        if op!='equal': print('   ',op,'A:',' '.join(a[i1:i2]),'| B:',' '.join(b[j1:j2]))
print('TOTAL A',ta,'B',tb,'match',tm,'agreement (match/max) = %.3f'%(tm/max(ta,tb)))
