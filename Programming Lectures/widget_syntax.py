from tkinter import *
main = Tk()

Label(main, text="Enter your Password: ")
Button(main, text="Search")
Checkbutton(main, text="RememberMe", varuable="v", value=True)
Entry(main, width=30)
Radiobutton(main, text="Male", varuable="v", value=1)
Radiobutton(main, text="Female", varuable="v", value=2)
OptionMenu(main, Variable, "Select Country", "USA", "UK", "INDIA", "Others")
Scrollbar(main, orient=VERTICAL)

main.mainloop()