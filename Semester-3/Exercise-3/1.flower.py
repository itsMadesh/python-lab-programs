# 1. Write a Python class, Flower, that has three instance variables of type str, 
# int, and float, that respectively represent the name of the flower, its number of petals, 
# and its price. Your class must include a constructor method that initializes each variable 
# to an appropriate value, and your class should include methods for setting the value of each 
# type and retrieving the value of each type


class flower:
    def __init__(self):
        self.flower_name = input("Enter flower name:")
        self.petals = int(input("Enter number of petals:"))
        self.price = float(input("Enter price:"))

    def set_name(self, flower_name):
        self.flower_name = flower_name

    def set_petals(self, petals):
        self.petals = petals

    def set_price(self, price):
        self.price = price

    def get_name(self):
        return self.flower_name

    def get_petals(self):
        return self.petals

    def get_price(self):
        return self.price


print("Create Object for flower")
flow = flower()
lot=flower()
while(1):
    print("1.Set flower Name\n2.Set number of petals\n3.Set price\n4.Get Name\n5.Get no of petals\n6.Get Price\n7.Exit")
    c = int(input("Enter your choice(1/2/3/4/5/6/7):"))
    if(c == 7):
        break
    if(c == 1):
        flower_name = input("Enter flower_name to set:")
        flow.set_name(flower_name)
    elif(c == 2):
        petals = int(input("Enter no of petals to set:"))
        flow.set_petals(petals)
    elif(c == 3):
        price = int(input("Enter price to set:"))
        flow.set_price(price)
    elif(c == 4):
        print("Flower name is", flow.get_name())
        print("Flower name is", lot.get_name())
    elif(c == 5):
        print("Number of petals is", flow.get_petals())
    elif(c == 6):
        print("Price is", flow.get_price())
    else:
        print("Invalid Input")
