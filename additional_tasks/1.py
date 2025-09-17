'''
Additional task 2 Написати програму, яка просить ввести 4 числа – кількість днів, годин,
хвилин і секунд. Програма виводить цей час у секундах.
'''

day = int(input('Enter days: '))
hour = int(input('Enter hours: '))
min = int(input('Enter minutes: '))
sek = int(input('Enter seconds: '))
rez = day * 24 * 60 * 60 + hour * 60 * 60 + min * 60 + sek
print(f'In entered days, hours, minutes and seconds are {rez} seconds')