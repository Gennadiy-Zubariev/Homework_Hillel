from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Сalculates the difference between the max and min element

    :param args: Variable number of arguments as numbers
    :return: Difference between the max and min
    """
    return round(max(args) - min(args), 2) if args else 0


assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
