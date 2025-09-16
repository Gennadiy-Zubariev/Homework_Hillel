'''
Additional task 18
# Напишіть програму, яка запитує у користувача рядок і визначає, чи містить
# він тільки унікальні символи. Якщо всі символи в рядку унікальні, виведіть
# відповідне повідомлення на екран. В іншому випадку виведіть повідомлення
# про те, які символи повторюються. Не використовуйте множини для
# перевірки унікальності символів.
#
# Приклад:
# Введіть рядок: Python
# Усі символи у рядку унікальні.
# Введіть рядок: Hello Konal
# Символи 'l' і 'o' повторюються.
'''
# from collections import defaultdict
#
# stroka = input('Enter string: ').lower()
# d_dict = defaultdict(lambda: 0)
#
# for i in stroka:
#     d_dict[i] += 1
# uniq = {k:v for k, v in d_dict.items() if v == 1}
# not_uniq = {k:v for k, v in d_dict.items() if v > 1}
#
# if len(d_dict) == len(uniq):
#     print('String is unique')
# else:
#     print('String not unique!')
#     for k, v in not_uniq.items():
#         print(f'{k} letter occurs {v} times')