# Nice_netcat {General Skills}

### picoctf

## Description

There is a nice program that you can talk to by using this command in a shell: $ nc mercury.picoctf.net 43239, but it doesn't speak English...

## Hints:

1. You can practice using netcat with this picoGym problem: what's a netcat?.

2. You can practice reading and writing ASCII with this picoGym problem: Let's Warm Up.

## Brief Description Of Challenge:

- When you connect to

```bash

nc mercury.picoctf.net 43239

```

You get some integers. Just copy them.

You can either use online tools to convert from integers to ASCII or use any language of your choice.

I'll be using python as always to solve it.

## Solution:

```python3

#!usr/bin/env python3

ascii_text = chr(112),chr(105),chr(99),chr(111),chr(67),chr(84),chr(70),chr(123),chr(103),chr(48),chr(48),chr(100),chr(95),chr(107),chr(49),chr(116),chr(116),chr(121),chr(33),chr(95),chr(110),chr(49),chr(99),chr(51),chr(95),chr(107),chr(49),chr(116),chr(116),chr(121),chr(33),chr(95),chr(55),chr(99),chr(48),chr(56),chr(50),chr(49),chr(102),chr(53),chr(125),chr(10)

#print(ascii_text)

flag_str_format = "".join(ascii_text)

print(flag_str_format)

```

## Flag

```diff

@@ picoCTF{g00d_k1tty!_n1c3_k1tty!_7c0821f5} @@

```
