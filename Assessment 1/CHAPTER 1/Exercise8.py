#Display the pattern
for row in range(1, 6): #The outer loop for i in range(1, 6) iterates from 1 to 5 and controls the pattern's rows
    for col in range(1, row + 1):  #To indicate the rows and columns, use (row and col)
        print(col, end=" ")  #Print column value with a space
    print() #Move to the next line for a new row