print("Enter 5 items you would pack for a trip. Seperate values with enter.")
item1=input("Input item 1: ")
item2=input("Input item 2: ")
item3=input("Input item 3: ")
item4=input("Input item 4: ")
item5=input("Input item 5: ")
list=[item1, item2, item3, item4, item5]



list.sort()
print (f"Sorted list: {list}")

del list[4]
print (f"Updated list after removing the last item: {list}")

list.append("Backpack")
print (f"Updated list after adding an item: {list}")

packed_items = {
    "Flashlight": 1,
    "Food": 1,
    "Sleeping bag": 1,
    "Tent": 1,
    "Backpack": 1
}

print(f"Packed items dictionary: {packed_items}")

for item, quantity in packed_items.items():
    print (f"Item: {item}, Quantity: {quantity}")

