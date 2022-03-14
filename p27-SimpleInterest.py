# Calculate Simple interest using input()

pa = int(input('Enter Principle amount='))
yr = int(input('Enter number of years='))
rate = float(input('Enter Interest of Rate='))
sint = (pa * yr * rate) / 100
totval = pa + sint
print('Simple interest ={:.2f}'.format(sint))
print('Total Value={:.2f}'.format(totval))
