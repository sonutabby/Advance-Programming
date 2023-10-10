from tkinter import *

app = Tk()
app.title("My App")

label1 = Label(app, text="Changed text")
label1.pack(side='top')

button1 = Button(app, text="Click me")
button1.pack(side='top')

app.mainloop()