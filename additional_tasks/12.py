'''
Additional task 12
# Напишіть програму, яка приймає число з плаваючою точкою і округляє його до
# цілого числа відповідно до правил шкільної математики. Використовувати
# модуль math та методи з нього не можна. Врахувати, що програма має коректно
# працювати з негативними числами.
#
# Приклад:
# Введіть дійсне число: -3.14
# Округлене значення: -3
# Введіть дійсне число: 4.5
# Округлене значення: 5
# Введіть дійсне число: 5.5
# Округлене значення: 6
'''

var = input("Enter var: ")
lst = var.split('.')
ost = float(f'0.{lst[-1]}')
if ost >= 0.5:
    print(f'{int(lst[0]) + 1}')
else:
    print(f'{int(lst[0])}')
##OR##
var = float(input("Enter var: "))
cile = int(var)
ostacha = var - cile
print(ostacha)
if ostacha >= 0.5:
    print(f'{cile + 1}')
else:
    print(f'{cile}')
##OR##
value = float(input('Введіть дійсне число:'))
if value > 0:
    new_value = int(value + 0.5)
else:
    new_value = int(value - 0.5)
print('Округлене значення:', new_value)