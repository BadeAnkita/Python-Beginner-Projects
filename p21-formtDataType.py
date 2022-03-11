# Printing data with Data type format()

rno = 25
name = 'Ankita'
per = 67.32
print('Rno={:d} Name={:s} Per={:f}'.format(rno, name, per))

# Print float data with two digits after decimal point
print('Rno={:d} Name={:s} Per={:.2f}'.format(rno, name, per))

# Print data with padding
print('\n\nRno={:20d} Name={:10s} Per={:15.2f}'.format(rno, name, per))

# Print data with padding and align
print('\n\nRno={:<20d} \n\nName={:>10s} \n\nPer={:<10.2f}'.format(rno, name, per))

# Print data with padding and align and replacing blank space
print('\n\nRno={:*<20d} \n\nName={:*>10s} \n\nPer={:*<10.2f}'.format(rno, name, per))
