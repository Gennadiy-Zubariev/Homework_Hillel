'''task 3'''

# lst = [1, 2, 3, 4, 5, 6]
lst = [1, 2, 3]
# lst = [1, 2, 3, 4, 5]
# lst = [1]
# lst = []
num_elem = len(lst)

if num_elem == 0:
    lst_1 = []
    lst_2 = []
    print(lst_1, lst_2)
else:
    if num_elem % 2 == 0:
        lst_1 = lst[:int(num_elem / 2)]
        lst_2 = lst[int(num_elem / 2):]
        print(lst_1, lst_2)
    else:
        lst_1 = lst[:int(num_elem // 2 + 1)]
        lst_2 = lst[int(num_elem // 2 + 1):]
        print(lst_1, lst_2)


input_list = [56, 78, 20]

mid = (len(input_list) + 1) // 2

first_half = input_list[:mid]
second_half = input_list[mid:]

print(input_list, "=>", [first_half, second_half])