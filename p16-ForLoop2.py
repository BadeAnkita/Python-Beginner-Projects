# for loop as range loop Default/First Type = Single parameter Range loop

for i in range(10):
    print(i)
print('------------------------------------------')
for i in range(11):
    print(i, end=' ')
print('\n------------------------------------------')
# Second Type = Two parameter range loop
for i in range(4, 9):
    print(i, end=' ')
print('\n------------------------------------------')
# Third Type = Three parameter range loop

for i in range(1, 11, 2):    # Forwarded loop
    print(i, end=' ')
print('\n------------------------------------------')
for i in range(5, 50, 5):
    print(i, end=' ')
print('\n------------------------------------------')
for i in range(5, 51, 5):
    print(i, end=' ')
print('\n------------------------------------------')

for i in range(10, 0, -1): # Backward Loop
    print(i, end=' ')
    