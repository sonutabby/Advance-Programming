import tkinter as tk
from tkinter import ttk

class ArithmeticOperations:
    def __init__(self):
        self.result = 0

    def Calculate(self, operation, value1, value2):
        if operation == "Addition":
            self.result = value1 + value2
        elif operation == "Subtraction":
            self.result = value1 - value2
        elif operation == "Multiplication":
            self.result = value1 * value2
        elif operation == "Division":
            if value2 != 0:
                self.result = value1 / value2
            else:
                self.result = "Cannot divide by zero"

def calculate_operation():
    operation = operation_var.get()
    value1 = float(value1_entry.get())
    value2 = float(value2_entry.get())

    arithmetic.Calculate(operation, value1, value2)
    result_label.config(text=f"Result: {arithmetic.result}")

arithmetic = ArithmeticOperations()

root = tk.Tk()
root.title("Arithmetic Operations")

operation_label = tk.Label(root, text="Select Operation:")
operation_label.pack()

operations = ["Addition", "Subtraction", "Multiplication", "Division"]
operation_var = tk.StringVar()
operation_var.set(operations[0])

operation_dropdown = ttk.Combobox(root, textvariable=operation_var, values=operations)
operation_dropdown.pack()

value1_label = tk.Label(root, text="Enter Value 1:")
value1_label.pack()

value1_entry = tk.Entry(root)
value1_entry.pack()

value2_label = tk.Label(root, text="Enter Value 2:")
value2_label.pack()

value2_entry = tk.Entry(root)
value2_entry.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_operation)
calculate_button.pack()

result_label = tk.Label(root, text="Result: ")
result_label.pack()

root.mainloop()