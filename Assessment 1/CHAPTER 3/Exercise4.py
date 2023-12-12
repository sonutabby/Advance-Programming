import tkinter as tk

def draw_shape():
    #Retrieve the selected shape from the dropdown menu
    selected_shape = shape_var.get()
    
    #Clear the canvas to remove previous drawings
    canvas.delete("all")
    
    try:
        #Get the width and height entered by the user and convert them to integers
        width = int(shape_width.get())
        height = int(shape_height.get())
    except ValueError:
        #If the user enters non-numeric values, display an error message
        print("Please enter valid numerical values for width and height.")
        return
    
    #Draw the selected shape based on user input
    if selected_shape == "Oval":
        canvas.create_oval(50, 50, 50 + width, 50 + height, outline="black", fill="red")
    elif selected_shape == "Rectangle":
        canvas.create_rectangle(50, 50, 50 + width, 50 + height, outline="black", fill="blue")
    elif selected_shape == "Square":
        side_length = min(width, height)
        canvas.create_rectangle(50, 50, 50 + side_length, 50 + side_length, outline="black", fill="green")
    elif selected_shape == "Triangle":
        canvas.create_polygon(50, 50 + height, 50 + width / 2, 50, 50 + width, 50 + height, outline="black", fill="yellow")

#Create the main Tkinter window
root = tk.Tk()
root.title("Draw Shape") #Set the title of the window

#Variable to store the selected shape
shape_var = tk.StringVar()
shape_var.set("Oval") #Default shape

#Label to prompt the user to select a shape
shape_label = tk.Label(root, text="Select a shape:")
shape_label.pack()

#Dropdown menu to select a shape
shapes = ["Oval", "Rectangle", "Square", "Triangle"]
shape_menu = tk.OptionMenu(root, shape_var, *shapes)
shape_menu.pack()

#Labels and Entry widgets for width and height input
width_label = tk.Label(root, text="Enter width:")
width_label.pack()
shape_width = tk.Entry(root)
shape_width.pack()

height_label = tk.Label(root, text="Enter height:")
height_label.pack()
shape_height = tk.Entry(root)
shape_height.pack()

#Button to trigger the drawing of the selected shape
draw_button = tk.Button(root, text="Draw Shape", command=draw_shape)
draw_button.pack()

#Canvas to draw shapes
canvas = tk.Canvas(root, width=250, height=200)
canvas.pack()

#Start the main loop for the Tkinter window
root.mainloop()