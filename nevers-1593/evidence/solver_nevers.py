#!/usr/bin/env python3
"""Extra control for the short Nevers text (139 letters): a FREE solver that fits a key to maximise cov3
(word list A), run on the true order and on 10 shuffled orders. If fitting on nonsense reaches the score of the
published key, then cov3 at this length shows only that the key is not random, not that it is right.
Written by the REPRODUCE skeptic of the review panel of 14 October 2026; copied into this folder with the
paths changed. It imports score.py of this folder.
"""
import sys, os, random
sys.dont_write_bytecode = True   # leave no cache folder in the repository
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import *
ALPH = 'abcdefghilmnopqrstuz'
key, ps = nevers_passages()
LG = sorted(g for g, (v, k) in key.items() if k in ('vowel', 'consonant'))
def stream_of(ps, assign):
    out = []
    for p in ps:
        s = ''
        for g in p:
            if g == '0': continue
            s += assign.get(g, '#')
        out.append(s)
    return '#'.join(out)
def f(ps, a): 
    st = stream_of(ps, a); n = sum(1 for c in st if c != '#'); return cover(st, DICT_A, 3) / n
def solve(ps, rnd, restarts=4, iters=3000):
    best_all = (-1, None)
    for r in range(restarts):
        a = {g: rnd.choice(ALPH) for g in LG}; sc = f(ps, a)
        for it in range(iters):
            b = dict(a)
            if rnd.random() < 0.5: b[rnd.choice(LG)] = rnd.choice(ALPH)
            else:
                x, y = rnd.sample(LG, 2); b[x], b[y] = b[y], b[x]
            s2 = f(ps, b)
            if s2 >= sc: a, sc = b, s2
        if sc > best_all[0]: best_all = (sc, a)
    return best_all
rnd = random.Random(1014)
pub = {g: norm_text(key[g][0]) for g in LG}
print(f'published key, true order: cov3 {f(ps, pub):.3f}')
sc, a = solve(ps, rnd)
print(f'free solver, true order: cov3 {sc:.3f}; letters equal to the published key in {sum(a[g]==pub[g] for g in LG)} of {len(LG)} groups')
print('   text:', stream_of(ps, a))
res = []
for i in range(10):
    q = [p[:] for p in ps]
    for p in q: rnd.shuffle(p)
    sc, a = solve(q, rnd)
    res.append(sc); print(f'free solver, shuffled order {i+1}: cov3 {sc:.3f}   {stream_of(q, a)[:80]}')
print(f'shuffled orders: best {max(res):.3f}, mean {sum(res)/len(res):.3f}')
