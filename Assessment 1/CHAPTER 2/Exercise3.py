from tkinter import *

#Login credentials
def validate_login():
    username = username_entry.get()
    password = password_entry.get()

    #the username and password input
    if username == "userabby" and password == "password123456789":
        login_status.config(text="Login successful!", fg="green")
    else:
        login_status.config(text="Invalid username or password", fg="red")

#Creating the main window
root = Tk()
root.title("Login Page")  #Setting window title

#Username label and entry field
username_label = Label(root, text="Username:")
username_label.grid(row=0, column=0, padx=5, pady=5)

username_entry = Entry(root)
username_entry.grid(row=0, column=1, padx=5, pady=5)

#Password label and entry field with password masking
password_label = Label(root, text="Password:")
password_label.grid(row=1, column=0, padx=5, pady=5)

password_entry = Entry(root, show="*")  #Making the password appear as ***
password_entry.grid(row=1, column=1, padx=5, pady=5)

#Login button to trigger the validation
login_button = Button(root, text="Login", command=validate_login)
login_button.grid(row=2, columnspan=2, padx=5, pady=5)

#Label to display login status
login_status = Label(root, text="", fg="black")
login_status.grid(row=3, columnspan=2, padx=5, pady=5)

root.mainloop() #Running the main event loop to display the window and handle events