import math
x1,y1 = 0, 0
x2 = int(input("Enter X value to find Distance:--"))
y2 = int(input("Enter Y value to find Distance:--"))
try:
    Distance = math.sqrt(math.pow(x2-x1, 2) + math.pow(y2-y1, 2)*1.0)
    print(Distance)
except:
    print("try again:")
