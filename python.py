from tkinter.messagebox import NO, YES
print("Before this program starts, make sure to use no caps when typing. Print your answers in yes and no.")
red= input("Do you like red? ") 

if red == YES:
    print("I like red as well.")
    gray= input("Do you like Gray? ")

if red == NO:
    print("Ok. There must be a color you like. Lets continue.")
    gray= input("Do you like Gray? ")    
    
if gray == NO:
    black= input("Do you like black? ")
    print("Alright. Lets continue.")

if gray == YES:
    print("Nice! Lets continue.")
    black= input("Do you like black? ")

if black == NO:
   silver= input("Do you like silver?")
   print("Do you like silver?")

if black == YES:
    silver =input("Nice! Do you like silver? ")

if silver ==YES:
    print("Nice! You passed the program! You like a ton of light and dark colors.")

if silver == NO:
    print("Um. The end of the program. You didn't pass.")

print("This software is distributible and uses the MIT Lisense.")