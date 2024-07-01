import json
from person import Person

class Student(Person):
    def __init__(self, name=None, email=None, phone=None, address=None, roll_no=None, marks=None):
        """Constructor of Student class

        Args:
            name (str): Name
            address (str): Address
            email (str): Email_address
            phone (int): Phone_no
            roll_no (str): Roll_no
            marks (int): Marks_of_subject
        """
        super().__init__(name, address, email, phone)
        self.roll_no = roll_no
        self.marks = marks

    def display_all(self):
        """Displays the record of the Student user
        """
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        for student in student_record:
            if student["name"] == self.name and student["roll_no"] == self.roll_no:
                print("Name:", student["name"])
                print("Email:", student["email"])
                print("Phone No:", student["phone"])
                print("Roll No:", student["roll_no"])
                print("Address:", student["address"])

    def search(self):
        """Search record related to the logged student 
        """
        choice = int(input("Choose an operation: 1.Check result 2.Check score 3.Check Percentage 4. Check rank \n=> "))
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        match choice:
            case 1:
                if self.pass_fail_determination() == True:
                    print("You passed the exam")
                else:
                    print("You failed the exam.")
            case 2:
                self.highest_and_lowest_score_in_each_subject()
            case 3:
                self.percentage()
            case 4:
                self.rank_calculation()
            case _:
                print("Choice Error")

    def pass_fail_determination(self):
        """Determines whether the student passed or failed in exam

        Returns:
            bool: True if passed all subjects
        """
        count = 0
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        for student in student_record:
            if student["name"] == self.name and student["roll_no"] == self.roll_no:
                for subject, mark in student['marks'].items():
                    if mark >= 32:
                        print(f"{subject} : {mark}, Pass")
                        count += 1
                    else:
                        print(f"{subject}: {mark}, Fail")
        if count == 3:
            return True

    def highest_and_lowest_score_in_each_subject(self):
        """Displays the highest and lowest score in each subject
        """
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        subjects = ["Science", "Math", "English"]
        for subject in subjects:
            scores = [student["marks"][subject] for student in student_record]
            if scores:
                highest = max(scores)
                lowest = min(scores)
                print(f"Highest score in {subject}: {highest}")
                print(f"Lowest score in {subject}: {lowest}")
            else:
                print(f"No scores found in {subject}.")

    def percentage(self):
        """Gives the total percentage of the student.
        """
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        for student in student_record:
            if student["name"] == self.name and student["roll_no"] == self.roll_no:
                total_marks = sum(student['marks'].values())
                percentage = (total_marks / 300) * 100
                print(f"Your percentage is: {percentage}%")

    def rank_calculation(self):
        """Calculates the rank of the student
        """
        with open(r"..\data_files\students.json", "r") as file:
            student_record = json.load(file)
        student_percentages = {}
        for student in student_record:
            total_marks = sum(student['marks'].values())
            percentage = (total_marks / 300) * 100
            student_percentages[student['name']] = percentage
        sorted_percentages = sorted(student_percentages.items(), key=lambda x: x[1], reverse=True)
        rank = 1
        for student, percentage in sorted_percentages:
            if student == self.name:
                print(f"Your rank is: {rank}")
                break
            rank += 1