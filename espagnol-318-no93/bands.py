# Control by the build of the code list: the first letter of a code word follows the first letter of its value.
# (A one-part code list has its words in the order of the alphabet.) The test: the rank correlation between the two
# first letters, against the same code words with their values shuffled 20,000 times.
# Run it in this folder:  python3 bands.py
import random
import key
AL='abcdefghijklmnopqrstuvxyz'
# The seven values that the audit of 11 October 2026 changed (evidence/audit.md).
BEFORE={'hog':('venecianos','C'),'ren':('estos','C'),'noe':('a','B')}
ADDED=('rud','mul')
def rank(xs):
    s=sorted(range(len(xs)),key=lambda i:xs[i]); r=[0]*len(xs); i=0
    while i<len(s):
        j=i
        while j+1<len(s) and xs[s[j+1]]==xs[s[i]]: j+=1
        for k in range(i,j+1): r[s[k]]=(i+j)/2
        i=j+1
    return r
def rho(a,b):
    ra,rb=rank(a),rank(b); n=len(a); ma=sum(ra)/n; mb=sum(rb)/n
    num=sum((x-ma)*(y-mb) for x,y in zip(ra,rb)); da=sum((x-ma)**2 for x in ra)**.5; db=sum((y-mb)**2 for y in rb)**.5
    return num/(da*db)
def test(codes,label,N=20000):
    c=[ord(k[0]) for k in codes]; v=[AL.index(codes[k][0]) for k in codes]
    r=rho(c,v); rng=random.Random(1); n=0
    for _ in range(N):
        w=v[:]; rng.shuffle(w)
        if rho(c,w)>=r: n+=1
    print('%-40s n=%2d  rho=%.3f  shuffled values that reach it: %d of %d'%(label,len(codes),r,n,N))
def outside(codes):
    return [(k,v) for k,v in sorted(codes.items()) if v[0] not in key.BAND[k[0]]]
if __name__=='__main__':
    now={k:v for k,(v,g) in key.CODES.items()}
    old={k:BEFORE.get(k,(v,''))[0] for k,v in now.items() if k not in ADDED}
    for name,C in (('key before the audit',old),('corrected key',now)):
        test(C,name+', all code words')
        bad=outside(C)
        print('   values outside the band of their code word: %d of %d: %s'%(len(bad),len(C),', '.join('%s = %s'%b for b in bad)))
    test({k:v for k,(v,g) in key.CODES.items() if g=='A'},'grade A only')
    print('bands:',key.BAND)
