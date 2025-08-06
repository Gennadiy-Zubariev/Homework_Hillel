'''
Additional task 45
# Створити програму-калькулятор у вигляді класу та кілька методів, як мінімум
# додавання, віднімання, ділення, множення, зведення в ступінь та вилучення
# квадратного кореня. Обернути кожен метод у блок try/except і зробити обробку
# кількох винятків, як мінімум ділення на 0. Створити свій виняток, наприклад,
# зведення в негативний ступінь.
'''

class NegativePower(Exception):
    pass


# class Calc:
#
#     # def __init__(self, a, b):
#     #     self.a = a
#     #     self.b = b
#
#     def add(self, a, b):
#         try:
#             return a + b
#         except TypeError as err:
#             print(err)
#
#     def sub(self, a, b):
#         try:
#             return a - b
#         except TypeError as err:
#             print(err)
#
#     def mult(self, a, b):
#         try:
#             return a * b
#         except TypeError as err:
#             print(err)
#
#     def div(self, a, b):
#         try:
#             return a / b
#         except ZeroDivisionError as err:
#             print(err)
#         except TypeError as err:
#             print(err)
#
#     def pow(self, a, pow=1):
#         try:
#             if pow < 0:
#                 raise NegativePower("Negative exponents are not allowed")
#             return a ** pow()
#         except NegativePower as err:
#             print(err)
#         except TypeError as err:
#             print(err)
#
#     def sqrt(self,a):
#         try:
#             if a < 0:
#                 raise ValueError("Cannot take square root of a negative number")
#             return x ** 0.5
#         except ValueError as err:
#             print(err)
#         except TypeError as err:
#             print(err)
#
#
# calc = Calc()
# print(calc.add(5, 3))         # 8
# print(calc.div(10, 0))     # Error: Cannot divide by zero
# print(calc.pow(2, -3))      # Error: Negative exponents are not allowed
# print(calc.sqrt(-4))