import tkinter as tk

def draw_shape():
    selected_shape = shape_var.get()
    
    canvas.delete("all") #Clear previous drawings
    
    try:
        width = int(shape_width.get())
        height = int(shape_height.get())
    except ValueError:
        print("Please enter valid numerical values for width and height.")
        return
    
    if selected_shape == "Oval":
        canvas.create_oval(50, 50, 50 + width, 50 + height, outline="black", fill="red")
    elif selected_shape == "Rectangle":
        canvas.create_rectangle(50, 50, 50 + width, 50 + height, outline="black", fill="blue")
    elif selected_shape == "Square":
        side_length = min(width, height)
        canvas.create_rectangle(50, 50, 50 + side_length, 50 + side_length, outline="black", fill="green")
    elif selected_shape == "Triangle":
        canvas.create_polygon(50, 50 + height, 50 + width / 2, 50, 50 + width, 50 + height, outline="black", fill="yellow")

root = tk.Tk()
root.title("Shape Drawer")

shape_var = tk.StringVar()
shape_var.set("Oval")  # Default shape

shape_label = tk.Label(root, text="Select a shape:")
shape_label.pack()

shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_menu = tk.OptionMenu(root, shape_var, *shapes)
shape_menu.pack()

width_label = tk.Label(root, text="Enter width:")
width_label.pack()
shape_width = tk.Entry(root)
shape_width.pack()

height_label = tk.Label(root, text="Enter height:")
height_label.pack()
shape_height = tk.Entry(root)
shape_height.pack()

draw_button = tk.Button(root, text="Draw Shape", command=draw_shape)
draw_button.pack()

canvas = tk.Canvas(root, width=250, height=200)
canvas.pack()

root.mainloop()