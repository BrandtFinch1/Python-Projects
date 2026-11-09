# 1. Ask the user to input a positive integer, n
n = int(input("Enter a positive integer: "))

# 2. Use a for loop to print all numbers from 1 to n
print(f"\nNumbers from 1 to {n}:")
for i in range(1, n + 1):
    print(i)

# 3. Use a while loop to calculate and print the sum of numbers from 1 to n
total_sum = 0
current_num = 1

while current_num <= n:
    total_sum += current_num
    current_num += 1

print(f"\nThe sum of numbers from 1 to {n} is: {total_sum}")