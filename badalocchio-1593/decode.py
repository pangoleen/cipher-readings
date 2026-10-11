#!/usr/bin/env python3
"""decode.py -- cut the transcription (transcription.txt) into groups and apply the key table (key.tsv).

Run it in any folder:  python3 decode.py

It prints each cipher line with its groups and their values. Then it prints the counts, the agreement of the two
transcription passes, and three controls that need no other file: the two halves of the sheet, the order of the
word table, and the held-out passage of f. 83r. It writes decoded_by_key.txt.
It needs Python 3.8 or later and no other package.

In the output: a raised dot = a null; a letter = a group for one letter; CAPITALS = a group for a word or a
syllable; [132] = a group with no value; [.17] = a name group (the dotted 1 with the figures 1 7).

The script does not make the reading. The word division, the Italian and the translation of reading.md are the
work of a reader. The script shows only what the key gives for each group.
"""
import collections, difflib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- the cut rule
# A row of figures has no gaps. The rule goes from left to right:
#   1 + two more figures       one group of the word table (1xy); but 1 2 is the group 12 (ma)
#   4, 8 or 9 + one figure     one group: a letter, or 91 (ente), 92 (per)
#   5 5 and 5 8                the groups 55 (se) and 58 (si)
#   6 6 before 1 5             the group 66 (stato); it stands two times, each time before 152 (di)
#   0 2 3 5 6 7                one figure alone: 0 and 2 are nulls, 3 5 6 7 are the vowels a i o u
#   the dotted stroke i        with the next two figures: a name group, written .17
#   a sign in < >, and ?       alone
# The rule leaves a doubt in two cases. The places where the sense decides are listed here.
# 1. "5 8" can be the group 58 (si), or the letter 5 (i) and the head of a pair 8x. NOT58 lists the places
#    where it is i + 8x: (line, n-th "5 8" of the line that the rule meets).
NOT58 = {('L2', 1): 'Milano', ('L5', 1): 'cosi bel-', ('L15', 1): 'Milano', ('L16', 1): 'Sicilia'}
# 2. "2 9" and "3 9" can be the groups 29 and 39, or a null / the letter a and the head of a pair 9x.
#    PAIR9 lists the two places where they are groups: (line, the cut by the rule, the cut that we use).
PAIR9 = [('L11', '2 3 99 3 5 48 193', '2 39 93 5 48 193'),      # [39] mie le-tere
         ('L16', '2 2 99 7 98 3 96', '2 29 97 98 3 96')]       # NON starebbono


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


def load_rows(name):
    """a file with rows 'L1: ...' -> {line: text}; the first row of each line counts"""
    out = collections.OrderedDict()
    for l in open(os.path.join(HERE, name), encoding='utf-8'):
        m = re.match(r'(L\d+):\s*(.*)', l.strip())
        if m and m.group(1) not in out:
            out[m.group(1)] = m.group(2).strip()
    return out


def lex(s):
    """a row -> items: ('D', figure), ('I', 'i') for the dotted stroke, ('S', sign)"""
    items, i = [], 0
    while i < len(s):
        c = s[i]
        if c == '<':
            j = s.index('>', i)
            items.append(('S', s[i:j + 1].replace(' ', '_')))
            i = j + 1
            continue
        if c in '0123456789?':
            items.append(('D', c))
        elif c == 'i':
            items.append(('I', 'i'))
        i += 1
    return items


def cut(items, line='', not58=NOT58):
    out, i, n58 = [], 0, 0

    def d(j):
        return items[j][1] if j < len(items) and items[j][0] == 'D' else None

    def take(i, n):
        g = ''
        for j in range(i, min(i + n, len(items))):
            if items[j][0] != 'D':
                break
            g += items[j][1]
        return g

    while i < len(items):
        k, v = items[i]
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
        elif v == '5' and d(i + 1) == '5':
            out.append('55')
            i += 2
        elif v == '5' and d(i + 1) == '8':
            n58 += 1
            if (line, n58) in not58:
                out.append('5')
                i += 1
            else:
                out.append('58')
                i += 2
        elif v == '6' and d(i + 1) == '6' and d(i + 2) == '1' and d(i + 3) == '5':
            out.append('66')
            i += 2
        else:
            out.append(v)
            i += 1
    return out


def groups_of(line, row):
    s = ' '.join(cut(lex(row), line))
    for ln, a, b in PAIR9:
        if ln == line:
            assert s.count(a) == 1, (line, a)
            s = s.replace(a, b)
    return s.split(' ')


def load_groups():
    """transcription.txt, cut by the rule -> {line: [group]}"""
    return collections.OrderedDict((k, groups_of(k, v)) for k, v in load_rows('transcription.txt').items())


def show(g, key):
    if g not in key:
        return '[' + g + ']'
    v = key[g]
    return '·' if v == '' else (v.upper() if len(v) > 1 else v)


def decode(groups, key):
    return ' '.join(show(g, key) for g in groups)


def counts(G, key):
    allg = [g for t in G.values() for g in t]
    n = len(allg)
    nul = sum(1 for g in allg if key.get(g) == '')
    val = sum(1 for g in allg if g in key)
    return {'groups': n, 'with a value': val, 'nulls': nul, 'not nulls': n - nul, 'no value': n - val}


# ---------------------------------------------------------------- the two passes

def pass_signs(s):
    s = re.sub(r'\^[^^]*\^', '', s)                  # the folio numbers above line 1
    s = re.sub(r'<[^>]*>', 'S', s)                   # a sign counts as one place
    s = re.sub(r'[()\[\] ]', '', s)                  # the marks for a blotted figure
    return s.replace('i', '1')


def agreement():
    """places that are the same in pass A and pass B (blind), by the longest common runs of each line"""
    A, B = load_rows('pass_a.txt'), load_rows('pass_b_blind.txt')
    total = same = 0
    diffs = []
    for k in A:
        a, b = pass_signs(A[k]), pass_signs(B.get(k, ''))
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        same += sum(x.size for x in sm.get_matching_blocks())
        total += max(len(a), len(b))
        diffs += [(k, a[i1:i2], b[j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
    return same, total, diffs


# ---------------------------------------------------------------- the halves
# WIT: a value that this sheet adds -> the lines with a clear word that fixes it (the words are in key.tsv).
# Limit: we made the key on the whole sheet. "Fixed in a half" means only that a clear word of that half fixes
# the value.
WIT = {'5': [2, 4, 5, 8, 9, 15, 16], '2': [3, 6, 7, 12, 14], '<pi>': [5, 9, 14, 16], '<Cn>': [9, 15], '<arch>': [1],
       '<0+>': [3, 15], '<female>': [7], '<triangle>': [10, 13], '12': [2, 3, 4, 5, 9, 17], '55': [7, 8, 10, 14],
       '58': [1, 3, 5, 6, 11, 12, 14, 17], '66': [2, 15], '91': [3, 6, 7, 12], '92': [7],
       '141': [1, 7, 10, 12, 16], '142': [7, 10], '143': [3], '146': [6], '148': [6, 10],
       '152': [2, 5, 6, 10, 11, 12, 15], '156': [8], '157': [12, 13, 14, 16], '158': [3], '162': [13], '175': [8, 11],
       '184': [7, 8, 10], '185': [9], '188': [11], '192': [4, 8, 10, 12, 18], '193': [5, 11], '197': [10],
       '135': [7], '154': [10], '163': [2], '29': [16]}


def half(G, key, rows, src, dst):
    """the key of the minute and the values that the lines src fix, applied to the lines dst"""
    k = {c[0]: key[c[0]] for c in rows if c[4] == 'minute'}
    k.update({g: key[g] for g, w in WIT.items() if any(x in src for x in w)})
    lack = [g for g in WIT if g not in k]
    seq = [g for i in dst for g in G['L%d' % i]]
    return len(seq), sum(1 for g in seq if g in k), lack


def word_table(rows):
    """the groups 1xy with a sure value, in the order of their numbers"""
    return sorted((c[0], c[1]) for c in rows if c[2] == 'word' and c[4] == 'sure' and len(c[0]) == 3)


if __name__ == '__main__':
    key, rows = load_key()
    G = load_groups()
    stored = load_rows('groups.txt')
    out = []
    for k, t in G.items():
        print(k + ':', ' '.join(t))
        print('    ', decode(t, key))
        out.append('%s: %s' % (k, decode(t, key)))
    open(os.path.join(HERE, 'decoded_by_key.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    print()
    print('the cut by the rule is the same as groups.txt:', all(' '.join(G[k]) == stored.get(k) for k in G) and len(G) == len(stored))
    c = counts(G, key)
    print('groups: %d; with a value: %d (%.1f %%), of these %d nulls; not nulls: %d; no value: %d' % (
        c['groups'], c['with a value'], 100.0 * c['with a value'] / c['groups'], c['nulls'], c['not nulls'], c['no value']))
    cnt = collections.Counter(g for t in G.values() for g in t)
    for r in rows:
        if int(r[3]) != cnt[r[0]]:
            print('key.tsv has another count for', r[0], ':', r[3], 'against', cnt[r[0]])
    for g in cnt:
        if g not in [r[0] for r in rows]:
            print('key.tsv has no row for', g)
    minute = sum(cnt[r[0]] for r in rows if r[4] == 'minute')
    print('groups that the key of the minute alone covers: %d (%.1f %%)' % (minute, 100.0 * minute / c['groups']))
    same, total, diffs = agreement()
    print()
    print('pass A against pass B (blind): %d of %d places are the same (%.1f %%)' % (same, total, 100.0 * same / total))
    print()
    for src, dst, name in ((range(1, 10), range(10, 19), 'lines 1-9 on lines 10-18'), (range(10, 19), range(1, 10), 'lines 10-18 on lines 1-9')):
        n, hv, lack = half(G, key, rows, src, dst)
        print('halves, %s: %d of %d groups have a value (%.1f %%); this half cannot supply: %s' % (
            name, hv, n, 100.0 * hv / n, ', '.join('%s = %s' % (g, key[g] or 'null') for g in lack)))
    wt = word_table(rows)
    words = [w for g, w in wt]
    print()
    print('word table: %d sure words in the order of their numbers: %s' % (len(wt), ' < '.join('%s %s' % x for x in wt)))
    print('   in the order of the alphabet:', words == sorted(words))
    held = load_rows('heldout_f83r.txt')
    hg = held['L1'].split()
    print()
    print('held-out passage of f. 83r, cut as it stood before we saw it: %d groups, %d with a value, %d of them nulls' % (
        len(hg), sum(1 for g in hg if g in key), sum(1 for g in hg if key.get(g) == '')))
    print('    ', decode(hg, key))
    print('the same passage, with 2 9 and 3 9 cut as the groups 29 and 39 (learned from this passage):')
    print('    ', decode(held['L2'].split(), key))
