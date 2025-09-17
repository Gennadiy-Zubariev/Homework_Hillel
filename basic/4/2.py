'''task 2'''

# l = [0, 2, 7, 2, 4, 8]
# l = [2, 3, 5]
# l = [6]
l = []

otw = sum(l[::2]) * l[-1] if l else 0
print(otw)
