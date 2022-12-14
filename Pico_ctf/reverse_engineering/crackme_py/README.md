# Crackme-py

### Points = 30

## Description

[crackme.py](https://mercury.picoctf.net/static/fd0e358d4b82695c220c0d6013c11484/crackme.py)

## Hints

"(None)"

## Solution

`If we examine(view) the source code of the python script,`

`The very fourth line gets the red flag.`

```diff

bezos_cc_secret = "A:4@r%uL`M-^M0c0AbcM-MFE055a4ce`eN"

```

`If we see the 12th line of the code, we can say that its "rot47" `

You can decode it online.

## Flag

```diff

+ picoCTF{1|\/|_4_p34|\|ut_dd2c4616}

```
