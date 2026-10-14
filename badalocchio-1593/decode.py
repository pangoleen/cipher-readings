#!/usr/bin/env python3
"""decode.py -- cut the three transcriptions into groups and apply the key table (key.tsv).

Run it in any folder:  python3 decode.py            (add  --no-shuffles  to leave out the slow part)

The three letters, all from BnF fr. 4700:
  f085r/transcription.txt   f. 85r, 5 December 1592: clear words and cipher in the same lines
  f065r/transcription.txt   f. 65r, 11 December 1592: a clear letter with two cipher runs
  transcription.txt         f. 80r, 9(?) January 1593: a sheet of 18 lines, all in figures
and heldout_f83r.txt, one short cipher passage in the clear letter of 6 February 1593 (f. 83r).

The script prints each line: the clear words as they stand, and each cipher run with its groups and their values.
Then it prints the counts, the agreement of the transcription passes, and the controls that need no other file:
the held-out test (the key and the cut of the first page, applied to f. 85r and f. 65r), the two halves of
f. 85r, and the order of the alphabet in the two word tables. It writes groups.txt and decoded_by_key.txt for
each letter. It needs Python 3.8 or later and no other package.

In the output: a raised dot = a null; a letter = a group for one letter; CAPITALS = a group for a word or a
syllable; a word with ? = a value that is a guess; [132] = a group with no value; [.143] = a name group (the
dotted stroke and the figures 1 4 3); [2] = a lone 2; { } = a cipher run in a line that has clear words too.

The script does not make the reading. The word division, the Italian and the translation of the reading files
are the work of a reader. The script shows only what the key gives for each group.
"""
import collections, difflib, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))

# (name, folder of the files, label of a run: 'line' = L1, 'run' = L5.1)
SHEETS = [('f085r', 'f085r', 'run'), ('f065r', 'f065r', 'run'), ('f080r', '', 'line')]
TITLE = {'f085r': 'f. 85r, 5 December 1592', 'f065r': 'f. 65r, 11 December 1592', 'f080r': 'f. 80r, 9(?) January 1593',
         'f083r': 'f. 83r, 6 February 1593 (one passage)'}

# ---------------------------------------------------------------- the cut rule
# A row of figures has no gaps. The rule:
#   a sign in < >                  one group
#   the dotted stroke i            with the next three figures 1xy: a name group, written .1xy
#                                  (two places of f. 80r have only two figures after the stroke: .38 and .78)
#   1 + two more figures           one group of table 1 (1xy)
#   2 + two more figures           one group of table 2 (2xy)
#   4, 8 or 9 + one figure (3-9)   one group: a letter
#   3 5 6 7                        one figure alone: the vowels a i o u
#   0                              one figure alone: a null
#   a lone 2                       taken only where "2xy" would give a group that is not in the tables and "2" with
#                                  the next groups gives groups that are. Six places in all. What it is, is open.
#   a lone 1                       two places (f. 85r line 13; f. 80r line 18, in the filler): no value
# The lone 2 is the one free choice of the rule. cut() takes, for each run, the division that leaves the fewest
# groups that are not in the tables; with the same number, the division with fewer lone 2.
# IN_TABLES below adds three groups that have no value but that the cut must know: 199 and 299 stand alone
# between clear words on f. 85r, so they are groups; the lone 2 is the free choice.
CUT_ONLY = ('2', '199', '299')


def load_key(path=None):
    """key.tsv -> ({group: value}, rows). A null has the value ''. A group with no value is not in the dict."""
    key, rows = {}, []
    for l in open(path or os.path.join(HERE, 'key.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('group\t') or not l.strip():
            continue
        c = l.rstrip('\n').split('\t')
        rows.append(c)
        if c[1] != '?':
            key[c[0]] = '' if c[1] == '·' else c[1]
    return key, rows


def in_tables(key, rows):
    """the groups that the cut takes as groups of the cipher: every group with a value, the name groups with
    three figures, and 2, 199, 299"""
    return set(key) | set(CUT_ONLY) | set(r[0] for r in rows if r[2] == 'name' and len(r[0]) == 4)


def lex(s):
    """a run -> items: figures (also ? for a figure that is not read), i for the dotted stroke, signs <..>"""
    s = re.sub(r'[()\s]', '', s)
    items, i = [], 0
    while i < len(s):
        if s[i] == '<':
            j = s.index('>', i)
            items.append(s[i:j + 1])
            i = j + 1
        else:
            items.append(s[i])
            i += 1
    return items


def cut(s, known):
    it = lex(s)
    n = len(it)
    best = [(10 ** 9, None)] * (n + 1)
    best[n] = (0, None)

    def dig(j):
        return j < n and len(it[j]) == 1 and it[j] in '0123456789?'

    for p in range(n - 1, -1, -1):
        c, opts = it[p], []
        if c.startswith('<'):
            opts.append((c, 1))
        elif c == 'i':
            if dig(p + 1) and it[p + 1] == '1' and dig(p + 2) and dig(p + 3):
                opts.append(('.' + ''.join(it[p + 1:p + 4]), 4))
            elif dig(p + 1) and dig(p + 2):
                opts.append(('.' + ''.join(it[p + 1:p + 3]), 3))
            else:
                opts.append(('i', 1))
        elif c in '12':
            if dig(p + 1) and dig(p + 2):
                opts.append((''.join(it[p:p + 3]), 3))
            opts.append((c, 1))
        elif c in '489':
            if dig(p + 1) and it[p + 1] in '3456789':
                opts.append((c + it[p + 1], 2))
            else:
                opts.append((c, 1))
        else:
            opts.append((c, 1))
        best[p] = min(((best[p + l][0] + (0 if g in known else 100) + (1 if g == '2' else 0), (g, l)) for g, l in opts),
                      key=lambda x: x[0])
    out, p = [], 0
    while p < n:
        g, l = best[p][1]
        out.append(g)
        p += l
    return out


# ---------------------------------------------------------------- the lines: clear words and cipher runs
ST = r'(?:<[^>]*>|\([0-9|?]\)|[0-9?]|i(?=[0-9(]))'       # a figure, a sign, or the dotted stroke before a figure
RUN = re.compile('(' + ST + r'(?:' + ST + r'|\s(?=[0-9<(]))*)')


def load_rows(name):
    """a file with rows 'L1: ...' -> {line: text}; the first row of each line counts"""
    out = collections.OrderedDict()
    for l in open(os.path.join(HERE, name), encoding='utf-8'):
        m = re.match(r'(L\d+):\s*(.*)', l.strip())
        if m and m.group(1) not in out:
            out[m.group(1)] = m.group(2).strip()
    return out


def parts(text):
    """one line -> [('clear', words) | ('run', figures) | ('lone', figures)].
    A run has three figures or more. 'lone' is one group 199 or 299 that stands alone between clear words."""
    out, buf = [], ''
    for j, p in enumerate(RUN.split(text)):
        if j % 2 == 1 and re.search(r'[0-9]{3}', re.sub(r'[()<>a-zA-Z+_ ]', '', p)):
            if buf.strip():
                out.append(('clear', buf.strip()))
            buf = ''
            f = re.sub(r'[() ]', '', p)
            out.append(('lone' if f in ('199', '299') else 'run', f))
        else:
            buf += p                                  # clear words, and marks like (?) after a word
    if buf.strip():
        out.append(('clear', buf.strip()))
    return out


def load_sheet(name, known):
    """-> [(line, [(kind, text, label, groups)])]; label and groups are set for 'run' and 'lone'"""
    folder, style = [(f, s) for n, f, s in SHEETS if n == name][0]
    out = []
    for line, text in load_rows(os.path.join(folder, 'transcription.txt')).items():
        n, row = 0, []
        for kind, t in parts(text):
            if kind == 'run':
                n += 1
                row.append((kind, t, line if style == 'line' else '%s.%d' % (line, n), cut(t, known)))
            elif kind == 'lone':
                row.append((kind, t, line, [t]))
            else:
                row.append((kind, t, None, None))
        out.append((line, row))
    return out


def runs(sheet):
    """the cipher runs of a sheet: [(label, groups)]"""
    return [(lab, g) for line, row in sheet for kind, t, lab, g in row if kind == 'run']


def show(g, key, grade=None):
    if g not in key:
        return '[' + g + ']'
    v = key[g]
    if v == '':
        return '·'
    return (v.upper() if len(v) > 1 else v) + ('?' if grade and grade.get(g) == 'guess' else '')


def decode(groups, key, grade=None):
    return ' '.join(show(g, key, grade) for g in groups)


def counted_null(g, key):
    """a null, or a group that the counts take as a null: a lone 2, 199, 299"""
    return key.get(g) == '' or g in CUT_ONLY


def counts(groups, key, rows):
    """the counts of a list of groups"""
    names = set(r[0] for r in rows if r[2] == 'name')
    c = collections.OrderedDict()
    c['groups'] = len(groups)
    c['nulls'] = sum(1 for g in groups if key.get(g) == '')
    c['lone 2'] = groups.count('2')
    c['199 and 299'] = groups.count('199') + groups.count('299')
    c['carry text'] = sum(1 for g in groups if not counted_null(g, key))
    c['letters and words'] = sum(1 for g in groups if key.get(g))
    c['names'] = sum(1 for g in groups if g in names)
    c['no value'] = sum(1 for g in groups if g not in key and g not in names and g not in CUT_ONLY)
    return c


# ---------------------------------------------------------------- the hand count of the connected sense
# NOT_IN_SENSE: the groups of f. 85r and f. 65r that stand in no word that we translate, run by run. It is a
# list by hand, by the first reader. A group that carries text and is not in this list counts as "in sense".
NOT_IN_SENSE = {
    'f085r': {'L5.1': [['.143']], 'L6.1': [['.124']], 'L8.1': [['86', '7', '97', '0', '98'], ['.195']],
              'L10.1': [['.195']], 'L11.2': [['48', '6', '97', '98', '0', '5']], 'L12.1': [['169']],
              'L13.1': [['289'], ['.128'], ['1']], 'L15.1': [['.144'], ['.143']], 'L23.1': [['86', '5']],
              'L25.2': [['<P>']]},
    'f065r': {'L1.1': [['.133']]}}
# f. 80r: the first reader gave a number of groups that are not in sense for each line, not the groups.
# Line 18: all groups from the first 199 to the end (filler).
NOT_IN_SENSE_F80 = {1: 7, 2: 1, 3: 2, 4: 1, 5: 1, 7: 3, 9: 4, 10: 3, 11: 1, 16: 3, 17: 8}


def gap_set(groups, seqs):
    """the places of the listed stretches in a run"""
    g = set()
    for s in seqs:
        for i in range(len(groups) - len(s) + 1):
            if groups[i:i + len(s)] == s and not any(j in g for j in range(i, i + len(s))):
                g.update(range(i, i + len(s)))
                break
        else:
            raise SystemExit('stretch not found: %s' % s)
    return g


def sense(name, sheet, key):
    """(groups that carry text, groups in sense) by the hand lists"""
    text = ins = 0
    for line, row in sheet:
        for kind, t, lab, g in row:
            if kind != 'run':
                continue
            n = sum(1 for x in g if not counted_null(x, key))
            text += n
            if name == 'f080r':
                k = int(line[1:])
                gaps = sum(1 for x in g[g.index('199'):] if not counted_null(x, key)) if k == 18 else NOT_IN_SENSE_F80.get(k, 0)
            else:
                gaps = sum(1 for i in gap_set(g, NOT_IN_SENSE[name].get(lab, [])) if not counted_null(g[i], key))
            ins += n - gaps
    return text, ins


# ---------------------------------------------------------------- the transcription passes

def pass_signs(s):
    s = re.sub(r'\^[^^]*\^', '', s)                  # the folio numbers above line 1
    s = re.sub(r'<[^>]*>', 'S', s)                   # a sign counts as one place
    s = re.sub(r'[()\[\] ]', '', s)                  # the marks for a blotted figure
    return s.replace('i', '1')


def agreement_f80():
    """f. 80r: places that are the same in pass A and pass B (blind), by the longest common runs of each line"""
    A, B = load_rows('pass_a.txt'), load_rows('pass_b_blind.txt')
    total = same = 0
    for k in A:
        a, b = pass_signs(A[k]), pass_signs(B.get(k, ''))
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        same += sum(x.size for x in sm.get_matching_blocks())
        total += max(len(a), len(b))
    return same, total


def figures(s):
    """figures and signs of a line of a mixed letter; clear words are dropped"""
    s = s.replace('(?)', '')
    s = s.replace('<sign like a capital P>', '<P>').replace('<sign like T, or a 7>', '<T>').replace('<arch>', '<lambda>')
    out = []
    for p in re.findall(r'<[^>]*>|\([0-9?|]+\)|[0-9?]|i(?=[0-9(])', s):
        out.append(p[1:-1].split('|')[0] if p.startswith('(') else p)
    return out


def agreement(folder, a='pass_a.txt', b='pass_b_blind.txt'):
    """f. 85r and f. 65r: (items of a, items of b, the same), over the lines with figures"""
    A, B = load_rows(os.path.join(folder, a)), load_rows(os.path.join(folder, b))
    ta = tb = same = 0
    for k in A:
        x, y = figures(A[k]), figures(B.get(k, ''))
        if k == 'L29' or (not x and not y):
            continue
        sm = difflib.SequenceMatcher(None, x, y, autojunk=False)
        ta, tb, same = ta + len(x), tb + len(y), same + sum(m.size for m in sm.get_matching_blocks())
    return ta, tb, same


# ---------------------------------------------------------------- the held-out test
# The key and the cut rule of the first page of this folder (11 October 2026) were made on f. 80r alone.
# key_first_page.tsv is that key, as it was. old_cut() is that rule, without the six places of f. 80r where the
# sense decided the cut. Here they are applied to f. 85r and f. 65r, which had no part in them.

def old_cut(s):
    it = [('S', x) if x.startswith('<') else ('I', x) if x == 'i' else ('D', x) for x in lex(s)]
    out, i = [], 0

    def d(j):
        return it[j][1] if j < len(it) and it[j][0] == 'D' else None

    def take(i, n):
        g = ''
        for j in range(i, min(i + n, len(it))):
            if it[j][0] != 'D':
                break
            g += it[j][1]
        return g

    while i < len(it):
        k, v = it[i]
        if k == 'S':
            out.append(v)
            i += 1
        elif k == 'I':
            g = take(i + 1, 2)
            out.append('.' + g)
            i += 1 + len(g)
        elif v == '1' and d(i + 1) == '2':
            out.append('12')
            i += 2
        elif v == '1':
            g = take(i, 3)
            out.append(g)
            i += len(g)
        elif v in '489':
            g = take(i, 2)
            out.append(g)
            i += len(g)
        elif v == '5' and d(i + 1) in ('5', '8'):
            out.append('5' + d(i + 1))
            i += 2
        elif v == '6' and d(i + 1) == '6' and d(i + 2) == '1' and d(i + 3) == '5':
            out.append('66')
            i += 2
        else:
            out.append(v)
            i += 1
    return out


def spans(groups):
    """the place of each group in its run, as (first item, last item + 1)"""
    out, p = [], 0
    for g in groups:
        n = 1 if g.startswith('<') else len(g)       # '.14' = the stroke and two figures = three items
        out.append((p, p + n))
        p += n
    return out


def heldout(name, sheet, key):
    """the first page's key on a letter that it did not see.
    -> (groups by the old cut, with a value, not nulls, with the value and the place that the final reading keeps)"""
    old, _ = load_key(os.path.join(HERE, 'key_first_page.tsv'))
    tot = val = notnull = kept = 0
    rows = []
    for line, row in sheet:
        for kind, t, lab, new in row:
            if kind != 'run':
                continue
            o = old_cut(t)
            gaps = gap_set(new, NOT_IN_SENSE[name].get(lab, []))
            good = {sp: key[new[i]].lower() for i, sp in enumerate(spans(new)) if i not in gaps and key.get(new[i])}
            k = sum(1 for g, sp in zip(o, spans(o)) if old.get(g) and good.get(sp) == old[g].lower())
            tot, val = tot + len(o), val + sum(1 for g in o if g in old)
            notnull, kept = notnull + sum(1 for g in o if old.get(g) != ''), kept + k
            rows.append((lab, decode(o, old)))
    return tot, val, notnull, kept, rows


# ---------------------------------------------------------------- the halves of f. 85r

def halves(s85, s65, key, rows):
    """the letters, the words that the first page had, and the new values that stand in one half, on the other half"""
    old, _ = load_key(os.path.join(HERE, 'key_first_page.tsv'))
    base = set(r[0] for r in rows if r[2] in ('letter', 'null')) | set(g for g in key if old.get(g, '').lower() == key[g].lower() and key[g])
    R = [('f085r', lab, g) for lab, g in runs(s85)] + [('f065r', lab, g) for lab, g in runs(s65)]
    h1 = [r for r in R if r[0] == 'f085r' and int(r[1][1:].split('.')[0]) <= 13]
    h2 = [r for r in R if r not in h1]
    known = in_tables(key, rows)
    out = []
    for src, dst in ((h1, h2), (h2, h1)):
        seen = set(x for _, _, g in src for x in g)
        k = set(g for g in known if g in base or g in seen)
        toks = [x for _, _, g in dst for x in g]
        miss = sorted(set(x for x in toks if x in known and x not in k))
        out.append((len(toks), sum(1 for x in toks if x in k), miss))
    return out


# ---------------------------------------------------------------- the order of the alphabet
# STRICT1: the ten words of table 1 that the first round fixed from the sense, before anybody saw the order.
# STRICT2: the five words that the first page had as groups of two figures (12 ma, 29 non, 55 se, 58 si, 66 stato).
# Nobody knew then that a 2 stands before each of them, and nobody knew of a second table.
STRICT1 = ['141', '142', '143', '152', '157', '158', '162', '184', '192', '193']
STRICT2 = ['212', '229', '255', '258', '266']
ENDINGS = ['289', '291', '294', '296']


def table(rows, kind):
    """[(group, word)] of table1, table2 or ending; only groups with one value"""
    return sorted((r[0], r[1].split('/')[0].lower()) for r in rows if r[2] == kind and r[1] not in ('?', '·'))


def in_order(pairs):
    w = [x for _, x in sorted(pairs)]
    return w == sorted(w)


def spearman(xs, ys):
    def rk(v):
        s = sorted(range(len(v)), key=lambda i: v[i])
        r, i = [0] * len(v), 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and v[s[j + 1]] == v[s[i]]:
                j += 1
            for k in range(i, j + 1):
                r[s[k]] = (i + j) / 2
            i = j + 1
        return r
    a, b = rk(xs), rk(ys)
    n = len(a)
    ma, mb = sum(a) / n, sum(b) / n
    return sum((x - ma) * (y - mb) for x, y in zip(a, b)) / math.sqrt(sum((x - ma) ** 2 for x in a) * sum((y - mb) ** 2 for y in b))


def shuffle_test(pairs, seed=2026, N=20000):
    """-> (rho, shuffles with rho as high, best shuffle)"""
    pairs = sorted(pairs)
    nums, words = [int(k) for k, _ in pairs], [w for _, w in pairs]
    r0, rnd, ge, best = spearman(nums, words), random.Random(seed), 0, -1
    for _ in range(N):
        w = words[:]
        rnd.shuffle(w)
        r = spearman(nums, w)
        best = max(best, r)
        if r >= r0 - 1e-12:
            ge += 1
    return r0, ge, best


def order_sets(rows):
    t1, t2, en = table(rows, 'table1'), table(rows, 'table2'), table(rows, 'ending')
    d = dict(t1 + t2)
    return [('table 1, all words', t1), ('table 2, all words', t2), ('table 2, words and the four endings', t2 + en),
            ('both tables as one list', t1 + t2),
            ('strict: the ten words of table 1', [(g, d[g]) for g in STRICT1]),
            ('strict: the five old two-figure words of table 2', [(g, d[g]) for g in STRICT2]),
            ('strict: the ten and the five as one list', [(g, d[g]) for g in STRICT1 + STRICT2])]


# ---------------------------------------------------------------- write the files

def file_rows(name, sheet, key, grade):
    """the rows of groups.txt and of decoded_by_key.txt for one letter"""
    style = [s for n, f, s in SHEETS if n == name][0]
    G, D = [], []
    for line, row in sheet:
        d = []
        for kind, t, lab, g in row:
            if kind == 'run':
                G.append('%s: %s' % (lab, ' '.join(g)))
                d.append(decode(g, key, grade) if style == 'line' else '{ ' + decode(g, key, grade) + ' }')
            elif kind == 'lone':
                d.append('{ [' + t + '] }')
            else:
                d.append(t)
        D.append('%s: %s' % (line, ' '.join(d)))
    return G, D


def write_files(name, sheet, key, grade):
    folder, style = [(f, s) for n, f, s in SHEETS if n == name][0]
    G, D = file_rows(name, sheet, key, grade)
    head = ['# BnF fr. 4700 %s: the cipher runs of the settled transcription (transcription.txt), cut into groups.' % TITLE[name],
            '# decode.py makes this file. A group is one figure (0 3 5 6 7, and a lone 1 or 2), two figures (4x, 8x, 9x)',
            '# or three figures (1xy, 2xy). .143 = the dotted stroke with the figures 1 4 3: a name group.',
            '# ? = a figure that is not read. Signs stand in < >. ' + (
                'L5.1 = the first cipher run of line 5.' if style == 'run' else 'Each line of this sheet is one run.')]
    open(os.path.join(HERE, folder, 'groups.txt'), 'w', encoding='utf-8').write('\n'.join(head + G) + '\n')
    open(os.path.join(HERE, folder, 'decoded_by_key.txt'), 'w', encoding='utf-8').write('\n'.join(D) + '\n')


if __name__ == '__main__':
    key, rows = load_key()
    grade = {r[0]: r[3] for r in rows}
    known = in_tables(key, rows)
    S = {n: load_sheet(n, known) for n, f, s in SHEETS}
    for name, sheet in S.items():
        print('==', TITLE[name])
        for line, row in sheet:
            for kind, t, lab, g in row:
                if kind == 'clear':
                    print('%s: %s' % (line, t))
                elif kind == 'lone':
                    print('%s: [%s]  (one group alone between clear words: no value)' % (line, t))
                else:
                    print('%s: %s' % (lab, ' '.join(g)))
                    print('      %s' % decode(g, key, grade))
        write_files(name, sheet, key, grade)
        print()

    print('== counts')
    cnt = {n: collections.Counter() for n in list(S) + ['f083r']}
    for name, sheet in S.items():
        allg = [x for _, g in runs(sheet) for x in g]
        lone = [t for line, row in sheet for kind, t, lab, g in row if kind == 'lone']
        cnt[name].update(allg + lone)
        c = counts(allg, key, rows)
        text, ins = sense(name, sheet, key)
        print('%s: %s' % (name, '; '.join('%s %d' % kv for kv in c.items())))
        if lone:
            print('   and %d groups alone between clear words (%s)' % (len(lone), ' '.join(lone)))
        print('   in words that we translate, by the hand list: %d of %d (%.1f %%)' % (ins, text, 100.0 * ins / text))
    held = load_rows('heldout_f83r.txt')
    h83 = cut(held['L1'], known)
    cnt['f083r'].update(h83)
    for r in rows:
        have = [cnt[n][r[0]] for n in ('f085r', 'f065r', 'f080r', 'f083r')]
        if [int(x) for x in r[4:8]] != have:
            print('key.tsv has other counts for', r[0], ':', r[4:8], 'against', have)
    listed = set(r[0] for r in rows)
    for n in cnt:
        for g in cnt[n]:
            if g not in listed:
                print('key.tsv has no row for', g, 'of', n)

    print()
    print('== the transcription passes')
    same, total = agreement_f80()
    print('f. 80r: pass A against pass B (blind): %d of %d places are the same (%.1f %%)' % (same, total, 100.0 * same / total))
    for f in ('f085r', 'f065r'):
        ta, tb, sab = agreement(f)
        _, ts, sas = agreement(f, 'pass_a.txt', 'transcription.txt')
        _, _, sbs = agreement(f, 'pass_b_blind.txt', 'transcription.txt')
        print('%s: pass A %d figures and signs, pass B (blind) %d, the settled text %d; the same in A and B: %d (%.1f %%); '
              'A and the settled text: %d (%.1f %%); B and the settled text: %d (%.1f %%)   [percent = 2 x same / sum]' % (
                  f, ta, tb, ts, sab, 200.0 * sab / (ta + tb), sas, 200.0 * sas / (ta + ts), sbs, 200.0 * sbs / (tb + ts)))

    print()
    print('== the held-out test: the key and the cut of the first page (made on f. 80r alone), with no change')
    for f in ('f085r', 'f065r'):
        tot, val, nn, kept, hrows = heldout(f, S[f], key)
        print('%s: %d groups by the old cut; %d have a value (%.1f %%); %d are not nulls; %d of them (%.1f %%) have the value '
              'and the place that the final reading keeps in a word that we translate' % (f, tot, val, 100.0 * val / tot, nn, kept, 100.0 * kept / nn))
        for lab, d in hrows:
            print('   %s: %s' % (lab, d))

    print()
    print('== the halves of f. 85r')
    for (n, hv, miss), nm in zip(halves(S['f085r'], S['f065r'], key, rows),
                                 ('the values of f. 85r lines 5-13, on lines 14-25 and f. 65r', 'the values of lines 14-25 and f. 65r, on lines 5-13')):
        print('%s: %d of %d groups are known (%.1f %%); only the tested half has: %s' % (nm, hv, n, 100.0 * hv / n, ', '.join(miss)))

    print()
    print('== the held-out passage of f. 83r (one transcription pass)')
    print('  ', ' '.join(h83))
    print('  ', decode(h83, key, grade))

    print()
    print('== the order of the alphabet in the word tables')
    for nm, pairs in order_sets(rows):
        line = '%s: %d values; in the order of the alphabet: %s; chance of the full order: 1 in %s' % (
            nm, len(pairs), in_order(pairs), '{:,}'.format(math.factorial(len(pairs))) if len(pairs) < 16 else '%.1e' % math.factorial(len(pairs)))
        if '--no-shuffles' not in sys.argv:
            r0, ge, best = shuffle_test(pairs)
            line += '; rank correlation %.3f; %d of 20,000 shuffles are as high; best shuffle %.3f' % (r0, ge, best)
        print(line)
