#Count from 1 to 100. The range(1, 101) contains numbers from 1 up to, but excluding, 101, and the for loop iterates over those integers from 1 to 100.
for number in range(1, 101):
    #Checking if the number is a multiple of both 3 and 5. Conditional expressions (if, elif, and else) inside the loop determine if the integer is divisible by 3, 5, both 3 and 5, or neither.
    if number % 3 == 0 and number % 5 == 0: #It outputs "FizzBuzz" if the number is divisible by both 3 and 5 ( % 3 == 0 and  % 5 == 0)
        print("FizzBuzz")  #If yes, print FizzBuzz
    #Checking if the number is a multiple of 3
    elif number % 3 == 0:
        print("Fizz")  #If yes, print Fizz
    #Check if the number is a multiple of 5
    elif number % 5 == 0:
        print("Buzz")  #If yes, print Buzz
    else:
        print(number)  #If none of the above, print the number