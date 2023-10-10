from tkinter import *

main = Tk()
main.title("My App")
main.geometry('1366x786')

Label(main, text="Enter your Password: ").pack()
Button(main, text="Search").pack()
v = BooleanVar()  # Define a BooleanVar for Checkbutton
Checkbutton(main, text="Remember Me", variable=v, onvalue=True, offvalue=False).pack()
Entry(main, width=30).pack()
v_gender = IntVar()  # Define an IntVar for Radiobutton
Radiobutton(main, text="Male", variable=v_gender, value=1).pack()
Radiobutton(main, text="Female", variable=v_gender, value=2).pack()

var = StringVar()  # Define a StringVar for OptionMenu
var.set("Select Country")  # Set the initial value
OptionMenu(main, var, "Select Country", "USA", "UK", "INDIA", "Others").pack()

Scrollbar(main, orient=VERTICAL).pack()

main.mainloop()