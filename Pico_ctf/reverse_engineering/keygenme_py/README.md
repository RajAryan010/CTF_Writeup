# Keygenme-py

### Points = 30

## Description

[keygenme-trial.py](https://mercury.picoctf.net/static/a6d9cac3bfa4935ceb50c145d3ff5586/keygenme-trial.py)

## Hints 

(None)

## Overview 

We can see parts of the flag except the dynamic part which we have to generate.

```python3

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"

key_part_dynamic1_trial = "xxxxxxxx"

key_part_static2_trial = "}"

key_full_template_trial = key_part_static1_trial + key_part_dynamic1_trial + key_part_static2_trial

```

While looking at the code, we can find some pattern/position of dynamic key.

```python3

if key[i] != hashlib.sha256(username_trial).hexdigest()[4]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[5]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[3]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[6]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[2]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[7]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[1]:

            return False

        else:

            i += 1

        if key[i] != hashlib.sha256(username_trial).hexdigest()[8]:

            return False

```

From here we got the position.

```diff

! dynamic_key_position = [4,5,3,6,2,7,1,8]

```

## Solution Code

```python3

#!/usr/bin/env python3

import hashlib







username_trial = b"PRITCHARD"

key_part_static1_trial = "picoCTF{1n_7h3_|<3y_of_"

key_part_dynamic1_trial = "xxxxxxxx"

key_part_static2_trial = "}"

dynamic_key = ""

# positions found from the code keygenme on if statements.

dynamic_key_position = [4,5,3,6,2,7,1,8]

for p in dynamic_key_position:

# Uses the hashlib and add the result to dynamic_key

  dynamic_key += hashlib.sha256(username_trial).hexdigest()[p]

key = key_part_static1_trial+dynamic_key+key_part_static2_trial

print(key)

```

## Flag

```diff

! picoCTF{1n_7h3_|<3y_of_54ef6292}

```

