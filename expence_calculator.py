# building an expense tracker using python fundamentals 

class Expence_tracker:
    expenses={
    "grocessories":10000,
    "shopping":2300,
    "current bill":500,
    "water bill":200
    }

    # Adding the new expences 
    def add_new_expences(self):
        self.new=input("Enter the new expence name :")
        self.expence_value=int(input("Enter the amount you spent :"))
        self.expenses[str(self.new)]=self.expence_value
        print("new expences added..")
        print("list of expences after the updations :")
        for key,value in self.expenses.items():
            print(key,value)

    #removing the existinng expences     
    def remove_old_expences(self):
        print("The expences you have :")
        for key,value in self.expenses.items():
            print(key,value)
        self.remove=input("enter the expence name to remove correctly : ")
        if self.remove in self.expenses:
            self.expenses.pop(self.remove)
        else:
            print("Enter the correct expence name...")
        print(f"the expences you have after the removal of {self.remove} expence :")
        for key,value in self.expenses.items():
            print(key,value)

    #updating the existing expences values 
    def update(self):
        self.updated=input("enter the expence name that you want to change :")
        if self.updated in self.expenses:
            self.new_updated_value=int(input("Enter the new updated value :"))
            self.expenses[self.updated]=self.new_updated_value
        else:
            print("Enter the correct expence name..")

    #calculating the total amount 
    def total(self):
        self.total_amount=sum(self.expenses.values())
        print("The total amount you spent in this month till now is ",self.total_amount)

    #Displaying the all expences one by one usimg the lists

    def display(self):
        print("the expences you have in this month : ")
        for key,value in self.expenses.items():
            print(key,value)

e=Expence_tracker()

while True:
    print(" 1.Add new expences \n 2.Remove old expences \n 3.Update existing expences \n 4.Calaculating the total  amount \n 5.View the expences \n 6.Exit")
    choice=int(input("Enter the your choice :"))
    if choice==1:
        e.add_new_expences()
    elif choice==2:
        e.remove_old_expences()
    elif choice==3:
        e.update()
    elif choice==4:
        e.total()
    elif choice==5:
        e.display()
    elif choice==6:
        break
    else:
        print("Enter the right choice :")
