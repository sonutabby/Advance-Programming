#Printing even numbers from 1 to 100
for number in range(1, 101): #Using the 'for' loop to iterates through numbers from 1 to 100
    if number % 2 != 0: #Using the condition number % 2!= 0, the if statement determines whether the number is odd
        continue #The continue statement is executed if the number is odd, meaning the remaining code for odd numbers in the loop is skipped
    print(number) #The print statement is retrieved and the even number is printed if the number is even