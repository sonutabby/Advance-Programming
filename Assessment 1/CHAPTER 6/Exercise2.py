#Given array with having the variable letter a
a = [20, 23, 82, 40, 32, 15, 67, 52]

#Find indices of even numbers
even_numbers = [i for i, num in enumerate(a) if num % 2 == 0]
print("The even numbers:", even_numbers)

#Program that sort the array
sorted_array = sorted(a)
print("The Sorted arrays:", sorted_array)

#Slicing elements from index 3 to the end of the array
ind_1 = a[3:]
print("Elements from index 3 to the end of the array:", ind_1)

#Slice elements from index 0 to index 4
ind_2 = a[:5]
print("Elements from index 0 to index 4:", ind_2)

#Print [32, 15, 67] using negative slicing
negative_slicing = a[-5:-2]
print("Elements using negative slicing:", negative_slicing)