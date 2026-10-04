#!/usr/bin/env python3
"""dec4.py [-t table] token ... | -f file : decode figure tokens with a list table (default lists_v3).
Mark -> list: none/^. -> A,C ; ^: -> E ; _: -> G ; _- -> I ; _. or ^._. -> M ; ^^ -> O ; _v -> P ; ^^_v -> Q ;
^._- -> S ; ^-_. -> T ; = -> PT ; () -> BR ; ^- -> N"""
import sys,re,collections
T='../tables/lists_v3.tsv'
args=sys.argv[1:]
if args and args[0]=='-t': T=args[1]; args=args[2:]
tab=collections.defaultdict(list)
for l in open(T,encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    p=l.rstrip('\n').split('\t')
    tab[(p[0],int(p[1]))].append(p[2])
def lists_of(mark,br):
    if br: return ['BR']
    m=mark.replace('?','').replace('~','')
    M={'':['A','C'],'^.':['A','C'],'^:':['E'],'_:':['G'],'_-':['I'],'_.':['M'],'^._.':['M'],'^^':['O'],'_v':['P'],
       '^^_v':['Q'],'^._-':['S'],'^-_.':['T'],'=':['PT'],'^-':['N'],'^-_-':['PT']}
    return M.get(m,[])
def window(L,f):
    fs=sorted(k[1] for k in tab if k[0]==L)
    lo=[x for x in fs if x<f]; hi=[x for x in fs if x>f]
    a=f"{lo[-1]} {tab[(L,lo[-1])][0]}" if lo else 'START'; b=f"{hi[0]} {tab[(L,hi[0])][0]}" if hi else 'END'
    return f"{a} < .. < {b}"
def dec(tok):
    m=re.match(r'^(\()?(\d\d)\)?(.*)$',tok)
    if not m: return tok
    br=bool(m.group(1)); f=int(m.group(2)); mark=m.group(3)
    out=[]
    for L in lists_of(mark,br):
        if (L,f) in tab: out.append(f"{L}:{'/'.join(tab[(L,f)])}")
        else: out.append(f"{L}:[{window(L,f)}]")
    if not out:
        out=[f"?mark; any list: "+'; '.join(f"{k[0]}:{'/'.join(v)}" for k,v in sorted(tab.items()) if k[1]==f)]
    return f"{tok} -> "+' | '.join(out)
if args and args[0]=='-f':
    for line in open(args[1],encoding='utf-8'):
        print(line.rstrip()); 
        for t in line.split():
            if re.match(r'^\(?\d\d',t): print('    ',dec(t))
else:
    for t in args: print(dec(t))
