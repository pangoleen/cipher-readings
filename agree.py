import sys, difflib, collections
sys.path.insert(0,'.')
from lib import load
def toks(line):
    out=[]
    for t in line:
        if t[0]=='clear': out.append('<clear>')
        else: out.append(t[1])
    return out
def main(fa,fb,show=True):
    A=dict(load(fa)); B=dict(load(fb))
    tot=agree=0; sign_tot=sign_ag=0; code_tot=code_ag=0; conf=collections.Counter()
    for lab in sorted(A):
        a=toks(A[lab]); b=toks(B.get(lab,[]))
        ka={i:t[0] for i,t in enumerate(A[lab])}
        sm=difflib.SequenceMatcher(None,a,b,autojunk=False)
        m=sum(bl.size for bl in sm.get_matching_blocks())
        n=max(len(a),len(b)); tot+=n; agree+=m
        diffs=[]
        for op,i1,i2,j1,j2 in sm.get_opcodes():
            if op=='equal':
                for i in range(i1,i2):
                    if ka[i]=='sign': sign_tot+=1; sign_ag+=1
                    elif ka[i]=='code': code_tot+=1; code_ag+=1
            else:
                for i in range(i1,i2):
                    if ka[i]=='sign': sign_tot+=1
                    elif ka[i]=='code': code_tot+=1
                diffs.append((' '.join(a[i1:i2]) or '-',' '.join(b[j1:j2]) or '-'))
                if i2-i1==1 and j2-j1==1: conf[(a[i1],b[j1])]+=1
        if show and diffs: print(lab, f'{m}/{n}', ' | '.join(f'{x} -> {y}' for x,y in diffs))
    print(f'TOTAL tokens agree {agree}/{tot} = {agree/tot:.1%}; signs(A) {sign_ag}/{sign_tot} = {sign_ag/sign_tot:.1%}; codes(A) {code_ag}/{code_tot} = {code_ag/code_tot:.1%}')
    print('confusions:',conf.most_common(40))
if __name__=='__main__': main(sys.argv[1],sys.argv[2])
