def number_pattern(n):  #Defining a function to print the number pattern. The function uses a loop to generate each row by patter by printing 1 to i where i range from 1 to n.
    for i in range(1, n + 1): #using the interger variable (i)
        print(*range(1, i + 1))

print(number_pattern(4)) #printing a number pattern up to 4 pattern and displays the result, if you put 5 or 10 in th column it will print 5 to 20 patterns