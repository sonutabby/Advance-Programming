import tkinter as tk

def count_occurrences():
    try:
        char = char_entry.get()
        with open("sentences.txt", "r") as file:
            occurrences = file.read().count(char)
            output_label.config(text=f"Occurrences of '{char}': {occurrences}")
    except FileNotFoundError:
        output_label.config(text="File not found.")

root = tk.Tk()
root.title("Letter Count")

char_label = tk.Label(root, text="Enter a character:")
char_label.pack()

char_entry = tk.Entry(root)
char_entry.pack()

count_button = tk.Button(root, text="Count Occurrences", command=count_occurrences)
count_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.geometry('200x200')
root.mainloop()