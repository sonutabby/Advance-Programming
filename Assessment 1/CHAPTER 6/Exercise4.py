import json

#A Function to write student details to a JSON file
def write_to_json(filename):
    student_details = {}

    #Asking user for  the student details
    student_details['Name'] = input("Enter student name: ")
    student_details['ID'] = int(input("Enter student ID: "))
    student_details['course'] = input("Enter course: ")

    #A program to write student details to JSON file
    with open(filename, 'w') as file:
        json.dump(student_details, file)
    print("Student details written to StudentJson.json")

#Function to read and display individual values from the JSON file
def read_from_json(filename):
    with open(filename, 'r') as file:
        student_details = json.load(file)
        print("\nDetails of the Student are")
        print("Name:", student_details['Name'])
        print("ID:", student_details['ID'])
        print("course:", student_details['course'])

#Function to append and update JSON file with additional details
def append_to_json(filename):
    with open(filename, 'r+') as file:
        data = json.load(file)

        #Append additional CourseDetails for student 1
        data['CourseDetails'] = {
            'Group': 'A',
            'Year': 2
        }

        #Update the file with the appended data
        file.seek(0)
        json.dump(data, file)
        print("\nCourseDetails added to StudentJson.json")

#File name
json_file = 'StudentJson.json'

#Write student details to JSON file
write_to_json(json_file)

#Read and display individual values from the JSON file
read_from_json(json_file)

# Append and update JSON file with additional details
append_to_json(json_file)

# Read and display individual values after updating the JSON file
read_from_json(json_file)