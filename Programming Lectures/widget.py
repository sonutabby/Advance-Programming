import tkinter as tk

root = tk.Tk()
root.title("Widgets Example")

mylabel = tk.Label(root, text="I am a label widget")
mylabel.pack()

mybutton = tk.Button(root, text="I am a button")
mybutton.pack(side=tk.LEFT)

root.geometry('350x200')

root.mainloop()