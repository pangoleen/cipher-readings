"""Agreement of two blind passes on a Cipher 2 page, line by line (difflib alignment of groups)."""
import sys, difflib, re
def load(p):
    d={}
    for line in open(p,encoding='utf-8'):
        line=line.rstrip('\n')
        if not line.strip() or not line.startswith('L'): continue
        lab,_,txt=line.partition('\t')
        if not _: lab,_,txt=line.partition(' ')
        gs=[]
        for g in re.sub(r'\{[^}]*\}','',txt).split():
            g=g.rstrip('?')
            if g in ('[gutter]','(empty)','/','/.',',','(',')','??',''): continue
            gs.append(g)
        d[lab.strip()]=gs
    return d
A,B=load(sys.argv[1]),load(sys.argv[2]); ta=tb=tm=0
verbose=len(sys.argv)>3
for lab in sorted(set(A)|set(B),key=lambda s:int(s[1:])):
    a,b=A.get(lab,[]),B.get(lab,[])
    sm=difflib.SequenceMatcher(None,a,b,autojunk=False); m=sum(x.size for x in sm.get_matching_blocks())
    ta+=len(a); tb+=len(b); tm+=m
    if verbose: print(lab,len(a),len(b),m)
print(sys.argv[1].split('/')[-1],'A',ta,'B',tb,'match',tm,'agreement = %.3f'%(tm/max(ta,tb,1)))
