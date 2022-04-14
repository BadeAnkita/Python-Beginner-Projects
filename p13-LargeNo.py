# Find largest number in 5  numbers

i = 1
large = 0
while i <= 5:
    n = int(input('Enter a number:'))
    if n > large:
        large = n
    i += 1
print('Largest number in 5 number is: {0}'.format(large))
