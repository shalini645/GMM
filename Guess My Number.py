import random

print("🎮 Welcome to Guess My Number Game!")

# Computer chooses a random number
number = random.randint(1, 100)

attempts = 0

while True:
    guess = int(input("Enter your guess (1 - 100): "))
    attempts += 1

    if guess < number:
        print("📉 Too low! Try again.")
    elif guess > number:
        print("📈 Too high! Try again.")
    else:
        print("🎉 Congratulations! You guessed the number.")
        print("✅ The number was:", number)
        print("🔢 Attempts taken:", attempts)
        break