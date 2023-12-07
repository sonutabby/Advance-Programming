from tkinter import *

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Cannot divide by zero"
        elif operation == "Modulo Division":
            result = num1 % num2 if num2 != 0 else "Cannot divide by zero"
        else:
            result = "Select operation"

        result_label.config(text=f"Result: {result}")

    except ValueError:
        result_label.config(text="Enter valid numbers")

root = Tk()
root.title("Calculator")

Label(root, text="Enter Number 1:").pack()
entry_num1 = Entry(root)
entry_num1.pack()

Label(root, text="Enter Number 2:").pack()
entry_num2 = Entry(root)
entry_num2.pack()

operations = ["Addition", "Subtraction", "Multiplication", "Division", "Modulo Division"]
operation_var = StringVar(root)
operation_var.set(operations[0])

OptionMenu(root, operation_var, *operations).pack()

Button(root, text="Calculate", command=calculate).pack()

result_label = Label(root, text="Result: ")
result_label.pack()

root.geometry("300x300") 
root.mainloop()