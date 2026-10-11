# Control of the sign key: the score of the decoded text against the same transcription with a shuffled key.
# Score = mean log-probability per group of five letters, on a table of Spanish five-letter groups.
# The table (lm5.npy, 47 MB) is too large for the repository. Give its path:  python3 control.py PATH/lm5.npy
# Shuffled key = the letter values permuted among the sign types, 500 times.
import sys, random, numpy as np
from lib import toks, FINAL, PASS_A, PASS_B
import key
LM=np.load(sys.argv[1])
def segs(files,k,codes=True):
    S=[];cur=[]
    for lab,kind,b in toks(files):
        v=None
        if kind in('sign','group') and b in k: v=k[b]
        elif codes and kind=='code' and b in key.CODES and key.CODES[b][1] in 'AB': v=key.CODES[b][0]
        if v and v.isalpha(): cur.extend(v)
        else:
            if len(cur)>=5: S.append(cur)
            cur=[]
    if len(cur)>=5: S.append(cur)
    return S
def score(S):
    tot=0;n=0
    for s in S:
        a=np.array([ord(c)-97 for c in s]); tot+=LM[a[:-4],a[1:-3],a[2:-2],a[3:-1],a[4:]].sum(); n+=len(a)-4
    return tot/n,n
K={s:v[0] for s,v in key.KEY.items()}
def run(files,codes,N=500,seed=1):
    rnd=random.Random(seed); t,n=score(segs(files,K,codes))
    signs=list(K); vals=[K[s] for s in signs]; ctl=[]
    for i in range(N):
        v=vals[:]; rnd.shuffle(v); ctl.append(score(segs(files,dict(zip(signs,v)),codes))[0])
    ctl=np.array(ctl)
    return f"key {t:.2f} (n={n} groups); {N} shuffled keys: mean {ctl.mean():.2f}, best {ctl.max():.2f}; {int((ctl>=t).sum())} of {N} reach the key"
if __name__=='__main__':
    for name,f in (('settled',FINAL),('pass A',PASS_A),('pass B',PASS_B)):
        print(f"{name}, signs and code words (grades A, B): {run(f,True)}")
        print(f"{name}, signs only: {run(f,False)}")
