nickels=int(input("Input Nickels: "))
dimes=int(input("Input Dimes: "))
quarters=int(input("Input Quarters: "))

nickel_value= (nickels* 0.05)
dime_value= (dimes* 0.10)
quarter_value= (quarters* 0.25)
final_value=nickel_value+dime_value+quarter_value

print(f"Amount: ${final_value:.2f}")
