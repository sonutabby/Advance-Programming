import tkinter as tk

class Employee:
    def __init__(self):
        self.name = ""
        self.position = ""
        self.salary = 0.0
        self.age = ""
        self.id = ""

    def setData(self, name, position, salary, age, id):
        self.name = name
        self.position = position
        self.salary = salary
        self.age = age
        self.id = id

    def getData(self):
        return f"Name:{self.name} Position:{self.position} Salary:{self.salary} Age:{self.age} Id:{self.id}"

class Employee_GUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Employees Details")
        self.geometry("400x400")
        self.employees = []
        self.add_employee()

    def add_employee(self):
        for _ in range(5):
            name = input("Enter name: ")
            position = input("Enter the position: ")
            salary = float(input("Enter the Salary: "))
            age = input("Enter Age: ")
            employee_id = input("Enter ID: ")

            employee = Employee()
            employee.setData(name, position, salary, age, employee_id)
            self.employees.append(employee)

        self.display_employees()

    def display_employees(self):
        for employee in self.employees:
            print(employee.getData())

if __name__ == "__main__":
    app = Employee_GUI()
    app.mainloop()
