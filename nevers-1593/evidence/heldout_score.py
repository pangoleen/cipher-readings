#!/usr/bin/env python3
"""Held-out mechanical score: a key that was made on one text, applied with no change to another text.
H1: the key of the Nevers minute (f. 72r, 149 groups) on the Badalocchio sheet f. 80r (published cut).
H2: the key of the first Badalocchio page (key_first_page.tsv, made on f. 80r alone) on f. 85r and f. 65r
    (published new cut; the 2xy groups did not exist in that key and are breaks).
Same score and controls as score.py (200 key shuffles within each table, 200 group shuffles within each passage).
Written by the REPRODUCE skeptic of the review panel of 14 October 2026; copied into this folder with the
paths changed. It imports score.py of this folder.
"""
import sys, os
sys.dont_write_bytecode = True   # leave no cache folder in the repository
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import *

def fix_kinds(key):
    # key_first_page.tsv has kinds letter/syllable/word: map them to the tables of score.py
    out = {}
    for g, (v, k) in key.items():
        if k == 'letter': out[g] = (v, 'letter')
        elif k in ('syllable', 'word'):
            out[g] = (v, 'table1' if g.startswith('1') else 'table2')
        else: out[g] = (v, k)
    return out

out = []
nk = read_key(os.path.join(NEV, 'key.tsv'))
_, sheet = bad_passages('f080r')
gs = sheet[0]
have = sum(1 for g in gs if g in nk and nk[g][1] != 'null' and g != '?')
nn = sum(1 for g in gs if g in nk and nk[g][1] == 'null')
out.append(f'H1: f. 80r has {len(gs)} groups (published cut); the minute key gives a letter to {have} and a null to {nn}: '
           f'{have+nn} of {len(gs)} have a value ({100*(have+nn)/len(gs):.1f} %)')
run('H1: Nevers minute key on f. 80r', nk, sheet, clear_badalocchio(), out, DICT_A, 'A')
ok = fix_kinds(read_key(os.path.join(BAD, 'key_first_page.tsv')))
_, a = bad_passages('f085r'); _, b = bad_passages('f065r')
run('H2: first-page key (f. 80r only) on f. 85r + f. 65r, new cut', ok, a + b, clear_badalocchio(), out, DICT_A, 'A')
# H0: the key of passage 1 of the minute (only the groups that passage 1 has) on passage 2
nk2, nps = nevers_passages()
g1 = set(nps[0])
k1 = {g: (v, k) for g, (v, k) in nk2.items() if g in g1}
run('H0: key of minute passage 1 only, on passage 2', k1, [nps[1]], clear_nevers(), out, DICT_A, 'A')
print('\n'.join(out))
