# find largest number in 3 numbers

a = 51
b = 23
c = 34

if a > b and a > c:
    print('Largest number is {0}'.format(a))
elif b > c:
    print('Largest Number is {0}.'.format(b))
elif c > b:
    print('Larger number is {0}'.format(c))
else:
    print('All numbers are equal')
