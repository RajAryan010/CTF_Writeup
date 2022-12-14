# Warmed Up

### Points 50

## Description

> What is 0x3D (base 16) in decimal (base 10)?

## Hints

Submit your answer in our flag format. For example, if your answer was '22', you would submit 'picoCTF{22}' as the flag.

## Overview (Brief description of challenge)

0X3D is a hexadecimal (hex) number. We can tell it is a hex number because it starts with 0X.

The hexadecimal number system has 16 symbols (base 16) instead of the decimal system 

which has 10 numbers (base 10). The hex symbols are 0 1 2 3 4 5 6 7 8 9 A B C D E F 

where A=10, B=11, C=12. D=13, E=14, and F=15.

Step 1) Multiply the last digit by 1, Multiply the second to last digit by 16, Multiply the third to the last digit by 16 x 16, 

Multiply the fourth to the last digit by 16 x 16 x 16,

and so on until all the digits are used.

## Solution

```

D x 1 = 13

3 x 16 = 48

13 + 48 = 61

```

## Flag

```diff

@@ picoCTF{61} @@

```
