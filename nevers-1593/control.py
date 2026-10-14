#!/usr/bin/env python3
"""control.py ITALIAN_TEXT -- the controls with shuffled keys and shuffled orders.

ITALIAN_TEXT is a large text file in Italian. The script keeps its letters only and counts its groups of four
letters. The second run used evidence/it_letters.txt (2,568,254 letters of six public-domain Italian texts of
Project Gutenberg; evidence/make_corpus.py rebuilds it):  python3 control.py evidence/it_letters.txt
The score of a text is the mean log10 probability of its groups of four letters. u and v are one letter.

C1: the letter values of the key, dealt at random to the 24 groups. 5,000 keys.
C2: the key as it is, and the groups of the text in a shuffled order. 5,000 orders.
C3: the key of passage 1 only, applied to passage 2; then 5,000 shuffled keys of passage 1 on passage 2.
C4: a free solver that knows nothing of the key, on the true order and on five shuffled orders.
C4 is a warning: for 139 letters a free key can make a text that is not Italian and scores as well as real Italian.
"""
import collections, math, random, statistics, sys
from decode import load_key, load_lines, letters


def model(path):
    t = ''.join(c for c in open(path, encoding='utf-8', errors='ignore').read().lower() if 'a' <= c <= 'z')
    t = t.replace('j', 'i').replace('k', 'c').replace('w', 'u').replace('v', 'u').replace('y', 'i')
    c = collections.Counter(t[i:i + 4] for i in range(len(t) - 3))
    n = sum(c.values())
    m = {k: math.log10(v / n) for k, v in c.items()}
    floor = math.log10(0.1 / n)
    return t, (lambda s: sum(m.get(s[i:i + 4], floor) for i in range(len(s) - 3)))


def solve(toks, score, restarts, iters, seed, slots='aaeeiioouunnlrrttsscdpmgbfhqz'):
    """a free key: each group takes one of the slots; two groups can end with the same letter"""
    rnd = random.Random(seed)
    syms = sorted(set(toks))
    ti = [syms.index(t) for t in toks]
    best = (-1e9, '')
    for r in range(restarts):
        perm = list(slots)
        rnd.shuffle(perm)
        cur = score(''.join(perm[i] for i in ti))
        for it in range(iters):
            a, b = rnd.randrange(len(syms)), rnd.randrange(len(perm))
            if a == b:
                continue
            perm[a], perm[b] = perm[b], perm[a]
            sc = score(''.join(perm[i] for i in ti))
            T = max(0.02, 0.6 * (1 - it / iters))
            if sc > cur or rnd.random() < math.exp((sc - cur) / T * 2.3):
                cur = sc
            else:
                perm[a], perm[b] = perm[b], perm[a]
        best = max(best, (cur, ''.join(perm[i] for i in ti)))
    return best


def report(name, x0, xs):
    m, sd = statistics.mean(xs), statistics.pstdev(xs)
    print('%s: mean %.2f, best %.2f; ours is %.1f sd above the mean' % (name, m, max(xs), (x0 - m) / sd))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    text, sc = model(sys.argv[1])
    key, rows = load_key()
    lines = load_lines()
    allt = [g for k in lines for g in letters(lines[k])]
    plain = ''.join(key[g] for g in allt)
    n4 = len(plain) - 3
    s0 = sc(plain) / n4
    print('text by our key:', plain)
    print('letters: %d; score: %.2f' % (len(plain), s0))
    rnd = random.Random(1)
    real = sorted(sc(text[q:q + len(plain)]) / n4 for q in (rnd.randrange(len(text) - len(plain)) for i in range(300)))
    print('real Italian of this length, 300 samples of the same text: median %.2f, worst %.2f' % (real[150], real[0]))
    rnd = random.Random(11)
    syms = sorted(set(allt))
    vals = [key[s] for s in syms]
    xs = []
    for i in range(5000):
        v = vals[:]
        rnd.shuffle(v)
        k = dict(zip(syms, v))
        xs.append(sc(''.join(k[t] for t in allt)) / n4)
    report('C1, 5000 shuffled keys on the %d groups' % len(syms), s0, xs)
    ys = []
    for i in range(5000):
        t = allt[:]
        rnd.shuffle(t)
        ys.append(sc(''.join(key[x] for x in t)) / n4)
    report('C2, our key, 5000 shuffled orders', s0, ys)
    b1 = [g for k in lines if k.startswith('B1') for g in letters(lines[k])]
    b2 = [g for k in lines if k.startswith('B2') for g in letters(lines[k])]
    k1 = {s: key[s] for s in set(b1)}

    def skip(txt):
        q = [txt[i:i + 4] for i in range(len(txt) - 3) if '?' not in txt[i:i + 4]]
        return sum(sc(x) for x in q) / len(q)

    p2 = ''.join(k1.get(t, '?') for t in b2)
    s2 = skip(p2)
    print('C3, passage 2 by the key of passage 1: %s' % p2)
    print('C3: %d of %d letter groups read; score %.2f' % (len(b2) - p2.count('?'), len(b2), s2))
    syms1 = sorted(k1)
    vals1 = [k1[s] for s in syms1]
    zs = []
    for i in range(5000):
        v = vals1[:]
        rnd.shuffle(v)
        k = dict(zip(syms1, v))
        zs.append(skip(''.join(k.get(t, '?') for t in b2)))
    report('C3, 5000 shuffled keys of passage 1 on passage 2', s2, zs)
    free = []
    for i in range(5):
        t = allt[:]
        rnd.shuffle(t)
        free.append(solve(t, sc, 10, 6000, i)[0] / n4)
    true, ftext = solve(allt, sc, 10, 6000, 99)
    print('C4, free solver on five shuffled orders: %s' % ', '.join('%.2f' % x for x in free))
    print('C4, free solver on the true order: %.2f (our reading: %.2f)' % (true / n4, s0))
    print('C4, its text: %s' % ftext)
    print('C4, places where its text has the letter of our reading: %d of %d' % (
        sum(x == y for x, y in zip(ftext, plain)), len(plain)))
