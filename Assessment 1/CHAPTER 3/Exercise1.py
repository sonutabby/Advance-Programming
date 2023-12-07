from tkinter import *

def update_greeting():
    name = name_entry.get()
    selected_color = color_var.get()
    greeting = f"Hello, nice to meet you, {name}!"
    display_label.config(text=greeting, fg=selected_color)

root = Tk()
root.title("Greeting App")

# InputFrame
input_frame = Frame(root, bg='lightblue', padx=20, pady=20)
input_frame.pack(padx=10, pady=10)

Label(input_frame, text="Greeting App", font=("Arial", 16, "bold"), fg="blue", bg="lightblue").grid(row=0, columnspan=2, pady=10)

Label(input_frame, text="Enter your name:").grid(row=1, column=0, pady=5)
name_entry = Entry(input_frame)
name_entry.grid(row=1, column=1, pady=5)

Label(input_frame, text="Select color:").grid(row=2, column=0, pady=5)
color_var = StringVar(root)
color_var.set("black")  # Default color
color_dropdown = OptionMenu(input_frame, color_var, "black", "red", "green", "blue", "yellow", "white")
color_dropdown.grid(row=2, column=1, pady=5)

Button(input_frame, text="Update Greeting", command=update_greeting).grid(row=3, columnspan=2, pady=10)

# DisplayFrame
display_frame = Frame(root, bg='thistle', padx=20, pady=20)
display_frame.pack(padx=10, pady=10)

display_label = Label(display_frame, text="", font=("Arial", 14), bg='lightpink')
display_label.pack()

root.geometry('390x350')
root.mainloop()
