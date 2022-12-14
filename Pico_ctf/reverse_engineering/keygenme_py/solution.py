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
# Use the hashlib and add the result to potential_dynamic_key
  dynamic_key += hashlib.sha256(username_trial).hexdigest()[p]
key = key_part_static1_trial+dynamic_key+key_part_static2_trial
print(key)