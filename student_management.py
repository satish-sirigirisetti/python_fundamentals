#student management system program 

students=[]

class Student_Management_System:
    def add(self):
        self.name=input("Enter the student name : ")
        try:
            self.roll=int(input("Enter the roll number :"))
            self.age=int(input("Enter the age :"))
            self.marks=int(input("Enter the total marks :"))
        except ValueError:
            print("-- Invalid input , enter only correct integers...")
        finally:
            print("student details are addeed succesfully..")
        self.student={"name":self.name,
                      "Roll":self.roll,
                      "age":self.age,
                      "marks":self.marks}
        students.append(self.student)
    def display(self):
        for student in students:
            print(student["name"])
            print(student["Roll"])
            print(student["age"])
            print(student["marks"])
    def search(self):
        self.serach_roll=int(input("enter the student roll to search :"))
        self.status=False
        for student in students:
            if self.serach_roll==student["Roll"]:
                print("student found")
                print(f"{student["Roll"]} student details are : ",student)
                self.status=True
                break
            else:
                continue
        if self.status==True:
            pass
        else:
            print("Student does not exist..")
            print("plaese try again")
    def delete(self):
        self.delete_student_roll=int(input("Enter the student roll number to delete :"))
        for student in students:
            if self.delete_student_roll==student["Roll"]:
                print("student found")
                print(f" roll No {student["Roll"]} student details are : ",student)
                students.remove(student)                      
                self.status=True
                break
            else:
                continue
        if self.status==True:
            pass
        else:
            print("Student does not exist..")
            print("plaese try again")
s1=Student_Management_System()
while True:
    print("1.Add student")
    print("2.View student")
    print("3.Search student")
    print("4.Delete student")
    print("5.Exit")

    user=int(input("Enter your choice :"))

    if user==1:
        s1.add()
    elif user==2:
        s1.display()
    elif user==3:
        s1.search()
    elif user==4:
        s1.delete()
    elif user==5:
        break
    else:
        print("--Invalid choice enter correct one--")