# _ => True
# __ => False
# ___ => False
# x => True
# get_value => True
# get value => False
# get!value => False
# some_super_puper_value => True
# Get_value => False
# get_Value => False
# getValue => False
# 3m => False
# m3 => True
# assert => False
# assert_exception => True

import string
import keyword

pun = string.punctuation.replace('_', ' ')
kw = keyword.kwlist

name = input('Enter variable name: ')

a = not name[0].isdigit()
b = name == name.lower()
c = not any(i in pun for i in name)
d = not name in kw
e = not (len(name) > 1 and all(i == '_' for i in name))

res = a and b and c and d and e

print(res)