#!/usr/bin/env python3
"""make_images.py WORKDIR [PAGE ...] -- cut the images of docs/img/ from the working images, as crops.json says.

The working images (full-size downloads from Gallica, archive.org and Google Books) are not in the repository.
WORKDIR is the folder that holds them. With one or more PAGE names (the keys of crops.json) the script cuts the
images of these pages only. build.py does not need this script: it only reads crops.json and docs/img/.
Each line of crops.json: file, x0, x1 (left and right edge), y (vertical centre at x0), h (height), shear (slope of
the written line), view (part of the line that the page shows), nseg (the line image is cut in nseg pieces, set one
above the other), vy (top and bottom of the band that the line image shows), signs (left and right edge of each sign, in pixels of the line), sy (top and bottom of a sign crop).
"""
import json, os, sys
from PIL import Image, ImageOps
Image.MAX_IMAGE_PIXELS = None
HERE = os.path.dirname(os.path.abspath(__file__))
WORK = sys.argv[1] if len(sys.argv) > 1 else '.'
C = json.load(open(os.path.join(HERE, 'crops.json')))
ONLY = sys.argv[2:]

def save(im, rel, gray=True, q=60):
    p = os.path.join(HERE, 'img', rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    im = im.convert('L' if gray else 'RGB')
    if gray: im = ImageOps.autocontrast(im, cutoff=(0.5, 20))
    im.save(p, quality=q, optimize=True)
    return os.path.getsize(p)

def linecrop(d):
    im = Image.open(os.path.join(WORK, d['file']))
    w, h = d['x1'] - d['x0'], d['h']
    return im.transform((w, h), Image.AFFINE, (1, 0, d['x0'], d.get('shear', 0), 1, d['y'] - h / 2), resample=Image.BICUBIC)

total = 0
for page, P in C.items():
    if ONLY and page not in ONLY:
        continue
    short = page
    for name, d in P.get('lines', {}).items():
        line = linecrop(d)
        gray = d.get('gray', True)
        if d.get('nseg'):
            a, b = d.get('view') or [0, line.width]
            n = d['nseg']; ov = 40 if n > 1 else 0
            segw = (b - a + ov * (n - 1)) // n
            t, u = d.get('vy') or [0, line.height]
            segs = [line.crop((a + i * (segw - ov), t, a + i * (segw - ov) + segw, u)) for i in range(n)]
            out = Image.new('RGB', (segw, (u - t) * n + 6 * (n - 1)), 'white')
            for i, s in enumerate(segs): out.paste(s, (0, i * (u - t + 6)))
            if out.width > 1000: out = out.resize((1000, round(out.height * 1000 / out.width)), Image.LANCZOS)
            total += save(out, f'{short}/{name}.jpg', gray)
        y0, y1 = d.get('sy', [0, line.height])
        for i, (a, b) in enumerate(d.get('signs', [])):
            c = line.crop((max(0, a - 4), y0, min(line.width, b + 4), y1))
            sc = d.get('sscale', 0.5)
            c = c.resize((max(1, round(c.width * sc)), round(c.height * sc)), Image.LANCZOS)
            total += save(c, f'{short}/{name}_{i:02d}.jpg', gray)
    for name, d in P.get('boxes', {}).items():
        im = Image.open(os.path.join(WORK, d['file']))
        if d.get('box'): im = im.crop(tuple(d['box']))
        if im.width > d['width']: im = im.resize((d['width'], round(im.height * d['width'] / im.width)), Image.LANCZOS)
        total += save(im, f'{short}/{name}.jpg', d.get('gray', True), 55)
print('images written, total bytes:', total)
