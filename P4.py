sum=0

while True:
    try:
        for i in range (1,8):
            print ("Enter a number: ")
            v= float(input())
            sum= sum + v

            print(f"Total is {sum}")
            average= sum / 7
            print(f"Average is {average}")


    except ValueError:
        print("Incorrect Enter a number: ")


