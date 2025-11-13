# ------------------------------------------------------------------------------------------ #
# Title: Assignment05
# Desc: This assignment demonstrates using dictionaries, files, and exception handling
# Change Log: (Who, When, What)
#   RRoot,1/1/2030,Created Script (Assignment05-Starter)
#   Medha S, 11/11/2025,Modified script for Assignment 05
# ------------------------------------------------------------------------------------------ #
import _io
import json
from json import JSONDecodeError

# Define the Data Constants
MENU: str = '''
---- Course Registration Program ----
  Select from the following menu:  
    1. Register a Student for a Course.
    2. Show current data.  
    3. Save data to a file.
    4. Exit the program.
----------------------------------------- 
'''
FILE_NAME: str = "Enrollments.json"

# Define the Data Variables and constants
student_first_name: str = ''  # Holds the first name of a student entered by the user.
student_last_name: str = ''  # Holds the last name of a student entered by the user.
course_name: str = ''  # Holds the name of a course entered by the user.
file = _io.TextIOWrapper  # Holds a reference to an opened file.
menu_choice: str  # Hold the choice made by the user.
student_data: dict = {}  # one row of student data
students: list = []  # a table of student data


# When the program starts, read the file data into a list of lists (table)
# Extract the data from the file by reading JSON file with exception handling
try:
    #For testing purposes
    # print(f"the file name is {FILE_NAME}")
    file = open(FILE_NAME, "r")
    students = json.load(file)
    file.close()
#Catches file not found error
except FileNotFoundError as e:
    print ("Text file must exist before running this script!\n")
    print ("-- Technical Error Message --")
    print (e, e.__doc__, type(e), sep='\n')
    print ("Creating file")
    file = open(FILE_NAME, "w") #Creates file if it doesn't exist
    json.dump(students, file, indent=2)
#Catches exception for empty file or invalid data
#Use for case where a new files is created because of FileNotFoundError
except JSONDecodeError as e:
    print("-- Technical Error Message --")
    print(e, e.__doc__, type(e), sep='\n')
    print ("Data in file is not valid. Resetting file.")
    file = open(FILE_NAME, "w")
    json.dump(students, file, indent=2)
#Catch all for all other errors
except Exception as e:
    print("There was a non-specific error!\n")
    print("-- Technical Error Message -- ")
    print(e, e.__doc__, type(e), sep='\n')
finally: #completes file closing if it wasn't closed above before an exception is thrown
    if file.close == False:
        file.close()

# Present and Process the data
while (True):

    # Present the menu of choices
    print(MENU)
    menu_choice = input("What would you like to do: ")

    # Input data from user
    if menu_choice == "1":  # This will not work if it is an integer!
        try:
            student_first_name = input("Enter the student's first name: ")
            if not student_first_name.isalpha():
                raise ValueError("The first name should not contain numbers.")

            student_last_name = input("Enter the student's last name: ")
            if not student_last_name.isalpha():
                raise ValueError("The last name should not contain numbers.")

            course_name = input("Please enter the name of the course: ")

            student_data = {"FirstName": student_first_name,
                            "LastName": student_last_name,
                            "CourseName": course_name}
            students.append(student_data)
            print\
                (f"You have registered {student_first_name} {student_last_name} for {course_name}.")

        except ValueError as e: #catches input error for values
            print(e)  # Prints efthe custom message
            print("-- Technical Error Message -- ")
            print(e.__doc__)
            print(e.__str__())
        except Exception as e: #catches all other errors
            print("There was a non-specific error!\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        continue

    # Present the current data
    elif menu_choice == "2":
        # Process the data to create and display a custom message
        print("-"*50)
        for student in students:
            print\
                (f"{student["FirstName"]},{student["LastName"]},{student["CourseName"]}")
        print("-"*50)
        continue

    # Save the data to a file
    elif menu_choice == "3":
        try:
            file = open(FILE_NAME, "w")
            json.dump(students, file, indent=2)
            file.close()
            print("The following data was saved to file!")
            for student in students:
                print\
                    (f"{student["FirstName"]} {student["LastName"]} is enrolled in {student["CourseName"]}")
            continue
        except TypeError as e: #catches file format mismatch
            print("Please check that the data is a valid JSON format\n")
            print("-- Technical Error Message -- ")
            print(e, e.__doc__, type(e), sep='\n')
        except Exception as e: #catches all other error types
            print("-- Technical Error Message -- ")
            print("Built-In Python error info: ")
            print(e, e.__doc__, type(e), sep='\n')
        finally:
            if file.closed == False:
                file.close()

    # Stop the loop
    elif menu_choice == "4":
        break  # out of the loop
    else:
        print("Please only choose option 1, 2, 3, or 4")

print("Program Ended")
