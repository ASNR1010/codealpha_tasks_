'''

How the Game Works:
1. Word Selection: The game randomly selects a word from a predefined list of words.
2. Player Input: The player guesses one letter at a time.
3. Word Display: After each guess, the word is displayed with guessed letters revealed and remaining letters as underscores.
4. Incorrect Guesses: Each incorrect guess increments a counter. If the player reaches the maximum number of incorrect guesses (6), they lose.
5. Winning Condition: If the player correctly guesses all the letters of the word before reaching the limit, they win.

'''

import random

# List of words for the hangman game
words = ['python', 'hangman', 'challenge', 'programming', 'algorithm']

def choose_random_word():
    """Selects a random word from the word list"""
    return random.choice(words)

def display_word(word, guessed_letters):
    """Displays the word with guessed letters revealed and remaining letters as underscores"""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def hangman():
    # Initialize game variables
    word = choose_random_word()
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect_guesses = 6  # Limit on incorrect guesses

    print("Welcome to Hangman!")
    print(f"You have {max_incorrect_guesses} incorrect guesses. Good luck!")

    while incorrect_guesses < max_incorrect_guesses:
        print("\nWord: ", display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please guess a single letter.")
            continue

        if guess in guessed_letters:
            print(f"You already guessed '{guess}'. Try a different letter.")
            continue

        guessed_letters.add(guess)

        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            incorrect_guesses += 1
            print(f"Oops! '{guess}' is not in the word. {max_incorrect_guesses - incorrect_guesses} incorrect guesses left.")

        # Check if the player has guessed the entire word
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations! You guessed the word:", word)
            break
    else:
        print(f"\nGame over! You've used up all your guesses. The word was '{word}'.")

# Run the hangman game
if __name__ == '__main__':
    hangman()
