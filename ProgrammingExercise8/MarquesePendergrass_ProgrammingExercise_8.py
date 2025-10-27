import csv

# Function to create a csv file for students grades
def file_grades():
    # Open the CSV file in write mode
    with open('grades.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        # Row for the CSV file
        writer.writerow(['First Name', 'Last Name', 'Exam 1', 'Exam 2', 'Exam 3'])

        # Ask the user how many student records to have in csv file
        num_students = int(input("Enter the number of students: "))

        # Loop through for each student
        for _ in range(num_students):
            # Collect student details and exam grades from the user
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            exam1 = int(input("Enter Exam 1 grade: "))
            exam2 = int(input("Enter Exam 2 grade: "))
            exam3 = int(input("Enter Exam 3 grade: "))

            # Write one complete record (row) to the CSV file
            writer.writerow([first_name, last_name, exam1, exam2, exam3])

    # Confirm that the file has been successfully created
    print("grades.csv has been created.")

# Call the function to execute the program
file_grades()