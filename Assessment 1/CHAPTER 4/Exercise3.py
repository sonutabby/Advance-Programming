with open("bio.txt", "r") as file:
    numbers_list = [int(line) for line in file]

for number in numbers_list:
    print(number)