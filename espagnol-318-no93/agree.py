# Agreement of the two transcription passes, token by token. A doubt mark "?" is ignored.
# Run it in this folder:  python3 agree.py [-v]
import sys, difflib, collections
from lib import load, PASS_A, PASS_B
def norm(toks): return [(k,b) for k,b,q in toks if k!='clear']
def agree(fa,fb,show=False):
    A=dict(load(fa)); B=dict(load(fb)); tot=collections.Counter(); ok=collections.Counter()
    for lab in sorted(A):
        a=norm(A[lab]); b=norm(B.get(lab,[]))
        for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
            for x in a[i1:i2]:
                kind='code' if x[0]=='code' else 'sign'; tot[kind]+=1
                if op=='equal': ok[kind]+=1
            if op!='equal' and show: print(lab,' A:',' '.join(x[1] for x in a[i1:i2]),' | B:',' '.join(x[1] for x in b[j1:j2]))
    return tot,ok
if __name__=='__main__':
    for fa,fb in zip(PASS_A,PASS_B):
        tot,ok=agree(fa,fb,show='-v' in sys.argv)
        T=sum(tot.values()); O=sum(ok.values())
        print(f"{fa}: tokens {T}, agree {O} = {100*O/T:.1f} %; signs {ok['sign']}/{tot['sign']} = {100*ok['sign']/tot['sign']:.1f} %; code words {ok['code']}/{tot['code']} = {100*ok['code']/tot['code']:.1f} %")
