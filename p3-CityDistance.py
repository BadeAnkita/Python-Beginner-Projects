# WAP to read distance between two cities in KM. Convert and print the distance in meter,centimeter,inches and feet

km = int(input('Enter Distance in KM:'))
mtr = km * 1000
cm = mtr * 100
inch = cm / 2.54
ft = inch / 12
print('Distance in Meter={:.2f}'.format(mtr))
print('Distance in Centimeter={:.2f}'.format(cm))
print('Distance in inch={:.2f}'.format(inch))
print('Distance in Feet={:.2f}'.format(ft))
