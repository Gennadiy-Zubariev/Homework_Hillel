num = int(input("Enter a number 'Example 12345': "))

a = num % 10
num //= 10
b = num % 10
num //= 10
c = num % 10
num //= 10
d = num % 10
num //= 10
e = num

print(a,b,c,d,e,sep='')

'''Пару варіантів зі списком ;(, але можна вводити більше, 
або менше 5и символів '''


num = int(input("Enter a number 'Example 1234': "))
rev_num = ''
while num > 0:
    num, digit = divmod(num, 10)
    rev_num += str(digit)
print(int(rev_num))


num = int(input("Enter a number 'Example 12345': "))
rev_num = ''
while num > 0:
    digit = num % 10
    num //= 10
    rev_num += str(digit)
print(int(rev_num))