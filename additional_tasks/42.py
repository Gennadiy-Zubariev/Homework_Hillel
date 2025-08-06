'''
Additional task 42
# Дана послідовність слів. Написати функцію, яка повертає послідовність
# слів, в якій у словах довжини 3 всі літери великі, а всі слова, що
# починаються на "q" або "f" виключені. Використовувати ланцюжки.
# Приклад: ["The", "quick", "brown", "fox"] -> ["THE", "brown"]
'''

# def words(lst):
#     return list(
#         map(lambda i: i.upper() if len(i)== 3 else i,
#                filter(lambda j: not j.startswith(('q', 'f')), lst)))
# a = ["The", "quick", "brown", "fox"]
# r = words(a)
# print(list(r))