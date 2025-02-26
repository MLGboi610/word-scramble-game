import random

# Bigger list of words
words = [
    "python", "developer", "computer", "programming", "keyboard",
    "monitor", "mouse", "internet", "software", "hardware",
    "database", "algorithm", "function", "variable", "debugging",
    "compiler", "network", "encryption", "artificial", "intelligence"
]

# Pick a random word
word = random.choice(words)

# Shuffle the letters
shuffled = "".join(random.sample(word, len(word)))

# Ask the user to unscramble it
print(f"🔀 Unscramble this word: {shuffled}")

guess = input("Your guess: ")

# Check if the guess is correct
if guess.lower() == word:
    print("🎉 Correct! You unscrambled it!")
else:
    print(f"❌ Wrong! The correct word was {word}.")
