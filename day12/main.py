import random

def pick_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    return 5 if difficulty == 'hard' else 10

def correct_guess(answer, guess):
    if guess == answer:
        print("You guessed it right!")
        return True
    elif guess > answer: 
        print("Too high.\nGuess again.")
        return False
    else:
        print("Too low.\nGuess again.")
        return False

def game():
    print('Welcome to the number guessing game!')
    print("I'm thinking of a number between 1 and 100.")
    game_over = False
    life = pick_difficulty()
    answer = random.randint(0,100)

    print(f"You have { life } remaining to guess the number.")
    guess = int(input('Make a guess: '))
    while not game_over:
        result = correct_guess(answer, guess)
        if result:
            game_over = True
        elif not result and life > 0:
            print(f"You have { life } remaining to guess the number.")
            life -= 1
            guess = int(input('Make a guess: '))
        else:
            print('Game over.')
            game_over = True


game()
