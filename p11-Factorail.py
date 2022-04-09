# print factorial number

num = int(input('Enter Number:'))
fact = 1
i = 1
while i <= num:
    fact = fact * i
    i += 1
print('Factorial of {0} is:{1}'.format(num, fact))
