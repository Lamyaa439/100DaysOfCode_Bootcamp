import random
import hangman_words as hw
import hangman_art as ha

print(ha.logo)

lives = 6
chosen_word = random.choice(hw.word_list)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    print(f"****************************<{lives}>/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()

    if guess in correct_letters:
        print(f" You've already guessed {guess}\n")
    else:
        correct_letters.append(guess)

    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        if lives == 0:
            game_over = True
            print(f"***********************YOU LOSE**********************")
            print(f"The word you try to guess is: {chosen_word}. \n YOU LOSE!!")

    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(ha.stages[lives])
