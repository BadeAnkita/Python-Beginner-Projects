# format() with truncating string data
print('format() with truncating string data')
print('{:.7}'.format('Programmer'))
x = 'Machine Learning'
print('{:.4}'.format(x))

# format() with truncating and padding of string data
print('\n\nformat() with truncating and padding of string data')
print('{:10.2}'.format('Programmer'))
x = 'Machine'
print('{:15.5}'.format(x))

# format() with truncating,padding and aligning of string data
print('\n\nformat() with truncating,padding and aligning of string data')
print('{:>20.7}'.format('Programmer'))  # Right align
x = 'Machine Learning'
print('{:<30.4}'.format(x))  # Left align

# format() with truncating,padding and aligning of string data Replaceing blank spaces
print('\n\nformat() with truncating,padding and aligning of string data Replaceing blank spaces')
print('{:*>20.7}'.format('Programmer'))  # Right align
x = 'Machine Learning'
print('{:*<30.4}'.format(x))  # Left align
