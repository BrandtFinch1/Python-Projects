import math
first_input= float(input("Enter x: "))
second_input= float(input("Enter y: "))
third_input= float(input("Enter z: "))
first_solution= math.pow(first_input, third_input)
second_solution= math.pow(first_input, math.pow(second_input, third_input))
third_solution=math.fabs(first_input-second_input)
squared_fourth=math.pow(first_input, third_input)
fourth_solution=math.sqrt(squared_fourth)

print(f"{first_solution:.2f} {second_solution:.2f} {third_solution:.2f} {fourth_solution:.2f}")
