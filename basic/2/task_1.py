num = int(input("Enter number 'Example 1234': "))

print(num % 10)
num //= 10
print(num % 10)
num //= 10
print(num % 10)
num //= 10
print(num)

'''Можна вводити числа більше, або менше 4х символів '''

num = int(input("Enter a number 'Example 1234': "))
while num > 0:
    num, digit = divmod(num, 10)
    print(digit)