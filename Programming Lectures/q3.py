import tkinter as tk #Importing the tkinter module and aliasing it as 'tk'

root = tk.Tk() #Creating the main window

button = tk.Button(root, text="click me") #Having a variable 'button' and creating a button widget
button.pack(side=tk.RIGHT)  #Using the .pack to place the button on the right side of the window you can place it either, bottom, top, left or right based on your preference/.

root.mainloop()
