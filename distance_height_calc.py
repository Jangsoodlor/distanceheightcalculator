import math
x=int(input("insert angle on the  floor: "))
y=int(input("insert angle perpendicular to the floor (if don't have enter zero): "))
a=(math.radians(x))
b=(math.radians(y))
d=(math.tan(a))
h=(math.tan(a)*math.tan(b))
if y==0:
    print("The distance from the object is",d ,"metres")
else:
    print("The distance from the object is",d ,"metres "
          "and the height of the object is", h ,"metres")
    
    
