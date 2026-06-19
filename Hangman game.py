import random

# Step 1: Initialization
words = ['python', 'alpha', 'developer', 'script', 'loops']
secret_word = random.choice(words)
display_word = ['_'] * len(secret_word)
turns_left = 6
guessed_letters = []

print("Welcome to Hangman!")

# Step 2: Main Game Loop
while turns_left > 0 and '_' in display_word:
    print("\nWord to guess: " + " ".join(display_word))
    print(f"Turns left: {turns_left}")
    
    # Step 3: User Input
    guess = input("Guess a letter: ").lower()
    
    # (Add validation for duplicate guesses here)
    
    # Step 4: Check Guess
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
        # Loop to update display_word
        for index, letter in enumerate(secret_word):
            if letter == guess:
                display_word[index] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        turns_left -= 1

# Step 5: Win/Loss Check
if '_' not in display_word:
    print(f"\nCongratulations! You guessed the word: {secret_word}")
else:
    print(f"\nGame Over! The word was: {secret_word}")