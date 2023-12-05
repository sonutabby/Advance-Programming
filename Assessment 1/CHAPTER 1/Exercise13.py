#The function calculate_product is defined in this program, it accepts a list as an input, multiplies its elements, and outputs the outcome 
def calculate_product(lst):
    result = 1
    for num in lst:
        result *= num
    return result

#Example list
numbers = [2, 3, 4, 5]

#The calculated product is then displayed and a list of numbers is passed to show how to utilize this function
product = calculate_product(numbers)

#After being shown, the returning product is kept in the product variable
print("Product of the list values:", product)