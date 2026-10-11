#!/usr/bin/env python3
"""decode.py -- apply the key table (key.tsv) to the transcription (transcription.txt).

Run it in any folder:  python3 decode.py

It prints each cipher line with its letters, the counts, the agreement of the two transcription passes, and one
control: the key of the first passage, applied to the second passage. It writes decoded_by_key.txt.
It needs Python 3.8 or later and no other package.

In the output: a raised dot = the null 0; [?] = a mark that is not read; a question mark after a letter = the
figure has a second candidate. Struck groups are not decoded.
"""
import collections, difflib, os, re

HERE = os.path.dirname(os.path.abspath(__file__))


def load_key(path=None):
    """key.tsv -> ({group: value}, rows)"""
    key, rows = {}, []
    for l in open(path or os.path.join(HERE, 'key.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('group\t') or not l.strip():
            continue
        c = l.rstrip('\n').split('\t')
        key[c[0]] = c[1]
        rows.append(c)
    return key, rows


def load_lines(path=None):
    """transcription.txt -> {line: [(group, flags)]}
    flags: s = struck, a = above the line, f = faint, d = two candidates (the first is used), u = not read"""
    out = collections.OrderedDict()
    for l in open(path or os.path.join(HERE, 'transcription.txt'), encoding='utf-8'):
        m = re.match(r'(B\dL\d): (.*)', l)
        if not m:
            continue
        toks, struck = [], False
        for w in m.group(2).split():
            fl = ''
            if w.startswith('['):
                struck = True
            if struck:
                fl += 's'
            if w.endswith(']'):
                struck = False
            w = w.strip('[]')
            if 's' not in fl:
                if '^' in w:
                    fl += 'a'
                    w = w.replace('^', '')
                if '(' in w:
                    fl += 'f'
                    w = w.replace('(', '').replace(')', '')
                if w == '{?}':
                    fl += 'u'
                elif '{' in w:
                    fl += 'd'
                    w = re.sub(r'\{(.)/.\}', r'\1', w)
            toks.append((w, fl))
        out[m.group(1)] = toks
    return out


def kept(toks):
    """the groups of the text as the writer corrected it"""
    return [(g, fl) for g, fl in toks if 's' not in fl]


def decode(toks, key):
    s = ''
    for g, fl in kept(toks):
        s += '[?]' if 'u' in fl else key.get(g, '{' + g + '}') + ('?' if 'd' in fl else '')
    return s


def letters(toks):
    """the groups that stand for a letter: no null, no unread mark"""
    return [g for g, fl in kept(toks) if 'u' not in fl and g != '0']


def pass_lines(name):
    out = {}
    for l in open(os.path.join(HERE, name), encoding='utf-8'):
        m = re.match(r'(B\dL\d): (.*)', l.strip())
        if m and m.group(1) not in out:
            s = re.sub(r'\{(.)/.\}', r'\1', m.group(2))        # of two candidates, the first
            out[m.group(1)] = re.sub(r'[^0-9us?]', '', s)      # signs only: no dots, no brackets
    return out


def agreement():
    """signs that are the same in pass 1 and pass 2, by the longest common runs of each line"""
    A, B = pass_lines('pass1.txt'), pass_lines('pass2_blind.txt')
    total = same = 0
    diffs = []
    for k in A:
        sm = difflib.SequenceMatcher(None, A[k], B[k], autojunk=False)
        same += sum(x.size for x in sm.get_matching_blocks())
        total += max(len(A[k]), len(B[k]))
        diffs += [(k, A[k][i1:i2], B[k][j1:j2]) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != 'equal']
    return same, total, diffs


def block1_key_on_block2(lines, key):
    """the values that the first passage fixes, applied to the second passage"""
    b1 = [g for k in lines if k.startswith('B1') for g in letters(lines[k])]
    b2 = [g for k in lines if k.startswith('B2') for g in letters(lines[k])]
    k1 = {g: key[g] for g in set(b1)}
    text = ''.join(k1.get(g, '?') for g in b2)
    new = sorted(set(g for g in b2 if g not in k1))
    return len(b2), len(b2) - text.count('?'), text, new


if __name__ == '__main__':
    key, rows = load_key()
    lines = load_lines()
    out = []
    for k, toks in lines.items():
        print(k + ':', ' '.join(g for g, fl in kept(toks)))
        print('     ', decode(toks, key))
        out.append('%s: %s' % (k, decode(toks, key)))
    open(os.path.join(HERE, 'decoded_by_key.txt'), 'w', encoding='utf-8').write('\n'.join(out) + '\n')
    allg = [g for toks in lines.values() for g, fl in kept(toks)]
    vals = collections.Counter(g for g in allg if g != '{?}')
    pairs = sum(1 for g in allg if len(g) == 2)
    print()
    print('groups: %d = %d pairs + %d single figures (with %d mark not read)' % (
        len(allg), pairs, len(allg) - pairs, allg.count('{?}')))
    print('different values: %d' % len(vals))
    print('letters: %d; nulls: %d' % (sum(len(letters(t)) for t in lines.values()), vals['0']))
    for c in rows:
        if int(c[3]) != vals[c[0]]:
            print('key.tsv has another count for', c[0], ':', c[3], 'against', vals[c[0]])
    same, total, diffs = agreement()
    print()
    print('pass 1 against pass 2 (blind): %d of %d signs are the same (%.1f %%)' % (same, total, 100.0 * same / total))
    for k, a, b in diffs:
        print('   %s: pass 1 "%s", pass 2 "%s"' % (k, a, b))
    n, read, text, new = block1_key_on_block2(lines, key)
    print()
    print('control: the key of passage 1 reads %d of the %d letter groups of passage 2 (%.0f %%)' % (read, n, 100.0 * read / n))
    print('   ' + text)
    print('   groups of passage 2 that passage 1 does not have: ' + ', '.join('%s = %s' % (g, key[g]) for g in new))
