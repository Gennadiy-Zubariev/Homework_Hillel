'''
Additional task 46
# Даний список, що складається з даних різного типу.
# Повернути новий список, де за допомогою функції map() кожен елемент типу
# int початкового списку приведений до типу str, елементи решти всіх типів
# передаються в новий список без зміни їх типу.
# У якості вхідної функції в map використовувати lambda-функцію.
'''

#
# mixed_list = [
#     42,                      # int
#     3.14,                    # float
#     "Hello, world!",         # str
#     True,                    # bool
#     None,                    # NoneType
#     [1, 2, 3],               # list
#     {"name": "Alice"},       # dict
#     (4, 5),                  # tuple
#     {1, 2, 3},               # set
#     lambda x: x + 1          # function
# ]
#
# new1 = []
# new2 = []
# res = list(map(lambda i: new2.append(str(i)) if isinstance(i, int)
#             and not isinstance(i, bool) else new1.append(i), mixed_list))
# print(new1)
# print(new2)