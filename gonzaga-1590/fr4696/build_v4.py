#!/usr/bin/env python3
"""build_v4.py : read harvest_units.tsv (from harvest.py) + manual.tsv (adjudication), write
agreement.md (agreement by list), lists_v4.tsv (lists_v3 + new values with source folio), order_breaks.txt."""
import re,collections,unicodedata,sys
V3='../tables/lists_v3.tsv'
def key(w):
    w=w.lower().split('(')[0].split('/')[0].strip()
    w=''.join(c for c in unicodedata.normalize('NFD',w) if unicodedata.category(c)!='Mn')
    w=re.sub(r'[^a-z]','',w).replace('j','i').replace('v','u')
    return w
v3=collections.defaultdict(list); v3lines=[]
for l in open(V3,encoding='utf-8'):
    v3lines.append(l.rstrip('\n'))
    if l.startswith('#') or not l.strip(): continue
    p=l.rstrip('\n').split('\t'); v3[(p[0],int(p[1]))].append(p[2])
ALPHA=['A','C','E','G','I','M','O','P','Q','S','T']   # alphabetical content lists
def fits(L,f,word):
    """is word in alphabetical order with its neighbours in list L of v3?"""
    k=key(word)
    lo=[(g,v3[(L,g)][0]) for (LL,g) in v3 if LL==L and g<f]; hi=[(g,v3[(L,g)][0]) for (LL,g) in v3 if LL==L and g>f]
    a=max(lo)[1] if lo else None; b=min(hi)[1] if hi else None
    ok=(a is None or key(a)[:4]<=k[:4] or key(a)<=k) and (b is None or k[:4]<=key(b)[:4] or k<=key(b))
    return ok,a,b
man={}
try:
    for l in open('manual.tsv',encoding='utf-8'):
        if l.startswith('#') or not l.strip(): continue
        p=l.rstrip('\n').split('\t'); man[(p[0],p[1],p[2])]=p[3:]   # page,line,n -> verdict, list, word, comment
except FileNotFoundError: pass
rows=[l.rstrip('\n').split('\t') for l in open('harvest_units.tsv',encoding='utf-8')][1:]
out=[]; new=collections.defaultdict(list)
for r in rows:
    page,line,n,cipher,fig,mlist,gloss,cat,val,doubt=r[:10]
    f=int(fig); verdict=cat; L=mlist; word=gloss; com=''
    if (page,line,n) in man:
        m=man[(page,line,n)]+['','','','']; verdict=m[0]; L=m[1] or mlist; word=m[2] or gloss; com=m[3]
    elif cat in('NEW','CONFLICT'):
        cand=[]
        for LL in (mlist.split('/') if mlist!='?' else [])+ALPHA:
            if LL in('BR','PT','N'):
                if (LL,f) not in v3 and LL in mlist.split('/'): cand.append((LL,'markread'))
                continue
            if (LL,f) in v3: continue
            ok,a,b=fits(LL,f,gloss)
            if ok and a is not None and b is not None and key(a)[:1]<=key(gloss)[:1]<=key(b)[:1]: cand.append((LL,f"{a} < {gloss} < {b}"))
        com='auto: '+('; '.join(f"{x}: {y}" for x,y in cand) if cand else 'no list fits')
        if cat=='NEW' and cand: L=cand[0][0]
    out.append([page,line,n,cipher,fig,mlist,gloss,cat,verdict,L,word,val,doubt,com])
    if verdict in('NEW','NEWMARK'): new[(L,f)].append((word,page))
with open('harvest_judged.tsv','w',encoding='utf-8') as o:
    o.write('page\tline\tn\tcipher\tfigure\tmarklist\tgloss\tauto\tverdict\tlist\tword\tv3\tmarkdoubt\tcomment\n')
    for r in out: o.write('\t'.join(r)+'\n')
c=collections.Counter(r[8] for r in out); print(len(out),dict(c))
by=collections.defaultdict(collections.Counter)
for r in out: by[r[9] if r[8]!='AGREE' else r[5]][r[8]]+=1
for L in sorted(by): print(L,dict(by[L]))
print('NEW values:',len(new))
for k in sorted(new): print(k, collections.Counter(w for w,p in new[k]).most_common(3), sorted(set(p for w,p in new[k])))

# ---------- lists_v4.tsv, agreement.md, order breaks ----------
LISTS=['A','C','E','G','I','M','O','P','Q','S','T','PT','BR','N']
conf=collections.defaultdict(set)   # (L,f) of v3 confirmed by fr.4696 -> pages
for r in out:
    page,line,n,cipher,fig,mlist,gloss,cat,verdict,L,word=r[:11]
    f=int(fig)
    if verdict in('AGREE','FORM','MARK'):
        cands=[x for x in ([L] if L in LISTS else mlist.split('/')) if (x,f) in v3]
        if verdict=='AGREE' and cat=='AGREE':
            cands=[x for x in mlist.split('/') if (x,f) in v3] if L not in LISTS else cands
        for x in cands[:1]: conf[(x,f)].add(page)
# v3 list of the AGREE rows: harvest.py wrote the list in column marklist when it agreed
v4=[]
for l in v3lines:
    if l.startswith('#') or not l.strip(): v4.append(l); continue
    p=l.split('\t'); k=(p[0],int(p[1]))
    if k in conf:
        p[3]+='; confirmed by fr.4696 gloss'; p[4]+=' | fr.4696 '+', '.join(sorted(conf[k]))
    v4.append('\t'.join(p))
hdr=['# Word code of Scipione Gonzaga and Nevers, version 4 (4 Oct 2026) = lists_v3 + values from the glosses of BnF fr. 4696.',
     '# New rows have status "new from fr.4696 gloss" and the folio. NEWMARK = the mark that the transcriber read names another list; the list is set by the alphabet.',
     '# Names: in fr. 4696 many names are plain figures followed by a point (no bar above).']
body=[x for x in v4]
newrows=[]
for (L,f),ws in sorted(new.items()):
    w=collections.Counter(x for x,p in ws).most_common(1)[0][0]
    pages=', '.join(sorted(set(p for x,p in ws)))
    kind='NEWMARK' if any(r[8]=='NEWMARK' and r[9]==L and int(r[4])==f for r in out) and not any(r[8]=='NEW' and r[9]==L and int(r[4])==f for r in out) else 'NEW'
    newrows.append(f"{L}\t{f}\t{w}\tnew from fr.4696 gloss ({len(ws)}x{', mark not as read' if kind=='NEWMARK' else ''})\tfr.4696 {pages}")
# insert new rows into their list blocks, sorted by figure
final=[]; cur=None; buf=[]; done=set()
def flush():
    global buf
    if cur is None: final.extend(buf); buf=[]; return
    add=[x for x in newrows if x.split('\t')[0]==cur and x not in done]; done.update(add)
    rows_=[x for x in buf if not x.startswith('#')]+add
    rows_.sort(key=lambda x:int(x.split('\t')[1]))
    final.extend([x for x in buf if x.startswith('#')]); final.extend(rows_); buf=[]
for l in body:
    if l.startswith('#') or not l.strip():
        m=re.match(r'# (A|C|E|G|I|M|O|P|Q|S|T|PT|BR|N) = ',l)
        if m: flush(); cur=m.group(1)
        buf.append(l); continue
    L=l.split('\t')[0]
    if L!=cur: flush(); cur=L
    buf.append(l)
flush()
open('lists_v4.tsv','w',encoding='utf-8').write('\n'.join(hdr+final)+'\n')
nval=sum(1 for l in final if l.strip() and not l.startswith('#'))
print('lists_v4 values:',nval,'(v3:',sum(1 for l in v3lines if l.strip() and not l.startswith("#")),') new:',len(newrows),'v3 values confirmed:',len(conf))
# order breaks in the alphabetical lists of v4
breaks=[]
t4=collections.defaultdict(list)
for l in final:
    if l.startswith('#') or not l.strip(): continue
    p=l.split('\t'); t4[p[0]].append((int(p[1]),p[2],'new' if 'fr.4696 gloss (' in p[3] else 'v3'))
for L in ALPHA+['PT']:
    seq=sorted(t4[L]); 
    for (f1,w1,s1),(f2,w2,s2) in zip(seq,seq[1:]):
        if f1==f2: continue
        if key(w1)>key(w2): breaks.append(f"{L}\t{f1} {w1} ({s1})\t{f2} {w2} ({s2})")
open('order_breaks.txt','w',encoding='utf-8').write('# pairs of neighbours in lists_v4 that are not in alphabetical order (u = v, accents dropped)\n'+'\n'.join(breaks)+'\n')
print('order breaks:',len(breaks)); print('\n'.join(b for b in breaks if 'new' in b))
# agreement table
tested=[r for r in out if r[8] in('AGREE','FORM','MARK','NEAR','CONFLICT')]
ag=collections.defaultdict(collections.Counter)
for r in tested:
    L=r[9] if r[9] in LISTS else (r[5] if r[5] in LISTS else 'A/C')
    ag[L][r[8]]+=1
lines=['| List | units tested | agree (word and mark) | same word, other form | word agrees, mark read names another list | near miss | conflict |','|---|---|---|---|---|---|---|']
T=collections.Counter()
for L in LISTS+['A/C']:
    c=ag.get(L)
    if not c: continue
    n=sum(c.values()); T.update(c)
    lines.append(f"| {L} | {n} | {c['AGREE']} | {c['FORM']} | {c['MARK']} | {c['NEAR']} | {c['CONFLICT']} |")
n=sum(T.values())
lines.append(f"| all | {n} | {T['AGREE']} | {T['FORM']} | {T['MARK']} | {T['NEAR']} | {T['CONFLICT']} |")
open('agreement_table.md','w',encoding='utf-8').write('\n'.join(lines)+'\n')
print('\n'.join(lines))
if n: print(f"word agrees: {(T['AGREE']+T['FORM']+T['MARK'])}/{n} = {100*(T['AGREE']+T['FORM']+T['MARK'])/n:.1f}% ; word and mark: {(T['AGREE']+T['FORM'])}/{n} = {100*(T['AGREE']+T['FORM'])/n:.1f}%")
