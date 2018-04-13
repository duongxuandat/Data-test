import sys
def Add():
    # Calculate value of a + b
    a = int(input('\nInput number a: '))
    b = int(input('\nInput number b: '))
    return a + b


def Sub():
    # Calculate value of a - b
    a = int(input('\nInput number a: '))
    b = int(input('\nInput number b: '))
    return a - b


def Div():
    # Calculate value of a / b
    a = int(input('\nInput number a: '))
    print ("\nInput value b <> 0!")
    b = int(input('\nInput number b: '))
    if b == 0:
        return print("Input value b != 0")
    return a / b


def Mul():
    # Calculate value of a * b
    a = int(input('\nInput number a: '))
    b = int(input('\nInput number b: '))
    return a * b


def Power():
    # Calculate value of x^y
    a = int(input('\nInput number a: '))
    b = int(input('\nInput number b: '))
    return a ** b


def Power2():
    # Calculate value of 2^n
    n = int(input('Input number n: '))
    return 2 ** n


def Factorial():
    # Calculate value of n!
    n = int(input('Input number n: '))
    fac = 1
    count = 1
    while count <= n:
        fac *= count
        count += 1
    return fac


def Sum_series():
    # Calculate value of 1 + 1/2 + 1/3 + ... + 1/n
    n = int(input('Input number n: '))
    if n == 0:
        return print("Input value > 0")
    total = 1
    for i in range(2, n + 1):
        a = float(1 / i)
        total = float(total + a)
    return total


def Function(option):
    # Switch equivalent in python
    switch={
        1: Add,
        2: Sub,
        3: Mul,
        4: Div,
        5: Power,
        6: Factorial,
        7: Sum_series,
        8: Power2,
        0: exit
    }
    # Get the function from switch dictionary
    func = switch.get(option, lambda: "Please choose a valid function\n")
    # show result
    print(f"\n====>Result: {func()}\n")
    

while True:
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    print("Press 1. to Calculate a + b")
    print("Press 2. to Calculate a - b")
    print("Press 3. to Calculate a * b")
    print("Press 4. to Calculate a / b")
    print("Press 5. to Calculate x ^ y")
    print("Press 6. to Factorial of N")
    print("Press 7. to Calculate 1 + 1/2 + 1/3 + .... + 1/n")
    print("Press 8. to Calculate 2 ^ n")
    print("Press 0. to Exit")
    print("\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
    try:
        option = int(input('\nPlease choose a function or press 0 to exit: '))
    except:
        print('\n\"It is NaN\". Please input a valid number!')
        continue
    if option not in [0,1,2,3,4,5,6,7,8]:
        print('--------Please choose a number from 0 to 8!---------\n')
        input('Please enter to continue!')
        continue
    Function(option)