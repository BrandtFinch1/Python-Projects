import math
import random

def generate_random_and_calculate():
    random_range=random.randrange(1,100)
    square_root= math.sqrt(random_range)
    print(f"Random Number: {random_range}")
    print(f"Square Root: {square_root}")
    if random_range % 2 ==0:
        print("Number is even")

    else:
        print("Number is odd")

generate_random_and_calculate()