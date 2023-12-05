#Create an integer list with 10 values
integerList = [10, 1, 44, 18, 28, 56, 5, 19, 4, 9]

#Output the list using a for loop
for number in integerList:
    print(number, end=" ")  #Print each number in the list separated by space

#Output the highest and lowest value
print("\nThe Highest value is:", max(integerList)) #Print the highest value in the list
print("The Lowest value is:", min(integerList)) #Print the lowest value in the list

#Sort the elements in ascending order
integerList.sort() #Sort the list in ascending order
print("List in ascending order:", integerList) #Print the list in ascending order

#Sort the elements in descending order
integerList.sort(reverse=True) #Sort the list in descending order
print("List in descending order:", integerList) #Print the list in descending order

#Append two elements
integerList.append(11) #Append the number 11 to the list
integerList.append(0) #Append the number 0 to the list

#Print the list after appending
print("List after appending:", integerList) #Print the final list after appending the elements
