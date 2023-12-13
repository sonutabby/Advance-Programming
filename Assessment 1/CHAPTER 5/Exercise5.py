import tkinter as tk

class Animal:
    def __init__(self, animal_type, name, color, age, weight, noise):
        self.type = animal_type
        self.name = name
        self.color = color
        self.age = age
        self.weight = weight
        self.noise = noise

    def sayHello(self):
        print(f"{self.name} says hello!")

    def makeNoise(self):
        print(f"{self.name} makes a {self.noise} sound.")

    def animalDetails(self):
        details = f"Type: {self.type}, Name: {self.name}, Color: {self.color}, Age: {self.age}, Weight: {self.weight}, Noise: {self.noise}"
        return details

def create_animal():
    animal_type = type_entry.get()
    name = name_entry.get()
    color = color_entry.get()
    age = int(age_entry.get())
    weight = float(weight_entry.get())
    noise = noise_entry.get()

    animal = Animal(animal_type, name, color, age, weight, noise)
    return animal

def invoke_functions():
    animal1 = create_animal()
    animal1.sayHello()
    animal1.makeNoise()
    details1 = animal1.animalDetails()
    details_text.insert(tk.END, f"{details1}\n\n")

    animal2 = create_animal()
    animal2.sayHello()
    animal2.makeNoise()
    details2 = animal2.animalDetails()
    details_text.insert(tk.END, f"{details2}\n\n")

root = tk.Tk()
root.title("Animal Details")

type_label = tk.Label(root, text="Type:")
type_label.pack()

type_entry = tk.Entry(root)
type_entry.pack()

name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

color_label = tk.Label(root, text="Color:")
color_label.pack()

color_entry = tk.Entry(root)
color_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

weight_label = tk.Label(root, text="Weight:")
weight_label.pack()

weight_entry = tk.Entry(root)
weight_entry.pack()

noise_label = tk.Label(root, text="Noise:")
noise_label.pack()

noise_entry = tk.Entry(root)
noise_entry.pack()

invoke_button = tk.Button(root, text="Invoke Functions", command=invoke_functions)
invoke_button.pack()

details_text = tk.Text(root, height=10, width=50)
details_text.pack()

root.mainloop()