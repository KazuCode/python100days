from draw import drawing_tabs
import random

player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n'))

if player_choice not in [0, 1, 2]:
    print("Unvalid choice, you lose.")
else :
    print(drawing_tabs[player_choice])

    print('\nComputer chose:')
    computer_choice = random.randint(0, 2)
    print(drawing_tabs[computer_choice])

    if player_choice == 0 and computer_choice == 2:
        print("You win.")
    elif computer_choice == 0 and player_choice == 2:
        print("You lose.")
    elif player_choice < computer_choice:
        print("You lose.")
    elif player_choice > computer_choice:
        print("You win.")
    elif player_choice == computer_choice:
        print("It's a draw.")