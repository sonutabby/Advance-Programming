from tkinter import *

def register_student():
    name = name_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    address = address_entry.get("1.0", END)  # Retrieve text from a Text widget
    gender = gender_var.get()
    course = course_var.get()
    languages = ", ".join([lang_var[i].get() for i in range(len(lang_var))])

    print(f"Student Name: {name}")
    print(f"Mobile Number: {mobile}")
    print(f"Email ID: {email}")
    print(f"Home Address: {address}")
    print(f"Gender: {gender}")
    print(f"Course Enrolled: {course}")
    print(f"Languages Known: {languages}")

root = Tk()
root.title("Student Registration")

# Labels and Entry fields
Label(root, text="Student Name:").grid(row=0, column=0, padx=5, pady=5)
name_entry = Entry(root)
name_entry.grid(row=0, column=1, padx=5, pady=5)

Label(root, text="Mobile Number:").grid(row=1, column=0, padx=5, pady=5)
mobile_entry = Entry(root)
mobile_entry.grid(row=1, column=1, padx=5, pady=5)

Label(root, text="Email ID:").grid(row=2, column=0, padx=5, pady=5)
email_entry = Entry(root)
email_entry.grid(row=2, column=1, padx=5, pady=5)

Label(root, text="Home Address:").grid(row=3, column=0, padx=5, pady=5)
address_entry = Text(root, height=1, width=15)  # Adjusting width to match other entry fields
address_entry.grid(row=3, column=1, columnspan=1, padx=5, pady=5)  # Setting column span

# Gender Radio Buttons
Label(root, text="Gender:").grid(row=0, column=0, padx=5, pady=5)
gender_var = StringVar()
gender_var.set("Select Gender")  # Set default value
OptionMenu(root, gender_var, "Select Gender", "Male", "Female").grid()

Scrollbar(root, orient=VERTICAL).grid()

# Course Enrolled OptionMenu
Label(root, text="Course Enrolled:").grid(row=5, column=0, padx=5, pady=5)
course_var = StringVar()
course_var.set("BSc CC")  # Set default value
courses = ["BSc CC", "BSc CY", "BSc PSY", "BA & BM"]

# Create radio buttons for courses in a horizontal row
for idx, course in enumerate(courses):
    Radiobutton(root, text=course, variable=course_var, value=course).grid(row=5, column=idx+1, padx=5, pady=5, sticky='w')

# Language Checkboxes
Label(root, text="Languages Known:").grid(row=6, column=0, padx=5, pady=5)
lang_var = [IntVar() for _ in range(3)]
languages = ["English", "Tagalog", "Hindi/Urdu"]
for i in range(len(languages)):
    Checkbutton(root, text=languages[i], variable=lang_var[i]).grid(row=6, column=i+1, padx=5, pady=5)

# Register Button
Button(root, text="Register", command=register_student).grid(row=7, columnspan=3, padx=5, pady=10)

root.mainloop()