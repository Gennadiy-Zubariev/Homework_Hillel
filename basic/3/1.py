'''task 2'''

num_one = int(input("Enter first num: "))
num_two = int(input("Enter second num: "))

if num_two != 0:
    operant = input("Enter operant '+', '-','*', '/'")
    if operant == '+':
        print(num_one + num_two)
    elif operant == '-':
        print(num_one - num_two)
    elif operant == '*':
        print(num_one * num_two)
    elif operant == '/':
        print(num_one / num_two)
    else:
        print("Wrong operant!")
else:
    print("You can't divide by zero")
