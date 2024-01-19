print("Welcome to Treasure Island!\nYour mission is to find the treasure!")

choice1 = input("Would you like to go left or right? ")
if choice1.lower() == 'right':
    print('You turn right.')
    choice2 = input("You arrive in front of the sea, and it seems like there is a boat not far away with loot on it.\nDo you want to swim or wait for a better weather? ")
    if choice2.lower() == 'wait':
        print('For now you prefer to wait for better condition to visit the boat.')
        choice3 = input("After waiting for 2 hours for the wind to stop, you swim to the boat and climb up. In the cabin, you're facing 3 doors. Do you visit the red, the blue or the yellow one? ")
        if choice3.lower() == 'yellow':
            print('Behind the yellow door, you find the treasure of the Treasure Island! You win.')
        else:
            print(f'Game over. Behind the { choice3.lower() } door, there are walls of spikes moving towards you, and you end up killed by it.')
    else:
        print('Game over. The wind is too strong and you end up drowning...')
        
else:
    print('Game over. You fall down a cliff and die.')