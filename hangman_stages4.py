import random

def choose_word():
    words = ["apple", "banana", "kiwi", "cherry", "orange", "grapes", "guava"]
    return random.choice(words)

def display_word(word, guessed_letters):
    display = ""
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
            display += ' '
    return display

def display_hangman(incorrect_guesses):
    hangman_stages = [
        """
         -----
         |   |
         |
         |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |   |
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  /
         |
        ---
        """,
        """
         -----
         |   |
         |   O
         |  /|\\
         |  / \\
         |
        ---
        """
    ]
    return hangman_stages[incorrect_guesses]

def hangman():
    word_to_guess = choose_word()
    guessed_letters = []
    incorrect_guesses = 0
    max_incorrect_guesses = len(display_hangman(0)) - 1

    print("Welcome to Hangman!\nLet's start the Hangman game")
    print(display_word(word_to_guess, guessed_letters))

    while incorrect_guesses < max_incorrect_guesses:
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        guessed_letters.append(guess)
        print("Good guess!")
       

        if guess not in word_to_guess:
            incorrect_guesses += 1
            print(display_hangman(incorrect_guesses))
            print("Incorrect guess! try again")

        word_display = display_word(word_to_guess, guessed_letters)
        print(word_display)
        

        if "_" not in word_display:
            print("\nYou guessed the word:",word_to_guess )
            print("\nCongratulations!YOU WIN ")
            break

    if incorrect_guesses == max_incorrect_guesses:
        print(f"Sorry, you ran out of attempts./n YOU LOSE!/n The word was: {word_to_guess}")

if __name__ == "__main__":
    hangman()
