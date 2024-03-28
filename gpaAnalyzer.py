# Program: GPA Analyzer
# Name: Ronit Patel
# Date: 2024-03-27
# Description: This program will take the student's last name, first name, and GPA as input and will display the student's name and GPA. If the student's GPA is greater than or equal to 3.5, the program will display that the student has made it to the Dean's list. If the student's GPA is greater than or equal to 3.2, the program will display that the student has made it to the Honor's list. Otherwise, the program will display that the student is on a good track. The program will continue to take input until the user enters "zzz" or "ZZZ" as the last name.

while True:
    print("Welcome to GPA analyzer.")
    last_name = input("Enter your last name: ")
    if last_name == "zzz" or last_name == "ZZZ":
        break
    first_name = input("Enter your first name: ")
    gpa = float(input("Enter your GPA: "))

    if gpa >= 3.5: #Dean List Checker
        print(f"{last_name}, {first_name} has a GPA of {gpa}.")
        print("This student has made to Dean's list.")
    elif gpa >= 3.2: #Honor List Checker
        print(f"{last_name}, {first_name} has a GPA of {gpa}.")
        print("This student has made to Honor's list.")
    else: #On Track Checker
        print(f"{last_name}, {first_name} has a GPA of {gpa}.")
        print("This student is on a good track.")
