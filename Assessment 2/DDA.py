import tkinter as tk
from tkinter import simpledialog, messagebox
from PIL import Image, ImageTk

class FoodOrderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Food Order App")

        # Adding background 
        image_path = 'C:/Users/avril/Downloads/pexels-pixabay-260922.jpg'
        img = Image.open(image_path)

        # Set the image size to match the screen size (1920x1080)
        img = img.resize((1920, 1080))
        self.background_image = ImageTk.PhotoImage(img)

        # Create a Canvas widget to display the background image
        self.canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
        self.canvas.pack(fill="both", expand=True)
        self.canvas.create_image(0, 0, anchor="nw", image=self.background_image)

        # Food options
        self.food_options = {
            "Breakfast": {"Pancakes": 10.00, "Omelette": 8.50, "Avocado Toast": 12.00},
            "Lunch": {"Chicken Caesar Salad": 15.00, "Spaghetti Bolognese": 14.00, "Vegetarian Wrap": 12.50},
            "Dinner": {"Grilled Salmon": 18.00, "Beef Stir-Fry": 16.50, "Vegetable Curry": 14.00},
            "Drinks": {"Water": 2.00, "Orange Juice": 4.00, "Soda": 2.50},
            "Desserts": {"Chocolate Cake": 7.50, "Ice Cream Sundae": 6.00, "Fruit Tart": 8.00}
        }

        # Variables to store user selections
        self.selected_meal_var = tk.StringVar()
        self.selected_item_var = tk.StringVar()
        self.selected_drink_var = tk.StringVar()
        self.selected_dessert_var = tk.StringVar()

        # Create GUI elements
        tk.Label(self.canvas, text="Select a Meal:", font=("Helvetica", 16), bg="white").pack(pady=5)
        self.meal_menu = tk.OptionMenu(self.canvas, self.selected_meal_var, *["Breakfast", "Lunch", "Dinner"], command=self.update_item_menu)
        self.meal_menu.pack(pady=5)

        tk.Label(self.canvas, text="Select an Item:", font=("Helvetica", 16), bg="white").pack(pady=5)
        self.item_menu = tk.OptionMenu(self.canvas, self.selected_item_var, *self.food_options["Breakfast"])
        self.item_menu.pack(pady=5)

        tk.Label(self.canvas, text="Select a Drink:", font=("Helvetica", 16), bg="white").pack(pady=5)
        self.drink_menu = tk.OptionMenu(self.canvas, self.selected_drink_var, *self.food_options["Drinks"])
        self.drink_menu.pack(pady=5)

        tk.Label(self.canvas, text="Select a Dessert:", font=("Helvetica", 16), bg="white").pack(pady=5)
        self.dessert_menu = tk.OptionMenu(self.canvas, self.selected_dessert_var, *self.food_options["Desserts"])
        self.dessert_menu.pack(pady=5)

        # Display initial cost label without individual costs
        self.cost_label = tk.Label(self.canvas, text="Cost:\nTotal: AED 0.00", font=("Helvetica", 16), bg="white")
        self.cost_label.pack(pady=5)

        tk.Button(self.canvas, text="Place Order", command=self.place_order, font=("Helvetica", 16)).pack(pady=5)

        # Variable to store the total cost
        self.total_cost = 0.0

    def update_item_menu(self, *args):
        meal_choice = self.selected_meal_var.get()
        items = self.food_options.get(meal_choice, {})
        self.item_menu['menu'].delete(0, 'end')
        for item in items:
            self.item_menu['menu'].add_command(label=item, command=lambda i=item: self.selected_item_var.set(i))
        self.update_cost_label()

    def update_cost_label(self):
        # Update the cost label with total cost only (remove individual costs)
        total_cost = self.total_cost
        self.cost_label.config(text=f"Cost:\nTotal: AED {total_cost:.2f}")

    def place_order(self):
        meal_choice = self.selected_meal_var.get()
        item_choice = self.selected_item_var.get()

        if meal_choice and item_choice:
            cost = self.food_options.get(meal_choice, {}).get(item_choice, 0)

            # Update total cost
            self.total_cost += cost

            # Display order summary with total cost
            order_summary = f"Order Summary:\nMeal: {meal_choice}\nItem: {item_choice}\nCost: AED {cost:.2f}\nTotal Cost: AED {self.total_cost:.2f}"
            messagebox.showinfo("Order Summary", order_summary)

            # Request payment
            payment = self.get_payment(self.total_cost)

            if payment is not None:
                change = payment - self.total_cost
                if change >= 0:
                    messagebox.showinfo("Order Placed", f"You ordered {item_choice} for {meal_choice}. Order placed!\nChange: AED {change:.2f}")
                else:
                    messagebox.showwarning("Insufficient Payment", "Insufficient payment. Please insert more money.")
            else:
                messagebox.showwarning("Payment Canceled", "Payment canceled.")
        else:
            messagebox.showwarning("Selection Missing", "Please select a meal and an item.")

    def get_payment(self, cost):
        try:
            payment = float(simpledialog.askstring("Payment", f"Please enter payment amount (AED {cost:.2f}):"))
            return payment
        except (ValueError, TypeError):
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = FoodOrderApp(root)
    root.geometry('1920x1080')
    root.mainloop()