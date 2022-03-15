# WAP to read length,breath of rectangular and radius of circle.
#Calculate and print area and Perimeter of Rectangular, area and Circumference of Circle

length = int(input('Enter Length:'))
breath = int(input('Enter Breath:'))
radius = int(input('Enter Radius:'))
aper = (length * 2) + (breath * 2)
arect = length * breath
acir = 2 * 3.14 * radius
ac = 3.14 * (radius ** 2)
print('Area of Perimeter={:.2f}'.format(aper))
print('Area of Rectangular={:.2f}'.format(arect))
print('Area of Circumference={:.2f}'.format(acir))
print('Area of Circle={:.2f}'.format(ac))
