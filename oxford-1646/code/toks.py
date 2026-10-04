import re
def load(path):
    lines=[]
    for ln in open(path):
        ln=ln.rstrip('\n')
        if not ln or ln.startswith('#'): continue
        toks=[]
        for m in re.finditer(r'\[[^\]]*\]|\S+', ln):
            toks.append(m.group(0))
        lines.append(toks)
    return lines
