import collections
from toks import load
from key1646 import KEY, E
from titus import TITUS
lines=load('../src/aay/f10_ct.txt')
cnt=collections.Counter()
for toks in lines:
    for t in toks:
        q=t.rstrip('?')
        if q.isdigit(): cnt[int(q)]+=1
def titus_match(n,v):
    v0=v.strip('[]?').lower()
    for s in (0,1,4,8,9,10):
        t=n-s
        if t in TITUS:
            tv=TITUS[t].strip('?').lower()
            if tv and (tv==v0 or tv.startswith(v0[:3]) and v0.startswith(tv[:3])): return t,s
    return None
GLOSS={112,121,209,213,234,250,251,269,270,280,281,341,360,409,412,413,422,429,503,550,520,162,197,200,56,63,17,67,78,31,18,81,90,27,40,7,19,147,111,366,141}
KEY.pop(26,None); KEY[133]='care'; KEY[258]='more'; E[133]='care'; E[258]='more'; E[431]='yield'; E[216]='ing'
OUT=[]
for n in sorted(KEY):
    v=KEY[n]
    if v.startswith('<'): continue
    unread = v.startswith('[') and v[1:4].isdigit()
    doubt = '?' in v or (v.startswith('[') and not unread)
    if n in GLOSS: g='E'; src='Evelyn iv 178-179: gloss by Nicholas in the print (page image read by us)'
    elif n in E: g='E2'; src='Evelyn iv 179: our reading of the part that Nicholas left without gloss (16 Aug 1646), or our split of a gloss over several figures'
    else:
        m=titus_match(n,v) if n>=100 else None
        if m: g='T'; src='Titus %d (Hillier 1852) + shift %d, and context in f.10'%m
        else: g='C'; src='context in f.10'
    if n<100 and n not in E: src='spelled words in f.10'
    if doubt: g+='?'
    if unread: g='U'
    OUT.append((n,v,g,cnt.get(n,0),src))
with open('../key1646.tsv','w') as f:
    f.write('# Key of the cipher of the King with Sir Edward Nicholas, 1646 (f.10 of BL Add MS 72438; Evelyn iv 178-179).\n')
    f.write('# grade: E = gloss by Nicholas in the print of Evelyn; E2 = our reading of the unglossed part of the letter of the King of 16 Aug 1646; T = sister key (Titus cipher 1648) with shift, fits context; C = context only; ? = doubtful; U = not read (a guess may follow the number).\n')
    f.write('# _ and . , = nulls or stops (their exact sense is not known).\n')
    f.write('code\tvalue\tgrade\tcount_in_f10\tbasis\n')
    for r in OUT: f.write('%d\t%s\t%s\t%d\t%s\n'%r)
g=collections.Counter(r[2] for r in OUT)
print(len(OUT),'codes',dict(g))
tot=sum(cnt.values()); 
for gr in ('E','E2','T','C','E?','T?','C?','U'):
    print(gr, sum(r[3] for r in OUT if r[2]==gr))
print('tokens',tot,'unkeyed', tot-sum(r[3] for r in OUT))
import re
ill=sum(1 for toks in lines for t in toks if t=='?')
print('illegible tokens',ill)
