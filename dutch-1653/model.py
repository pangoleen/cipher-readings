# Boreel cipher of 1653 (Thurloe i.435): 24-cell number ring, alphabet shifted by an indicator digit.
ALPHA = "abcdefghiklmnopqrstvwxyz"                      # 24 letters: i=j, v=u
RING  = list(range(32, 8, -2)) + list(range(11, 34, 2))  # 32,30,...,10,11,13,...,33
assert len(RING) == 24 and len(set(RING)) == 24
def table(k):
    """alphabet k: number -> letter"""
    return {RING[(i + k - 1) % 24]: ALPHA[i] for i in range(24)}
def dec(k, nums):
    t = table(k)
    return "".join(t.get(n, "[%d]" % n) for n in nums)
def enc(k, text):
    inv = {v: n for n, v in table(k).items()}
    return [inv[c] for c in text]
if __name__ == "__main__":
    for k in range(1, 10):
        t = table(k)
        print(k, " ".join("%s=%d" % (c, n) for n, c in sorted(t.items(), key=lambda x: ALPHA.index(x[1]))))
