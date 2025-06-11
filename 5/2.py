while True:
    while True:
        try:
            num_one = float(input('Enter a: '))
            break
        except ValueError:
            print('wrong param a!Try again')
    while True:
        try:
            num_two = float(input('Enter b: '))
            break
        except ValueError:
            print('wrong param b!Try again')
    while True:
        operant = input('Enter operant "+", "-","*", "/":')
        lst = ['+', '-', '*', '/']
        if operant in lst:
            if operant == '+':
                print(num_one + num_two)
            elif operant == '-':
                print(num_one - num_two)
            elif operant == '*':
                print(num_one * num_two)
            elif operant == '/':
                if num_two == 0:
                    print("You can't divide by zero")
                else:
                    print(num_one / num_two)
            break
        else:
            print('Wrong operant')
    stop = input(f'For exit enter anything. \n'
                 f'If you want calculated more, enter "y": ')
    if stop.lower() == 'y':
        continue
    else:
        break