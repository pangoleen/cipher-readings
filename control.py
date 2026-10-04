"""Wrong-key control: trigram score of the decoded letter stream with the real key and with 500 shuffled keys.
python3 control.py c4 es passes/perez_passA.txt      (Cipher 4, Spanish model)
python3 control.py c2 it passes/f273r_passA.tsv ...  (Cipher 2, Italian or Spanish model)"""
import sys, re, random, numpy as np
kind,lang,files=sys.argv[1],sys.argv[2],sys.argv[3:]
T=np.load(f'corpus/{lang}_3.npy')
def score(s):
    s=re.sub(r'\[[^\]]*\]|<[^>]*>|\{[^}]*\}','',s)          # drop codes, unread signs, plain words
    s=re.sub(r'[^a-z]','',s.lower().replace('ñ','n').replace('ç','c'))
    ix=[ord(c)-97 for c in s]
    if len(ix)<3: return float('nan'),0
    return float(np.mean([T[a,b,c] for a,b,c in zip(ix,ix[1:],ix[2:])])),len(ix)
if kind=='c4':
    import c4 as K
    txt=' '.join(' '.join(re.findall(r'<<(.*?)>>',open(f,encoding='utf-8').read(),re.S)) for f in files)
    dec=lambda alpha,vow: K.dec(txt,alpha=alpha,vow=vow)
else:
    import c2 as K
    lines=[]
    for f in files:
        for l in open(f,encoding='utf-8'):
            if l.startswith('L'): lines.append(l.rstrip('\n').partition('\t')[2])
    txt=' '.join(lines)
    dec=lambda alpha,vow: K.dec_line(txt,alpha=alpha,vow=vow)
real,n=score(dec(K.ALPHA,K.VOW))
random.seed(132); null=[]; null2=[]
ks=list(K.ALPHA); vk=list(K.VOW)
for i in range(500):
    vs=[K.ALPHA[k] for k in ks]; random.shuffle(vs); a=dict(zip(ks,vs))
    null.append(score(dec(a,K.VOW))[0])
    vv=[K.VOW[k] for k in vk]; random.shuffle(vv)
    null2.append(score(dec(a,dict(zip(vk,vv))))[0])
for name,nl in (('letters shuffled, vowel marks kept',null),('letters and vowel marks shuffled',null2)):
    nl=np.array(nl); print(f'{kind} {lang} N={n} letters: real {real:.3f} | {name}: mean {nl.mean():.3f} sd {nl.std():.3f} max {nl.max():.3f} | z = {(real-nl.mean())/nl.std():.1f} | keys >= real: {(nl>=real).sum()}/500')
