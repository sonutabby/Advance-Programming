import tkinter as tk
from tkinter import messagebox
import re

def validate_password():
    global attempts_left
    password = password_entry.get()

    #Define the regular expressions for the password criteria
    lowercase_check = re.search(r'[a-z]', password)
    uppercase_check = re.search(r'[A-Z]', password)
    digit_check = re.search(r'[0-9]', password)
    special_char_check = re.search(r'[$#@]', password)
    length_check = 6 <= len(password) <= 12

    #Check if the password meets all criteria
    if lowercase_check and uppercase_check and digit_check and special_char_check and length_check:
        messagebox.showinfo("Password Valid", "Password meets the criteria!")
    else:
        attempts_left -= 1
        messagebox.showwarning("Invalid Password", f"Password does not meet the criteria. Attempts left: {attempts_left}")
        if attempts_left == 0:
            messagebox.showwarning("Alert!", "The authorities have been alerted!")
            root.quit()

def on_closing():
    global attempts_left
    if attempts_left != 5:
        messagebox.showinfo("Info", f"{attempts_left} attempts left.")
    root.destroy()

root = tk.Tk()
root.title("Password Check")
attempts_left = 5

password_label = tk.Label(root, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(root, show="*")
password_entry.pack()

validate_button = tk.Button(root, text="Validate Password", command=validate_password)
validate_button.pack()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()