#!/usr/bin/env python3
"""Share of the 200 shuffled keys (same seed as score.py) whose decode has an IC above the real IC.
Written by the REPRODUCE skeptic of the review panel of 14 October 2026; copied into this folder with the
paths changed. It imports score.py of this folder.
"""
import sys, os, random
sys.dont_write_bytecode = True   # leave no cache folder in the repository
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import *
def j(ps, k): return '#'.join(to_stream(p, k) for p in ps)
sets = [('Nevers',) + nevers_passages()] + [(p,) + bad_passages(p) for p in ('f085r', 'f065r', 'f080r')]
for name, key, ps in sets:
    rnd = random.Random(SEED); r = ic(j(ps, key))
    xs = [ic(j(ps, shuffled_key(key, rnd))) for _ in range(N)]
    print(f'{name}: real IC {r:.4f}; {sum(x > r for x in xs)} of {N} shuffled keys have a higher IC')
