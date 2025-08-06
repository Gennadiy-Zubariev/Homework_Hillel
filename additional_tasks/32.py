'''
Additional task 32
# Напишіть програму, яка приймає список слов і повертає список, містить тільки
# анаграми. Анаграми - це слова, складені з тих самих букв, але у різному
# порядку. Створіть функцію anagrams, яка приймає список слів як аргумент
# та повертає список анаграм. Використовуйте безліч і сортування букв у слові
# для перевірки на анаграму. Виведіть результат на екран.
#
# Приклад переданого списку слів:
# ['cat', 'dog', 'tac', 'god', 'act']
#
# Приклад висновку:
# Анаграми: ['dog', 'god'], ['cat', 'tac', 'act']
'''

# def anagramm(lst):
#     from collections import defaultdict
#     an = defaultdict(list)
#     for i in lst:
#         key = ''.join(sorted(i.lower()))
#         an[key].append(i)
#     for v in an.values():
#         print(v)
#
# anagramm(['cat', 'dog', 'tac', 'god', 'act'])