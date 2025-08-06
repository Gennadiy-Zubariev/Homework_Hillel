'''
Additional task 8 # Напишіть програму, яка запитує користувача три числа і виводить їх у порядку
# зростання, розділені комою. Використовуйте умовні оператори та вкладені
# умови для вирішення завдання. Передбачається, що це три числа різні.

# Приклад:
# Введіть перше число: 5
# Введіть друге число: 2
# Введіть третє число: 7

# Числа в порядку зростання: 2, 5, 7
'''

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a > b:
    if b > c:
        print(c, b, a, 1)
    elif c > a:
        print(b, a, c, 2)
    elif c > b and a > c:
        print(b, c, a, 3)
else:
    if a > c:
        print(c, a, b, 4)
    elif c > b:
        print(a, b, c, 5)
    elif c > a and b > c:
        print(a, b, c, 6)

##########OR##############
a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))

if a <= b and a <= c:
    if b <= c:
        print(a, b, c)
    else:
        print(a, c, b)
elif b <= a and b <= c:
    if a <= c:
        print(b, a, c)
    else:
        print(b, c, a)
else:
    if a <= b:
        print(c, a, b)
    else:
        print(c, b, a)

##########OR##############
first_number = int(input('Введіть перше число: '))
second_number = int(input('Введіть друге число: '))
third_number = int(input('Введіть третє число: '))

if first_number > second_number:
    first_number, second_number = second_number, first_number
if second_number > third_number:
    second_number, third_number = third_number, second_number
if first_number > second_number:
    first_number, second_number = second_number, first_number

print(f'Числа в порядку зростання: {first_number}, {second_number}, {third_number}')
