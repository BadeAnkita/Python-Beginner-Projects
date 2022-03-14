# Calculate Result of student using input()

rno = input('Enter Roll no.=')
name = input('Enter Name=')
phy = int(input('Physics marks='))
che = int(input('Chemistry marks='))
maths = int(input('Maths marks='))
tot = phy + che + maths
per = float(phy + che + maths) / 3.0
print('Student Roll no={0} \nStudent Name={1}'.format(rno, name))
print(f'Total Marks={tot}')
print(f'Percent={per}')
