
class Reasturent_bill_system:
    def __init__(self):
        self.ordered_items=[]

    def menu(self):
        self.items={
            1:"Chicken Biryani",
            2:"Full meals",
            3:"Half meals",
            4:"Veg biryani",
            5:"Mutton Biryani"
        }
        self.prices={
            "Chicken Biryani":120,
            "Full meals":100,
            "Half meals":80,
            "Veg biryani":100,
            "Mutton Biryani":150
        }
        for key,value in self.items.items():
            print(f"{key}.{value}")

    def order(self):
        for key,value in self.items.items():
            print(f"{key}.{value}")

        self.select_item=int(input("Enter the item number to order : "))
        self.ordered_item=self.items[self.select_item]
        print("You orderd ",self.ordered_item)
        self.ordered_items.append(self.ordered_item)

    def amount(self):
        print("You orderd items and their prices  : ")
        for item in self.ordered_items:
            print(f"{item}:{self.prices[item]}")

        self.total_amount=0
        for item in self.ordered_items:
            self.cost=self.prices[item]
            self.total_amount+=self.cost
        print("Total amount : ",self.total_amount)

obj=Reasturent_bill_system()

while True:
    print("1.Menu")
    print("2.Order")
    print("3.Amount")
    print("4.Exit")
    choice=int(input("Enter the number to perform any action :"))
    if choice==1:
        obj.menu()
        print()
    elif choice==2:
        obj.order()
        print()
    elif choice==3:
        obj.amount()
        print()
    elif choice==4:
        print("Thanks for visinting. plaese visit  agian 🙏🙏🙏🙏 ")
        print()
        break
    else:
        print("Error: choose correct number.")
    