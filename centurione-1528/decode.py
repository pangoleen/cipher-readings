#!/usr/bin/env python3
"""Apply key/table.tsv to a transcription of the letters.

Usage:  python3 decode.py FILE [FILE ...]

A transcription file holds one line of the manuscript per line. A cipher group is a base letter and a number
(c170, p149). A line that starts with '|' is clear text. A line that starts with '#' is a comment.
D. Bourdeau's transcription files (github.com/dbourdeau/cyphersolver, targets/vasto1527) have this format.
They are not copied here: his repository has no licence.

The script first applies our corrections to that transcription (evidence/transcription_corrections.tsv: file,
line, position, old group, new group), which come from a check on the page images.

Output: each line with every group replaced by its value. Classes: plain = sure, value? = probable,
value?? = guess, [group] = no value, _ = null (numbers 0 to 5)."""
import re, sys, os

HERE = os.path.dirname(os.path.abspath(__file__))


def load_key():
    key = {}
    for line in open(os.path.join(HERE, 'key', 'table.tsv'), encoding='utf8').read().split('\n')[1:]:
        f = line.split('\t')
        if len(f) >= 3 and f[1]:
            key[f[0]] = (f[1], f[2])
    return key


def load_corrections():
    """Our corrections to the transcription, by file name, line of the file and position in the line."""
    cor = {}
    path = os.path.join(HERE, 'evidence', 'transcription_corrections.tsv')
    for line in open(path, encoding='utf8').read().split('\n')[1:]:
        f = line.split('\t')
        if len(f) == 5:
            cor[(f[0], int(f[1]), f[3])] = f[4]
    return cor


def main():
    key = load_key()
    cor = load_corrections()
    mark = {'sure': '', 'probable': '?', 'guess': '??', 'null': ''}
    for path in sys.argv[1:]:
        name = os.path.basename(path)
        print('## ' + name)
        for lineno, line in enumerate(open(path, encoding='utf8'), 1):
            line = line.rstrip('\n')
            if line.startswith('#'):
                continue
            if line.startswith('|'):
                print(line[1:].upper())
                continue
            out = []
            for tok in line.split():
                tok = cor.get((name, lineno, tok), tok)
                if tok == '(delete)':
                    continue
                m = re.match(r'^([A-Za-z])(\d+)$', tok)
                if not m:
                    out.append(tok)
                    continue
                letter, number = m.group(1), int(m.group(2))
                if letter == 'L':
                    letter = 'l'
                if letter == 'g' and number > 214:   # the g list has 214 entries: an 8-like s
                    letter = 's'
                if letter == 't' and number > 196:   # the t list has 196 entries: a tau-like r
                    letter = 'r'
                g = '%s%d' % (letter, number)
                if g in key:
                    v, c = key[g]
                    out.append(v + mark.get(c, '?'))
                elif number <= 5:
                    out.append('_')
                else:
                    out.append('[' + g + ']')
            print(' '.join(out))
        print()


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    main()
