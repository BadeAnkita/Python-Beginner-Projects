# Enter Name, age and check the age

name = input('Enter your Name=')
age = int(input('Enter your age:'))
if age >= 18:
    print('{0} You can vote and drive'.format(name))
else:
    print('{0} You can not vote and drive'.format(name))
    