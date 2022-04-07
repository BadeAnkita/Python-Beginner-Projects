# simple calculator program using control condition statement

a = int(input('Enter 1st number:'))
b = int(input('Enter 2nd Number:'))
op = input("Enter Arithmatic Operator:")

if op == '+':
    res = a + b
    print('Addition is:{:d}'.format(res))
elif op == '-':
    res = a - b
    print('Subtraction is:{:d}'.format(res))
elif op == '*':
    res = a * b
    print('Multiply is:{:d}'.format(res))
elif op == '/':
    res = a / b
    print('Division is:{:f}'.format(res))
else:
    print('Operator is incorrect ')
