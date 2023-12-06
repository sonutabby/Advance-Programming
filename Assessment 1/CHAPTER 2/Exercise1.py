import tkinter as tk

#Function to change the font style when the user clocked the button
def change_font(): #Change _font is the name of the variable
    label.config(font=('Helvetica', 20, 'bold')) #Modifies the font of the label

#Setting up the root window
root = tk.Tk()
root.title("Welcome") #Window title

#Creating a label with text and a specific font
label = tk.Label(root, text="GUI program using Tkinter module", font=('Arial', 14))
label.pack(padx=20, pady=30)  # Placing the label in the window with padding

#Creating a button that changes the font once clicked
font_button = tk.Button(root, text="Click here to change font", command=change_font)
font_button.pack(padx=10, pady=10) #Placing the button in the window with padding

root.geometry("1920x1080") #Setting window size
root.resizable(False, False) #Disabling window resizing
root.configure(bg='lightpink') #Setting background color

root.mainloop() #Running the main event loop