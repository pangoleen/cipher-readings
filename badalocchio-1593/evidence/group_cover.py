#!/usr/bin/env python3
"""Group-level mechanical count beside the hand counts of the pages: the share of the groups that carry text
whose decoded letters all lie inside words of word list A (3+ letters, and 4+ letters).
Uses score.py for the word list and the published groups.
Written by the REPRODUCE skeptic of the review panel of 14 October 2026; copied into this folder with the
paths changed. It imports score.py of this folder.
"""
import sys, os
sys.dont_write_bytecode = True   # leave no cache folder in the repository
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from score import *

def covered_positions(stream, D, L):
    n = len(stream); best = [0]*(n+1); choice = [None]*(n+1)
    for i in range(n-1, -1, -1):
        b, c = best[i+1], None
        if stream[i] != '#':
            for j in range(i+L, min(n, i+MAXW)+1):
                seg = stream[i:j]
                if '#' in seg: break
                if seg in D and j-i+best[j] > b: b, c = j-i+best[j], j
        best[i], choice[i] = b, c
    cov, i = set(), 0
    while i < n:
        if choice[i]: cov.update(range(i, choice[i])); i = choice[i]
        else: i += 1
    return cov

def group_count(groups, key, D, L):
    spans, s = [], ''
    for g in groups:
        v, kind = key.get(g, ('?', 'none'))
        if kind == 'null' or g in ('2', '199', '299'): continue
        t = norm_text(v.split('/')[0]) if kind in ('letter','consonant','vowel','table1','table2','ending') else '#'
        spans.append((len(s), len(s)+len(t), t)); s += t
    cov = covered_positions(s, D, L)
    inw = sum(1 for a, b, t in spans if t != '#' and all(p in cov for p in range(a, b)))
    return inw, len(spans)

if __name__ == '__main__':
    key, ps = nevers_passages()
    for L in (3, 4):
        a = n = 0
        for q in ps:
            x, y = group_count(q, key, DICT_A, L); a += x; n += y
        print(f'Nevers f. 72r, words of {L}+ letters: {a} of {n} groups that carry text ({100*a/n:.1f} %)')
    for p in ('f085r', 'f065r', 'f080r'):
        k, ps2 = bad_passages(p)
        for L in (3, 4):
            # a run is cut at its ends: score each run (passage) alone, as the words do not cross clear text
            a = n = 0
            for q in ps2:
                x, y = group_count(q, k, DICT_A, L); a += x; n += y
            print(f'Badalocchio {p}, words of {L}+ letters: {a} of {n} groups that carry text ({100*a/n:.1f} %)')
