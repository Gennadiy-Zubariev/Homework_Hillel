'''
Additional task 2 Давайте створимо простий калькулятор. Напишіть програму, яка запитує у
користувача два цілих числа і виконує такі дії:
- обчислює суму та виводить результат.
- обчислює різницю і виводить результат (перше число мінус друге число).
- обчислює добуток та виводить результат.
- обчислює ділення (результат поділу першого числа на друге) та виводить
  результат.
- обчислює залишок від поділу першого числа на друге та виводить результат.
- Зводить перше число у ступінь другого числа та виводить результат.

Приклад:
Введіть перше число: 5
Введіть друге число: 2

Сума: 7
Різниця: 3
Добуток: 10
Ділення: 2.5
Залишок від ділення: 2
Перше число у ступені другого числа: 25
'''

def inp_digit(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print('Ви ввели не число, спробуйте ще.')

def operations(a, b):
    results = {
        'Сума': a + b,
        'Різниця': a - b,
        'Добуток': a * b,
        'Перше число у ступені другого числа': a ** b,
    }
    if b != 0:
        results['Ділення'] = round(a / b, 2)
        results['Залишок від ділення'] = a % b
    else:
        results['Ділення'] = 'На нуль ділити не можна'
        results['Залишок від ділення'] = 'На нуль ділити не можна'

    return results

a = inp_digit('Enter a:')
b = inp_digit('Enter b:')

res = operations(a, b)
for k, v in res.items():
    print(f'{k} = {v}')

#########OR ###########
# def inp_digit(prompt):
#     while True:
#         try:
#             return int(input(prompt))
#         except ValueError:
#             print('Ви ввели не число, спробуйте ще.')
#
# def operations(a, b):
#     results = {
#         '+': a + b,
#         '-': a - b,
#         '*': a * b,
#         '**': a ** b,
#     }
#     if b != 0:
#         results['/'] = round(a / b, 2)
#         results['%'] = a % b
#     else:
#         results['/'] = 'На нуль ділити не можна'
#         results['%'] = 'На нуль ділити не можна'
#
#     return results
#
# a = inp_digit('Enter a:')
# b = inp_digit('Enter b:')
# oper = input('Enter operant "+,-,*,/,**,%"')
#
# res = operations(a, b)
# print(f'{a} {oper} {b} = {res[oper]}')