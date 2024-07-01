from person import Person
from student import Student
from teacher import Teacher

"""This code section identifies the identity of the program user i.e. Teacher or Student and perform respective functions
"""

test_person = Person()
select_role = int(input("Are you: 1. Teacher or 2. Student? \n=> "))

if select_role == 1:
    if test_person.teacher_authentication() == True:
        teacher = Teacher()
        print("------------------------------------------------------------------------------")
        while True:
            operation = int(input("Select an operation:\n1. Accept details\n2. Display records\n3. Search details \n4. Delete record\n5. Exit\n=> "))
            match operation:
                case 1:
                    teacher.accept_details()
                case 2:
                    teacher.display()
                case 3:
                    teacher.search()
                case 4:
                    teacher.delete()
                case 5:
                    print("Exiting...")
                    break
                case _:
                    print(f"{operation} is not a valid operation")

                

elif select_role == 2:
    student = Student()
    student.name = input("Enter name: ")
    student.roll_no = input("Enter roll no: ")
    if student.student_authentication(student.name, student.roll_no) == True:
        while True:
            print("-----------------------------------------------------------------------------")
            operation = int(input("Select an operation: \n1.Display record \n2.Search \n3.Exit\n=> "))
            match operation:
                case 1:
                    student.display_all()
                case 2:
                    student.search()
                case 3:
                    print("Exiting...")
                    break
                case _:
                    print(f"{operation} is not a valid operation")

else:
    print("Invalid role selected")

