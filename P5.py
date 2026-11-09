import math
print("Enter 3 numbers: ")
a= int(input())
b= int(input())
c= int(input())

disc= (b*b) = (4 * a * c)
if disc < 0:
    exit(0)

sqr_disc= math.sqrt(disc)
denom = 2 * a
if denom == 0:
    x1= -b /c
    print(f"Linear equation x1= {x1}")

x1 = (-b + sqr_disc)/ denom
x2 = (-b- sqr_disc)/ denom
