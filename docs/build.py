#!/usr/bin/env python3
"""build.py -- write the pages of docs/ from the files of the repository.

Run it from any folder:  python3 docs/build.py

Every token and every value on a page comes from a key file and a transcription file of the repository.
The script applies the key again, and it compares each worked line with the reading file of the folder.
It stops with an error if a line does not reproduce. The only text that is not in a folder of the repository
is docs/data/oxford_lines.txt: three lines of A. Aymeloglu's transcription of the Oxford letter.
The images of docs/img/ are cut by make_images.py; this script only reads crops.json and the image sizes.
It needs Python 3.8 or later and no other package.
"""
import ast, difflib, html, importlib.util, json, os, re, struct, sys, unicodedata

sys.dont_write_bytecode = True   # leave no cache folders in the repository

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
REPO = 'https://github.com/pangoleen/cipher-readings'
CROPS = json.load(open(os.path.join(HERE, 'crops.json'), encoding='utf-8'))
CHECKS = []


def rd(rel):
    return open(os.path.join(ROOT, rel), encoding='utf-8').read()


def check(page, ok, text):
    CHECKS.append((page, bool(ok), text))
    if not ok:
        print('FAIL', page, text)


def esc(s):
    return html.escape(str(s), quote=True)


def norm(s):
    """letters only, lower case, no accents; u = v and i = j, as in the manuscripts"""
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.replace('v', 'u').replace('j', 'i')


def collapse(s):
    return re.sub(r'\s+', ' ', re.sub(r'\n> ?', '\n', s)).strip()


def quoted(page, rel, sentence):
    """the sentence must stand in the file, word for word"""
    ok = collapse(sentence) in collapse(rd(rel))
    check(page, ok, 'in %s: "%s"' % (rel, collapse(sentence)[:70]))
    return sentence


def letter_diffs(a, b):
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    return [(a[i1:i2], b[j1:j2]) for tag, i1, i2, j1, j2 in sm.get_opcodes() if tag != 'equal']


def load_module(rel, name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(ROOT, rel))
    mod = importlib.util.module_from_spec(spec)
    old = sys.path[:]
    sys.path.insert(0, os.path.dirname(os.path.join(ROOT, rel)))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path[:] = old
    return mod


def literal(rel, name):
    """the value of NAME = {...} in a script, read without running the script"""
    m = re.search(r'^%s\s*=\s*(\{.*?\})' % re.escape(name), rd(rel), re.S | re.M)
    return ast.literal_eval(m.group(1))


def jpeg_size(path):
    with open(path, 'rb') as f:
        f.read(2)
        while True:
            b = f.read(1)
            while b and b != b'\xff':
                b = f.read(1)
            while b == b'\xff':
                b = f.read(1)
            if not b:
                raise ValueError(path)
            if 0xC0 <= b[0] <= 0xCF and b[0] not in (0xC4, 0xC8, 0xCC):
                f.read(3)
                h, w = struct.unpack('>HH', f.read(4))
                return w, h
            n = struct.unpack('>H', f.read(2))[0]
            f.read(n - 2)


def img(rel, alt, cls=''):
    w, h = jpeg_size(os.path.join(HERE, rel))
    return '<img src="%s" alt="%s" width="%d" height="%d"%s loading="lazy">' % (
        esc(rel), esc(alt), w, h, ' class="%s"' % cls if cls else '')


def figure(rel, alt, caption, cls='scan'):
    return '<figure class="%s"><div class="scroll">%s</div><figcaption>%s</figcaption></figure>' % (
        cls, img(rel, alt), caption)


def sign_img(page, line, i, name):
    rel = 'img/%s/%s_%02d.jpg' % (page, line, i)
    return img(rel, 'sign ' + name, 'sg')


# ---------------------------------------------------------------- tokens, words, cells

def tok(t, v, letters=None, kind='letter', image='', extra=None, mark=''):
    return {'t': t, 'v': v, 'L': norm(v) if letters is None else letters, 'k': kind, 'img': image,
            'x': extra, 'm': mark}


def group(page, label, toks, units):
    """put the tokens in words; the letters of the tokens must give each word exactly"""
    units = units.split()
    out, cur, acc, ui = [], [], '', 0
    for tk in toks:
        if tk['L'] == '' and not cur:
            out.append(([tk], None))
            continue
        if ui >= len(units):
            check(page, False, '%s: tokens left after the last word' % label)
            out.append(([tk], None))
            continue
        cur.append(tk)
        acc += tk['L']
        target = norm(units[ui])
        if acc == target:
            out.append((cur, units[ui].replace('_', ' ')))
            cur, acc, ui = [], '', ui + 1
        elif not target.startswith(acc):
            check(page, False, '%s: the key gives "%s", the word is "%s"' % (label, acc, units[ui]))
            out.append((cur, '?'))
            cur, acc, ui = [], '', ui + 1
    check(page, ui == len(units) and not cur,
          '%s: %d tokens give the %d words of the page by the key' % (label, len(toks), len(units)))
    return out


def cells(groups, rows3=False):
    h = ['<div class="line">']
    for toks, word in groups:
        h.append('<span class="w"><span class="cs">')
        for tk in toks:
            h.append('<span class="c k-%s">' % tk['k'])
            if tk['img']:
                h.append(tk['img'])
            h.append('<span class="t">%s</span>' % tk['t'])
            if tk['m']:
                h.append('<span class="m">%s</span>' % esc(tk['m']))
            h.append('<span class="v">%s</span>' % (esc(tk['v']) if tk['v'] else '&nbsp;'))
            if rows3:
                h.append('<span class="x">%s</span>' % (esc(tk['x']) if tk['x'] else '&nbsp;'))
            h.append('</span>')
        h.append('</span><span class="wd%s">%s</span></span>' % ('' if word else ' e', esc(word) if word else '&nbsp;'))
    h.append('</div>')
    return ''.join(h)


def keytext(groups):
    return ' '.join(w for _, w in groups if w)


def compare(page, label, key_text, reading, declared, strip=None):
    r = reading
    if strip:
        r = re.sub(strip, ' ', r)
    d = letter_diffs(norm(key_text), norm(r))
    check(page, d == declared, '%s: key text against the reading file: %s' % (
        label, 'the same letters' if not d else 'differences %s (expected %s)' % (d, declared)))


def md(s):
    """the small part of Markdown that the README tables use"""
    s = esc(s)
    s = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', lambda m: '<a href="%s">%s</a>' % (m.group(2), m.group(1)), s)
    s = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'\*([^*]+)\*', r'<em>\1</em>', s)
    s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
    return s


def table(head, rows, cls=''):
    h = ['<div class="scroll"><table%s><thead><tr>' % (' class="%s"' % cls if cls else '')]
    h += ['<th>%s</th>' % c for c in head]
    h.append('</tr></thead><tbody>')
    for r in rows:
        h.append('<tr>' + ''.join('<td>%s</td>' % c for c in r) + '</tr>')
    h.append('</tbody></table></div>')
    return ''.join(h)


CSS = """
:root{--bg:#fbf9f4;--ink:#1f1d1a;--soft:#5d574e;--rule:#d8d1c3;--card:#fffdf8;--link:#7a3b12;--warn:#a23b1e;--mark:#f1e8d2}
@media (prefers-color-scheme:dark){:root{--bg:#191817;--ink:#e9e4d9;--soft:#aaa294;--rule:#3c3934;--card:#22201e;--link:#e0a878;--warn:#f08c6c;--mark:#3a3324}
 img{filter:brightness(.92)}}
*{box-sizing:border-box}
html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:1.06rem/1.62 Georgia,"Iowan Old Style","Palatino Linotype",Palatino,"Times New Roman",serif}
main,header,footer{max-width:54rem;margin:0 auto;padding:0 1.1rem}
header{padding-top:1.4rem}
nav{font-size:.92rem;color:var(--soft)}
a{color:var(--link)}
h1{font-size:1.65rem;line-height:1.25;margin:.5rem 0 .9rem;font-weight:600;text-wrap:balance}
h2{font-size:1.22rem;margin:2.2rem 0 .6rem;padding-top:.7rem;border-top:1px solid var(--rule);font-weight:600}
h3{font-size:1.04rem;margin:1.5rem 0 .4rem;font-weight:600}
p{margin:.55rem 0}
dl.facts{margin:.6rem 0;display:grid;grid-template-columns:max-content 1fr;gap:.35rem .9rem}
dl.facts dt{font-variant:small-caps;letter-spacing:.03em;color:var(--soft)}
dl.facts dd{margin:0}
@media (max-width:34rem){dl.facts{grid-template-columns:1fr;gap:0}dl.facts dd{margin-bottom:.5rem}}
code,.t,.mono{font-family:ui-monospace,"SF Mono",Menlo,Consolas,"DejaVu Sans Mono",monospace;font-size:.86em}
.scroll{overflow-x:auto;max-width:100%}
table{border-collapse:collapse;margin:.6rem 0;font-size:.95rem;font-variant-numeric:tabular-nums}
th,td{border:1px solid var(--rule);padding:.28rem .55rem;text-align:left;vertical-align:top}
th{background:var(--mark);font-weight:600}
table.ring td,table.ring th{text-align:center;padding:.2rem .38rem}
table.ring td.p{color:var(--soft);font-style:italic}
figure{margin:.9rem 0}
figure img{display:block;max-width:100%;height:auto;border:1px solid var(--rule);border-radius:2px}
figure.scan img{min-width:34rem}
figure.sheet img{min-width:0}
figcaption{font-size:.86rem;color:var(--soft);margin-top:.3rem}
.line{display:flex;flex-wrap:wrap;gap:.7rem .8rem;margin:.6rem 0 1rem;align-items:flex-start;overflow-x:auto;max-width:100%;padding-bottom:2px}
.w{display:inline-flex;flex-direction:column}
.cs{display:flex;gap:2px}
.c{display:flex;flex-direction:column;align-items:center;justify-content:flex-end;min-width:1.75rem;padding:2px 4px 1px;background:var(--card);border:1px solid var(--rule);border-radius:3px;line-height:1.25}
.c img.sg{height:3rem;width:auto;border-radius:2px;margin-bottom:2px}
.c .t{color:var(--soft);white-space:nowrap}
.c .t b{color:var(--ink)}
.c .m{font-size:.66rem;color:var(--soft);max-width:5.2rem;text-align:center;line-height:1.15}
.c .v{font-weight:600;white-space:nowrap}
.c .x{font-size:.86rem;color:var(--soft);white-space:nowrap}
.k-null .v,.k-stop .v,.k-unread .v,.k-ill .v{font-weight:400;color:var(--soft);font-style:italic}
.k-clear .v,.k-clear .t{font-style:italic}
.k-conflict{border-color:var(--warn)}
.k-conflict .v,.k-conflict .x{color:var(--warn)}
.k-doubt .v::after{content:" ?";color:var(--warn)}
.wd{margin-top:3px;padding-top:1px;border-top:2px solid var(--soft);text-align:center;font-size:1.02rem;min-height:1.5rem;white-space:nowrap}
.wd.e{border-color:transparent}
.keygrid{display:flex;flex-wrap:wrap;gap:3px;margin:.6rem 0}
blockquote{margin:.6rem 0;padding:.1rem 0 .1rem .9rem;border-left:3px solid var(--rule)}
blockquote p{margin:.3rem 0}
.orig{font-style:italic}
.note{font-size:.92rem;color:var(--soft)}
.diff{color:var(--warn)}
ul{padding-left:1.2rem;margin:.5rem 0}
li{margin:.25rem 0}
footer{margin-top:2.6rem;padding-top:.8rem;padding-bottom:2rem;border-top:1px solid var(--rule);font-size:.88rem;color:var(--soft)}
@media print{body{background:#fff;color:#000;font-size:10.5pt}a{color:#000}nav{display:none}.scroll{overflow:visible}figure.scan img{min-width:0}h2{break-after:avoid}.w,figure,tr{break-inside:avoid}.c{background:#fff}}
"""


def page(fname, title, body, folder=None):
    nav = '<nav><a href="index.html">Readings of historical ciphers</a></nav>' if fname != 'index.html' else ''
    foot = ('The work was done by a model (Claude, by Anthropic), directed by Paolo Rosson. '
            'No palaeographer or historian has checked it yet. Corrections are welcome: '
            '<a href="%s/issues">open an issue</a>. ' % REPO)
    if folder:
        foot += 'All files of this result: <a href="%s/tree/main/%s">%s</a>. ' % (REPO, folder, folder)
    foot += ('Text: CC BY 4.0. Images: under the conditions of their sources. '
             'This page is made by <code>docs/build.py</code> from the files of the repository.')
    doc = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
           '<meta name="viewport" content="width=device-width, initial-scale=1">\n'
           '<title>%s</title>\n<style>%s</style>\n</head>\n<body>\n<header>%s<h1>%s</h1></header>\n'
           '<main>\n%s\n</main>\n<footer>%s</footer>\n</body>\n</html>\n') % (
               esc(title), CSS, nav, esc(title), body, foot)
    open(os.path.join(HERE, fname), 'w', encoding='utf-8').write(doc)
    return fname


def facts(page_id, rel, items):
    """items: (label, html, [phrases that must stand in the README])"""
    readme = collapse(rd(rel))
    h = ['<dl class="facts">']
    for label, text, phrases in items:
        for p in phrases:
            check(page_id, collapse(p) in readme, 'README has: "%s"' % p[:60])
        h.append('<dt>%s</dt><dd>%s</dd>' % (label, text))
    h.append('</dl>')
    return ''.join(h)


def sure(page_id, rel, rows, phrases):
    readme = collapse(rd(rel))
    for p in phrases:
        check(page_id, collapse(p) in readme, 'README has: "%s"' % p[:60])
    return table(['Measure', 'Value'], rows)


def title_of(folder):
    return rd(folder + '/README.md').splitlines()[0].lstrip('# ').strip()


def gh(folder, path, text=None):
    return '<a href="%s/blob/main/%s/%s"><code>%s</code></a>' % (REPO, folder, path, text or path)


# ---------------------------------------------------------------- oxford-1646

def oxford():
    P, F = 'oxford-1646', 'oxford-1646'
    key = {}
    for l in rd(F + '/key1646.tsv').splitlines():
        if l.startswith('#') or l.startswith('code') or not l.strip():
            continue
        c = l.split('\t')
        key[c[0]] = {'v': c[1], 'g': c[2], 'basis': c[4]}
    titus = {}
    for l in rd(F + '/titus_key.tsv').splitlines():
        if l.startswith('#') or l.startswith('code') or not l.strip():
            continue
        c = l.split('\t')
        titus[c[0]] = c[1]
    lines = {}
    for l in open(os.path.join(HERE, 'data', 'oxford_lines.txt'), encoding='utf-8'):
        if l.startswith('#') or not l.strip():
            continue
        n, rest = l.split('\t', 1)
        lines[n] = re.findall(r'\[[^\]]*\]|\S+', rest)
    used = {}

    def toks(raw):
        out = []
        for t in raw:
            if t.startswith('['):
                out.append(tok('clear', t[1:-1], kind='clear'))
            elif t == '?':
                out.append(tok('?', 'illegible', '', 'ill'))
            else:
                n = t.rstrip('?')
                k = key[n]
                used[int(n)] = k
                v, g = k['v'], k['g']
                if g == 'U':
                    out.append(tok(n, 'not read', '', 'unread', extra=g))
                elif v == '_':
                    out.append(tok(n, 'null', '', 'null', extra=g))
                elif v in '.,':
                    out.append(tok(n, 'stop', '', 'stop', extra=g))
                else:
                    out.append(tok(n, v, kind='doubt' if (t.endswith('?') or '?' in g) else 'letter', extra=g))
        return out

    EX = [
        ('3', 'Line 3: the summons of Fairfax',
         'to render Oxford to him for the use of_ye Parliament and expressing that he may hav honorable terms for '
         'himselve and al within_ye garrison if he reasonably accept t r',
         'to render Oxford to him for the use {of ye} Parliament , and {express}ing that he may have honorable terms '
         '{for} himselve and all with{in ye} garrison if he [...] {reasonably} accept . t r(?)',
         'And he [sent] to have Oxford rendered to him for the use of the Parliament, and said that the Governor may '
         'have honourable terms for himself and all within the garrison if he accepts in good time.',
         [('', 'e'), ('', 'l')],
         'The key gives <span class="mono">hav</span> and <span class="mono">al</span>. '
         'The reading file writes "have" and "all".'),
        ('4', 'Line 4, first part: the safe conduct',
         'directions was That_ye y e desired a safe conduct for Sir io munson and Mr to com to with Fairfax',
         'directions was {That ye} y e (they) desired {a} safe conduct for Sir Io. Munson and {Mr} <629: Warwick> '
         'to come to <384> with Fairfax',
         'The direction was that they asked a safe conduct for Sir John Monson and Mr [Warwick] to come to [confer] '
         'with Fairfax',
         [('', 'they'), ('', 'e')],
         'The reading file adds the gloss "(they)" and writes "come" for <span class="mono">com</span>. '
         'The codes 629 and 384 are not read. The reading file gives "Warwick" for 629 as a guess; the printed answer '
         'of the governor names "Master Philip Warwick".'),
        ('6', 'Line 6, first part: no word from the King',
         'what condition for since your departure we hav not received a word from your Majesty',
         '{what} condition , for since your {depart}ure , we have not received {a} word from your Majesty',
         'for since your departure we have received not a word from your Majesty',
         [('', 'e')],
         'The key gives <span class="mono">hav</span>. The reading file writes "have".'),
    ]
    ex_html = []
    for n, title, units, reading, english, declared, note in EX:
        g = group(P, 'line ' + n, toks(lines[n]), units)
        quoted(P, F + '/reading_f10.txt', reading)
        quoted(P, F + '/reading_f10.txt', english)
        compare(P, 'line ' + n, keytext(g), reading, declared, strip=r'<[^>]*>')
        ex_html.append('<h3>%s</h3>%s<blockquote><p class="orig">%s</p><p>%s</p></blockquote><p class="note">%s</p>' % (
            esc(title), cells(g, rows3=True), esc(reading), esc(english), note))

    # the shifts against the Titus cipher
    bands = {}
    for n, k in sorted(key.items(), key=lambda x: int(x[0])):
        m = re.match(r'Titus (\d+) \(Hillier 1852\) \+ shift (\d+)', k['basis'])
        if m:
            tn, sh = m.group(1), int(m.group(2))
            check(P, int(tn) + sh == int(n), 'shift: %s = Titus %s + %d' % (n, tn, sh)) if int(tn) + sh != int(n) else None
            bands.setdefault(sh, []).append((k['v'], tn, n, titus.get(tn, '')))
    readme = rd(F + '/README.md')
    sect = readme[readme.index('| Words | Shift from Titus 1648'):readme.index('74 words are in both tables')]
    band_rows = re.findall(r'^\| ([^|]+) \| \+?(\d+) \|$', sect, re.M)
    check(P, len(band_rows) == 6, 'README has the table of six shifts')
    same = sum(1 for sh in bands for v, tn, n, tv in bands[sh] if norm(tv) == norm(v))
    total = sum(len(b) for b in bands.values())
    for sh in bands:
        for v, tn, n, tv in bands[sh]:
            if norm(tv) != norm(v):
                print('  note: key1646 %s = %s; titus_key %s = %s' % (n, v, tn, tv))
    check(P, same >= total * 0.85, 'Titus values: %d of %d key rows have the same word in titus_key.tsv' % (same, total))
    rows = []
    # an example must have the same word in both key files, and it must stand in the part of the list that the
    # README names for its shift (the key file has some rows with another shift than the README band)
    part = {4: lambda v, tn: 'a' <= v[0].lower() <= 'h' and tn < 450, 0: lambda v, tn: 'i' <= v[0].lower() <= 'n' and tn < 450,
            1: lambda v, tn: 'o' <= v[0].lower() <= 't' and tn < 450, 8: lambda v, tn: v[0].lower() == 'w' and tn < 450,
            9: lambda v, tn: tn >= 600, 10: lambda v, tn: 450 <= tn < 600}
    outside = []
    for sh in bands:
        for v, tn, n, tv in bands[sh]:
            if not part[sh](v, int(tn)):
                outside.append('%s %s -> %s' % (v, tn, n))
    print('  note: key1646.tsv rows with another shift than the README band:', '; '.join(outside))
    nex = 0
    for words, sh in band_rows:
        exs = [x for x in bands.get(int(sh), []) if norm(x[3]) == norm(x[0]) and part[int(sh)](x[0], int(x[1]))][:3 if sh in '48' else 4 if sh == '9' else 3]
        nex += len(exs)
        rows.append([esc(words), '+' + sh if sh != '0' else '0',
                     ', '.join('<span class="mono">%s</span> %s &rarr; %s' % (esc(v), tn, n) for v, tn, n, tv in exs)])
    check(P, nex >= 12, 'shift table: %d example words, each the same word in titus_key.tsv and key1646.tsv' % nex)
    shift_table = table(['Words', 'Shift', 'Examples: word, number of 1648 &rarr; number of 1646'], rows)

    grid = ['<div class="keygrid">']
    for n in sorted(used):
        k = used[n]
        v = k['v']
        kind = 'unread' if k['g'] == 'U' else 'null' if v == '_' else 'stop' if v in '.,' else 'letter'
        show = {'unread': 'not read', 'null': 'null', 'stop': 'stop'}.get(kind, v)
        grid.append('<span class="c k-%s"><span class="t">%d</span><span class="v">%s</span><span class="x">%s</span></span>' % (
            kind, n, esc(show), esc(k['g'])))
    grid.append('</div>')

    body = facts(P, F + '/README.md', [
        ('Document', 'London, British Library, Add MS 72438, f. 10 (DECODE record R8624). [Sir Edward Nicholas, '
         'Secretary of State,] to King Charles I, Oxford, 13 May 1646. The letter was written in Oxford during the '
         'siege and taken by Fairfax\'s army. The name of the writer is our inference.',
         ['London, British Library, Add MS 72438, f. 10 (DECODE record R8624)', 'The name of the writer is our inference']),
        ('New', 'The first connected reading of the letter: 89 % of the tokens read. The key is rebuilt from the '
         'printed cipher of the King with Captain Titus of 1648: the numbers of 1646 are the Titus numbers with a small shift.',
         ['The first connected reading of an intercepted cipher letter', '89 % of the tokens read',
          'The numbers of 1646 are the Titus numbers with a small shift']),
        ('Not ours', 'The cipher text is the transcription of A. Aymeloglu, made in one pass from the DECODE image '
         '(<a href="https://github.com/aaymeloglu/unsolved-ciphers">aaymeloglu/unsolved-ciphers</a>, folder '
         '<code>royalist-1646</code>). He also had about 45 code values from the glosses of Nicholas. '
         'We did not see the manuscript, and we have no image.',
         ['We did not see the manuscript', 'made in one pass from the', 'about 45 code values']),
    ])
    body += '<h2>The key</h2>'
    body += ('<p>The cipher has 261 codes in the rebuilt table: numbers for single letters, for common words and '
             'syllables, for names, and nulls. The word list is the list of the Titus cipher, which George Hillier '
             'printed in 1852 (<em>Narrative of the Attempted Escapes of Charles the First</em>, pp. 153-161). '
             'The letter alphabets of the two keys differ; the one of 1646 was solved from context.</p>')
    body += shift_table
    body += ('<p>The codes of the three worked lines, in order of number. Third row: the basis of the value. '
             '<span class="mono">E</span> = gloss by Nicholas in the print of Evelyn (iv. 178-179); '
             '<span class="mono">E2</span> = our reading of the part of the King\'s letter of 16 August 1646 that Nicholas left without gloss; '
             '<span class="mono">T</span> = Titus cipher with the shift, and it fits the context; '
             '<span class="mono">C</span> = context only; <span class="mono">?</span> = doubtful; '
             '<span class="mono">U</span> = not read.</p>')
    body += ''.join(grid)
    body += '<p>Full table: %s (261 codes, each with its basis). The Titus key: %s.</p>' % (
        gh(F, 'key1646.tsv'), gh(F, 'titus_key.tsv'))
    body += '<h2>Worked example</h2>'
    body += ('<p>We have no image of the manuscript. The numbers below are three lines of A. Aymeloglu\'s '
             'transcription, file <code>royalist-1646/f10_ct.txt</code> of '
             '<a href="https://github.com/aaymeloglu/unsolved-ciphers">his repository</a>. '
             'The rest of his transcription is not copied here. '
             'Each box holds one token: the number, its value, and the basis of the value. '
             'Words in italics are clear words of the manuscript. The line under a group of boxes gives the word.</p>')
    body += ''.join(ex_html)
    body += ('<p class="note">Marks of the reading file: {..} = clear words of the manuscript; (?) = doubtful; '
             '&lt;n&gt; = code not read; [...] = illegible in the transcription.</p>')
    body += '<h2>How sure</h2>'
    body += sure(P, F + '/README.md', [
        ['Tokens in the transcription', '735, of which 20 are illegible there'],
        ['Tokens read with no doubt mark', '652 (89 %)'],
        ['Tokens read with a doubt mark', '43'],
        ['Tokens not read', '20 (17 codes)'],
        ['Words that Nicholas glossed in 1646 and that fit the Titus list with the shifts',
         '20 of 20; with the Titus values shuffled 20,000 times: 5 at most'],
    ], ['735, of which 20 are illegible there', '652 (89 %)', '20 (17 codes)', '20 of 20; with the Titus values shuffled 20,000 times: 5 at most'])
    body += ('<p><strong>Outside check.</strong> The printed papers of 11 May 1646. '
             'Fairfax\'s summons says: "honourable termes for your selfe, and all within the Garrison, if you '
             'seasonably accept thereof". The governor\'s answer asks "a safe conduct for Sir Iohn Mounson, &amp; '
             'Master Philip Warwick". Lines 3 and 4 above give both. On 2 June 1646 the King wrote to Nicholas that he '
             'had received "but one letter from you, w<sup>ch</sup> was of the 5th of May"; this letter begins '
             '"Since mine of ye fift of May".</p>')
    for p in ['honourable termes for your selfe, and all within the', 'a safe conduct for Sir Iohn Mounson, &',
              'but one letter from you', 'Since mine of ye fift of May']:
        check(P, collapse(p) in collapse(readme), 'README has: "%s"' % p)
    body += '<h2>What is not resolved</h2>'
    body += ('<ul><li>17 codes are not read (20 tokens), and 20 tokens are illegible in the transcription.</li>'
             '<li>The transcription had one pass, and it is not ours. The decipherment had one pass. A second, blind pass needs the image.</li>'
             '<li>130 of the 261 code values rest on context only. The key table marks them.</li></ul>')
    for p in ['130 of the 261 code values rest on context only', 'One pass for the decipherment']:
        check(P, p in readme, 'README has: "%s"' % p)
    body += '<p>Reading in words, with an English version: %s. Folder: <a href="%s/tree/main/%s">%s</a>.</p>' % (
        gh(F, 'reading_f10.txt'), REPO, F, F)
    return page('oxford-1646.html', title_of(F), body, F)


# ---------------------------------------------------------------- cocquet-1616

def cocquet():
    P = F = 'cocquet-1616'
    KEY = literal(F + '/decode.py', 'KEY')
    CONS = literal(F + '/decode.py', 'CONS')
    sheet = {}
    for l in rd(F + '/key_fr18009_f156.tsv').splitlines():
        if l.startswith('#') or l.startswith('class'):
            continue
        c = l.split('\t')
        sheet.setdefault((c[0], c[1]), c)
    special = {'n_': ('underlined letter', 'pi (n_)'), '86': ('number', '86'), '89': ('number', '89'),
               'T': ('rule', 'T'), 'DBL': ('rule', 'DBL'), 'oo': ('rule', 'oo (and the other vowels with two dots)'),
               'Z': ('alphabet', 'z'), 'S': ('alphabet', 's')}
    decoded = dict(l.split(': ', 1) for l in rd(F + '/decoded_by_key.txt').splitlines() if l.strip())
    first = {}

    def toks(L):
        out, prev = [], ''
        names = [t for t in CONS[L].split() if t != '|']
        check(P, len(names) == len(CROPS[P]['lines'][L]['signs']), '%s: one sign image for each of the %d signs' % (L, len(names)))
        for i, t in enumerate(names):
            v = KEY[t]
            im = sign_img(P, L, i, t)
            first.setdefault(t, im)
            if v == '=':
                out.append(tok(esc(t), 'doubles: ' + prev, prev, 'letter', im))
            elif v == '':
                out.append(tok(esc(t), 'null', '', 'null', im))
            else:
                v = v.strip().lower()
                out.append(tok(esc(t), v, None, 'letter', im))
                prev = v[-1]
        return out

    UNITS = {'L01': 'que le duc de montaleon auoit mande que sa maieste',
             'L02': 'auoit un sy grand desuoyement hault et bas quil croy',
             'L03': 'oit que elle ne pouuoit passer',
             'L05': 'a don pedro'}
    G = {}
    for L in UNITS:
        G[L] = group(P, L, toks(L), UNITS[L])
        check(P, norm(keytext(G[L])) == norm(decoded[L]), '%s: the same letters as decoded_by_key.txt' % L)
    r1 = quoted(P, F + '/reading.md', '**que le duc de Montaleon auoit mande que sa maieste auoit un sy grand '
                'desuoyement hault et bas qu\'il croyoit qu\'elle ne pouuoit passer**').strip('*')
    e1 = quoted(P, F + '/reading.md', '**that the duke of Monteleone had written that His Majesty had so great a flux '
                'upward and downward (vomiting and diarrhoea) that he believed that His Majesty could not last**').strip('*')
    r2 = quoted(P, F + '/reading.md', '**a don Pedro**').strip('*')
    e2 = quoted(P, F + '/reading.md', '**to Don Pedro**').strip('*')
    compare(P, 'L01-L03', ' '.join(keytext(G[L]) for L in ('L01', 'L02', 'L03')), r1, [('e', '')])
    compare(P, 'L05', keytext(G['L05']), r2, [])

    def line_fig(L, n):
        return figure('img/%s/%s.jpg' % (P, L), 'Cipher line %d of the lower half of f. 317r' % n,
                      'Clairambault 369, f. 317r, cipher line %d (set in two rows here). Source: gallica.bnf.fr / BnF.' % n
                      if L != 'L05' else 'Clairambault 369, f. 317r, line 5: the cipher run between clear French. Source: gallica.bnf.fr / BnF.')

    order = sorted(first, key=lambda t: (len(KEY[t].strip()) != 1 or KEY[t] == '=', KEY[t].lower(), t))
    kg = {}
    for t in order:
        c = sheet.get(special.get(t, ('alphabet', t)))
        check(P, c is not None, 'key sheet file has the sign %s' % t)
        v = KEY[t].strip().lower()
        val = 'doubles' if v == '=' else 'null' if v == '' else v
        if c[0] == 'alphabet':
            m = re.match(r'column (\w), row (\d)', c[3])
            place = '%s, row %s' % (m.group(1), m.group(2))
        else:
            place = {'underlined letter': 'word list', 'number': 'word list', 'rule': 'rule'}[c[0]]
        if c[0] != 'rule' and t not in ('Z', 'S'):
            check(P, v in [x.strip().lower() for x in re.split('[/ ]', c[2])] or norm(c[2]) == norm(v), 'sign %s: value %s on the key sheet file' % (t, c[2]))
        kg.setdefault(val, []).append(tok(esc(t), val, '', 'letter', first[t], extra=place))
    keygrid = cells([(v, k if len(k) == 1 else None) for k, v in kg.items()], rows3=True)
    body = facts(P, F + '/README.md', [
        ('Document', 'Paris, BnF, Clairambault 369, ff. 316-317 (Gallica <code>btv1b9000782k</code>, views 328-330). '
         'Coquet, secretary of the French ambassador in Rome, to Claude Mangot, secretary of state, Rome, 13 November 1616.',
         ['Paris, BnF, Clairambault 369, ff. 316-317', 'secretary of the French ambassador in Rome']),
        ('New', 'A first reading of the cipher passages. The cipher was first solved from context, with the crib '
         '"a don pedro". The key sheet was found afterwards. We found no earlier use of this sheet for this letter.',
         ['A first reading of the cipher passages', 'The cipher was first solved from context, with the crib "a don pedro"',
          'We found no earlier use of this sheet for this letter']),
        ('Not ours', 'The key. It is a period document: Paris, BnF, ms. français 18009, f. 156, "Double du chiffre '
         'baillé à monsieur le marquis de Treinel" (Gallica <code>btv1b90638776</code>, view 181). The marquis de '
         'Tresnel was the ambassador, and Coquet was his secretary.',
         ['Double du chiffre baillé à monsieur le marquis de Treinel', 'The marquis de Tresnel was the ambassador, and Coquet was his secretary']),
    ])
    body += '<h2>The key</h2>'
    body += ('<p>The cipher has several signs for each letter, numbers and underlined letters for common words, '
             'nulls, and two signs that double the letter before them. Here is each sign of the worked lines, cut from '
             'the letter and set under its letter. The names of the signs are ours.</p>')
    body += keygrid
    body += ('<p class="note">In each box: the sign, our name for it, its value, and its place on the key sheet '
             '(column letter and row of the alphabet; "word list" = the list of numbers and underlined letters; '
             '"rule" = a note on the sheet). <span class="mono">Z</span> and <span class="mono">S</span> are '
             '<span class="mono">z</span> and <span class="mono">s</span> written larger. On the sheet the column V '
             'serves for u and v.</p>')
    body += figure('img/%s/fr18009_f156_key.jpg' % P, 'The key sheet of the marquis de Tresnel, BnF fr. 18009, f. 156',
                   'The key sheet, reduced: BnF, ms. français 18009, f. 156. The alphabet is the band at the top: '
                   '22 columns, A to Z, with two to four signs under each letter. Source: gallica.bnf.fr / BnF.', 'scan sheet')
    body += figure('img/%s/fr18009_f156_alphabet_left.jpg' % P, 'Key sheet, alphabet, columns A to M',
                   'The alphabet of the key sheet, left half (columns A to M). Row 1 is the first sign under a letter. Source: gallica.bnf.fr / BnF.')
    body += figure('img/%s/fr18009_f156_alphabet_right.jpg' % P, 'Key sheet, alphabet, columns N to Z',
                   'The alphabet of the key sheet, right half (columns N to Z). Source: gallica.bnf.fr / BnF.')
    body += '<p>Our transcription of the whole sheet (259 rows, one pass): %s. The decoder with the key table: %s.</p>' % (
        gh(F, 'key_fr18009_f156.tsv'), gh(F, 'decode.py'))
    body += '<h2>Worked example</h2>'
    body += ('<p>The first cipher run fills three lines of f. 317r. Each box holds one sign: its image, our name for '
             'it, and its value by the key. The line under a group of boxes gives the word; the word division is ours. '
             'Spelling is that of the cipher (u and v are one letter).</p>')
    for n, L in enumerate(('L01', 'L02', 'L03'), 1):
        body += '<h3>Line %d</h3>%s%s' % (n, line_fig(L, n), cells(G[L]))
    body += ('<blockquote><p class="orig">%s</p><p>%s [two hours].</p></blockquote>'
             '<p class="note">The word "croyoit" runs over the end of line 2. The cipher has "que elle"; the reading '
             'file writes "qu\'elle". The signs <span class="mono">T</span> and <span class="mono">DBL</span> double '
             'the letter before them: gran<strong>dd</strong>esuoyement, pou<strong>uu</strong>oit, pa<strong>ss</strong>er.</p>') % (esc(r1), esc(e1))
    body += '<h3>Line 5</h3>%s%s' % (line_fig('L05', 5), cells(G['L05']))
    body += ('<blockquote><p class="orig">[cest homme est dangereux et mande force choses] %s</p><p>[this man is '
             'dangerous and writes many things] %s</p></blockquote><p class="note">The two last signs are nulls. '
             '"a don pedro" was the crib that opened the cipher.</p>') % (esc(r2), esc(e2))
    body += '<h2>How sure</h2>'
    body += sure(P, F + '/README.md', [
        ['Cipher signs', '189, in nine runs inside clear French'],
        ['Signs identical in the two transcription passes (the second blind)', '179 (94.7 %); no difference changes a word'],
        ['Sign values of the context solution that agree with the key sheet', '43 of 43'],
        ['Four-letter-group score of the reading', '-10.47; 2,000 shuffled keys: mean -15.42, best -13.13'],
    ], ['189, in nine runs inside clear French', '179 (94.7 %); no difference changes a word', '43 of 43',
        '-10.47; 2,000 shuffled keys: mean -15.42, best -13.13'])
    body += ('<p><strong>Outside check.</strong> The key sheet itself. The solution from context came first; all 43 '
             'sign values of that solution agree with the sheet, with no conflict. The sheet then corrected five points '
             '(the code 89 = "qu\'il", the words "hault" and "quant", the sign for "il", and the doubling sign).</p>')
    body += '<h2>What is not resolved</h2>'
    body += ('<ul><li>The clear French around the cipher had one pass only, and some clear words are doubtful ("son frere" among them).</li>'
             '<li>The first sign of the word read "car" has no exact match on the key sheet.</li>'
             '<li>Two pairs of signs are close in shape, and the context decides between them.</li>'
             '<li>Our transcription of the key sheet had one pass.</li></ul>')
    readme = rd(F + '/README.md')
    for p in ['The first sign of the word read "car" has no exact match on the key sheet', 'Two pairs of signs are close',
              'The sheet then corrected five points']:
        check(P, p in collapse(readme), 'README has: "%s"' % p)
    body += '<p>French text with the cipher passages, and an English translation: %s. Folder: <a href="%s/tree/main/%s">%s</a>.</p>' % (
        gh(F, 'reading.md'), REPO, F, F)
    return page('cocquet-1616.html', title_of(F), body, F)


# ---------------------------------------------------------------- espagnol-318

def es318():
    P = F = 'espagnol-318'
    lib = load_module(F + '/lib.py', 'es318lib')
    keymod = load_module(F + '/key.py', 'es318key')
    KEY, CODES = keymod.KEY, keymod.CODES
    shapes = dict(re.findall(r'^\| ([^|]+?) \| (.+?) \|$', rd(F + '/transcription/SIGNS.md'), re.M))
    raw = {}
    for f in ('f120r', 'f121r'):
        for lab, t in lib.load(os.path.join(ROOT, F, 'transcription', f + '_passA.txt')):
            raw[f + '_' + lab] = t
        for lab, t in lib.load(os.path.join(ROOT, F, 'transcription', f + '_passB.txt')):
            raw[f + '_' + lab + 'B'] = t
    first, usedcodes = {}, {}

    def toks(L, a=0, b=None, off=0):
        out = []
        src = raw[L][a:b]
        check(P, len(src) == len(CROPS[P]['lines'][L]['signs']) - off, '%s: one image for each of the %d tokens' % (L, len(src)))
        for i, t in enumerate(src):
            im = sign_img(P, L, i + off, t[1])
            if t[0] == 'code':
                c = t[1]
                if c in ('otto', 'malz'):
                    out.append(tok(esc(c), CODES[c][0], None, 'letter', im))
                    usedcodes[c] = CODES[c]
                elif c in CODES:
                    usedcodes[c] = CODES[c]
                    out.append(tok(esc(c), CODES[c][0], None, 'doubt' if CODES[c][1] == 'C' else 'letter', im))
                else:
                    out.append(tok(esc(c), 'no value', '', 'unread', im))
            elif t[1] in ('.', ',', '/', '/.'):
                out.append(tok(esc(t[1]), 'stop', '', 'stop', im))
            else:
                first.setdefault(t[1], im)
                out.append(tok(esc(t[1]), KEY[t[1]], None, 'letter', im))
        return out

    def passes_agree(L, a=0, b=None):
        x = [(t[0], t[1]) for t in raw[L][a:b]]
        y = [(t[0], t[1]) for t in raw[L + 'B'][a:b]]
        return sum(1 for p, q in zip(x, y) if p == q), len(x)

    EX = [
        ('f120r_L01', (12, 33, 1), 'f. 120r, line 1, tokens 13 to 33: after the rout',
         'luego depues del desbarate', 'luego depues del desbarate',
         'The viceroy wrote right after the "desbarate" (the French defeat near Gioia, 21 April 1503).', [],
         'The line begins with code words that have no sure value; the example starts at the first sign of "luego".'),
        ('f120r_L07', (0, None, 0), 'f. 120r, line 7: the captains in the fortress',
         'el aseguradoles que puestos en la aortaleza a don ioan de',
         'el, asegurandoles que, puestos en la fortaleza a don Joan de',
         'Don Juan de Cardona, Antonio de Leyva and Carvajal were put in the fortress so that an inventory could be made and a good account given.',
         [('', 'n'), ('a', 'f')],
         'Two letters differ. The key gives <span class="mono">aseguradoles</span>; the reading file writes '
         '"asegurandoles". The key gives <span class="mono">aortaleza</span>; the reading file writes "fortaleza": '
         'the transcription has one name, <span class="mono">p</span>, for the sign of a and the sign of f, and the '
         'reading restores f by context. The name "Cardona" follows in line 8.'),
        ('f121r_L21', (0, None, 0), 'f. 121r, line 21: the threat to don Hugo',
         'y me han dicho stuuieron para dar le de punyaladas',
         'y me han dicho stuvieron para darle de punyaladas',
         'Some knights told him they came near to stabbing don Hugo.', [],
         'The first token is a code word with no value.'),
    ]
    ex_html = []
    for L, (a, b, off), title, units, reading, english, declared, note in EX:
        g = group(P, L, toks(L, a, b, off), units)
        quoted(P, F + '/READING.md', reading)
        quoted(P, F + '/READING.md', english)
        compare(P, L, keytext(g), reading, declared)
        same, n = passes_agree(L, a, b)
        d = CROPS[P]['lines'][L]
        cap = 'Espagnol 318, %s%s. Source: gallica.bnf.fr / BnF.' % (
            title.split(':')[0], ' (set in two rows here)' if d['nseg'] > 1 else '')
        ex_html.append('<h3>%s</h3>%s%s<blockquote><p class="orig">%s</p><p>%s</p></blockquote><p class="note">%s '
                       'The two transcription passes have the same token in %d of these %d places.</p>' % (
                           esc(title), figure('img/%s/%s.jpg' % (P, L), 'Cipher line: ' + title, cap), cells(g),
                           esc(reading), esc(english), note, same, n))
    counts = dict((s, c) for s, l, c in re.findall(r'^\| `([^`]+)` \| (\w+) \| (\d+) \|$', rd(F + '/KEY_TABLE.md'), re.M))
    kg = {}
    for s in sorted(KEY, key=lambda s: (KEY[s], -int(counts.get(s, 0)))):
        kg.setdefault(KEY[s], []).append(tok(esc(s), KEY[s], '', 'letter', first.get(s, ''), extra=counts.get(s, '') + ' times'))
    keygrid = cells([(v, k) for k, v in kg.items()], rows3=True)
    check(P, len(KEY) == 44, 'key.py has 44 signs')
    crow = [['<span class="mono">%s</span>' % c, '<strong>%s</strong>' % esc(v[0]),
             {'A': 'A: fixed by several clear contexts', 'B': 'B: fits every place, but few places', 'C': 'C: a guess'}[v[1]]]
            for c, v in sorted(usedcodes.items())]
    body = facts(P, F + '/README.md', [
        ('Document', 'Paris, BnF, ms. Espagnol 318, no. 94, ff. 120r-121v (Gallica <code>btv1b52503046q</code>, '
         'views 452-455). Juan de Lanuza, viceroy of Sicily, to King Ferdinand, Messina, 27 April 1503.',
         ['Paris, BnF, ms. Espagnol 318, no. 94, ff. 120r-121v', 'Juan de Lanuza, viceroy of Sicily, to King Ferdinand, Messina, 27 April 1503']),
        ('New', 'A first reading. The key is rebuilt from the letter itself. It is a reading in large part, not a full '
         'one: 64 code words have no value. We found no earlier reading and no printed text.',
         ['The key is rebuilt from the letter itself', 'It is a reading in large part, not a full one', '64 code words have no value',
          'We found no earlier reading and no printed text']),
        ('Not seen', 'The original key ("Cifra del visorrey", Real Academia de la Historia, 9/15 ff. 1-6) is not '
         'online and was not seen. The published keys of the Catholic Monarchs do not fit.',
         ['is not online and was not seen', 'The published keys of the Catholic Monarchs do not fit']),
    ])
    body += '<h2>The key</h2>'
    body += ('<p>A symbol alphabet with several signs for each letter (44 signs for 20 letters), and code words of '
             'two to four letters for common words and names. Two code words stand for letters: '
             '<span class="mono">otto</span> is c, and <span class="mono">malz</span> is ll. '
             'The names of the signs are ours. The image of a sign is cut from the three lines below.</p>')
    body += keygrid
    body += ('<p class="note">In each box: the sign, our name for it, its letter, and how many times the letter has '
             'it. A box with no image: the sign is not in the three lines below. The shapes in words: %s.</p>') % gh(F, 'transcription/SIGNS.md')
    body += '<p>The code words of the three lines:</p>' + table(['Code word', 'Value', 'Basis'], crow)
    body += '<p>All 36 code words with a value, and the 64 with none: %s. The key as a table for the decoder: %s.</p>' % (
        gh(F, 'KEY_TABLE.md'), gh(F, 'key.py'))
    body += '<h2>Worked example</h2>'
    body += ('<p>Each box holds one token of the first transcription pass: its image, its name, and its value by the '
             'key. The line under a group of boxes gives the word; the word division is ours.</p>')
    body += ''.join(ex_html)
    body += '<h2>How sure</h2>'
    body += sure(P, F + '/README.md', [
        ['Cipher lines', '98, on three pages'],
        ['Tokens identical in two blind transcription passes', '93.2 %, 96.0 % and 92.9 % for the three pages'],
        ['Sign tokens with a letter value', '2,521 of 2,537'],
        ['Code-word tokens with a value', '570 of 677'],
        ['Five-letter-group score of the key', '-12.1 to -12.4; 200 shuffled keys: mean -18.5, best -17.5; real Spanish: -10.8'],
    ], ['98, on three pages', '93.2 %, 96.0 % and 92.9 % for the three pages', '2,521 of 2,537', '570 of 677',
        '-12.1 to -12.4; 200 shuffled keys: mean -18.5, best -17.5; real Spanish: -10.8'])
    body += ('<p><strong>Outside check.</strong> The names agree with the chronicles of the Great Captain; they were '
             'not used as a crib. Zurita (<em>Historia del rey don Hernando</em>, book 5, ch. 25 and 29) used the same '
             'matter: he has "Hernando de Valencia", "Alonso Guerrero", the anger of the Cardonas, and Gioia "puesto a '
             'saco, y quemado". He does not have the sack of the fortress by night, the inquiry, or the threat to stab '
             'don Hugo. A search of the printed sources found no clear text of the letter.</p>')
    readme = collapse(rd(F + '/README.md'))
    for p in ['The names agree with the chronicles of the Great Captain. They were not used as a crib.',
              'puesto a saco, y quemado', 'He does not have the sack of the fortress by night, the inquiry, or the threat to stab don Hugo']:
        check(P, p in readme, 'README has: "%s"' % p[:60])
    body += '<h2>What is not resolved</h2>'
    body += ('<ul><li>64 code words have no value. They stand mostly in the stretches that the reading marks with "...".</li>'
             '<li>The transcription does not separate the sign for f from one sign for a. The letter f was restored by context.</li>'
             '<li>Three signs that look alike were confused by the passes. A third pass can change single words.</li>'
             '<li>A line that we do not show for this reason: f. 120r, line 12, where the reading has "la camara de mosse '
             'de Aubeni". The two passes give <span class="mono">clmara</span> and <span class="mono">mosae</span> or '
             '<span class="mono">mousae</span> there. Both passes are in %s.</li></ul>') % gh(F, 'DECODE_RAW.md')
    for p in ['The transcription does not separate the sign for f from one sign for a', 'Three signs that look alike were confused by the passes']:
        check(P, p in readme, 'README has: "%s"' % p[:60])
    check(P, 'clmara DE mo(|u)sae DE aubeni' in rd(F + '/DECODE_RAW.md'), 'DECODE_RAW.md has the two passes of f. 120r line 12')
    body += '<p>Edited reading and English summary: %s. Folder: <a href="%s/tree/main/%s">%s</a>.</p>' % (
        gh(F, 'READING.md'), REPO, F, F)
    return page('espagnol-318.html', title_of(F), body, F)


# ---------------------------------------------------------------- dutch-1653

def dutch():
    P = F = 'dutch-1653'
    model = load_module(F + '/model.py', 'dutchmodel')
    runs, cur = {}, None
    for l in rd(F + '/thurloe_groups.txt').splitlines():
        if re.match(r'RUN\d', l):
            cur = l.strip()
            runs[cur] = []
        elif l.startswith('[clear]') or l.startswith('#') or not l.strip():
            cur = None if l.startswith('[clear]') else cur
        elif cur:
            runs[cur] += re.findall(r'\d+', l)
    align = {}
    for l in rd(F + '/alignment.tsv').splitlines()[1:]:
        c = l.split('\t')
        align[(c[0], int(c[1]))] = c
    keyrows = [l.split('\t') for l in rd(F + '/key.tsv').splitlines() if l and not l.startswith('#')][1:]
    seen = {(int(a), int(n)): int(s) + int(s2) for a, let, n, s, s2 in keyrows}
    for a, let, n, s, s2 in keyrows:
        check(P, model.table(int(a))[int(n)] == let, 'key.tsv') if model.table(int(a))[int(n)] != let else None
    check(P, len(keyrows) == 120, 'key.tsv has 5 x 24 = 120 values, and model.py gives the same table')

    def toks(nums, run=None):
        out, k = [], None
        for i, g in enumerate(nums, 1):
            if len(g) == 3 and g[0] in '12345' and (run is None or align[(run, i)][3] not in ('?', '')):
                k = int(g[0])
                n = int(g[1:])
                show = '<b>%s</b>%s' % (g[0], g[1:])
            elif len(g) == 3:
                out.append(tok(g, 'code word', '', 'unread', extra=''))
                continue
            else:
                n, show = int(g), g
            v = model.table(k).get(n) if k else None
            if run:
                c = align[(run, i)]
                check(P, c[2] == g and c[5] == v, '%s group %d' % (run, i)) if not (c[2] == g and c[5] == v) else None
                kind = 'letter' if c[7] == 'FIT' else 'conflict' if c[7] == 'CONFLICT' else 'doubt'
                out.append(tok(show, v, None, kind, extra=c[6] if c[6] not in ('-', '') else '(none)'))
            elif v is None:
                out.append(tok(show, 'not in the ring', '', 'unread'))
            else:
                out.append(tok(show, v))
        return out

    g1 = group(P, 'run 1', toks(runs['RUN1'], 'RUN1'),
               'om door xxdn expressen afgesonden de plotsn van desen staet te doen recognoszceren')
    st = [align[('RUN1', i)][7] for i in range(1, 71)]
    check(P, st.count('FIT') == 64 and st.count('CONFLICT') == 6, 'run 1: 64 groups fit the minute, 6 conflict (alignment.tsv)')
    allst = [c[7] for c in align.values()]
    check(P, allst.count('FIT') == 124 and allst.count('CONFLICT') == 6 and allst.count('SPELLING') == 3,
          'alignment.tsv: 124 fit, 3 spelling, 6 conflicts')
    minute = quoted(P, F + '/verbael_no6.txt', '{{om door eenen Expressen afgesonden, de Vlooten van desen Staet te doen recognosceeren}}').strip('{}')
    rtxt = rd(F + '/reading_boreel_to_deputies_1653-09-13.txt')
    m = re.search(r'alone with ([\d. ]+?) ;', collapse(rtxt))
    g2 = group(P, '13 September', toks(re.findall(r'\d+', m.group(1))), 'in iames p rc')
    quoted(P, F + '/reading_boreel_to_deputies_1653-09-13.txt', 'IN IAMES P?RC')
    quoted(P, F + '/reading_boreel_to_deputies_1653-09-13.txt', 'dat sy seer qualyck geinformeert syn, van de gementioneerde Conferentie in St. James Parck')

    ring = model.RING
    rows = []
    for k in range(1, 6):
        t = {v: n for n, v in model.table(k).items()}
        rows.append('<tr><th>%d</th>%s</tr>' % (k, ''.join(
            '<td%s>%d</td>' % ('' if seen[(k, t[c])] else ' class="p"', t[c]) for c in model.ALPHA)))
    ringtable = ('<div class="scroll"><table class="ring"><thead><tr><th>Indicator</th>%s</tr></thead><tbody>%s</tbody></table></div>' % (
        ''.join('<th>%s</th>' % c for c in model.ALPHA), ''.join(rows)))
    body = facts(P, F + '/README.md', [
        ('Document', 'Thurloe, <em>State Papers</em>, vol. 1 (1742), p. 435: Beverningk and Van de Perre, deputies '
         'of the States General in England, to Willem Boreel, the Dutch ambassador in France, Westminster, '
         '22 August / 1 September 1653. Cromwell\'s government intercepted the letter; the print gives an English '
         'translation and leaves the cipher in numbers.',
         ['Thurloe i.435', 'Willem Boreel, the Dutch ambassador in France', "Cromwell's government intercepted the letters"]),
        ('New', 'The link between the two printed books, and the key of the cipher. We found no earlier '
         'reconstruction of it. New and small: a reading of 12 cipher groups in Boreel\'s letter of 13 September 1653.',
         ['The link between the two printed books, and the key of the cipher. We found no earlier reconstruction of it.',
          'A reading of 12 cipher groups']),
        ('Reproduced', 'The text of the letter of 1 September 1653. The Dutch minute of this letter is in print: '
         '<em>Verbael gehouden door de Heeren H. van Beverningk ...</em> (1725), pp. 97-99, No. 6.',
         ['The text of the letter of 1 September 1653 (Thurloe i.435). The Dutch minute of this letter is in print']),
    ])
    body += '<h2>The key</h2>'
    body += ('<ol><li><strong>A ring of 24 numbers</strong>, 10 to 33, in this order: <span class="mono">%s</span>. '
             'Even numbers go down, odd numbers go up.</li>'
             '<li><strong>24 letters</strong> follow the ring: <span class="mono">%s</span> (i = j, v = u).</li>'
             '<li><strong>An indicator digit</strong>, 1 to 5, sets the letter a on that place of the ring.</li>'
             '<li><strong>A group of three digits</strong> is the indicator and the first letter: '
             '<span class="mono"><b>2</b>22</span> is alphabet 2 and the number 22, which is e. The groups of two '
             'digits that follow stay in that alphabet until the next group of three digits.</li></ol>') % (
                 ' '.join(map(str, ring)), ' '.join(model.ALPHA))
    check(P, '`32 30 28 26 24 22 20 18 16 14 12 10 11 13 15 17 19 21 23 25 27 29 31 33`' in rd(F + '/README.md')
          and ' '.join(map(str, ring)) == '32 30 28 26 24 22 20 18 16 14 12 10 11 13 15 17 19 21 23 25 27 29 31 33', 'the ring of model.py is the ring of the README')
    body += ringtable
    body += ('<p class="note">The whole table is 5 &times; 24 = 120 values from this one rule. A number in grey '
             'italics is predicted by the ring only: neither letter shows it. Alphabet 4 is not used in either letter. '
             'There are no nulls and no syllables. Numbers above 100 that are not indicators are words of an older '
             'general code.</p>')
    body += '<p>The table as a file: %s. The rule as a script: %s.</p>' % (gh(F, 'key.tsv'), gh(F, 'model.py'))
    body += '<h2>Worked example</h2>'
    body += '<h3>The first cipher run of the letter of 1 September 1653</h3>'
    body += figure('img/%s/thurloe_i435_run1.jpg' % P, 'Thurloe, State Papers, vol. 1, p. 435: the first cipher run',
                   'Thurloe, <em>State Papers</em>, vol. 1 (London, 1742), p. 435: "but we thought fit and that it did '
                   'concerne us," and 70 cipher groups. Public domain; scan of the Internet Archive.')
    body += figure('img/%s/verbael_p98.jpg' % P, 'Verbael (1725), p. 98: the same sentence of the Dutch minute',
                   'The Dutch minute of the same sentence: <em>Verbael</em> (1725), p. 98. Public domain; scan of Google Books.')
    body += ('<p>Each box holds one group: the group as printed (the indicator digit is bold), the letter that the '
             'ring gives, and the letter of the Dutch minute at that place. A red box is a conflict.</p>')
    body += cells(g1, rows3=True)
    body += ('<blockquote><p class="orig">[maer wy hebben ons laeten gelegen syn,] %s</p><p>[but we made it our '
             'business] to have the fleets of this State reconnoitred by a man sent on purpose (our translation of the '
             'minute; Thurloe has no English for the cipher).</p></blockquote>') % esc(minute)
    body += ('<p class="note">64 of the 70 groups give the letter of the minute. The six conflicts: '
             '<span class="mono">29 29 26</span> give "xxd" where the minute has "eene"; <span class="mono">17</span> '
             'gives p for the V of "Vlooten", and <span class="mono">23</span> gives s for its e; '
             '<span class="mono">26</span> gives one z too many in "recognosceeren". The print probably has wrong '
             'digits there: in a letter with a known key the same edition prints 12 wrong groups in 207.</p>')
    check(P, 'it prints 12 wrong\ngroups in 207' in rd(F + '/README.md') or 'it prints 12 wrong groups in 207' in collapse(rd(F + '/README.md')), 'README: 12 wrong groups in 207')
    body += '<h3>Boreel to the deputies, 13 September 1653 (Thurloe i.454)</h3>'
    body += figure('img/%s/thurloe_i454.jpg' % P, 'Thurloe, State Papers, vol. 1, p. 454: twelve cipher groups',
                   'Thurloe, <em>State Papers</em>, vol. 1 (London, 1742), p. 454. Public domain; scan of the Internet Archive.')
    body += ('<p>The print: "a conference or discourse, which the lord Beverning should have lately all alone with '
             '168. 116. 11. 16. 32. 10. 24. 21. 15. 52. 19. 28". Above 168 the print has the gloss "general Cromwell". '
             'No Dutch text of this letter is known; the ring alone gives the letters.</p>')
    body += cells(g2)
    body += ('<blockquote><p class="orig">[Cromwell] IN IAMES P?RC</p><p>in James parc (St James\'s Park). The group '
             '52 is not in the ring; with 32 (a) the word is "parc". The deputies\' printed reply names the '
             '"Conferentie in St. James Parck" (<em>Verbael</em>, p. 111), so the fact itself is known.</p></blockquote>')
    body += '<h2>How sure</h2>'
    body += sure(P, F + '/README.md', [
        ['Groups of the letter of 1 September, all checked on the page image of the 1742 edition', '136'],
        ['Groups that fit the minute', '124, and 2 more if "6" is a misprint of "16"'],
        ['Spelling differences between the letter and the minute', '3'],
        ['Conflicts', '6'],
        ['Open', '1 (the group 117, probably a code word)'],
        ['Alphabets 1 and 3 predicted from alphabets 2 and 5', '41 of 43 groups right'],
        ['Best of 5,000 random rings, with a free shift for each alphabet', '60 of 131 groups; the ring above gives 127'],
    ], ['All 136 groups were checked on the page image of the 1742 edition', '124, and 2 more if "6" is a misprint of "16"',
        '41 of 43 groups right', '60 of 131 groups; the ring above gives 127', '1 (the group 117, probably a code word)'])
    body += ('<p><strong>Outside check.</strong> The printed <em>Verbael</em> of the embassy. Its first sentence agrees '
             'word for word with the clear text in Thurloe, and its minute gives the letters of all three cipher runs. '
             'The alignment of the runs with the minute gave two alphabets; the ring and the indicator rule came from '
             'their structure; the other two alphabets were then predicted and tested.</p>')
    body += '<h2>What is not resolved</h2>'
    body += ('<ul><li>Three groups that give "xxd" where the minute has "eene". No shift explains them.</li>'
             '<li>The code group 117.</li>'
             '<li>The manuscript of the intercepted letter (Bodleian, Rawlinson A) was not seen. It can settle the printed groups that conflict.</li>'
             '<li>The letters to De Witt in the same volume use another cipher. R. Fruin printed its key in 1906; it is not ours.</li></ul>')
    readme = collapse(rd(F + '/README.md'))
    for p in ['Three groups that give "xxd" where the minute has "eene". No shift explains them', 'The code group 117',
              'R. Fruin printed its key in 1906', 'Its first sentence agrees word for word with the clear text in Thurloe']:
        check(P, p in readme, 'README has: "%s"' % p[:60])
    body += '<p>All 136 groups against the minute: %s. Our transcription of the minute: %s. Folder: <a href="%s/tree/main/%s">%s</a>.</p>' % (
        gh(F, 'alignment.tsv'), gh(F, 'verbael_no6.txt'), REPO, F, F)
    return page('dutch-1653.html', title_of(F), body, F)


# ---------------------------------------------------------------- espagnol-132

def es132():
    P = F = 'espagnol-132'
    c2 = load_module(F + '/c2.py', 'es132c2')
    c4 = load_module(F + '/c4.py', 'es132c4')
    passA = dict(l.rstrip('\n').split('\t', 1) for l in rd(F + '/passes/f26r_passA.tsv').splitlines() if '\t' in l)
    passB = dict(l.rstrip('\n').split('\t', 1) for l in rd(F + '/passes/f26r_passB.tsv').splitlines() if '\t' in l)

    def toks2(L):
        out = []
        for g in passA[L].split():
            v = c2.dec_group(g)
            if g.startswith('~'):
                out.append(tok(esc(g), 'null', '', 'null'))
            else:
                out.append(tok(esc(g), v, None, 'doubt' if g.endswith('?') else 'letter'))
        return out

    U = {'L18': 'en yrlanda le he mandado proueer de', 'L19': 'ueynte mill escudos en oro con purso',
         'L20': 'na propria secretamente para este efeto'}
    G = {L: group(P, 'f. 26r ' + L, toks2(L), U[L]) for L in U}
    reading = quoted(P, F + '/reading_f26r.md', 'en Yrlanda, le he mandado proveer de veynte mill escudos en oro, con '
                     'persona propria, secretamente, para este efeto')
    english = quoted(P, F + '/reading_f26r.md', 'that he means to raise in Ireland. I have therefore ordered twenty '
                     'thousand escudos in gold to be provided to him, by a man of my own, in secret, for this purpose.')
    compare(P, 'f. 26r L18-L20', ' '.join(keytext(G[L]) for L in ('L18', 'L19', 'L20')), reading, [('u', 'e')])
    agree = {}
    for L in U:
        a, b = passA[L].split(), passB[L].split()
        sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
        agree[L] = (sum(x.size for x in sm.get_matching_blocks()), len(a))

    m = re.search(r'dado de q\[ue\] no << (.*?) >>', rd(F + '/passes/perez_passA.txt'))
    mb = re.search(r'dado de q\[ue\] no << (.*?) >>', rd(F + '/passes/f157_passB.txt'))
    check(P, m and mb and m.group(1) == mb.group(1), 'f. 157r: the two passes have the same 16 groups')
    t4 = []
    for g in m.group(1).split():
        v = c4.dec_group(g)
        t4.append(tok(esc(g), 'null', '', 'null') if v == '' else tok(esc(g), v))
    g4 = group(P, 'f. 157r', t4, 'aya ay arcauti ni nadie')
    r4 = quoted(P, F + '/reading_perez_f87_f157_f179.md', 'de que no «aya ay Arcauti ni nadie» sino solo «[V.m.]»')
    e4 = quoted(P, F + '/reading_perez_f87_f157_f179.md', '**that neither Arcauti nor anyone else be there, but only you.**').strip('*')
    compare(P, 'f. 157r', keytext(g4), 'aya ay Arcauti ni nadie', [])

    def alpha_table(alpha, per=11):
        items = sorted(alpha.items())
        h = '<div class="scroll"><table class="ring"><tbody>'
        for i in range(0, len(items), per):
            part = items[i:i + per]
            h += '<tr><th>figure</th>%s</tr><tr><th>letter</th>%s</tr>' % (
                ''.join('<td class="mono">%d</td>' % n for n, _ in part), ''.join('<td><strong>%s</strong></td>' % c for _, c in part))
        return h + '</tbody></table></div>'

    def pairs(d, names):
        return table(names, [['<span class="mono">%s</span>' % esc(k), '<strong>%s</strong>' % esc(v)] for k, v in d.items()])

    marks2 = {'p': 'a small hook like a rho, after the figure', '+': 'a small cross after the figure',
              ',': 'a dot below the figure', "'": 'a dot above the figure', '.': 'a dot to the right of the figure'}
    marks4 = {'.': 'a dot to the right', '+': 'a small cross after the figure', ',': 'a dot below',
              'o': 'a hook like a 6 after the figure', "'": 'a dot above'}
    body = facts(P, F + '/README.md', [
        ('Document', 'Paris, BnF, ms. Espagnol 132 (Gallica <code>btv1b10032556x</code>): the secret letters of Philip II '
         'and of his secretary Antonio Pérez to Juan de Vargas Mexía, Spanish ambassador in France, 1577 to 1580. '
         'Five pieces: Pérez to Vargas, Madrid, 13 September 1578 (f. 87), 8 December 1578 (f. 157) and 26 January 1579 '
         '(f. 179); Philip II to Vargas, March 1578 (f. 26r, first page only); a memorial in Italian of the Duke of '
         'Savoy (ff. 273-274).',
         ['Paris, BnF, ms. Espagnol 132 holds the secret letters of Philip II and of his secretary Antonio Pérez to Juan de Vargas Mexía',
          'Madrid, 13 September 1578 (f. 87), 8 December 1578 (f. 157), 26 January 1579 (f. 179)']),
        ('New', 'The readings of five pieces that no other project had. For the Pérez letters: the cipher passages '
         '(the plain Spanish is in print, with <code>[CIFRA]</code> in place of every cipher passage). A few code values, '
         'each with its evidence.',
         ['This repository reads the five pieces that none of them had', 'in place of every cipher passage',
          'added a few code values, each with its evidence']),
        ('Not ours', 'The keys. J. P. Devos published the ciphers of Vargas Mexía in 1950, and S. Tomokiyo completed '
         'and broke the remaining ones in 2020. The project <code>el-descifrador/cabinet-noir</code> published some '
         'code values of Pérez\'s private cipher on 2 October 2026. We applied these keys.',
         ['J. P. Devos published the ciphers of Vargas Mexía in 1950, and S. Tomokiyo completed and broke the remaining ones in', 'We applied these keys']),
    ])
    body += '<h2>The keys</h2>'
    body += ('<p>Both ciphers work in the same way. A figure stands for a consonant or a vowel. A small mark on the '
             'figure adds the vowel that follows. A few letter-like signs stand for a pair of consonants. '
             'The tables below are the tables of the two decoders, %s and %s; the notation of the marks is that of our '
             'transcription passes.</p>') % (gh(F, 'c2.py'), gh(F, 'c4.py'))
    body += '<h3>"Cipher 2" (Philip II, f. 26r; the memorial of Savoy)</h3>' + alpha_table(c2.ALPHA)
    body += table(['Mark, as we write it', 'Mark on the page', 'Vowel'],
                  [['<span class="mono">%s</span>' % esc(k), marks2[k], '<strong>%s</strong>' % v] for k, v in c2.VOW.items()])
    body += ('<p class="note">Other signs: <span class="mono">rho</span> (a lone hook) = y; <span class="mono">v</span> '
             '= ll; <span class="mono">n</span> = pr; <span class="mono">f</span> = cr; <span class="mono">p</span> = tr; '
             '<span class="mono">R</span> = rr; <span class="mono">0+</span> = ss; a figure with a bar above '
             '(<span class="mono">~</span>) is a null; <span class="mono">16+</span> = que.</p>')
    for k, v in (('rho', 'y'), ('v', 'll'), ('n', 'pr'), ('f', 'cr'), ('p', 'tr'), ('R', 'rr')):
        check(P, c2.LET[k] == v, 'c2.py: %s = %s' % (k, v)) if c2.LET[k] != v else None
    check(P, c2.dec_group('0+') == 'ss' and c2.dec_group('16+') == 'que' and c2.dec_group('~12') == '', 'c2.py: 0+ = ss, 16+ = que, bar = null')
    body += '<h3>"Cipher 4" (the private cipher of Antonio Pérez)</h3>' + alpha_table(c4.ALPHA)
    body += table(['Mark, as we write it', 'Mark on the page', 'Vowel'],
                  [['<span class="mono">%s</span>' % esc(k), marks4[k], '<strong>%s</strong>' % v] for k, v in c4.VOW.items()])
    body += ('<p class="note">Other signs: <span class="mono">y</span> = a; <span class="mono">a</span> = u; '
             '<span class="mono">o</span> = o; a sign with a caret or an acute above (<span class="mono">^</span>) is '
             'a null; <span class="mono">xe</span> = V.m.; <span class="mono">vo</span> = Su Magestad.</p>')
    check(P, c4.LET['y'] == 'a' and c4.LET['a'] == 'u' and c4.CODES['xe'] == '[V.m.]' and c4.CODES['vo'] == '[S.M.]', 'c4.py: y = a, a = u, xe, vo')
    body += '<h2>Worked example</h2>'
    body += ('<h3>Philip II on Thomas Stukeley: f. 26r, lines 18 to 20 ("Cipher 2")</h3>'
             '<p>Each box holds one group of the first transcription pass and its value. '
             'The line under a group of boxes gives the word; the word division is ours.</p>')
    for L in ('L18', 'L19', 'L20'):
        n = L[1:]
        body += figure('img/%s/f26r_%s.jpg' % (P, L), 'Espagnol 132, f. 26r, line %s' % n,
                       'Espagnol 132, f. 26r, line %s (set in two rows here). Source: gallica.bnf.fr / BnF.' % n)
        body += cells(G[L])
        body += '<p class="note">The second pass has the same group in %d of these %d places.</p>' % agree[L]
    body += '<blockquote><p class="orig">[... que pensava levantar] %s</p><p>[... some foot and horse] %s</p></blockquote>' % (esc(reading), esc(english))
    body += ('<p class="note"><span class="diff">One letter differs.</span> In line 19 both passes have '
             '<span class="mono">15.</span>, which is "pu" by the key; the reading file writes "persona". '
             'The word "persona" runs over the end of line 19.</p>')
    check(P, passB['L19'].split()[-3] == '15.' and passA['L19'].split()[-3] == '15.', 'both passes have 15. in line 19')
    body += ('<h3>Antonio Pérez, 8 December 1578: f. 157r ("Cipher 4")</h3>'
             '<p>One cipher run inside clear Spanish: "... con la nueva orden que se ha dado de que no [cipher] sino solo '
             '[cipher]". The two passes have the same 16 groups. This page shows no image of the run; the leaf is view '
             '154 of the Gallica scan.</p>')
    body += cells(g4)
    body += '<blockquote><p class="orig">%s</p><p>[all will go better with the new order,] %s</p></blockquote>' % (esc(r4), esc(e4))
    body += '<h2>How sure</h2>'
    rows = re.findall(r'^\| (Pérez, f\. \d+|f\. 26r|ff\. 273-274) \| ([^|]+) \| ([^|]+) \|$', rd(F + '/README.md'), re.M)
    check(P, len(rows) == 5, 'README has the table of five pieces')
    body += table(['Piece', 'Two transcription passes agree', 'Of 500 shuffled keys, as good as the true key'], [list(map(esc, r)) for r in rows])
    body += ('<p><strong>Outside check.</strong> No decipherment is on any of these leaves, and a search of the printed '
             'sources found no clear text. The content of the page of Philip II is known from the other side: the '
             'Calendar of State Papers, Rome, vol. 2, no. 770 (22 March 1578) has "the paymaster, who is the bearer of '
             'the 20,000 crowns" for Stukeley, under secrecy. The King\'s own words and motive are not in print.</p>')
    body += '<h2>What is not resolved</h2>'
    body += ('<ul><li>For "Cipher 2" the passes differ in 13 to 20 % of the groups, mostly in the place of a dot. '
             'The differences were settled by sense and not by a third look at the image.</li>'
             '<li>f. 26 stops after line 27: ff. 26v to 31r are not in the Gallica scan.</li>'
             '<li>Eight code words of Pérez\'s cipher have no value, and two places on f. 87r are not resolved.</li>'
             '<li>For the Pérez letters the second pass was blind and the first was not.</li>'
             '<li>The Simancas minute of the letter of Philip II exists and was not seen.</li></ul>')
    readme = collapse(rd(F + '/README.md'))
    for p in ['the passes differ in 13 to 20 % of the groups, mostly in the place of a dot', 'f. 26 stops after line 27',
              'Eight code words of Pérez\'s cipher have no value, and two places on f. 87r are not resolved',
              'the second pass was blind and the first was not', 'the paymaster, who is the bearer of the 20,000 crowns',
              "The King's own words and motive are not in print"]:
        check(P, p in readme, 'README has: "%s"' % p[:60])
    body += '<p>Readings: %s, %s, %s. Folder: <a href="%s/tree/main/%s">%s</a>.</p>' % (
        gh(F, 'reading_f26r.md'), gh(F, 'reading_perez_f87_f157_f179.md'), gh(F, 'reading_f273_274_savoy_memorial.md'), REPO, F, F)
    return page('espagnol-132.html', title_of(F), body, F)


# ---------------------------------------------------------------- gonzaga-1590

OLD = [('dd', 'two dots above'), ('bb', 'two dots below'), ('d', 'dot above'), ('b', 'dot below'), ('=', 'two bars'),
       ('-', 'bar above'), ('_', 'bar below'), ('^', 'circumflex above'), ('v', 'caron below')]
NEW = [('^.', 'dot above'), ('^:', 'two dots above'), ('_.', 'dot below'), ('_:', 'two dots below'), ('^-', 'bar above'),
       ('_-', 'bar below'), ('=', 'two bars'), ('^^', 'circumflex above'), ('_v', 'caron below'), ('~', 'arc above')]


def mark_words(suffix, tab):
    out = []
    while suffix:
        for code, words in tab:
            if suffix.startswith(code):
                out.append(words)
                suffix = suffix[len(code):]
                break
        else:
            suffix = suffix[1:]
    return ', '.join(out) if out else 'no mark'


def gonzaga():
    P = F = 'gonzaga-1590'
    lists, names = {}, {}
    for l in rd(F + '/tables/lists_v4.tsv').splitlines():
        m = re.match(r'# (\w+) = (.+?): (.+)$', l)
        if m and m.group(1).isupper():
            names[m.group(1)] = (m.group(2), m.group(3))
        if l.startswith('#') or not l.strip():
            continue
        c = l.split('\t')
        if not c[3].startswith('from a clerk'):
            lists.setdefault((c[0], int(c[1])), []).append(c[2])
    nvalues = sum(1 for l in rd(F + '/tables/lists_v4.tsv').splitlines() if l.strip() and not l.startswith('#'))
    check(P, nvalues == 448 and len(names) == 14, 'lists_v4.tsv has 448 values in 14 lists')
    interp = {}
    for l in rd(F + '/tables/interp_v4.tsv').splitlines():
        if l.startswith('#') or not l.strip():
            continue
        c = l.split('\t')
        interp[(c[0], int(c[1]))] = c[2]
    M = ast.literal_eval(re.search(r"M=(\{.*?\})\n", rd(F + '/fr4696/dec4.py'), re.S).group(1))
    # the symbol alphabet: the table of the work log
    wl = rd(F + '/evidence/worklog.md')
    sec = wl[wl.index('### Symbol alphabet'):]
    sec = sec[:sec.index('\n\n', sec.index('| letter |'))]
    alpha, descr, order = {}, {}, []
    for letter, signs in re.findall(r'^\| ([a-z, ]+) \| (.+) \|$', sec, re.M):
        if letter.strip() == 'letter':
            continue
        for part in signs.split(';'):
            m = re.match(r'\s*`([^`]+)`\s*(.*)$', part)
            alpha[m.group(1)] = letter.split(',')[0].strip()
            descr[m.group(1)] = m.group(2).strip().strip('()')
            order.append((letter.strip(), m.group(1)))
    # transcription of f. 30r and its alignment with the clerk
    tr = dict(re.findall(r'^(R\d\d): (.+)$', rd(F + '/transcription/f30r_transcription.txt'), re.M))
    first = {}
    for L in ('R01', 'R02', 'R03'):
        syms = [t for seg in tr[L].split('|') for t in seg.split() if all(x in alpha for x in seg.split())]
        n = len(CROPS[P]['lines']['f30r_' + L]['signs'])
        check(P, len(syms) == n or L == 'R01', 'f. 30r %s: one image for each spelled sign' % L)
        for i, t in enumerate(syms[:n]):
            first.setdefault(t, sign_img(P, 'f30r_' + L, i, t))
    al = [l.split('\t') for l in rd(F + '/alignment/alignment_f30.tsv').splitlines() if l.startswith('f30r\tR01\t')]
    toks, ai, clerk_words = [], 0, []
    for seg in tr['R01'].split('|'):
        parts = seg.split()
        if all(x in alpha for x in parts):
            row = al[ai]
            ai += 1
            word = ''.join(alpha[x] for x in parts)
            check(P, row[3] == 'SPELLED' and norm(row[7]) == norm(word), 'f. 30r R01: the spelled word is %s' % row[7])
            for i, x in enumerate(parts):
                toks.append(tok(esc(x), alpha[x], None, 'letter', sign_img(P, 'f30r_R01', i, x), extra=''))
            toks[-1]['x'] = 'cagionata'
            clerk_words.append('cagionata')
            continue
        for t in parts:
            row = al[ai]
            ai += 1
            check(P, row[3] == t, 'alignment row = transcription token %s' % t) if row[3] != t else None
            if t == '<.>':
                toks.append(tok('&#9671;', 'et', None, 'letter', extra=row[8], mark='diamond with a dot'))
                clerk_words.append(row[8])
                continue
            m = re.match(r'^(\()?(\d\d)\)?(.*)$', t)
            mark = 'in brackets' if m.group(1) else mark_words(m.group(3).replace('?', ''), OLD)
            fig = int(row[4])
            ok = row[7] in lists.get((row[6], fig), [])
            check(P, ok, 'f. 30r R01: %s is list %s, figure %d in lists_v4.tsv' % (row[7], row[6], fig)) if not ok else None
            note = mark + ('; list ' + row[6] if row[5] == row[6] else '; the mark names list %s, the word is in list %s' % (row[5], row[6]))
            if row[10]:
                note += '; ' + row[10]
            kind = 'conflict' if row[9] else 'letter'
            toks.append(tok(('(%s)' % m.group(2)) if m.group(1) else m.group(2), row[7], None, kind, extra=row[8], mark=note))
            clerk_words.append(row[8])
    check(P, ai == len(al) == 27, 'f. 30r R01: 27 units in the transcription and in alignment_f30.tsv')
    clerk_lines = dict(re.findall(r'^(\d\d): (.+)$', rd(F + '/decipherments_1590/fr4702_f94-95_decipherment.txt').split('## f. 94v')[0], re.M))
    clerk_text = ' '.join(clerk_lines[k] for k in ('03', '04', '05', '06'))
    pos, ok = 0, True
    cn = norm(re.sub(r'\[struck:[^\]]*\]', ' ', clerk_text))
    for w in clerk_words:
        stem = norm(w)[:3]
        j = cn.find(stem, pos)
        if j < 0:
            ok = False
            print('  clerk word not found in order:', w)
        else:
            pos = j + len(stem)
    check(P, ok, 'f. 30r R01: the 27 words of the clerk stand in this order in fr4702_f94-95_decipherment.txt, lines 3 to 6')
    g1 = [([t], None) for t in toks]
    # regroup: the nine spelled signs are one word
    sp = [i for i, t in enumerate(toks) if t['img']]
    g1 = [([t], None) for t in toks[:sp[0]]] + [(toks[sp[0]:sp[-1] + 1], 'cagionata')] + [([t], None) for t in toks[sp[-1] + 1:]]
    ed = quoted(P, F + '/editions/edition_1590-01-21_f30.txt', 'sodisfatione che Papa mostra [havere] di persona sua, '
                'cagionata principalmente da alcune lettere di lei ritenute et aperte, oltre il sdegno aggiunto per quello che si sono')
    en1 = quoted(P, F + '/editions/edition_1590-01-21_f30.txt', 'the little satisfaction that the Pope shows with your '
                 'person. Its main cause is some letters of yours that were held and opened; added to this is the anger at what was seen of Volta')
    nclerk = sum(1 for t in toks if t['k'] == 'conflict')
    nmark = sum(1 for r in al if r[3] not in ('SPELLED', '<.>') and r[5] != r[6])

    # the letter of 24 March 1590, line 13
    t4 = dict(re.findall(r'^([LR]\d\d): (.+)$', rd(F + '/transcription/f26v-27r_transcription_v4.txt'), re.M))
    toks2, plain = [], []
    for t in re.findall(r'"[^"]*"|\S+', t4['L13']):
        if t.startswith('"'):
            toks2.append(tok('clear', t.strip('"'), None, 'clear'))
            plain.append(t.strip('"'))
            continue
        if t == '[et]':
            toks2.append(tok('&#9671;', 'et', mark='diamond with a dot'))
            plain.append('et')
            continue
        q = '?' in t
        s = t.replace('?', '').rstrip('!%')
        m = re.match(r'^(\()?(\d\d)\)?([^@]*)(?:@(\w+))?$', s)
        fig, marks = int(m.group(2)), m.group(3)
        cand = ['BR'] if m.group(1) else list(M.get(marks.replace('~', ''), []))
        if marks == '^.':
            cand = ['C', 'A']
        word = kind = L = None
        for c in cand:
            if (c, fig) in lists:
                word, L, kind = ' / '.join(sorted(lists[(c, fig)], key=len)), c, 'doubt' if q else 'letter'
                break
        if word is None:
            for c in cand:
                if (c, fig) in interp:
                    word, L, kind = '{%s}' % interp[(c, fig)], c, 'doubt'
                    break
        check(P, word is not None, '24 March, line 13: %s has a value' % t) if word is None else None
        note = ('in brackets' if m.group(1) else mark_words(marks, NEW)) + '; list ' + L
        toks2.append(tok(('(%s)' % m.group(2)) if m.group(1) else m.group(2), word, None, kind, mark=note))
        plain.append(word)
    g2 = [([t], None) for t in toks2]
    r2 = quoted(P, F + '/reading/f26v-27r_1590-03-24.md', 'Et {in somma}(?) il parere di quasi tutti *fu* che non conveniva '
                'a dignità di Papa *il far alcuna delle* cose domandate se non con debito termine, et dopo')
    e2 = quoted(P, F + '/reading/f26v-27r_1590-03-24.md', 'And {in short}(?) the opinion of almost all was that it did not '
                'befit the dignity of the Pope to do any of the things asked, except in due time, and after')
    pos, ok, rn = 0, True, norm(r2)
    for w in plain:
        js = []
        for alt in w.split(' / '):
            stem = norm(alt)[:4] if len(norm(alt)) > 4 else norm(alt)[:max(1, len(norm(alt)) - 1)]
            js.append((rn.find(stem, pos), len(stem)))
        js = [x for x in js if x[0] >= 0]
        j, stem = (min(js)[0], 'x' * min(js)[1]) if js else (-1, '')
        if j < 0:
            ok = False
            print('  word not found in order in the reading:', w)
        else:
            pos = j + len(stem)
    check(P, ok and len(toks2) == 25, '24 March, line 13: the 25 units give, in order, the words of the reading file (dictionary forms)')

    lrows = []
    for L in ('A', 'C', 'E', 'G', 'I', 'M', 'O', 'P', 'Q', 'S', 'T', 'PT', 'BR', 'N'):
        figs = sorted(f for (l, f) in lists if l == L)
        pick = [figs[i] for i in sorted(set([0, len(figs) // 3, 2 * len(figs) // 3, len(figs) - 1]))]
        lrows.append(['<span class="mono">%s</span>' % L, esc(names[L][0]), esc(names[L][1]),
                      ', '.join('<span class="mono">%d</span> %s' % (f, esc(lists[(L, f)][0])) for f in pick), str(len(figs))])
    kg = {}
    for letter, s in order:
        kg.setdefault(letter, []).append(tok(esc(s), alpha[s], '', 'letter', first.get(s, '')))
    alphagrid = cells([(v, k) for k, v in kg.items()])
    body = facts(P, F + '/README.md', [
        ('Document', 'Paris, BnF, ms. français 4698 (Gallica <code>btv1b9058291p</code>, microfilm): letters in '
         'Italian from Cardinal Scipione Gonzaga in Rome to Louis de Gonzague, Duke of Nevers, with long passages in '
         'cipher. Here: the letters of 21 January 1590 (ff. 30r-31r) and of 24 March 1590 (ff. 26v-27r).',
         ['Paris, BnF, ms. français 4698 holds letters in Italian from Cardinal Scipione Gonzaga in Rome to Louis de Gonzague, Duke of Nevers']),
        ('New', 'The reconstruction of the cipher, built without a key sheet: three layers, a word code of 448 values '
         'in 14 lists, a symbol alphabet. The link between fr. 4698 and the period decipherments in fr. 4702. A test of '
         'the rebuilt code on a second volume, fr. 4696. The letters of 24 March and 31 March 1590, which have no '
         'period decipherment, read with gaps.',
         ['Three layers; a word code of 448 values in 14 lists; a symbol alphabet. Built without a key sheet.',
          'No period decipherment was found for them']),
        ('Reproduced', 'The plain text of the letters of 21 January and 16 February 1590. It is the text of Nevers\'s '
         'own clerk of 1590 (BnF fr. 4702). We transcribed and translated it. It is not a new decipherment.',
         ["It is the text of Nevers's own clerk of 1590 (BnF fr. 4702). We transcribed and translated it. It is not a new decipherment."]),
    ])
    body += '<h2>The key</h2>'
    body += ('<p><strong>1. A word code.</strong> A two-digit figure, 10 to 99, stands for one word in its dictionary '
             'form. A mark on the figure says which list the figure belongs to. Each list is a slice of one '
             'alphabetical word list; u and v count as one letter.</p>')
    body += table(['List', 'Mark on the figure', 'Slice', 'Sample: figure and word', 'Values'], lrows)
    body += ('<p class="note">The names of the lists are ours. On the microfilm lists A and C both carry a dot above '
             'most of the time; the word decides between them. Full table: %s (448 values, each with its period gloss). '
             'Proposals with no gloss: %s.</p>') % (gh(F, 'tables/lists_v4.tsv'), gh(F, 'tables/interp_v4.tsv'))
    body += ('<p><strong>2. A symbol alphabet</strong> for words that are not in the lists. The images are cut from '
             'f. 30r, lines 1 to 3, of the letter of 21 January 1590. The names of the signs are ours.</p>')
    body += alphagrid
    body += ('<p class="note">In each box: the sign, our name for it, and its letter. A box with no image: the sign '
             'is not in these three lines. Source of the sign images: BnF, ms. français 4698, f. 30r (microfilm), gallica.bnf.fr / BnF. '
             'The table of the signs is in the work log: %s.</p>') % gh(F, 'evidence/worklog.md')
    body += ('<p><strong>3. A verb sign.</strong> An arc above a figure means: read the verb of the noun in the list. '
             'The Cardinal states this rule in clear on f. 17v.</p>')
    body += '<h2>Worked example</h2>'
    body += '<h3>21 January 1590: f. 30r, cipher line 1, with the text of the clerk of 1590</h3>'
    body += figure('img/%s/f30r_R01.jpg' % P, 'BnF fr. 4698, f. 30r, first cipher line',
                   'BnF, ms. français 4698, f. 30r, first cipher line (microfilm; set in two rows here). Source: gallica.bnf.fr / BnF.')
    body += figure('img/%s/fr4702_f94r_l3-6.jpg' % P, 'BnF fr. 4702, f. 94r, lines 3 to 6: the decipherment of 1590',
                   'The decipherment by the clerk of Nevers, 1590: BnF, ms. français 4702, f. 94r, lines 3 to 6. Source: gallica.bnf.fr / BnF.')
    body += ('<p>Each box holds one unit: the figure, its mark as we read it on the film and the list, the word of the '
             'rebuilt code (dictionary form), and the word that the clerk wrote in 1590. A red box: we keep another '
             'word than the clerk.</p>')
    body += cells(g1, rows3=True)
    body += ('<blockquote><p>Clerk, fr. 4702 f. 94r, lines 3 to 6: <span class="orig">%s</span></p>'
             '<p>Edition (the clerk\'s text with agreement made regular): <span class="orig">%s</span></p><p>%s</p></blockquote>') % (
                 esc(collapse(clerk_text)), esc(ed), esc(en1))
    body += ('<p class="note">In %d of the 26 figure units of this line the mark that we read on the film names '
             'another list than the list of the clerk\'s word. In %d unit we keep another word than the clerk: for '
             '<span class="mono">(32)</span> he wrote "così", and the list has "havere". '
             'The clerk writes the dictionary form of each word, with no agreement.</p>') % (nmark, nclerk)
    body += '<h3>24 March 1590: f. 26v, line 13. No period text is known for this letter</h3>'
    body += figure('img/%s/f26v_L13.jpg' % P, 'BnF fr. 4698, f. 26v, line 13',
                   'BnF, ms. français 4698, f. 26v, line 13 (microfilm; set in three rows here). Source: gallica.bnf.fr / BnF.')
    body += ('<p>Each box holds one unit of the transcription: the figure, its mark and the list that the mark names, '
             'and the word of the table. Italic boxes are clear words of the letter. A word in {braces} has no period '
             'gloss: it is a proposal inside its alphabetical window.</p>')
    body += cells(g2)
    body += '<blockquote><p class="orig">%s</p><p>%s</p></blockquote>' % (esc(r2), esc(e2))
    body += ('<p class="note">The code gives dictionary forms; number, gender and tense in the reading are ours. '
             'In the reading file, *..* marks clear text and (?) a doubt. The figure 10 without a mark has two values in '
             'the table, "a" and "Ambasciatore".</p>')
    body += '<h2>How sure</h2>'
    body += sure(P, F + '/README.md', [
        ['Test on fr. 4696 (letters of 1586 to 1589 with the clear text above the cipher): units whose word is in the table of 378 values', '463'],
        ['The gloss on the page is the word of the table', '452 (97.6 %)'],
        ['Word and mark both agree', '408 (88.1 %)'],
        ['The same test with a shuffled table', '2 of 572'],
        ['Blind test before fr. 4702 was found: code words with a period gloss', '344 of 371 (93 %)'],
        ['Blind test: code words chosen inside an alphabetical window', '42 of 64 (66 %), and 8 near misses in the same window'],
        ['24 March 1590: code units; with a period gloss; window proposals; not resolved', '584; 509 (87 %); 41; 17'],
    ], ['452 (97.6 %)', '408 (88.1 %)', '2 of 572', '344 of 371 (93 %)', '42 of 64 (66 %), and 8 near misses in the same window',
        '| 24 March 1590 (ff. 26v-27r) | 584 | 509 (87 %) | 41 | 17 |'])
    body += ('<p><strong>Outside check.</strong> After the reading, the statements of the two letters of March 1590 '
             'were compared with L. von Pastor, <em>History of the Popes</em>, vol. 21, pp. 343-362. Pastor confirms 19 '
             'of 22 statements of the first letter and 7 of 11 of the second. For the letter of 21 January the check is '
             'the clerk of 1590 himself.</p>')
    body += '<h2>What is not resolved</h2>'
    body += ('<ul><li>No key sheet was found. The cipher is on black-and-white microfilm: one dot against two dots '
             'often cannot be decided, and a wrong mark gives a wrong word that looks real. In about one unit in ten '
             'the mark that was read names another list.</li>'
             '<li>24 March 1590: 17 units are not resolved, and 41 words are proposals. The name of the person who left Rome is a code that is not resolved.</li>'
             '<li>Four words of the March readings were shaped by what the history says; the reading files mark them.</li></ul>')
    readme = collapse(rd(F + '/README.md'))
    for p in ['Pastor confirms 19 of 22 statements of the first letter and 7 of 11 of the second', 'in about one unit in ten the mark that was read names another list',
              'The name of the person who left Rome is a code that is not resolved', 'Four words were shaped by what the history says',
              'An arc above a figure means: read the verb of the noun in the list', 'No key sheet was found']:
        check(P, p in readme, 'README has: "%s"' % p[:60])
    body += '<p>Editions and readings: %s, %s. Folder: <a href="%s/tree/main/%s">%s</a>.</p>' % (
        gh(F, 'editions/edition_1590-01-21_f30.txt'), gh(F, 'reading/f26v-27r_1590-03-24.md'), REPO, F, F)
    return page('gonzaga-1590.html', title_of(F), body, F)


# ---------------------------------------------------------------- index

def index():
    P = 'index'
    readme = rd('README.md')
    rows = re.findall(r'^\| \[([\w-]+)\]\([\w-]+/\) \| (.+?) \| (.+?) \| (.+?) \|$', readme, re.M)
    check(P, len(rows) == 6, 'README has the table of six results')
    trs = []
    for folder, doc, new, state in rows:
        check(P, os.path.exists(os.path.join(HERE, folder + '.html')), 'page for ' + folder)
        trs.append(['<a href="%s.html"><strong>%s</strong></a>' % (folder, folder), md(doc), md(new), md(state)])
    body = ('<p>Cipher letters from European archives of 1503 to 1653, read or rebuilt in October 2026. Each page '
            'below shows one result in a form that you can check by hand: the key, a few lines of cipher, and the '
            'decoding token by token.</p>')
    body += table(['Page', 'Document', 'What is new', 'State'], trs)
    body += ('<h2>How the work was done</h2><p><strong>The work was done by a model</strong> (Claude, by Anthropic, '
             'running as Claude Code with subagents), directed by Paolo Rosson. No palaeographer or historian has '
             'checked it yet.</p><p>Most cipher lines had two transcription passes, the second one blind. Each reading '
             'has a control: a wrong-key or shuffled-key score, period glosses, or an outside source that was not used '
             'as a crib. Each page gives the numbers and the limits, and it says what is new, what is only reproduced '
             'from a period source, and what stays open.</p>')
    check(P, 'No palaeographer or historian has checked it yet' in collapse(readme), 'README: no palaeographer has checked it')
    body += ('<h2>Two earlier results</h2><ul>'
             '<li><a href="https://github.com/pangoleen/desportes-1593">pangoleen/desportes-1593</a>: two letters of the '
             'Catholic League of 22 July 1593, read for the first time (BnF fr. 3984).</li>'
             '<li><a href="https://github.com/pangoleen/senecey-1594">pangoleen/senecey-1594</a>: two League letters of '
             '1594, read with the alphabet that the royal decipherers rebuilt (BnF, Cinq Cents de Colbert 33).</li></ul>')
    body += ('<p>Four of these documents are on S. Tomokiyo\'s list of '
             '<a href="https://cryptiana.web.fc2.com/code/unsolved.htm">unsolved historical ciphers</a>: the letter to '
             'Charles I, Cocquet\'s cipher, the Dutch ciphers of 1653, and the Spanish letters of 1497 to 1504. '
             'All files are in the repository <a href="%s">pangoleen/cipher-readings</a>.</p>') % REPO
    return page('index.html', 'Readings of historical ciphers', body)


if __name__ == '__main__':
    made = [oxford(), cocquet(), es318(), dutch(), es132(), gonzaga(), index()]
    bad = [c for c in CHECKS if not c[1]]
    by = {}
    for p, ok, t in CHECKS:
        by.setdefault(p, [0, 0])[0 if ok else 1] += 1
    if '-v' in sys.argv:
        for p, ok, t in CHECKS:
            print('ok  ' if ok else 'FAIL', p, t)
    for p, (a, b) in by.items():
        print('%-14s %3d checks passed, %d failed' % (p, a, b))
    print('pages:', ', '.join(made))
    sys.exit(1 if bad else 0)
