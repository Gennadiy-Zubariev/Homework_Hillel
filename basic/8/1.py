def add_one(some_list):
    """add one func"""
    lst_copy = int(''.join(map(str, some_list[:])))
    lst_copy += 1
    res = [int(i) for i in str(lst_copy)]
    return res


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")
