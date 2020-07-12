from ITAcademyConsoleApplication.Student.Student import Student

import csv

import pandas as pan


class Academy:
    courseOfStudy = {"Name": "FullStack Web Development",
                     "CourseDetails": ["1.Big Picture Software Engineering",
                                       "2.Fundamentals of Web Development",
                                       "3.Python Programming",
                                       "4.Backend Framework: Django",
                                       "5.Django REST Framework",
                                       "6.Frontend Library:React",
                                       "7.Capstone Project:Final Project"],
                     "CoursePrice": 20000
                     }

    def main_application(self):
        """
        Main code to drive the whole console application based on user choice.
        """
        print("Welcome to IT Academy!")
        print("Please choose an action:")
        try:
            userChoice = int(input("\nPress 1 to enquire about course."
                                   "\nPress 2 to register a student."
                                   "\nPress 3 to display all students."
                                   "\nPress 4 to update a student record."
                                   "\nPress 5 to delete a student record."
                                   "\nPress any other key to exit"
                                   )
                             )

            if userChoice == 1:
                self.enquiry_course()
            elif userChoice == 2:
                self.register_student()
            elif userChoice == 3:
                self.display_all_records()
                self.main_application()
            elif userChoice == 4:
                self.update_record()
                self.main_application()
            elif userChoice == 5:
                self.delete_record()
                self.main_application()
            else:
                print("Application Terminated.")
                return None
        except ValueError:
            print("Application Terminated.")
            return None

    def enquiry_course(self):
        """
        Enquiry of the course provided by the Academy
        """
        print("\nCourse Available:", self.courseOfStudy["Name"])
        print("Course Contents:\n" + "\n".join(self.courseOfStudy["CourseDetails"]))
        print("\nCourse Price:", self.courseOfStudy["CoursePrice"])

        try:
            userChoice = int(input("Please choose an option:"
                                   "\n Press 1 to register for the course."
                                   "\n Press 0 to exit and go back to the previous menu."
                                   )
                             )

            if userChoice == 1:
                self.register_student()
            else:
                self.main_application()

        except ValueError:
            print("Invalid Choice. Returning back to previous menu.")
            self.main_application()

    def register_student(self):
        """
        Register a new student with the details provided and linking to the parent Student class
        """
        print(self.courseOfStudy["Name"], " Registration")
        name = str(input("Enter your full name: "))
        emailAddress = str(input("Enter your email address:"))
        phoneNumber = str(input("Enter your phone number:"))
        collegeName = str(input("Enter your College Name:"))
        course = self.courseOfStudy["Name"]
        print("Payment options: \n 1) Full payment - 20000 \n2) Partial Payment - 10000")
        try:
            userChoice = int(input("Press 1 for full payment of the course."
                                   "\n Press 2 for partial payment of the course. "
                                   "\n Press 0 to cancel and exit."
                                   )
                             )
            if userChoice == 1:
                deposit = 20000
                newRegisteredStudent = Student(name, emailAddress, phoneNumber, collegeName, course, deposit)
                newRegisteredStudent.save_record()
                print(f"Congratulations! {name}.You have successfully registered.")
                self.main_application()
            elif userChoice == 2:
                deposit = 10000
                newRegisteredStudent = Student(name, emailAddress, phoneNumber, collegeName, course, deposit)
                newRegisteredStudent.save_record()
                print(f"Congratulations! {name}.You have successfully registered.")
                self.main_application()
            else:
                self.enquiry_course()
        except ValueError:
            print("Invalid Choice.Returning back to previous menu.")
            self.enquiry_course()

    def display_all_records(self):
        allStudents = pan.read_csv('student.csv')
        print(allStudents)

    def update_record(self):
        self.display_all_records()
        temp = []
        row = input("Enter the student name you would like to update: ")
        with open('student.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            fileTitles = next(reader)
            for i in reader:
                temp += [i]
            for i in temp:
                if i[0] == row:
                    name = str(input("Enter your full name: "))
                    emailAddress = str(input("Enter your email address:"))
                    phoneNumber = str(input("Enter your phone number:"))
                    collegeName = str(input("Enter your college Name:"))
                    i[0] = name
                    i[1] = emailAddress
                    i[2] = phoneNumber
                    i[3] = collegeName
                    i[4] = self.courseOfStudy["Name"]
                    if i[5] == 20000:
                        print("All dues already cleared.")
                    else:
                        print("Second installment of 10000 is due. You can enter the same or skip it for later.")
                        try:
                            dueAmountChoice = int(
                                "Press 1 to pay the remaining dues or any other key to skip for later.")
                            if dueAmountChoice == 1:
                                i[5] = 20000
                            else:
                                i[5] = 10000
                        except ValueError:
                            i[5] = 10000
                    i[6] == 20000 - i[5]

        with open("student.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fileTitles)
            writer.writerows(temp)
            print("Successfully updated the record.")

    def delete_record(self):
        self.display_all_records()
        temp = []
        row = input("Enter the student name you would like to delete: ")
        with open('student.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            fileTitles = next(reader)
            for i in reader:
                temp += [i]
            for i in temp:
                if i[0] == row:
                    temp.remove(i)
        with open("student.csv", 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(fileTitles)
            writer.writerows(temp)
            print("Record Deleted.")


academyDemo = Academy()
academyDemo.main_application()
