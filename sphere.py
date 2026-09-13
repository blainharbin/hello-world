from math import pi

radius = float(input("What is the radius of the sphere?:    "))
diameter = 2 * radius
circumference = 2 * pi * radius
surfaceArea = 4 * pi * radius ** 2
Volume = 4/3 * pi * radius ** 3

print ("Your diameter circumference, surface area, and volume are as follows in that order")
       
print (str(diameter) + ",     " + str(circumference) + ",     " + str(surfaceArea) + ",     " + str(Volume))
