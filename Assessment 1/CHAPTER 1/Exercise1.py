#ADDING GREETINGS TO THE USER
print ("Hello, user!")
user_name = input ("What is your name?\n")
age = int (input ("What is your age?\n"))
print ("It is good to meet you, " + user_name)

username_length = len(user_name) #length of username
print("The length of your name is:")
print(username_length)

print ("You will be", age + 1, "after a year\n")