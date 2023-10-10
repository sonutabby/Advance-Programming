from tkinter import *

app = Tk()
app.title("GUI Example 3")
app.geometry('200x100')
def copyTextToLabel():
    print(v.get())

b1 = Button(app, text="Copy Text", command=copyTextToLabel)
l1 = Label(app, text="Text is displayed here")
v = StringVar()
e1 = Entry(app, textvariable = v)
l1.pack(side='bottom')
b1.pack(side='bottom')
e1.pack(side='bottom')

app.mainloop()