import csv

# Reading a CSV file
with open('students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)