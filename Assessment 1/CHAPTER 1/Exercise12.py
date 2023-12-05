#Importing the math module in order to compute circle area using pi
import math

#Function to calculate square area
def calculate_square_area():
    side = float(input("Enter the side length of the square: "))  #Asking user input for the side length
    area = side ** 2  #Calculating the area of the square
    print(f"Area of the square: {area}")  #Print the calculated area

def calculate_circle_area():
    radius = float(input("Enter the radius of the circle: ")) #Asking user input for the radius
    area = math.pi * radius ** 2 #Using pi from the math module to calculate the circle's area
    print(f"Area of the circle: {area:.2f}") #The computed area being shown to two decimal places

def calculate_triangle_area():
    base = float(input("Enter the base length of the triangle: ")) #Taking input for the base length
    height = float(input("Enter the height of the triangle: "))  #Asking user input for the height
    area = 0.5 * base * height #Calculating the area of the triangle
    print(f"Area of the triangle: {area}")  #Printng the calculated area

while True:
    print("\nCalculate the area options:")  #Displaying the menu options
    print("1: Square")
    print("2: Circle")
    print("3: Triangle")
    print("0: Exit")

    choice = input("Enter your choice (1-3) or 0 to exit: ") #Taking input for user choice

    if choice == '1':
        calculate_square_area() #Calling function to calculate square area
    elif choice == '2':
        calculate_circle_area() #Calling function to calculate circle area
    elif choice == '3':
        calculate_triangle_area() #Calling function to calculate triangle area
    elif choice == '0':
        print("Exiting...") #Exiting the program
        break
    else:
        print("Invalid choice. Please choose a valid option.") #Handling invalid input