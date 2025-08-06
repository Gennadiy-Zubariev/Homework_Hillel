'''
Additional task 21
# Існує функція coffee(), яка варить каву і якщо її викликати, то вона друкує
# "кава".
# Написати декоратор та декорувати цю функцію так, щоб можна було варити каву
# з цукром, молоком або тим та іншим водночас. Також можна заварити подвійну
# каву, або каву з подвійним молоком, чи подвійним цукром. Якщо виклакити
# задекоровану функцію без аргументів, то вона зварить звичайну каву, так
# наче функція не декорована. При чому ніяких змін до самої функції coffee()
# вносити не можна.
'''

# def decorator(func):
#     def wrapper(*args, **kwargs):
#         supplements = []
#         if kwargs.get('milk') == 1:
#             supplements.append('з молоком')
#         if kwargs.get('milk') == 2:
#             supplements.append('з подвійним молоком')
#         if kwargs.get('sugar') == 1:
#             if kwargs.get('milk', 0):
#                 supplements.append('та цукром')
#             else:
#                 supplements.append('з цукром')
#         if kwargs.get('sugar') == 2:
#             if kwargs.get('milk', 0):
#                 supplements.append('та подвійним цукром')
#             else:
#                 supplements.append('з подвійним цукром')
#         if kwargs.get('double'):
#                 supplements.append('подвійна')
#
#         if supplements:
#             print(f"{' '.join(supplements)}", end=' ')
#         func()
#     return wrapper
# @decorator
# def coffe():
#     print('кава')
#
# a = coffe(milk=2, sugar=1, double=True)