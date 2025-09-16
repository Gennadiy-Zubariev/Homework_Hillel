# 999 -> 2 # Ось чому - 999 розбиваємо на цифри і перемножуємо 9 * 9 * 9 = 729,
# Потім 7 * 2 * 9 = 126, потім 1 * 2 * 6 = 12 і в результаті 1 * 2 = 2
# 1000 -> 0
# 423 -> 8
# 33 -> 9
# 25 -> 0
# 1 -> 1

num = input('Enter number: ')

l = len(num)
s = 1
while True:
    for i in num:
        n = int(i)
        n *= s
        s = n

    if len(str(s)) <= 1:
        print(s)
        break

    num = str(s)
    s = 1
