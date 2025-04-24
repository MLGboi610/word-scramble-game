import random


def play_round():
    words = [
        "python", "developer", "computer", "programming", "keyboard",
        "monitor", "mouse", "internet", "software", "hardware",
        "database", "algorithm", "function", "variable", "debugging",
        "compiler", "network", "encryption", "artificial", "intelligence"
    ]


    word = random.choice(words)
    shuffled = "".join(random.sample(word, len(word)))

    print(f"🔀 Unscramble this word: {shuffled}")

    attempts=0
    while True:
        guess = input("Your guess: ").lower()
        attempts += 1

        if guess.lower() == word:
            print("🎉 Correct! You got it in {attempts} attempts.")
            return attempts
        else:
            print(f"❌ Wrong! Try again.")
def play_game():
    rounds = int(input("How many rounds do you want to play? ")
    score = 0
    for _ in range(rounds):
        attempts = play_round()
        score += max(10 - attempts, 1)
    print(f"\n🏆 Game Over! Your final score: {score}")
