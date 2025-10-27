import csv

def read_grades():
    with open('grades.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            print("{:<12} {:<12} {:<8} {:<8} {:<8}".format(*row))

read_grades()