import json


class Person:
    def __init__(self, name = None, address = None, email = None, phone = None):
        """Constructor of Person class

        Args:
            name (str): Name
            address (str): Address
            email (str): Email_address
            phone (int): Phone_number
        """
        self.name = name
        self.address = address
        self.email = email
        self.phone = phone
        
    def teacher_authentication(self):
        """Checks if the program user is really a Teacher or not

        Returns:
            bool: True if is Teacher
        """
        check_name = input("Enter name: ")
        check_id = str(input("Enter ID: "))
        with open(r"..\data_files\teachers.json", "r") as file:
            teacher_record = json.load(file)
        for record in teacher_record:
                if record["teacher_id"] == check_id and record["name"] == check_name:
                    print("Teacher authentication successful")
                    return True 
        print("Teacher authentication error")
        return False
    

    
    def student_authentication(self, student_name, student_roll):
        """Checks wether the program user is a regisered Student or not     

        Returns:
            bool: True if is a Student 
        """
        
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        for record in student_record:
                if record["roll_no"] == student_roll and record["name"] == student_name:
                    print("Student authentication successful")
                    return True 
        print("Student authentication error")
        return False
    
    def data_validation(self, roll_no, email):
        """Checks wheter the student data exists or not

        Args:
            roll_no (str): Roll no of the student
            email (str): Email addrss

        Returns:
            bool: True if data does not exist
        """
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        for record in student_record:
            if record["roll_no"] == roll_no or record["email"] == email:
                print("The data already exists")
                return False
        return True


