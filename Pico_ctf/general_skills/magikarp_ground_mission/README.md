# Magikarp Ground Mission

### Points = 30

## Description

Do you know how to move between directories and read files in the shell? Start the container, `ssh` to it, and then `ls` once connected to begin. Login via `ssh` as `ctf-player` with the password, `6d448c9c`

```

This challenge launches an instance on demand.

Its current status is: RUNNING

Instance Time Remaining:

```

## Hints

Finding a cheatsheet for bash would be really helpful!

## Solution

Start/launch the server/instance.

connect to the server/instance through ssh.

```bash

ssh ctf-player@venus.picoctf.net -p 54682

passwd = 6d448c9c

```

After successful connection, and listing file it will spat out

```bash

ctf-player@pico-chall$ ls

1of3.flag.txt  instructions-to-2of3.txt

  cat 1of3.flag.txt

picoCTF{xxsh_

cat instructions-to-2of3.txt

Next, go to the root of all things, more succinctly `/`

cd /

ls

2of3.flag.txt             lib    run

bin                       lib64  sbin

boot                      media  srv

dev                       mnt    sys

etc                       opt    tmp

home                      proc   usr

instructions-to-3of3.txt  root   var

  cat 2of3.flag.txt

0ut_0f_\/\/4t3r_

cat instructions-to-3of3.txt

Lastly, ctf-player, go home... more succinctly `~`

cd ~/

ls

3of3.flag.txt  drop-in

cat 3of3.flag.txt

5190b070}

```

### Just join the flag parts

## Flag

```

@@ picoCTF{xxsh_0ut_0f_\/\/4t3r_5190b070} @@

```
