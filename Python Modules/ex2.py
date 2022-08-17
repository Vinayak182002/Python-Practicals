import math
rad=float(input("Enter Radius of Circle: "));
# Calculating area and circumference
area = math.pi * rad ** 2
circumference = 2 * math.pi * rad
# Displaying output
print('Area = %0.2f.' % (area))
print('Circumference = %0.2f.' % (circumference))
