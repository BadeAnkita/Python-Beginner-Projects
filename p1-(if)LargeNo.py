# control statement "if else" Find large number

a = int(input('Enter 1st number:'))
b = int(input("Enter 2nd number:"))

if a > b:
    print('Large no is :{:d}'.format(a))
elif b > a:
    print('Large no is :{:d}'.format(b))
else:
    print('Both numbers are equal')
    