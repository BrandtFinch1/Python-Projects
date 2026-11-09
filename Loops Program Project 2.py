positive_integer=int((input("Input a positive integer: ")))

for positive_integer in range(positive_integer+1):
    print(positive_integer)
#Prints all the numbers from 1 to whatever the positive integer input is    


current = 0
total = 0 
#Both variables are initalized to be used in the while statement
while current <= positive_integer:
    total += current
    current += 1

print(f"The sum of the numbers from 1 to {positive_integer} is {total}")    
