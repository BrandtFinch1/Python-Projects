import os; 
from datetime import datetime
now = datetime.now()

if os.path.isfile('sample.txt') == False:
    print("The file 'sample.txt' does not exist. Creating it now...")

with open("sample.txt", "w") as file:
    file.write("This is a sample file for Assignment 4.\n")


with open("sample.txt", "r") as file:
    contents = file.read()


print("Contents of 'sample.txt':")
print(contents)  



datetime_string = now.strftime("%d/%m/%Y %H:%M:%S")


with open("sample.txt", "a") as f:
    f.write(f"Appended on: {datetime_string}\n")

with open("sample.txt", "r") as file:
    contents = file.read()
print("Updated contents of 'sample.txt")
print(contents)



