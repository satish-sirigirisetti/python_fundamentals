#Lets build an calculatir with the basic python fundamentals 
#Calculator class
class Calculator:

    def add(self,a,b):
        self.a=a
        self.b=b
        return a+b
    def sub(self,a,b):
        self.a=a
        self.b=b
        return a-b
    def mul(self,a,b):
        self.a=a
        self.b=b
        return a*b
    def div(self,a,b):
        self.a=a
        self.b=b
        return a/b

obj=Calculator()
print("1.Add")
print("2.Subtract")
print("3.multiplication")
print("4.Division")
user_choice=int(input("Enter your choice :"))
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
if user_choice==1:
    obj.add(num1,num2)
elif user_choice==2:
    obj.sub(num1,num2)
elif user_choice==3:
    obj.mul(num1,num2)
elif user_choice==4:
    if num2==0:
        print("Error : divided by zero is not possible..")
    else:
        obj.div(num1,num2)
else:
    print("Enter the correct number...")    


