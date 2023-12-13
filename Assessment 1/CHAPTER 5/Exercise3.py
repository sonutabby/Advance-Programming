import tkinter as tk

class Employee:
    def __init__(self, name, position, salary, emp_id):
        self.name = name
        self.position = position
        self.salary = salary
        self.emp_id = emp_id

    def display_employee(self):
        return f"{self.name}\t{self.position}\t{self.salary}\t{self.emp_id}"

def add_employee():
    name = name_entry.get()
    position = position_entry.get()
    salary = float(salary_entry.get())
    emp_id = int(id_entry.get())

    employee = Employee(name, position, salary, emp_id)
    employees.append(employee)

def display_employees():
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, "Name\tPosition\tSalary\tID\n")
    for employee in employees:
        output_text.insert(tk.END, employee.display_employee() + "\n")

employees = []

root = tk.Tk()
root.title("Employee Details")

name_label = tk.Label(root, text="Enter Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

position_label = tk.Label(root, text="Enter Position:")
position_label.pack()

position_entry = tk.Entry(root)
position_entry.pack()

salary_label = tk.Label(root, text="Enter Salary:")
salary_label.pack()

salary_entry = tk.Entry(root)
salary_entry.pack()

id_label = tk.Label(root, text="Enter ID:")
id_label.pack()

id_entry = tk.Entry(root)
id_entry.pack()

add_button = tk.Button(root, text="Add Employee", command=add_employee)
add_button.pack()

display_button = tk.Button(root, text="Display Employees", command=display_employees)
display_button.pack()

output_text = tk.Text(root, height=10, width=40)
output_text.pack()

root.mainloop()