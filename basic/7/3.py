def second_index(text, some_str):
    """Not empty docstring"""
    ind_1 = text.find(some_str)
    if ind_1 == -1:
        return
    ind_2 = text.find(some_str, ind_1 + 1)
    if ind_2 == -1:
        return
    return ind_2


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
