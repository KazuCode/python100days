import art, game_data, random, os

def check_victory(choice, pick_a, pick_b):
    if choice == 'a' and pick_a['follower_count'] > pick_b['follower_count']:
        return True
    elif choice == 'b' and pick_b['follower_count'] > pick_a['follower_count']:
        return True
    else:
        return False

def game():
    print(art.logo)
    print(f"Compare A: {pick_a['name']}, a {pick_a['description']}, from {pick_a['country']}")
    print(art.vs)
    print(f"Compare B: {pick_b['name']}, a {pick_b['description']}, from {pick_b['country']}")
    choice = input("Who has more followers? Type 'A' or 'B'. ").lower()
    return choice

pick_a = random.choice(game_data.data)
pick_b = random.choice(game_data.data)
score = 0
game_on = True
choice = game()

while game_on:
    if check_victory(choice, pick_a, pick_b):
        os.system("cls")
        print(f"You're right! Your current score is {score}.")
        pick_a = pick_b
        pick_b = random.choice(game_data.data)
        choice = game()
        score += 1
    else:
        game_on = False
        os.system("cls")
        print(f"You lose. Your score is {score}.")