# import random

# emojis = {ROCK:'🪨', SCISSORS : '✂️', PAPER: '📃'}
# choices = (ROCK,PAPER, SCISSORS)

# while True:
#     user_Choice = input('Rock, Paper or Scissors? (r/p/s): ').lower()
#     if user_Choice not in choices:
#         print("Invalid Choice!")
#         continue 

#     computer_choice = random.choice(choices)

#     print(f'you choose {emojis[user_Choice]}')
#     print(f'computer choose {emojis[computer_choice]}')

#     if user_Choice == computer_choice:
#         print('Tie!')
#     elif(
#         user_Choice == ROCK and computer_choice == PAPER or
#         user_Choice == PAPER and computer_choice == SCISSORS or
#         user_Choice == SCISSORS and computer_choice == ROCK
#     ):
#         print("you loose!")

#     else: 
#         print('you win!')

#     should_continue = input('Continue? (any key excpet(N)/N): ').lower()
#     if should_continue == 'n':
#         break











# OPTIMIZED


import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'

emojis = {ROCK:'🪨', SCISSORS : '✂️', PAPER: '📃'}
# choices = (ROCK,PAPER, SCISSORS)
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_Choice = input('Rock, Paper or Scissors? (r/p/s): ').lower()
        if user_Choice in choices:
            return user_Choice
        else:
            print('Invalid choice!')
            continue

def display_choices(user_Choice, computer_choice):
    print(f'you choose {emojis[user_Choice]}')
    print(f'computer choose {emojis[computer_choice]}')

def detemine_winner(user_Choice,computer_choice):
    if user_Choice == computer_choice:
        print('Tie!')
    elif(
        user_Choice == ROCK and computer_choice == PAPER or
        user_Choice == PAPER and computer_choice == SCISSORS or
        user_Choice == SCISSORS and computer_choice == ROCK
    ):
        print("you loose!")

    else: 
        print('you win!')

def play_game():
    while True:
        user_Choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_Choice,computer_choice)
    
        detemine_winner(user_Choice,computer_choice)
        
        should_continue = input('Continue? (any key excpet/N): ').lower()
        if should_continue == 'n':
            break

play_game()


























# import random

# choices = {ROCK:1, PAPER:-1, SCISSORS:0}
# reversed_choices = {1:"🪨", -1:"📃", 0:"✂️"}

# while True:
#     computer_choice = random.choice([1,-1,0])
#     your_choice = input("Enter your choice(ROCK/PAPER/SCISSORS/): ").lower()
#     if your_choice not in choices:
#         print('Invalid Choice!')
#         continue
        
#     choose = choices[your_choice]

#     print(f"your chose{reversed_choices[choose]} and computer chose{reversed_choices[computer_choice]}")

#     if choices[your_choice] == computer_choice:
#         print("Tie!")
#     elif((computer_choice - choices[your_choice]) == -1  or (computer_choice - choices[your_choice]) == 2):
#             print("You win!")
#     else:
#             print('you loose!')

#     should_continue = input('continue? any key except /N):').lower()
#     if should_continue == 'n':
#         break