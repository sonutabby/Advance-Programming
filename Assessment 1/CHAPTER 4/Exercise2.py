import tkinter as tk

def count_occurrences():
    try:
        with open("sentences.txt", "r") as file:
            content = file.read()

            #Strings to count occurrences
            strings_to_count = [
                "Hello my name is Peter Parker",
                "I love Python Programming",
                "Love",
                "Enemy"
            ]

            #Count occurrences of each string
            occurrences = {string: content.count(string) for string in strings_to_count}

            #Display counts in the output label
            output_label.config(text=f"Occurrences:\n{occurrences}")
    except FileNotFoundError:
        output_label.config(text="File not found.")

def search_text():
    try:
        search_term = search_entry.get()

        with open("sentences.txt", "r") as file:
            content = file.read()

            #Count occurrences of the search term
            occurrences = content.count(search_term)

            #Display counts in the output label
            output_label.config(text=f"Occurrences of '{search_term}': {occurrences}")
    except FileNotFoundError:
        output_label.config(text="File not found.")

root = tk.Tk()
root.title("CountString")

search_label = tk.Label(root, text="Search:")
search_label.pack()

search_entry = tk.Entry(root)
search_entry.pack()

search_button = tk.Button(root, text="Search", command=search_text)
search_button.pack()

count_button = tk.Button(root, text="Count Occurrences", command=count_occurrences)
count_button.pack()

output_label = tk.Label(root, text="")
output_label.pack()

root.geometry('300x300')
root.mainloop()