from tkinter import *

def update_greeting():
    #Retrieves the name and selected color from the input fields
    name = name_entry.get()
    selected_color = color_var.get()
    #Constructs the greeting message with the name that the user input
    greeting = f"Hello, nice to meet you, {name}!"
    #Updates the DisplayFrame label with the chosen color and customized greeting
    display_label.config(text=greeting, fg=selected_color)

#Initializing the Tkinter application
root = Tk()
root.title("Greeting App")

#InputFrame Configuration
input_frame = Frame(root, bg='lightblue', padx=20, pady=20) #Creating InputFrame
input_frame.pack(padx=30, pady=30) #Placing InputFrame in the main window

Label(input_frame, text="Greeting App", font=("Arial", 16, "bold"), fg="blue", bg="lightblue").grid(row=0, columnspan=2, pady=10) #Title label

Label(input_frame, text="Enter your name:").grid(row=1, column=0, pady=5) #Input field for name and Name entry, where the user can input the name
name_entry = Entry(input_frame)
name_entry.grid(row=1, column=1, pady=5)

Label(input_frame, text="Select color:").grid(row=2, column=0, pady=5) #Label for color the selection of the user
color_var = StringVar(root)
color_var.set("black") #Default color. If the user does not enter any color before clicking the update message, the greetings will be displayed as black
color_dropdown = OptionMenu(input_frame, color_var, "black", "red", "green", "blue", "yellow", "white") #Dropdown for color
color_dropdown.grid(row=2, column=1, pady=5)

Button(input_frame, text="Update Greeting", command=update_greeting).grid(row=3, columnspan=2, pady=10) #Update Greeting button once clicked it will show the greeting twith the name of the user

# DisplayFrame Configuration
display_frame = Frame(root, bg='thistle', padx=20, pady=20) #Creating a DisplayFrame with padding
display_frame.pack(padx=10, pady=10)  # Place DisplayFrame in the main window with padding

display_label = Label(display_frame, text="", font=("Arial", 14), bg='lightpink') #Label to display greeting
display_label.pack() #Pack the label in DisplayFrame

root.geometry('390x350') #Setting an initial window size
root.mainloop() #Start the main event loop