# Transformation {pico_ctf}

### Reverse Engeneering

## Discription:

I wonder what this really is... enc ''.join([chr((ord(flag[i]) << 8) + ord(flag[i + 1])) for i in range(0, len(flag), 2)])

## Hint:

You may find some decoders online.

```diff

+ This task(challenge) has a downloadable file called enc which contains a rather encrypted text with 16 bits encryption.

```

###You can do it (decrypt it) online or with any language of your choice. I'll be doing it in python3.

## Code/Solution:

```python3

#!/usr/bin/env python3

flag = "灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰㑣〷㘰摽"

sol = flag.encode("utf-16-be")

print(sol)

```

## Flag:

picoCTF{16_bits_inst34d_of_8_04c0760d}
