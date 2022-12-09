# Information (Forensics)

## Description:

Files can always be changed in a secret way. Can you find the flag? cat.jpg

## Hints:

1. Make sure to submit the flag as picoCTF{XXXXX}.

2. Look at the details of the file.

```diff

+ This challenge contain a jpg file named cat.

! You can use either exiftool or simply strings to find its data.

```

## Solution:

I'll be using strings command to examine the data of the jpg file.

```bash

strings cat.jpg | less

```

And it'll give the following output

![alt text](https://github.com/RajAryan010/CTF_Writeup/raw/main/Pico_ctf/forensic/information/strings_output.jpg)

You can see some base64 encoded text in the above picture.

```bash

echo "cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9" | base64 -d

```

## Flag:

```diff

@@ picoCTF{the_m3tadata_1s_modified} @@

```
