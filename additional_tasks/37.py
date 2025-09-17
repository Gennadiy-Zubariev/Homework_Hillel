'''
Additional task 37
# Дано натуральне число N. Написати функцію power_of_2(N), яка друкує
# слово YES, якщо число N є точним ступенем двійки, або слово NO в
# інакше. Користуємося рекурсією, а операцією зведення на ступінь не
# користуємося.
#
# Приклад:
# power_of_2(8) поверне YES
# poser_of_2(3) поверне NO.
'''

# def power_of_2(n):
#     if n == 2:
#         return f'Yes'
#     elif n < 2 or n % 2 != 0:
#         return 'No'
#     else:
#         return power_of_2(n / 2)
#
# power_of_2(8) #поверне YES
# power_of_2(3) #поверне NO.