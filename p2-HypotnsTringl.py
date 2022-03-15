# Hypotenuse of Triangle
import math

ht = int(input('Enter Height:'))
bs = int(input('Enter Base:'))
hypt = math.sqrt((ht ** 2) + (bs ** 2))
print('Hypotenuse of Triangle is:{:.2f}'.format(hypt))
