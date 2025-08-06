'''
Additional task 44
# Реалізувати клас Counter, який представляє лічильник. Клас повинен
# підтримувати такі операції:
# - Збільшення значення лічильника на задане число (оператор +=)
# - Зменшення значення лічильника на задане число (оператор -=)
# - Перетворення лічильника на рядок (метод __str__)
# - Отримання поточного значення лічильника (метод __int__)
#
# Приклад використання:
# counter = Counter(5)
# counter += 3
# print(counter) # Результат: "Counter: 8"
# counter -= 2
# print(int(counter)) # Результат: 6
'''

# class Counter:
#     def __init__(self, count):
#         self.count = count
#
#     def __iadd__(self, other):
#         self.count += other
#         return self
#
#     def __isub__(self, other):
#         self.count -= other
#         return self
#
#     def __str__(self):
#         return f'{self.count}'
#
#     def __int__(self):
#         return  self.count
#
# counter = Counter(5)
# counter += 3
# print(counter) # Результат: "Counter: 8"
# counter -= 2
# print(int(counter)) # Результат: 6