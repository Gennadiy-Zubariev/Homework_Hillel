# Рядки (Strings):
# Напишіть функцію, яка приймає рядок і повертає його довжину.

def len_row(row):
    return len(row)

# Створіть функцію, яка приймає два рядки і повертає об'єднаний рядок.

def combine_row(row1, row2):
    if not isinstance(row1, str):
        row1 = str(row1)
    if not isinstance(row2, str):
        row2 = str(row2)
    return f'{row1 + row2}'

# Числа (Int/float):
# Реалізуйте функцію, яка приймає число і повертає його квадрат.

def square(num):
    if not isinstance(num, (int, float)):
        return f'num is not digit'
    return num ** 2


# Створіть функцію, яка приймає два числа і повертає їхню суму.

def summ(num1, num2):
    if not isinstance(num1, (int, float)) or not isinstance(num2, (int, float)):
        return f'one of num is not digit'
    return num1 + num2


# Створіть функцію яка приймає 2 числа типу int, виконує операцію ділення та повертає цілу частину і залишок.

def whole_part_and_residue(num1: int, num2: int) -> str | tuple[int, int]:
    if num2 == 0:
        return f"you can't divide by zero"
    return divmod(num1, num2)

# Списки (Lists):
# Напишіть функцію для обчислення середнього значення списку чисел.

def average(lst_of_nums):
    numbers = [float(i) for i in lst_of_nums if to_float(i)]
    return sum(numbers)/len(numbers) if numbers else None

def to_float(i):
    try:
        float(i)
        return True
    except (ValueError, TypeError):
        return False


# Реалізуйте функцію, яка приймає два списки і повертає список, який містить спільні елементи обох списків.

def common_elements(lst1, lst2):
    lst1 = set(lst1)
    lst2 = set(lst2)
    return list(lst1.intersection(lst2))


# Словники (Dictionaries):
# Створіть функцію, яка приймає словник і виводить всі ключі цього словника.

def dictionary_keys(d):
    print(d.keys())

# Реалізуйте функцію, яка приймає два словники і повертає новий словник, який є об'єднанням обох словників.

def combining_dictionaries(d1, d2):
    return {**d1, **d2}


# Множини (Sets):
# Напишіть функцію, яка приймає дві множини і повертає їхнє об'єднання.

def combining_sets(s1, s2):
    return s1.union(s2)

# Створіть функцію, яка перевіряє, чи є одна множина підмножиною іншої.

def subset(s1, s2):
    if s1.issubset(s2):
        return f'{s1} is subset {s2}'
    elif s1.issuperset(s2):
        return f'{s1} is superset {s2}'
    else:
        return f'{s1} and {s2} is different sets'

#Умовні вирази та цикли:
# Реалізуйте функцію, яка приймає число і виводить "Парне", якщо число парне, і "Непарне", якщо непарне.

def even_odd(num):
    return f'Парне' if num % 2 == 0 else f'Непарне'

# Створіть функцію, яка приймає список чисел і повертає новий список, що містить тільки парні числа.

def even_list(lst):
    return [i for i in lst if i % 2 == 0]
    # or list(filter(lambda i: i % 2 == 0, lst)) (не розумію як краще:))