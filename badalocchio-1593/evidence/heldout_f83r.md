# A held-out text: the cipher passage of BnF fr. 4700 f. 83r

Source: Paris, BnF, ms. français 4700, f. 83r (Gallica `btv1b90582908`, view 95, right page). Image:
`../images/f83r_cipher.jpg`. Data: [`../heldout_f83r.txt`](../heldout_f83r.txt). `python3 decode.py` decodes it.

## What it is

- f. 83r is a clear letter of Badalocchio to the Duke: "In Roma: il di VI di Febraro: MDXCIII", signed.
- One passage of it is in cipher: the end of one line and the start of the next.
- We found it on 11 October 2026, in a survey of the views 86 to 95 on small images.
- It is the only other cipher text of Badalocchio that we saw in ff. 73-83. We did not see views 96 to 100
  (ff. 83v-88).
- **This text had no part in the making of the key.**

## The clear text around it (seen on the image; one reading)

"... Ho di poi hieri inteso che Navara con la sorella si catechizano sotto quattro Vescovi, che così Dio piaccia
che sia, et ad honore di s. divina M.tà: **[cipher]**. ne fa male per le sue pretensioni: Le bascio humiliss.te le
mani ..."

Earlier in the same letter: "... dice haver caro il Vescovado di Pavia per esser passato di Barbaria in
Lombardia ...".

## The figures (one pass)

`2 2 9 1 9 3 9 7 4 3 5 7 4 6 1 8 4 [7 with a long flag] 1 5 2 9 5 3 7 5 4 5 2 3 9 1 9 3 4 3 6 0` / next line
`9 7 4 8 1 5 2 9 4 3 7 4 5 9 6 3`

53 figures and one sign.

## The key of f. 80r applied, unchanged

The cut rule is the rule as it stood before we saw this text.

`2 2 91 93 97 43 5 7 46 184 [sign] 152 95 3 7 5 45 2 3 91 93 43 6 0 | 97 48 152 94 3 7 45 96 3`

= `· · ENTE m s c i u e IL [sign] DI p a u i a · a ENTE m c o · | s e DI n a u a r a`

- 33 groups. 32 have a value (97 %). 4 of them are nulls. The sign has no value.
- **Words that read: "il [..] di Pavia" and "co·se di Navara".** They are 18 of the 29 groups that are not nulls
  (62 %).
- Both names stand in the clear text of the same letter: the see of Pavia, and Navarre.
- The reader predicted "43 6" (c o) at the cut end of the first line, from "97 48" (s e) on the next line, before
  it had the last tile. The tile shows 4 3 6 0.
- The word-table values 184 (il) and 152 (di, two times) read in a text that was not used for them.
- **What does not read:** "ENTE m" in two places (`9 1 9 3`), and "s c i u e".

A correction: the working notes of 11 October gave "31 groups, 30 with a value, 18 of 27 (67 %)". The row of
groups above has 33 groups, and `decode.py` counts 33. The numbers here are the counts of the row.

## What the test taught (this part is not blind)

- `9 1 9 3` reads if the 9 goes with the null before it: `2 29 193 ...` and `2 39 193 43 6 0 97 48`. This gives
  "[29] le sciue il [..] di Pavia [39] le cose di Navara". 193 = le is the value of f. 80r.
- So the figures 2 and 3 can head a pair with 9: **29 and 39 are groups.**
- The same cut repairs two places of f. 80r:
  - line 16: `2 29 97 98 3 96 46 83 0 <pi> 83 6 94 49` = "[29] starebbono a segno" (before: "qutarebbono");
  - line 11: `39 93 5 48 193 98 48 96 46` = "[39] mie lettere" (before: "a q a i e lettere").
- The value 29 = "non" is probable: "non starebbono a segno" on f. 80r, and "Non le sc[r]ive ..." here.
- 39 is open. It is a short word before "mie lettere" and "le cose": in, con, per or ne.
- "s c i u e" stays open ("scrive" without r?).
- So the passage is not fully read: "[Non?] le sc[r]ive(?) il [Vescovo?] di Pavia [39] le cose di Navara. ne fa
  male per le sue pretensioni."

## Limits of this test

- **The passage is short:** 33 groups.
- **It is not fully blind.** The first application was blind. Then the passage taught two cuts (29 and 39), and we
  used them on f. 80r. The value "non" for 29 rests on one place of f. 80r and on this passage together.
- The figures have one pass only.
- By the first cut, 11 of the 29 groups that are not nulls did not read: ten letter groups and the sign.
