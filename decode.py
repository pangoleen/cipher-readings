#!/usr/bin/env python3
"""Apply the Tresnel key (BnF fr. 18009 f.156) to the consensus transcription; agreement of the two passes;
shuffled-key control with a French 4-gram model."""
import re, random, math, numpy as np
P1 = {l.split(':')[0]: l.split(':',1)[1].split() for l in open('pass1.txt') if re.match(r'L\d\d:', l)}
P2 = {}
for l in open('pass2_blind.txt'):
    if re.match(r'L\d\d:', l):
        k, v = l.split(':', 1)
        P2[k] = [t for t in v.split() if not t.startswith('?[') and not t.endswith(']') or t == '[clear]']
def clean(toks):
    return [t for t in toks if t not in ('|', '[clear]', '.') and not t.startswith('?') and not t.startswith('[') and not t.endswith(']') and t not in ('+','long','slash,','end','flourish','dot','slash')]
strict = lenient = total = 0
for k in sorted(P1):
    a, b = clean(P1[k]), clean(P2.get(k, []))
    if len(a) != len(b):
        print('length differs', k, len(a), len(b)); print(a); print(b)
    for x, y in zip(a, b):
        total += 1
        alts = y.split('/')
        strict += (alts[0] == x); lenient += (x in alts)
        if x not in alts or alts[0] != x: print(f'  {k}: pass1 {x:5s} pass2 {y}')
print(f'tokens {total}  strict agreement {strict} ({100*strict/total:.1f}%)  lenient {lenient} ({100*lenient/total:.1f}%)')

# key: sign name -> value, as read in fr. 18009 f.156 (column letter, row). '=' doubles the previous letter, '' null.
KEY = {'f':'a','del':'a','delx':'a','c':'b','3':'c','z':'c','Z':'c','J':'d','5':'d','L':'e','t':'e','g':'e','pi':'e',
 'C':'g','dd':'h','q':'i','ub':'i','x':'l','PI':'l','2':'m','ff':'m','s':'n','S':'n','xi':'n','sl':'o','ss':'o','mu':'o',
 'Zb':'p','$':'p','o':'q','ep':'r','nb':'s','th':'s','ot':'t','gam':'t','ob':'t','eta':'u','w':'u','H':'u','6':'y',
 'n_':'LE ','y_':'IL ','c_':'LA ','86':'QUE ','89':'QUIL ','T':'=','DBL':'=','oo':''}
# consensus transcription (differences settled on the images and by the key; see NOTES.md)
CONS = {
'L01': '86 n_ | J w z | J g | 2 mu s ot del n_ mu xi | del w sl q gam | ff f s 5 pi | 86 | th del | 2 del q L th ot t',
'L02': 'del eta mu ub ob | H xi | th 6 | C ep del s J T | t th w mu 6 L 2 L s gam | dd del w x ot | g gam | c delx nb | 89 | z ep mu 6',
'L03': 'ss q ot | 86 L x n_ | xi g | $ mu w T sl q ot | Zb del th DBL t ep',
'L05': 'del | J mu s | $ g J ep mu | oo oo',
'L07': 'Z del ep | o w del s ot',
'L08': 'y_ n_ th | delx | w L eta | 2 del x | f PI n_ ep | y_ del | $ mu ep ot g',
'L09': 'y_ n_ | J q th $ mu nb L | del | c_ | $ del q th',
'L10': 'f S g del xi ot q ep | c_ w z ot mu ep q gam L',
'L11': 'J w | ep mu 6 | L s | 3 t | $ del 6 th | oo oo'}  # a tall cross with three bars follows the nulls: end mark, left out
def dec(key, show=True):
    out = {}
    for k, v in CONS.items():
        s = ''
        for t in v.split():
            if t == '|': s += ' '; continue
            val = key[t]
            if val == '=': s += s.rstrip()[-1] if s.strip() else ''
            else: s += val
        out[k] = re.sub(' +', ' ', s).strip()
    return out
plain = dec(KEY)
for k, v in plain.items(): print(k, v)
open('decoded_by_key.txt', 'w').write('\n'.join(f'{k}: {v}' for k, v in plain.items()) + '\n')

# control: French 4-gram score of the true key against keys with shuffled letter values
q = np.load('../corpus/fr_4.npy')
q = q.reshape(26, 26, 26, 26) if q.ndim == 1 else q
def score(out):
    s = ''.join(out.values()).lower(); s = re.sub('[^a-z]', '', s)
    idx = [ord(c) - 97 for c in s]
    return sum(q[idx[i], idx[i+1], idx[i+2], idx[i+3]] for i in range(len(idx) - 3)) / (len(idx) - 3)
true = score(plain)
letters = [k for k, v in KEY.items() if len(v) == 1 and v != '=']
random.seed(1616); sc = []
for _ in range(2000):
    vals = [KEY[k] for k in letters]; random.shuffle(vals)
    K = dict(KEY); K.update(dict(zip(letters, vals)))
    sc.append(score(dec(K)))
sc = np.array(sc)
print(f'4-gram score per 4-gram: true key {true:.3f}; 2000 shuffled keys mean {sc.mean():.3f} sd {sc.std():.3f} max {sc.max():.3f}; z = {(true-sc.mean())/sc.std():.1f}')
