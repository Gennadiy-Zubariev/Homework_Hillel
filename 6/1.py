# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

import string

a = input('Enter a: ')
b = input('Enter b: ')
let = string.ascii_letters
if let.index(a) > let.index(b):
    a, b = b, a
res = let[let.index(a):let.index(b) + 1]
print(res)
