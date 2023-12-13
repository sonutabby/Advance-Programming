import tkinter as tk

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def oldest_dog_woof(cls, dogs):
        oldest_dog = max(dogs, key=lambda dog: dog.age)
        return f"{oldest_dog.name} says: Woof!"

root = tk.Tk()
root.title("Dog Characteristics")

#Create two Dog objects and assign data
dog1 = Dog("Oreo", 3)
dog2 = Dog("Biscuit", 2)

# Display data for each dog
dog1_info_label = tk.Label(root, text=f"Dog 1: Name - {dog1.name}, Age - {dog1.age}")
dog1_info_label.pack()

dog2_info_label = tk.Label(root, text=f"Dog 2: Name - {dog2.name}, Age - {dog2.age}")
dog2_info_label.pack()

# Call the class method to make the oldest dog woof
oldest_dog_woof_label = tk.Label(root, text=Dog.oldest_dog_woof([dog1, dog2]))
oldest_dog_woof_label.pack()

root.mainloop()