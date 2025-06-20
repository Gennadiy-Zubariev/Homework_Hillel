from collections import defaultdict


def find_unique_value(some_list):
    """find unique value"""
    res_dict = defaultdict(int)
    for i in some_list:
        res_dict[i] += 1
    if res_dict:
        for k, v in res_dict.items():
            if v == 1:
                return k
    else:
        return


assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")
