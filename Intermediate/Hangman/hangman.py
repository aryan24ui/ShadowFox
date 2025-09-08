import random

# Hangman drawings for each wrong guess
HANGMAN = [
    """
     ------
     |    |
     |
     |
     |
     |
    ===
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
    ===
    """,
    """
     ------
     |    |
     |    O
     |    |
     |
     |
    ===
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |
     |
    ===
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |
     |
    ===
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |
    ===
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ===
    """
]

# Words with simple hints
WORDS = {
    "python": "A programming language",
    "guitar": "A musical instrument",
    "elephant": "A large animal",
    "pizza": "Italian food",
    "jupiter": "A planet in the solar system"
}

def play():
    word = random.choice(list(WORDS.keys()))
    hint = WORDS[word]
    guessed = []
    wrong = 0
    max_wrong = len(HANGMAN) - 1

    print("🎮 Welcome to Hangman!")
    print("You can type 'hint' once to get help.\n")

    while wrong < max_wrong:
        # Show hangman and current word
        print(HANGMAN[wrong])
        display_word = " ".join([c if c in guessed else "_" for c in word])
        print("Word:", display_word)

        # Check if player won
        if all(c in guessed for c in word):
            print("✅ You guessed it! The word was:", word)
            return

        guess = input("Guess a letter: ").lower()

        if guess == "hint":
            print("💡 Hint:", hint)
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue

        if guess in guessed:
            print("You already guessed that letter.")
            continue

        guessed.append(guess)

        if guess not in word:
            wrong += 1
            print("❌ Wrong guess!")

    # Game over
    print(HANGMAN[wrong])
    print("💀 Game Over! The word was:", word)

# Run the game
play()


