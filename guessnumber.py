#Guess the Number Game
secret_number = 87
n = input('Guess the secret number from 1 to 100: ')
n = int(n)
if n == secret_number:
    print("You got it!!")

else:
    #Not equal to secret_number so check if higher or lower.
    if n > secret_number:
        print("Your guess was too high")
    else:
        print("Your guess was too low.")
print("Thanks for playing.")

