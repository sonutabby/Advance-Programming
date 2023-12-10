import tkinter as tk
from tkinter import ttk
import math

def calculate_circle_area():
    try:
        radius = float(circle_radius_entry.get())
        area = math.pi * radius ** 2
        circle_area_label.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        circle_area_label.config(text="Please enter a valid radius")

def calculate_square_area():
    try:
        side = float(square_side_entry.get())
        area = side ** 2
        square_area_label.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        square_area_label.config(text="Please enter a valid side length")

def calculate_rectangle_area():
    try:
        length = float(rectangle_length_entry.get())
        width = float(rectangle_width_entry.get())
        area = length * width
        rectangle_area_label.config(text=f"Area: {area:.2f} square units")
    except ValueError:
        rectangle_area_label.config(text="Please enter valid length and width")

root = tk.Tk()
root.title("Area Calculator")

tab_control = ttk.Notebook(root)

circle_tab = ttk.Frame(tab_control)
square_tab = ttk.Frame(tab_control)
rectangle_tab = ttk.Frame(tab_control)

tab_control.add(circle_tab, text='Circle')
tab_control.add(square_tab, text='Square')
tab_control.add(rectangle_tab, text='Rectangle')

# Circle Tab
tk.Label(circle_tab, text="Radius:").grid(row=0, column=0, padx=5, pady=5)
circle_radius_entry = tk.Entry(circle_tab)
circle_radius_entry.grid(row=0, column=1, padx=5, pady=5)
circle_area_button = tk.Button(circle_tab, text="Calculate Area", command=calculate_circle_area)
circle_area_button.grid(row=1, columnspan=2, padx=5, pady=5)
circle_area_label = tk.Label(circle_tab, text="")
circle_area_label.grid(row=2, columnspan=2)

# Square Tab
tk.Label(square_tab, text="Side Length:").grid(row=0, column=0, padx=5, pady=5)
square_side_entry = tk.Entry(square_tab)
square_side_entry.grid(row=0, column=1, padx=5, pady=5)
square_area_button = tk.Button(square_tab, text="Calculate Area", command=calculate_square_area)
square_area_button.grid(row=1, columnspan=2, padx=5, pady=5)
square_area_label = tk.Label(square_tab, text="")
square_area_label.grid(row=2, columnspan=2)

# Rectangle Tab
tk.Label(rectangle_tab, text="Length:").grid(row=0, column=0, padx=5, pady=5)
rectangle_length_entry = tk.Entry(rectangle_tab)
rectangle_length_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Label(rectangle_tab, text="Width:").grid(row=1, column=0, padx=5, pady=5)
rectangle_width_entry = tk.Entry(rectangle_tab)
rectangle_width_entry.grid(row=1, column=1, padx=5, pady=5)
rectangle_area_button = tk.Button(rectangle_tab, text="Calculate Area", command=calculate_rectangle_area)
rectangle_area_button.grid(row=2, columnspan=2, padx=5, pady=5)
rectangle_area_label = tk.Label(rectangle_tab, text="")
rectangle_area_label.grid(row=3, columnspan=2)

tab_control.pack(expand=1, fill="both")

root.mainloop()