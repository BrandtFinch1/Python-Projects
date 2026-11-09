import math
def circle_calculations():
    radius=float(input("Input circle radius: "))
    #Asks for circle radius as a float input
    print(f"A circle with radius {radius} is:")

    circumference= 2*math.pi*radius
    #Calculates circumference by multiplying 2* pi * the input we got from the radius input
    print(f"Circumference: {circumference}")

    circle_area = math.pi * (radius ** 2)
    #Radius squared * pi
    print(f"Area of Circle: {circle_area}")
#Invoking the function that was created by doing def circle_calculations()
circle_calculations()


