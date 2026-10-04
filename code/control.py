import random, re
from titus import TITUS
random.seed(1)
# Control 1. Words glossed by Nicholas in Evelyn iv 178-179 (1646 key), found without the Titus key.
EV = {'and':112,'be':121,'I':209,'if':213,'me':250,'my':251,'no':269,'not':270,'of':280,'or':281,'send':340+1,'to':360,
      'with':409,'where':412,'which':413,'write':422,'you':429,'for':162,'had':197,'de':141}
inv = {v:k for k,v in TITUS.items()}
def stat(inv):
    n=0; diffs=[]
    for w,c in EV.items():
        if w in inv:
            d=c-inv[w]
            diffs.append((w,d))
            if 0<=d<=9: n+=1
    return n,diffs
obs,diffs=stat(inv)
print('Control 1: Evelyn words also in our Titus list:',len(diffs),' with 0<=shift<=9:',obs)
print(' shifts:',diffs)
codes=[c for c in TITUS if 100<=c<=430]; vals=[TITUS[c] for c in codes]
cnt=[];
for _ in range(20000):
    random.shuffle(vals)
    inv2=dict(zip(vals,codes))
    cnt.append(stat(inv2)[0])
print(' shuffled Titus values (20000): mean %.2f max %d ; >=obs: %d'%(sum(cnt)/len(cnt),max(cnt),sum(1 for c in cnt if c>=obs)))
# monotone test: is the shift non-decreasing inside each band?
# Control 2. spelled runs in f.10: share of letter runs (>=4 letters) that are English words or the place names of the siege
from toks import load
from key1646 import KEY
words=set()
for p in ('../src/evelyn4.txt','../src/hillier_uoft.txt'):
    for ln in open(p,encoding='utf8',errors='ignore'):
        for w in re.findall(r"[a-z]+",ln.lower().replace('ſ','s')):
            if len(w)>=3: words.add(w)
print(' word list size',len(words))
lines=load('../src/aay/f10_ct.txt')
flat=[t.rstrip('?') for toks in lines for t in toks]
letters={c:v for c,v in KEY.items() if c<100 and len(v)==1 and v.isalpha()}
def runs(letmap):
    out=[];cur=''
    for t in flat:
        if t.isdigit() and int(t) in letmap: cur+=letmap[int(t)]
        else:
            if len(cur)>=4: out.append(cur)
            cur=''
    if len(cur)>=4: out.append(cur)
    return out
def score(rs):
    good=0;tot=0
    for r in rs:
        tot+=len(r)
        # greedy: is the run a word, or a concatenation of two words of 3+ letters
        ok = r in words or any(r[:i] in words and r[i:] in words for i in range(3,len(r)-2)) or any(w.startswith(r) for w in words if len(w)>len(r))
        if ok: good+=len(r)
    return good/max(tot,1)
rs=runs(letters); print('Control 2: letter runs (>=4):',rs)
obs2=score(rs); print(' share of run letters in word runs: %.2f'%obs2)
cs=list(letters); vs=[letters[c] for c in cs]; res=[]
for _ in range(2000):
    random.shuffle(vs); res.append(score(runs(dict(zip(cs,vs)))))
print(' shuffled letter values (2000): mean %.3f max %.3f ; >=obs: %d'%(sum(res)/len(res),max(res),sum(1 for x in res if x>=obs2)))
