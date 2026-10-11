# Decode a transcription with key.py. Run it in this folder.
#   python3 decode.py                    the settled transcription
#   python3 decode.py FILE_R FILE_V      two other files, for example the two files of pass A
#   python3 decode.py --passes           pass A and pass B together; (a|b) where they differ
# CAPITALS = code word. "?" after it = grade C (guess or doubtful). [xxx] = code word with no value.
# {x} = sign with no value. [..] = struck-out or unread sign. <...> = clear Spanish on the page.
import sys, difflib, collections
from lib import load, merge, FINAL, PASS_A, PASS_B
from key import KEY, CODES, WORDS
def dtok(k,b):
    if b in WORDS: return ' '+WORDS[b]+' '
    if k in('sign','group'): return KEY[b][0] if b in KEY else '{'+b+'}'
    if k=='code': return ' '+CODES[b][0].upper()+('?' if CODES[b][1]=='C' else '')+' ' if b in CODES else ' ['+b+'] '
    if k=='clear': return ' <'+b+'> '
    return ' [..] '
def clean(s): return ' '.join(s.split())
def dec(files=FINAL):
    out=collections.OrderedDict()
    for f in files:
        for lab,t in load(f): out[lab]=clean(''.join(dtok(k,b) for k,b,q in merge(t)))
    return out
def passes():
    out=collections.OrderedDict()
    for fa,fb in zip(PASS_A,PASS_B):
        A=dict(load(fa)); B=dict(load(fb))
        for lab in A:
            a=[dtok(k,b) for k,b,q in merge(A[lab])]; b=[dtok(k,b) for k,b,q in merge(B.get(lab,[]))]; s=''
            for op,i1,i2,j1,j2 in difflib.SequenceMatcher(None,a,b,autojunk=False).get_opcodes():
                s+=''.join(a[i1:i2]) if op=='equal' else ' ('+clean(''.join(a[i1:i2]))+'|'+clean(''.join(b[j1:j2]))+') '
            out[lab]=clean(s)
    return out
if __name__=='__main__':
    a=sys.argv[1:]
    d=passes() if a==['--passes'] else dec(tuple(a[:2])) if len(a)>=2 else dec()
    for lab,s in d.items(): print(lab+': '+s)
