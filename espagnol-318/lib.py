import re, collections
SIGNS=set("7 6 3 3o 5 5o G 8 9 III N a ao p P k x X + al dl tb tbo ot o- = :. ss ff F QQ Q q & Z8 R B ß C. M V Z E A l H qo tz . / , /. ?? 4f 9t if ßo w gt 5bar".split())
ALIAS={'Z8':'&','4f':'ff','mals':'malz','gt':'9t','ßo':'qo','w':'N','K':'k'}
def load(path):
    lines=[]
    for ln in open(path,encoding='utf-8'):
        ln=ln.strip()
        if not ln or not re.match(r'^L\d+:',ln): continue
        lab,rest=ln.split(':',1)
        toks=[]
        # clear text in <...>
        parts=re.split(r'(<[^>]*>)',rest)
        for p in parts:
            if p.startswith('<'):
                toks.append(('clear',p[1:-1]))
            else:
                for t in p.split():
                    q=t.endswith('?') and t!='??'
                    base=t[:-1] if q else t
                    base=ALIAS.get(base,base)
                    kind='sign' if base in SIGNS else 'code'
                    toks.append((kind,base,q))
        lines.append((lab,toks))
    return lines
