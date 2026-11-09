name= input()

split_name= name.split()

if len(split_name)==3:
    first_name= split_name[0]
    middle_name= split_name[1]
    last_name= split_name[2]
    print(f"{last_name}, {first_name[0]}.{middle_name[0]}.")    

elif len(split_name)==2:
    first_name= split_name[0]
    last_name= split_name[1] 
    print(f"{last_name}, {first_name[0]}.")   



