#file handling practice questions

#[1] 

lines=0
words=0
characters=0

f=open("student.txt","r")
for i in f:
    lines+=1
    words+=len(i.split())
    characters+=len(i)
print("number of lines: ",lines)
print("number of words: ",words)
print("number of characters: ",characters)

#[2] 

f=open("student.txt","r")
read=f.read()
f1=open("destination.txt","w")
f1.write(read)
f1.close()
f1=open("destination.txt","r")
print(f1.read())

#[3]

user=input("enter the you want to find: ").lower()
count=0
f=open("student.txt","r")
for i in f:
    line=i.split()
    for j in line:
        if user==j.lower():
            count+=1
if count==0:
    print(f"{user} word does not exist..")
else:
    print(f"{user} word appears {count} times..")

#[4]
n=int(input("how many students data you want to enter :"))
for i in range(0,n):
    student_name=input("enter the student name :")
    student_marks=float(input("enter the student marks:"))
    f=open("student.txt","a")
    f.write(student_name+" ")
    f.write(str(student_marks)+"\n")
    f.close()
f=open("student.txt","r")
for i in f:
    words=i.split()
    print(f"{words[0]} scores {words[1]}..")
f.close()
f=open("student.txt","r")
l=[]
for i in f:
    words=i.split()
    l.append(float(words[1]))
f.close()
maximum=max(l)
f=open("student.txt","r")
for i in f:
    words=i.split()
    if maximum==float(words[1]):
        print(f"{words[0]} scores highest marks '{maximum}'")
total=0
for i in l:
    total+=i
avg=total/len(l)
f.close()
print("the average marks are: ",avg)