# let's warm up

## Description

If I told you a word started with 0x70 in hexadecimal, what would it start with in ASCII?

## Hint

`Submit your answer in our flag format. For example, if your answer was 'hello', you would submit 'picoCTF{hello}' as the flag.`

## Solution

you can do it with python3 

```bash

python3

>>> bytes.fromhex("70")

b'p'

```

## Flag

```diff

@@ picoCTF{p} @@

```
