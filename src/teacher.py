import json
import re

from person import Person

class Teacher(Person):
    
    def __init__(self,name = None, email = None, phone = None,address = None, subject = None, teacher_id = None):
        """Constructor for teacher class

        Args:
            name (str): Name
            email (str): Email_address
            phone (int): Phone_number
            address (str): Address
            subject (str): Subject_name
            teacher_id (str): Teacher_ID
        """
        super().__init__(name,address, email, phone,)
        self.subject = subject
        self.teacher_id = teacher_id
        
    def accept_details(self):
        """Adds the details of new students into the students.json file
        """
        print("Enter the details of the new student: ")
        
        new_student_name = input("Enter name: ")
        
        while True:
            new_student_email = input("Enter email: ")
            email_pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
            if re.match(email_pattern, new_student_email):
                break
            else:
                print("Invalid email address. Please enter a valid email.")
                
        while True:
            new_student_phone = input("Enter phone_no: ")
            if new_student_phone.isdigit() and len(new_student_phone) == 10:
                new_student_phone = int(new_student_phone)
                break
            else:
                print("Invalid phone number. Please enter a 10-digit integer.")
                
        new_student_address= input("Enter address: ")
        new_student_roll_no= input("Enter roll_no: ") 
        science_marks = int(input("Enter marks for Science: "))
        math_marks = int(input("Enter marks for Math: "))
        english_marks = int(input("Enter marks for English: "))
        
        new_student_info = {
            "name" : new_student_name,
            "email": new_student_email,
            "phone": new_student_phone,
            "address": new_student_address,
            "roll_no": new_student_roll_no,
            "marks":{  
                        "Science": science_marks,
                        "Math": math_marks,
                        "English": english_marks
                    }
        }        
        try:
            with open(r"..\data_files\students.json", "r") as file:
                student_record = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            student_record = []

        student_record.append(new_student_info)

        with open(r"..\data_files\students.json", "w") as file:
            json.dump(student_record, file, indent=4)
    

    def display(self):
        """To display all the student records
        """
        with open(r"..\data_files\students.json", "r") as file:
            student_records = json.load(file)
            for student in student_records:
                print("Name:", student["name"])
                print("Email:", student["email"])
                print("Phone No:", student["phone"])
                print("Roll No:", student["roll_no"])
                print("Address:", student["address"])
                print("------------------------------")
            
    def search(self):
        """Search for the record of a particular student
        """
        try:
            search_roll_no = input("Enter the roll no to search: ")
            with open(r"..\data_files\students.json", "r") as file:
                student_record = json.load(file)
            found = False
            for student in student_record:
                if student["roll_no"] == search_roll_no:
                    print(f"The details of the student with roll {search_roll_no} are below: ")
                    print("Name:", student["name"])
                    print("Email:", student["email"])
                    print("Phone No:", student["phone"])
                    print("Roll No:", student["roll_no"])
                    print("Address:", student["address"])
                    print("Marks:")
                    for subject, mark in student['marks'].items():
                        print(f"  {subject}: {mark}")
                    print("-----------------------------------------------------")
                    found = True
                    break
            if not found:
                print(f"No student found with roll no {search_roll_no}")
        except FileNotFoundError:
            print("Error: students.json file not found")
        except json.JSONDecodeError:
            print("Error: Invalid JSON format in students.json file")
        except Exception as e:
            print(f"Error: {e}")
                       
    
    def delete(self):
        """Delete a record of a particular student
        """
        try:
            with open(r"..\data_files\students.json", "r") as file:
                student_record = json.load(file)
            student_to_del = input("Enter the roll no of student to delete: ")
            found = False
            for i, student in enumerate(student_record):
                if student["roll_no"] == student_to_del:
                    print(f"The details of {student['name']} have been deleted.")
                    del student_record[i] 
                    found = True
                    break 
            if not found:
                print(f"No student found with roll no {student_to_del}")
                print("----------------------------------------------------")
            with open(r"..\data_files\students.json", "w") as file:
                json.dump(student_record, file, indent=4)
        except FileNotFoundError:
            print("Error: students.json file not found")
        except Exception as e:
            print(f"Error: {e}")  
                    
        
        
