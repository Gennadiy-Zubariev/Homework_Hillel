# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

x = input('Enter a-b: ')
res = x.split('-')

if len(res) == 2 and len(res[0]) == len(res[1]) == 1:
    a = res[0]
    b = res[1]
else:
    print('Wrong parameters!')

let = string.ascii_letters

if let.index(a) > let.index(b):
    a, b = b, a
res = let[let.index(a):let.index(b) + 1]

print(res)
