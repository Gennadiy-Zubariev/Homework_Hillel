'''
Additional task 33
# Напишіть функцію is_subset, яка приймає дві множини set1 і set2 і
# перевіряє, чи є set1 підмножиною set2. Функція має повертати
# True, якщо всі елементи set1 містяться в set2, і False в іншому
# Випадок. Функція має бути реалізована без використання вбудованих методів
# issubset або <=.
#
# Приклад множин
# {2, 2, 3}
# {2, 2, 3, 4, 5}
#
# Приклад висновку:
# True
'''

# def is_subset(set1, set2):
#     upd_set = set2.union(set1)
#     if len(upd_set) == len(set2):
#         return True
#     return False
#
# print(is_subset({2, 2, 3}, {2, 2, 3, 4, 5}))