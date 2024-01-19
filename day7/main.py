from random_word import RandomWords
r = RandomWords()

# Return a single random word
random_word = r.get_random_word()
display = []
lives = 10
for letter in random_word:
    display.append('_')

print(f"Pssst, the word is { random_word }")
game_on = True

while game_on:
    print(display)
    print(f'Lives: { lives }')
    bad_answer = True
    guess = input("Try to guess a letter in the word to guess: ").lower()
    for i in range(len(random_word)):
        if random_word[i] == guess:
            display[i] = guess
            bad_answer = False
    if bad_answer:
        lives -= 1
    if '_' not in display:
        game_on = False
        print(str(display)+"\nYou won!")
    if lives == 0:
        game_on = False
        print(str(display)+"\nYou lose...")