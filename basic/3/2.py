'''task 2'''

# lst = [12, 3, 4, 10, 8]
lst = [12, 3, 4, 10]
# lst = [1]
# lst = []

# if lst:
#     lst.insert(0, lst.pop())
#     print(lst)
# else:
#     print(lst)

'''OR'''

lst.insert(0, lst.pop()) if lst else lst
print(lst)
