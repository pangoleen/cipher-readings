import sys, random, numpy as np
sys.path.insert(0,'.')
from lib import load
from key import KEY, CODES
LM=np.load('src/lm5.npy')
def letters(f, key):
    segs=[]; cur=[]
    for lab,toks in load(f):
        for t in toks:
            if t[0]=='sign' and t[1] in key: cur.extend(key[t[1]])
            elif t[0]=='code' and t[1] in ('otto','malz'): cur.extend(CODES[t[1]][0])
            else:
                if len(cur)>=5: segs.append(cur)
                cur=[]
    if len(cur)>=5: segs.append(cur)
    return segs
def score(segs):
    tot=0;n=0
    for s in segs:
        a=np.array([ord(c)-97 for c in s])
        tot+=LM[a[:-4],a[1:-3],a[2:-2],a[3:-1],a[4:]].sum(); n+=len(a)-4
    return tot/n,n
rnd=random.Random(1)
for f in sys.argv[1:]:
    t,n=score(letters(f,KEY))
    signs=list(KEY); vals=[KEY[s] for s in signs]; ctl=[]
    for i in range(200):
        v=vals[:]; rnd.shuffle(v); ctl.append(score(letters(f,dict(zip(signs,v))))[0])
    ctl=np.array(ctl)
    print(f"{f}: key {t:.2f} per 5-gram (n={n}); shuffled keys: mean {ctl.mean():.2f}, best {ctl.max():.2f}, {int((ctl>=t).sum())}/200 at or above the key")
