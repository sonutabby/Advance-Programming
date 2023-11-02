from tkinter import *

root = Tk()


canvas = Canvas(root, width=1920, height=1080)
canvas.pack()

line = canvas.create_line(50, 70, 100, 70, fill="red", width=2)
rectangle = canvas.create_rectangle(70, 80, 100, 110, fill="blue",outline="Black", width=2)
oval = canvas.create_oval(170, 180, 300, 310, fill="red", width=2)
canvas.moveto(oval, 50, 100)
text = canvas.create_text(40, 30, text="What if ako nalang", font=('Arial', 14), fill="green")
canvas.moveto(text, 50, 100)
#image = PhotoImage(file="image.png")
#image_item = canvas.create_image(x1, y1)

root.mainloop()