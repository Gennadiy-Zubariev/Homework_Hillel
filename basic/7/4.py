def common_elements():
    """Not empty docstring"""
    mult_3 = [i for i in range(100) if i % 3 == 0]
    mult_5 = [i for i in range(100) if i % 5 == 0]
    res = set(mult_3) & set(mult_5)
    return res


assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
