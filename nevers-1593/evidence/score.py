#!/usr/bin/env python3
"""score.py -- the mechanical score of PROTOCOL rule 8 (dictionary coverage and IC, against 400 controls).

Written by the REPRODUCE skeptic of the review panel of 14 October 2026. Copied into this folder with two changes
only: the paths, so that it runs from the repository, and the second word list (list B) is left out.
The same file stands in nevers-1593/evidence/ and in badalocchio-1593/evidence/.

For the decoded Italian of the cipher parts of each letter:
  cov3 = share of decoded letters that lie inside words of the word list with 3 letters or more
         (the most letters that non-overlapping dictionary words can cover; a group with no value is a break)
  cov4 = the same with words of 4 letters or more
  IC   = index of coincidence of the decoded letters
Controls (same pipeline): 200 decodes with the key's values shuffled within each table (letters, table 1,
table 2, endings), 200 decodes with the groups shuffled within each passage. Positive control: clear Italian
of the same writer (our own readings of the clear text, not editions), windows of the same number of letters.

Word list: wordlist_it.txt in this folder: the word forms of six Italian texts of Project Gutenberg (public
domain), seen 2 times or more, 3 letters or more. make_corpus.py rebuilds it. Nothing of the cipher passages
under test, and nothing of the positive-control texts, is in the list.

Run:  python3 score.py      (it needs nevers-1593/ and badalocchio-1593/ of this repository)
"""
import os, re, random, collections, statistics, sys


def norm_text(t):
    t = t.lower()
    for a, b in (('à', 'a'), ('è', 'e'), ('é', 'e'), ('ì', 'i'), ('ò', 'o'), ('ù', 'u'), ('j', 'i'), ('v', 'u')):
        t = t.replace(a, b)
    return t


def words_txt(t):
    return re.findall(r'[a-z]+', norm_text(t))


# ------------------------------------------------------------------ word list
HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
NEV = os.path.join(REPO, 'nevers-1593')
BAD = os.path.join(REPO, 'badalocchio-1593')
N = 200
SEED = 1014
DICT_A = set(l.strip() for l in open(os.path.join(HERE, 'wordlist_it.txt'), encoding='utf-8')
             if l.strip() and not l.startswith('#'))
MAXW = 22


def cover(stream, D, L):
    """most letters that non-overlapping words of D with L letters or more can cover; '#' is a break"""
    n = len(stream)
    best = [0] * (n + 1)
    for i in range(n - 1, -1, -1):
        b = best[i + 1]
        if stream[i] != '#':
            for j in range(i + L, min(n, i + MAXW) + 1):
                seg = stream[i:j]
                if '#' in seg:
                    break
                if seg in D:
                    b = max(b, j - i + best[j])
        best[i] = b
    return best[0]


def ic(s):
    s = [c for c in s if c.isalpha()]
    n = len(s)
    if n < 2:
        return float('nan')
    cnt = collections.Counter(s)
    return sum(v * (v - 1) for v in cnt.values()) / (n * (n - 1))


def scores(stream, D=DICT_A):
    letters = sum(1 for c in stream if c != '#')
    return {'n': letters, 'cov3': cover(stream, D, 3) / letters, 'cov4': cover(stream, D, 4) / letters,
            'ic': ic(stream)}


# ------------------------------------------------------------------ keys and texts
def read_key(path):
    key = {}
    for line in open(path, encoding='utf-8'):
        if line.startswith('#') or not line.strip() or line.startswith('group\t'):
            continue
        f = line.rstrip('\n').split('\t')
        key[f[0]] = (f[1], f[2])
    return key


def to_stream(groups, key):
    s = []
    for g in groups:
        v, kind = key.get(g, ('?', 'none'))
        if kind == 'null' or g in ('2', '199', '299'):      # counted as nulls, as the pages do
            continue
        if kind in ('letter', 'consonant', 'vowel', 'table1', 'table2', 'ending'):
            s.append(norm_text(v.split('/')[0]))
        else:
            s.append('#')
    return ''.join(s)


def shuffled_key(key, rnd):
    """values shuffled within each table (each 'kind' that carries text)"""
    new = dict(key)
    bykind = collections.defaultdict(list)
    for g, (v, kind) in key.items():
        if kind in ('letter', 'consonant', 'vowel', 'table1', 'table2', 'ending'):
            bykind['letter' if kind in ('consonant', 'vowel') else kind].append(g)
    for kind, gs in bykind.items():
        vals = [key[g][0] for g in gs]
        rnd.shuffle(vals)
        for g, v in zip(gs, vals):
            new[g] = (v, key[g][1])
    return new


def nevers_passages():
    key = read_key(os.path.join(NEV, 'key.tsv'))
    passages = collections.OrderedDict()
    for line in open(os.path.join(NEV, 'transcription.txt'), encoding='utf-8'):
        m = re.match(r'^(B\d)L\d: (.*)$', line.rstrip('\n'))
        if m:
            row = m.group(2)
            row = re.sub(r'\[[^\]]*\]', ' ', row).replace('^', ' ')
            row = re.sub(r'\{\?\}', ' ? ', row)
            row = re.sub(r'\{([^/}]+)/[^}]*\}', r'\1', row).replace('(', '').replace(')', '')
            passages.setdefault(m.group(1), []).extend(row.split())
    return key, list(passages.values())


def read_groups(path):
    d = collections.OrderedDict()
    for line in open(path, encoding='utf-8'):
        m = re.match(r'^(L[\d.]+): (.*)$', line.rstrip('\n'))
        if m:
            d[m.group(1)] = m.group(2).split()
    return d


def bad_passages(page):
    key = read_key(os.path.join(BAD, 'key.tsv'))
    if page == 'f080r':
        g = read_groups(os.path.join(BAD, 'groups.txt'))
        return key, [[x for gs in g.values() for x in gs]]           # the sheet is one passage
    g = read_groups(os.path.join(BAD, page, 'groups.txt'))
    return key, list(g.values())                                      # each cipher run is a passage


# ------------------------------------------------------------------ positive controls
def clear_nevers():
    t = open(os.path.join(NEV, 'cleartext_f72r.txt'), encoding='utf-8').read()
    t = '\n'.join(l for l in t.split('\n') if not l.startswith('#') and 'PASSAGE' not in l)
    t = t.replace('(?)', '').replace('[struck]', '').replace('[..]', '')
    t = t.replace('(', '').replace(')', '')
    return ''.join(words_txt(t))


def clear_badalocchio():
    t = open(os.path.join(BAD, 'evidence', 'clear_letter_f79.md'), encoding='utf-8').read().split('\n')
    a = t[t.index('## f. 79r'):]
    a = a[:[i for i, l in enumerate(a) if l.startswith('## What the page')][0]]
    txt = '\n'.join(l for l in a if not l.startswith('#'))
    txt = re.sub(r'\[[^\]]*\]', ' ', txt).replace('(?)', '')
    # the clear words of f. 85r and f. 65r
    for p in ('f085r', 'f065r'):
        for line in open(os.path.join(BAD, p, 'transcription.txt'), encoding='utf-8'):
            m = re.match(r'^L\d+: (.*)$', line)
            if m:
                txt += ' ' + ' '.join(w for w in m.group(1).split() if not re.search(r'[0-9<]', w))
    return ''.join(words_txt(txt))


def windows(text, n, step=None):
    step = step or max(1, n // 2)
    return [text[i:i + n] for i in range(0, len(text) - n + 1, step)]


# ------------------------------------------------------------------ run
def run(name, key, passages, clear, out, D=DICT_A, tag='A'):
    rnd = random.Random(SEED)
    join = lambda ps, k: '#'.join(to_stream(p, k) for p in ps)     # a passage ends a word
    real = scores(join(passages, key), D)
    ks = []
    for _ in range(N):
        k2 = shuffled_key(key, rnd)
        ks.append(scores(join(passages, k2), D))
    os_ = []
    for _ in range(N):
        ps = []
        for p in passages:
            q = p[:]
            rnd.shuffle(q)
            ps.append(q)
        os_.append(scores(join(ps, key), D))
    pos = [scores(w, D) for w in windows(clear, real['n'])]
    out.append(f'--- {name} (word list {tag}); decoded letters {real["n"]}')
    for m in ('cov3', 'cov4', 'ic'):
        bk, bo = max(x[m] for x in ks), max(x[m] for x in os_)
        mk, mo = statistics.mean(x[m] for x in ks), statistics.mean(x[m] for x in os_)
        beats = real[m] > max(bk, bo)
        if pos:
            pm, pmin, pmax = statistics.median(x[m] for x in pos), min(x[m] for x in pos), max(x[m] for x in pos)
            ptxt = f'positive control ({len(pos)} windows of clear text): median {pm:.3f} [{pmin:.3f}, {pmax:.3f}]'
        else:
            ptxt = 'positive control: clear text too short'
        out.append(f'  {m}: real {real[m]:.3f} | shuffled keys mean {mk:.3f} best {bk:.3f} | shuffled order mean {mo:.3f} '
                   f'best {bo:.3f} | real beats all {2*N} controls: {beats} | {ptxt}')
    return real


if __name__ == '__main__':
    out = []
    out.append(f'word list: wordlist_it.txt, {len(DICT_A)} forms (seen >= 2 times, >= 3 letters)')
    out.append(f'controls: {N} shuffled keys (values shuffled within each table) + {N} shuffled orders '
               f'(groups shuffled within each passage); seed {SEED}')
    out.append('NOTE: a group shuffle keeps the multiset of decoded letters, so it cannot change IC; IC is tested '
               'by the key shuffles only.')
    cn, cb = clear_nevers(), clear_badalocchio()
    out.append(f'positive-control texts: Nevers clear f. 72r without the two passages: {len(cn)} letters; '
               f'Badalocchio clear f. 79r-v + clear words of f. 85r and f. 65r: {len(cb)} letters')
    key, ps = nevers_passages()
    run('Nevers 1593 f. 72r, both passages', key, ps, cn, out)
    for p in ('f085r', 'f065r', 'f080r'):
        k, ps2 = bad_passages(p)
        run(f'Badalocchio {p}', k, ps2, cb, out)
    k, a = bad_passages('f085r'); _, b = bad_passages('f065r'); _, c = bad_passages('f080r')
    run('Badalocchio f085r+f065r+f080r', k, a + b + c, cb, out)
    print('\n'.join(out))
