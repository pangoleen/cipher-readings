# Builds alignment.tsv and key.tsv from thurloe_groups.txt and the model.
import re, collections
from model import table, ALPHA, RING
runs = {}
cur = None
for line in open("thurloe_groups.txt"):
    line = line.strip()
    if line.startswith("RUN"): cur = line; runs[cur] = []; continue
    if line.startswith("[") or line.startswith("#") or not line: 
        if line.startswith("["): cur = None
        continue
    if cur: runs[cur] += [int(x) for x in re.findall(r"\d+", line)]
assert [len(runs[r]) for r in ("RUN1","RUN2","RUN3")] == [70, 50, 16]

# minute letters aligned by hand to each group. Upper case words = notes.
# '-' = no letter of the minute for this group; a string of 2 letters = the group stands where the minute has 2 letters.
minute = {
 "RUN1": list("omdoor") + ["e","e","ne","n"]                      # om door eenen
       + list("expressen") + list("afgesonden") + list("de") + ["v","l","o","t","e","n"]   # minute: Vlooten
       + list("vandesenstaettedoen")
       + list("recognos") + ["-"] + list("ceren"),                # minute: recognosceeren
 "RUN2": ["DE VLOOTE VAN HAERE HOOG MOG."] + list("metde") + ["k~c"] + list("oopvaerd") + ["y~i","~e"] + list("schepen")
       + list("noor") + ["t","w","a","e","r","t","s"] + list("aenisvertrocken"),
 "RUN3": list("terv") + ["g","g","e"] + list("convoyer") + ["n"],
}
rows = []; key = collections.defaultdict(lambda: collections.Counter())
stat = collections.Counter()
for r in ("RUN1","RUN2","RUN3"):
    k = None
    assert len(minute[r]) == len(runs[r]), (r, len(minute[r]), len(runs[r]))
    for pos, (g, m) in enumerate(zip(runs[r], minute[r]), 1):
        note = ""
        if g >= 100:
            k2, n = divmod(g, 100)
            if g == 117:
                rows.append((r, pos, g, "?", "", "q (if 1|17)", m, "OPEN", "code group of the general code, or alphabet 1 letter q; the minute has 'de Vloote van haere Hoog Mog.' here"))
                stat["open"] += 1; continue
            k = k2; note = "indicator %d + first letter %d" % (k, n)
        else:
            n = g
        sp = None
        if "~" in m: m, sp = m.split("~")
        if n == 6:
            n2 = 16; note = "print has 6; read as 16 (see NOTES)"
            letter = table(k)[n2]
            st = "FIT(6=16)" if letter == m else "CONFLICT"
        else:
            letter = table(k)[n]
            st = "FIT" if letter == m else ("SPELLING" if letter == sp else "CONFLICT")
            if st == "SPELLING": note = "sent letter spells '%s' where the minute has '%s'" % (letter, m or "nothing")
        if st.startswith("FIT") or st == "SPELLING": key[(k, n if n != 6 else 16)][letter] += 1
        stat[st] += 1
        rows.append((r, pos, g, k, n, letter, m, st, note))
with open("alignment.tsv", "w") as f:
    f.write("run\tpos\tgroup\talphabet\tnumber\tmodel_letter\tminute_letter\tstatus\tnote\n")
    for row in rows: f.write("\t".join(str(x) for x in row) + "\n")
print(stat, sum(stat.values()))
# plain reading
for r in ("RUN1","RUN2","RUN3"):
    print(r, "".join((" |%s| " % x[3] if x[2] >= 100 and x[2] != 117 else "") + (x[5] if x[2] != 117 else " [117] ") for x in rows if x[0] == r))
# key table: full model with attestation
with open("key.tsv", "w") as f:
    f.write("# Boreel cipher 1653. Ring of 24 numbers: " + " ".join(map(str, RING)) + " (then back to 32).\n")
    f.write("# Alphabet k: a = k-th number of the ring; the 24 letters a b c d e f g h i k l m n o p q r s t v w x y z follow the ring.\n")
    f.write("# A 3-digit group = indicator digit k + the number of the first letter in alphabet k.\n")
    f.write("# seen = times the pair (alphabet, number) occurs in Thurloe i.435 with the minute letter equal to the model letter. 0 = predicted by the ring only.\n")
    f.write("# seen_13sept = the same count in Boreel's letter of 13 Sept 1653 (Thurloe i.454), read 'iniamesp[a]rc'; no crib, so this column is a reading, not a control.\n")
    f.write("# Alphabet 4 is not used in either letter: all its values are predicted.\n")
    f.write("alphabet\tletter\tnumber\tseen\tseen_13sept\n")
    s13 = collections.Counter(zip([1]*11, [16, 11, 16, 32, 10, 24, 21, 15, 19, 28]))
    att = single = 0
    for k in (1, 2, 3, 4, 5):
        t = table(k)
        for n, c in sorted(t.items(), key=lambda x: ALPHA.index(x[1])):
            s = key[(k, n)][c]
            if k != 4 and s: att += 1; single += (s == 1)
            f.write("%d\t%s\t%d\t%d\t%d\n" % (k, c, n, s, s13[(k, n)]))
print("attested pairs", att, "of 96 in alphabets 1,2,3,5; single occurrence:", single)
for k in (1,2,3,5):
    print(k, sorted((c, n) for (kk, n), cc in key.items() if kk == k for c in cc))
