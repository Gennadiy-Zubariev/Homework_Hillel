def is_even(number):
    """
    Odd or even function

    :param number: int number
    :return: True or False
    """
    if bin(number)[-1] == '0':
        return True
    return False


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'