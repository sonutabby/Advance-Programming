count = 0

while True:
    user_input = input("Do you want to continue? (Y/N): ")
    if user_input.lower() == 'y':
        count += 1
    elif user_input.lower() == 'n':
        break
    else:
        print("Invalid input. Please enter 'Y' to continue or 'N' to exit.")

print(f"The loop was executed {count} times.")
