import random

while True:
    print("Select 1 to roll the dice or 2 to quit")
    try:
        c = int(input("Enter your choice: "))  
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue

    if c == 1:
        print("You rolled:", random.randint(1, 6))  
    elif c == 2:
        print("Exiting the game.")
        break  
    else:
        print("Invalid choice. Please enter 1 to roll the dice or 2 to quit.")
