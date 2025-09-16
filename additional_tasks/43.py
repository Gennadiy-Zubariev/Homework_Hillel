'''
Additional task 43
# Створіть клас BankAccount для надання банківського рахунку. Клас повинен
# мати атрибути account_number (номер рахунку) та balance (баланс), а також
# методи deposit() для внесення грошей на рахунок і withdraw() для зняття
# грошей з рахунку. Потім створіть екземпляр класу BankAccount, внесіть на
# рахунок деяку суму і зніміть частину грошей. Виведіть баланс, що залишився.
# Не забудьте передбачити варіант, при якому при знятті баланс може стати
# меншим за нуль. У цьому випадку йти в мінус не будемо, замість чого
# повертатимемо повідомлення "Недостатньо коштів на рахунку".
'''

# class BankAccount:
#     def __init__(self, account_number, balance=0):
#         self.account_number = account_number
#         self.balance = balance
#
#     def deposit(self, dep):
#         self.balance += dep
#
#     def withdraw(self, wit):
#         if self.balance > wit:
#             self.balance -= wit
#         else:
#             print("Недостатньо коштів на рахунку")
#
#     def __str__(self):
#         return f'account number-{self.account_number}\nbalance-{self.balance}'
#
# a = BankAccount('0000_0000_0000_0001', 999)
# a.deposit(1300)
# a.withdraw(5000)