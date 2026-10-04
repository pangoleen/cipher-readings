# Controls for the ring model.
import random, csv, collections
from model import RING, ALPHA, table
rows = list(csv.DictReader(open("alignment.tsv"), delimiter="\t"))
obs = []   # (alphabet, number, crib letter) for every letter group with a single crib letter
for r in rows:
    if r["status"] == "OPEN": continue
    m = r["minute_letter"]; n = int(r["number"])
    if r["status"] == "SPELLING": m = r["model_letter"]
    if len(m) != 1 or m == "-": continue
    if n == 6: continue            # outside the ring
    obs.append((int(r["alphabet"]), n, m))
print("letter groups with one crib letter, number inside the ring:", len(obs))
def score(ring, offs):
    s = 0
    for k, n, m in obs:
        if ALPHA[(ring.index(n) - offs[k]) % 24] == m: s += 1
    return s
true = score(RING, {1: 0, 2: 1, 3: 2, 5: 4})
print("ring model, offsets k-1 (no free parameter per alphabet):", true)
# control 1: random rings, best offset chosen freely for each alphabet
random.seed(1653)
best = collections.Counter()
for trial in range(5000):
    ring = RING[:]; random.shuffle(ring)
    tot = 0
    for k in (1, 2, 3, 5):
        tot += max(sum(1 for kk, n, m in obs if kk == k and ALPHA[(ring.index(n) - o) % 24] == m) for o in range(24))
    best[tot] += 1
print("5000 random rings with the best offset per alphabet: max =", max(best), " mean = %.1f" % (sum(k * v for k, v in best.items()) / 5000))
# control 2: out-of-sample. Ring and step fixed from alphabets 2 and 5 only; alphabets 1 and 3 predicted.
o13 = [(k, n, m) for k, n, m in obs if k in (1, 3)]
hit = sum(1 for k, n, m in o13 if table(k).get(n) == m)
print("alphabets 1 and 3 predicted from 2 and 5: %d of %d groups fit" % (hit, len(o13)))
# control 3: one number, one value inside each alphabet
val = collections.defaultdict(collections.Counter)
for k, n, m in obs: val[(k, n)][m] += 1
multi = {kn: dict(c) for kn, c in val.items() if len(c) > 1}
print("pairs (alphabet, number) seen:", len(val), " with more than one crib letter:", multi)
