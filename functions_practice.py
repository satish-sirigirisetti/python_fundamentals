#Function practice questions

#[1] basic function

def student_info(name,age):
    print("Name:",name)
    print("Age:",age)

student_info("satish",19)
student_info("aditya",19)
student_info("balaji",19)

#[2] calculator

def add(a,b):
    c=a+b
    return c
def sub(a,b):
    c=a+b
    return c
def div(a,b):
    c=a/b
    return c
def mul(a,b):
    c=a*b
    return c
print(add(10,20))
print(div(10,20))
print(sub(10,20))
print(mul(10,20))

#[3] student grade calclualor 

def calculate_grade(marks):
    if 90<=marks<=100:
        print("A")
    elif 80<=marks<=89:
        print("B")
    elif 70<=marks<=79:
        print("C")
    elif 60<=marks<=69:
        print("D")
    elif marks<60:
        print("F")

calculate_grade(96)
calculate_grade(45)
calculate_grade(78)
calculate_grade(67)

#[4] student result management system
def student_data():
    marks=[]
    student_name=input("enter the student name: ")
    print("enter marks of each subject :")
    social=int(input("social:"))
    physics=int(input("physics:"))
    chemistry=int(input("chemistry:"))
    maths=int(input("maths:"))
    english=int(input("english:"))
    marks.append(social)
    marks.append(physics)
    marks.append(chemistry)
    marks.append(maths)
    marks.append(english)
    print("student name: ",student_name)
    return marks
def calculate_total(marks):
    total=0
    for i in marks:
        total+=i
    return total
def calculate_average(total,marks):
    n=len(marks)
    a=total/n
    return a
def calculate_grade(marks):
    if 90<=marks<=100:
        g="A"
    elif 80<=marks<=89:
        g="B"
    elif 70<=marks<=79:
        g="C"
    elif 60<=marks<=69:
        g="D"
    elif marks<60:
        g="F"
    return g
def display():
    print(marks)
    print(total)
    print(avg)
    print(grade)
marks=student_data()
total=calculate_total(marks)
avg=calculate_average(total,marks)
grade=calculate_grade(avg)
display()
