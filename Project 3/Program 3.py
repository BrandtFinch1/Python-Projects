class TripItem:
    def __init__(self, name, quantity):
        self.name = name
        self.quantity= quantity
        
    def describe(self):
        print(f"Item: {self.name}, Quantity: {self.quantity}")  

list= []


for i in range (1, 4):
    nameinput1= input("Enter the name of the item: ")
    quantity1= int(input("Enter the quantity of the item: "))
    item= TripItem(nameinput1, quantity1)
    list.append(item)

print("Packing List:")
for item in list:
    item.describe()