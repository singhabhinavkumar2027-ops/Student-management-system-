import json
students=[]
def add_student():
    roll=int(input("Enter roll number:"))
    name=input("Enter students name:")
    age=int(input("Enter age:"))
    marks1=float(input("Enter marks for subject 1:"))
    marks2=float(input("Enter marks for subject 2:"))
    marks3=float(input("Enter marks for subject 3:"))
    total=marks1+marks2+marks3
    percentage=total/3
    if percentage>=90:
        grade="A"
    elif percentage>=75:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=50:
        grade="D"
    else:
        grade="E"
    student={ 
        "roll":roll,
        "name":name,
        "age":age,
        "marks":[marks1,marks2,marks3],
        "percentage":percentage,
        "grade":grade}
    students.append(student)
    print("Student added succesfully")
def view_students():
    if len(students)==0:
            print("No students found")
            return
    for student in students:
        print("Roll number:",student["roll"])
        print("name:",student["name"])
        print("age:",student["age"])
        print("marks:",student["marks"])
        print("percentage:",student["percentage"])
        print("grade:",student["grade"])
def search_student():
    roll=int(input("enter roll number to search:"))
    for student in students:
        if student["roll"]==roll:
            print("Student found!")
            print("name:",student["name"])
            print("age:",student["age"])
            print("marks:",student["marks"])
            print("percentage:",student["percentage"])
            print("grade:",student["grade"])
            return
        print("Student not found")
def delete_student():
    roll=int(input("enter roll number to delete:"))
    for student in students:
        if student["roll"]==roll:
             students.remove(student)
        print("Student deleted!")
        return
    print("Student not found")
def update_students():
    roll=int(input("enter roll number to update:"))
    for student in students:
        if student["roll"]==roll:
            student["name"]=input("Enter students name:")
            student["age"]=int(input("Enter new age:"))
        print("Student updated successfully!")
        return
    print("Student not found")
while True:
        print("\nStudent Management System")
        print("1.Add Student")
        print("2.View Students")
        print("3.Search Student")
        print("4.Delete Student")
        print("5.update Student")
        print("6.Exit")
        choice=input("enter your choice:")
        if choice=="1":
            add_student()
        elif choice=="2":
            view_students()
        elif choice=="3":
            search_student()
        elif choice=="4":
            delete_student()
        elif choice=="5":
            update_students()
        elif choice=="6":
            print("thank you for using the student management system")
            break