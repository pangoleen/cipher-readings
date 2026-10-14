#!/usr/bin/env python3
"""Try to repeat control 6 of the Badalocchio README (four-letter score) with a four-letter table built here
from nevers-1593/evidence/it_letters.txt (2,568,254 letters of six Italian texts of Project Gutenberg).
Score = mean log10 probability of the four-letter windows inside the decoded runs (a group with no value breaks).
Written by the REPRODUCE skeptic of the review panel of 14 October 2026; copied into this folder with the
paths changed. It imports score.py of this folder.
"""
import sys, os, math, collections, random, statistics
sys.dont_write_bytecode = True   # leave no cache folder in the repository
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import read_key, bad_passages, norm_text, shuffled_key, NEV
t = ''.join(c for c in open(os.path.join(NEV, 'evidence', 'it_letters.txt'), encoding='utf-8', errors='ignore').read().lower() if 'a' <= c <= 'z')
t = t.replace('j', 'i').replace('k', 'c').replace('w', 'u').replace('v', 'u').replace('y', 'i')
c = collections.Counter(t[i:i+4] for i in range(len(t)-3)); n = sum(c.values())
M = {k: math.log10(v/n) for k, v in c.items()}; FL = math.log10(0.1/n)
def segs(groups, key):
    s = ''
    for g in groups:
        v, kind = key.get(g, ('?', 'none'))
        if kind == 'null' or g in ('2', '199', '299'): continue
        s += norm_text(v.split('/')[0]).replace('j','i') if kind in ('letter','table1','table2','ending') else '#'
    return [x for x in s.split('#')]
def score(passages, key):
    tot = w = 0
    for p in passages:
        for sg in segs(p, key):
            for i in range(len(sg)-3): tot += M.get(sg[i:i+4], FL); w += 1
    return tot / w, w
key, a = bad_passages('f085r'); _, b = bad_passages('f065r'); _, f80 = bad_passages('f080r')
r, w = score(a + b, key)
rnd = random.Random(1014)
ks = [score(a + b, shuffled_key(key, rnd))[0] for _ in range(2000)]
os_ = []
for _ in range(2000):
    q = [p[:] for p in a + b]
    for p in q: rnd.shuffle(p)
    os_.append(score(q, key)[0])
sd = lambda xs: statistics.pstdev(xs)
print(f'f. 85r + f. 65r: {r:.3f} on {w} windows')
print(f'  2000 shuffled keys: mean {statistics.mean(ks):.3f}, best {max(ks):.3f}; real is {(r-statistics.mean(ks))/sd(ks):.1f} sd above')
print(f'  2000 shuffled orders: mean {statistics.mean(os_):.3f}, best {max(os_):.3f}; real is {(r-statistics.mean(os_))/sd(os_):.1f} sd above')
r8, w8 = score(f80, key); print(f'f. 80r: {r8:.3f} on {w8} windows')
