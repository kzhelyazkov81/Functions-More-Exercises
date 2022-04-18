def sign(x, y, z):
    numbers = [x, y, z]
    zero = 0
    negative = 0
    for i in numbers:
        if i == 0:
            zero += 1
        elif i < 0:
            negative += 1
    if zero != 0:
        print('zero')
    elif negative % 2 == 0:
        print('positive')
    else:
        print('negative')


num1, num2, num3 = int(input()), int(input()), int(input())

sign(num1, num2, num3)
