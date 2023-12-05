#Creating the tuple
year = (2017, 2003, 2011, 2005, 1987, 2009, 2020, 2018, 2009) #Defines a named tuple that consists of years

#Prints a value that is accessed at index -3.
value_at_index_minus_3 = year[-3]
print("Value at index -3:", value_at_index_minus_3)

#Outputs both the original and reversed tuples after reversing the original tuple
reversed_year = tuple(reversed(year))
print("Original tuple:", year)
print("Reversed tuple:", reversed_year)

#Displays the count after counting the times the value 2009 appears in the tuple
count_2009 = year.count(2009)
print("Number of times 2009 appears:", count_2009)

#Prints the index after obtaining the value 2018's index from the tuple
index_2018 = year.index(2018)
print("Index of 2018:", index_2018)

#Uses len() to calculate and print the tuple's length.
tuple_length = len(year)
print("Length of the tuple:", tuple_length)