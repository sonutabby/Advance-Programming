import tkinter as tk

def write_to_file():
    #Getting user input for name, age, and hometown
    name = name_entry.get()
    age = age_entry.get()
    hometown = hometown_entry.get()

    #Write the data to the file named "bio.txt"
    with open("bio.txt", "w") as file:
        file.write(f"Name: {name}\nAge: {age}\nHometown: {hometown}")

def read_from_file():
    try:
        #Attempt to read data from the file
        with open("bio.txt", "r") as file:
            data = file.read()
            #Display the data in the output label
            output_label.config(text=data)
    except FileNotFoundError:
        #Handle the case where the file is not found
        output_label.config(text="File not found. Write data first.")

#Create the main Tkinter window
root = tk.Tk()
root.title("User Information") #Set the title of the window

#Labels and Entry widgets for user input
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()
age_entry = tk.Entry(root)
age_entry.pack()

hometown_label = tk.Label(root, text="Hometown:")
hometown_label.pack()
hometown_entry = tk.Entry(root)
hometown_entry.pack()

#Button to write data to file
write_button = tk.Button(root, text="Write to File", command=write_to_file)
write_button.pack()

#Button to read data from file
read_button = tk.Button(root, text="Read from File", command=read_from_file)
read_button.pack()

#Label to display output
output_label = tk.Label(root, text="")
output_label.pack()

#Set the initial window size
root.geometry('500x300')

#Start the main loop for the Tkinter window
root.mainloop()