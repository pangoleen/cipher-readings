# Counts of the reading: the firm share (grade A) and the share with the probable values (grades A and B).
# Run it in this folder:  python3 counts.py
import collections
from lib import toks
import key
def counts():
    tok=collections.Counter(); typ=collections.defaultdict(set)
    for lab,k,b in toks():
        if b in key.WORDS or k in('clear','unk'): continue
        kind='sign' if k in('sign','group') else 'code'
        tab=key.KEY if kind=='sign' else key.CODES
        g=tab[b][1] if b in tab else 'none'
        tok[kind,g]+=1; typ[kind,g].add(b)
    return tok,typ
if __name__=='__main__':
    tok,typ=counts(); G=('A','B','C','none')
    for kind in('sign','code'):
        n=sum(tok[kind,g] for g in G); t=sum(len(typ[kind,g]) for g in G)
        print(f"{kind}: {t} types, {n} tokens; "+'; '.join(f"grade {g}: {len(typ[kind,g])} types, {tok[kind,g]} tokens" for g in G))
    N=sum(tok.values()); s={g:tok['sign',g]+tok['code',g] for g in G}
    print(f"all tokens: {N}")
    print(f"firm (grade A): {s['A']} = {100*s['A']/N:.1f} %")
    print(f"probable (grade B): {s['B']} = {100*s['B']/N:.1f} %")
    print(f"firm and probable: {s['A']+s['B']} = {100*(s['A']+s['B'])/N:.1f} %")
    print(f"guess or doubtful (grade C): {s['C']} = {100*s['C']/N:.1f} %")
    print(f"no value: {s['none']} = {100*s['none']/N:.1f} %")
