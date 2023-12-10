from tkinter import *
from tkinter import messagebox

def order_coffee(): 
    #Function to process coffee orders and calculate change
    coffee_choice = coffee_var.get()
    sugar_choice = sugar_var.get()
    milk_choice = milk_var.get()
    brownsugar_choice = brownsugar_var.get()
    whippedcream_choice = whippedcream_var.get()

    selected_coffee_price = coffee_prices[coffee_choice]
    total_price = selected_coffee_price

    message = f"You ordered {coffee_choice} with "
    options = [] #If else Statement
    if sugar_choice:
        options.append("sugar")
    if milk_choice:
        options.append("milk")
    if brownsugar_choice:
        options.append("brownsugar")
    if whippedcream_choice:
        options.append("whippedcream")

    if options:
        message += ", ".join(options)
    else:
        message += "no additional options"

    try:
        money = float(money_entry.get())
        if total_price <= money:
            change = money - total_price
            if change > 0:
                # Show order summary with change if applicable
                messagebox.showinfo("Order Summary", f"{message}\nTotal Price: AED {total_price}\nChange: AED {change}\nOrder placed!")
            else:
                # Show order summary without change
                messagebox.showinfo("Order Summary", f"{message}\nTotal Price: AED {total_price}\nOrder placed!")
        else:
            #Show warning for insufficient funds
            messagebox.showwarning("Insufficient Funds", f"Total Price: AED {total_price}\nPlease insert more money.")
    except ValueError:
        #Show error for invalid input
        messagebox.showerror("Invalid Input", "Please enter a valid amount of money.")

root = Tk()
root.title("Coffee Vending Machine")

coffee_var = StringVar()
sugar_var = BooleanVar()
milk_var = BooleanVar()
brownsugar_var = BooleanVar()
whippedcream_var = BooleanVar()

Label(root, text="Please select your choice of Coffee:").grid(row=0, column=0, padx=10, pady=5)
#These are the available coffee from the vending machine
OptionMenu(root, coffee_var, "Espresso", "Latte", "Cappuccino", "Black Coffee", "Java Chip", "French Vanilla", "Mocha").grid(row=0, column=1, padx=10, pady=5)

#Additional Options
Checkbutton(root, text="Sugar", variable=sugar_var).grid(row=1, column=0, padx=10, pady=5)
Checkbutton(root, text="Milk", variable=milk_var).grid(row=1, column=1, padx=10, pady=5)
Checkbutton(root, text="Brown Sugar", variable=brownsugar_var).grid(row=1, column=2, padx=10, pady=5)
Checkbutton(root, text="Whipped Cream on top", variable=whippedcream_var).grid(row=1, column=3, padx=10, pady=5)

Label(root, text="Please Insert Money: AED").grid(row=2, column=0, padx=10, pady=5) #Label to let the user enter the amount of money to pay for their coffee
money_entry = Entry(root)
money_entry.grid(row=2, column=1, padx=10, pady=5)

Button(root, text="Place Order", command=order_coffee).grid(row=3, columnspan=2, padx=10, pady=10) #Button to place the order

#These are the coffee prices
coffee_prices = {
    "Espresso": 22.50,
    "Latte": 23.00,
    "Cappuccino": 33.50,
    "Black Coffee": 12.00,
    "Java Chip": 34.00,
    "French Vanilla": 32.50,
    "Mocha": 23.50
}

root.mainloop()