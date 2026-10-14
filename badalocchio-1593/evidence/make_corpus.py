#!/usr/bin/env python3
"""make_corpus.py GUTENBERG_FOLDER -- rebuild the two Italian data files of the controls, and compare them.

The data come from six Italian texts of Project Gutenberg. All six are in the public domain:
  45334 Manzoni, I promessi sposi          38637 Albertazzi, Il diavolo nell'ampolla
  52484 Collodi, Le avventure di Pinocchio   1012 Dante, La Divina Commedia
  28910 Rovetta, Mater dolorosa             18456 Pirandello, Enrico IV
Put the plain-text files pg45334.txt ... pg18456.txt (from https://www.gutenberg.org/cache/epub/N/pgN.txt) in
GUTENBERG_FOLDER, then run this script. It writes nothing; it prints whether the rebuilt data are the same as
the files of this folder, with the SHA-256 of each.

1. wordlist_it.txt: the word forms of the six whole files (lower case; accents dropped; j = i, v = u), seen
   2 times or more, of 3 letters or more. This is the list of the review panel of 14 October 2026. The panel
   took the whole files, so the list holds about 600 English forms of the Project Gutenberg header and licence.
2. it_letters.txt (in nevers-1593/evidence/ only): the six texts without the Project Gutenberg header and
   licence, letters a-z only (accents dropped), in the order above. control.py of nevers-1593 and fourgram.py
   make their four-letter tables from it.
A newer download of a Gutenberg file can differ from the files of October 2026. Then the SHA-256 differs.
"""
import collections, hashlib, os, re, sys, unicodedata

IDS = (45334, 38637, 52484, 1012, 28910, 18456)
HERE = os.path.dirname(os.path.abspath(__file__))


def norm_text(t):
    t = t.lower()
    for a, b in (('à', 'a'), ('è', 'e'), ('é', 'e'), ('ì', 'i'), ('ò', 'o'), ('ù', 'u'), ('j', 'i'), ('v', 'u')):
        t = t.replace(a, b)
    return t


def strip_gutenberg(text):
    a = re.search(r"\*\*\* ?START OF.*?\*\*\*", text)
    b = re.search(r"\*\*\* ?END OF.*?\*\*\*", text)
    return text[a.end() if a else 0: b.start() if b else len(text)]


def fold(text):
    return re.sub(r'[^a-z]', '', unicodedata.normalize('NFD', text.lower()))


def sha(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    folder = sys.argv[1]
    c = collections.Counter()
    letters = []
    for i in IDS:
        raw = open(os.path.join(folder, 'pg%d.txt' % i), encoding='utf-8', errors='replace').read()
        c.update(re.findall(r'[a-z]+', norm_text(raw)))
        letters.append(fold(strip_gutenberg(raw)))
    words = sorted(w for w, n in c.items() if n >= 2 and len(w) >= 3)
    have = sorted(l.strip() for l in open(os.path.join(HERE, 'wordlist_it.txt'), encoding='utf-8')
                  if l.strip() and not l.startswith('#'))
    print('wordlist_it.txt: rebuilt %d forms, file %d forms; the same: %s; SHA-256 of the rebuilt list %s'
          % (len(words), len(have), words == have, sha('\n'.join(words))))
    text = ''.join(letters)
    path = os.path.join(HERE, 'it_letters.txt')
    if os.path.exists(path):
        old = open(path, encoding='utf-8').read().strip()
        print('it_letters.txt: rebuilt %d letters, file %d letters; the same: %s; SHA-256 %s'
              % (len(text), len(old), text == old, sha(text)))
    else:
        print('it_letters.txt: rebuilt %d letters; SHA-256 %s (the file is in nevers-1593/evidence/)' % (len(text), sha(text)))


if __name__ == '__main__':
    main()
