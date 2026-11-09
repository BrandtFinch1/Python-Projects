import math

inital_frequency=float(input("Enter a key frequency: "))
r= math.pow(2, 1/12)

frequency_one=(inital_frequency * math.pow(r, 1))
frequency_two=(inital_frequency * math.pow(r, 2))
frequency_three=(inital_frequency * math.pow(r, 3))

print(f"{inital_frequency:.2f} Hz")
print(f"{frequency_one:.2f} Hz")
print(f"{frequency_two:.2f} Hz")
print(f"{frequency_three:.2f} Hz")