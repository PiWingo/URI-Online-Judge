import math
line = input()
x1, y1 = line.split()
x1, y1 = [float(x1), float(y1)]

line2 = input ()
x2, y2 = line2.split()
x2, y2  = [float(x2), float(y2)]

Dist= math.sqrt ((x2-x1)**2+(y2-y1)**2)

print ("%.4f" %Dist)