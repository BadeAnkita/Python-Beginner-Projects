# pritn table in multiplication format

n = int(input('Enter Number:'))
i = 1
while i <= 10:
    a = n * i
    print('{0} x {1} ={2}'.format(n, i, a))
    i += 1