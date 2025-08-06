'''
Additional task 16
# Напишіть програму, яка запитує у користувача рядок і виводить на екран
# кількість голосних і приголосних літер в ній. Використовуйте функцію len()
# для підрахунку кількості літер. Виведіть результат на екран за допомогою
# команди print. Розв'язати задачу для латиниці.
#
# Приклад:
# Введіть рядок: Hello World
# Кількість голосних літер: 3
# Кількість приголосних літер: 7
'''
# import string
#
# line = input('Введіть рядок: ')
# x = line[:].lower()
# p = string.punctuation + ' '
# for i in p:
#     if i in line:
#         x = x.replace(i, '')
# g = 'aeiou'
# s = 'bcdfghjklmnpqrstvwxyz'
# gl = [i for i in x if i in g]
# sogl = [i for i in x if i in s]
# print(f'Кількість голосних літер: {len(sogl)}\nКількість приголосних літер: {len(gl)}')
