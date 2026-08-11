#[1] Student marks

student_marks={
    "satish":200,
    "aditya":233,
    "rohith":221,
    "balaji":224,
    "hemanth":188
}
print(student_marks)
print(student_marks.get("satish"))
student_marks.update({"phani":255})
print(student_marks)
student_marks.update({"satish":190})
print(student_marks)
student_marks.pop("rohith")
print(student_marks)

#[2] Employeee database

employee_details={
    101:"satish",
    102:"rohith",
    103:"aditya"
}

print("1.add employee")
print("2.search employee")
print("3.update employee")
print("4.delete employee")
print("5.display all employees")
print("6.exit")
choice=int(input("enter the choice :"))
if choice==1:
    new_employee_name=input("enter the new employee name: ")
    new_employee_id=int(input("enter the new employee id :"))
    employee_details.update({new_employee_id: new_employee_name})
    print("employee details after adding the  new employeee :\n")
    print("Employees amd their ID")
    for i,j in employee_details:
        print(f"{i}:{j}")
elif choice==2:
    employee_id=input("enter the employee ID :")
    if employee_details.get(employee_id):
        print(f"{employee_id} is an existing employee and his name is{employee_details.get(employee_id)}")
    else:
        print(f"{employee_id} is not an existing employeee..")
elif choice==3:
    update_employee=input("enter the employeee name to change the emplyee id :")
    update_employee_id=int(input("enter the new employee id :"))
    employee_details.update({update_employee : update_employee_id})
    print("employee details after updating  the  new employeee :\n")
    print("Employees amd their ID")
    for i,j in employee_details:
        print(f"{i}:{j}")
elif choice==4:
    delete_employee=input("enter the employee name to remove :")
    employee_details.pop(delete_employee)
    print("employee details after remove  the   employeee :\n")
    print("Employees amd their ID")
    for i,j in employee_details:
        print(f"{i}:{j}")
elif choice==5:
    print("Employees amd their ID")
    for i,j in employee_details:
        print(f"{i}:{j}")
else:
    print("Enter the correct integer ..") 
