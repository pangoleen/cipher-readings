import csv
from toks import load
rows=[r for r in csv.reader(open('../key1646.tsv'),delimiter='\t') if r and not r[0].startswith('#') and r[0]!='code']
K={int(r[0]):(r[1],r[2],int(r[3])) for r in rows}
OUTSIDE={572,512,342,614,629,562,329,647,681}
lines=load('../src/aay/f10_ct.txt')
out=[]
for i,toks in enumerate(lines,1):
    o=[]
    for t in toks:
        if t.startswith('['): o.append('{'+t[1:-1]+'}'); continue
        q=t.rstrip('?')
        if not q.isdigit(): o.append('<illegible>'); continue
        n=int(q); v,g,c=K[n]
        mark=''
        if g=='U': v='<%d>'%n if v=='[%d]'%n else '<%s>'%v.strip('[]')
        elif '?' in g or v.endswith('?'): mark='(?)'; v=v.rstrip('?')
        elif g=='C' and n>=100 and c==1 and n not in OUTSIDE and v not in '_.,': mark='(?)'
        if t.endswith('?'): mark='(?)'
        o.append(v+mark)
    out.append('%2d  '%i+' '.join(o))
open('../reading_f10_tokens.txt','w').write(
'# BL Add MS 72438 f.10, 13 May 1646. Token-by-token decipher with key1646.tsv.\n'
'# Cipher text: transcription of A. Aymeloglu (github.com/aaymeloglu/unsolved-ciphers, royalist-1646/f10_ct.txt, commit d2800bb2), one pass, not ours; we saw no image.\n'
'# {..} = clear words of the manuscript as he read them; _ = null; . , = stop signs; <n> = code not read; (?) = doubtful; <illegible> = his "?".\n'
+'\n'.join(out)+'\n')
print('\n'.join(out))
