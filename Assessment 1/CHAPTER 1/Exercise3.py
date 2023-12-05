# Input from the user
s1 = float(input("Enter the length of the first side of the triangle: "))
s2 = float(input("Enter the length of the second side of the triangle: "))
s3 = float(input("Enter the length of the third side of the triangle: "))

# Check if the lengths can form a valid triangle
if (s1 + s2 > s3) and (s2 + s3 > s1) and (s1 + s3 > s2):
    print("These side lengths can form a valid triangle.")

    # Check for the type of triangle
    if s1 == s2 and s2 == s3:
        print("This is an Equilateral triangle.")
    elif s1 == s2 or s2 == s3 or s1 == s3:
        print("This is an Isosceles triangle.")
    else:
        print("This is a Scalene triangle.")
else:
    print("These side lengths cannot form a valid triangle.")