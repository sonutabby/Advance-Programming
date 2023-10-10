from tkinter import *

root = Tk()
root.title('Changed title')
root.geometry('200x500')

def clicked():
    print("Abby tumira ng tres I miss you hanggang lunes")

mybutton = Button(root, text="Pindutin mo", command=clicked)
mybutton.pack(side=TOP)

root.mainloop()