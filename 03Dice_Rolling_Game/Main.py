import random
Rolled_count = 0
while True:
    Choice = input("Roll the dice? (Y/N): ").lower()
    if Choice == 'y':
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        print(f"You rolled a {a} and a {b}.")
        Rolled_count += 1
        print(f"you rolled {Rolled_count} times")
    elif Choice == 'n':
        print("Thank you for playing!")
        break
    else:
        print("Invalid Choice!")


