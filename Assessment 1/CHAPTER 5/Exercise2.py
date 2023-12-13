import tkinter as tk

class Students:
    def __init__(self, name, mark1, mark2, mark3):
        self.name = name
        self.mark1 = mark1
        self.mark2 = mark2
        self.mark3 = mark3

    def calcGrade(self):
        return (self.mark1 + self.mark2 + self.mark3) / 3

    def display(self):
        grade = self.calcGrade()
        return f"Name: {self.name}, Average Grade: {grade:.2f}"

def create_student_with_values():
    # Create a student object using constructor parameters
    student = Students("Abby", 90, 85, 98)
    student_info_label.config(text=student.display())

def create_student():
    name = name_entry.get()
    mark1 = int(mark1_entry.get())
    mark2 = int(mark2_entry.get())
    mark3 = int(mark3_entry.get())

    student = Students(name, mark1, mark2, mark3)
    student_info_label.config(text=student.display())

root = tk.Tk()
root.title("Students Grade Calculator")

create_student_with_values_button = tk.Button(root, text="Create Student with Values", command=create_student_with_values)
create_student_with_values_button.pack()

name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

mark1_label = tk.Label(root, text="Enter Mark 1:")
mark1_label.pack()

mark1_entry = tk.Entry(root)
mark1_entry.pack()

mark2_label = tk.Label(root, text="Enter Mark 2:")
mark2_label.pack()

mark2_entry = tk.Entry(root)
mark2_entry.pack()

mark3_label = tk.Label(root, text="Enter Mark 3:")
mark3_label.pack()

mark3_entry = tk.Entry(root)
mark3_entry.pack()

create_student_button = tk.Button(root, text="Create Student", command=create_student)
create_student_button.pack()

student_info_label = tk.Label(root, text="")
student_info_label.pack()

root.mainloop()