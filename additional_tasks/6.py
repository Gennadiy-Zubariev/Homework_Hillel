'''
Additional task 6 # Напишіть програму, яка запитує у користувача два логічні значення (True або
# False) і виводить результати наступних логічних операцій:

# Логічне І (and) між двома значеннями.
# Логічне АБО (or) між двома значеннями.
# Логічне НЕ (not) кожного значення.
# Результат порівняння двох значень на рівність.
# Результат порівняння двох значень на нерівність.

# Результати мають бути виведені за допомогою print. Введену строку "True"
# або "False" треба привести до булевого типу "True" або "False" і потім вже
# над булевими значеннями проводити операції.
'''

var_1 = input('Enter True or False: ')
var_2 = input('Enter True or False: ')
a = False if var_1.lower() == 'false' else True
b = False if var_2.lower() == 'false' else True

print(f'{a} and {b} = {a and b}')
print(f'{a} or {b} = {a or b}')
print(f'not {a} = {not a}')
print(f'not {b} = {not b}')
print(f'{a} == {b} = {a == b}')
print(f'{a} != {b} = {a != b}')