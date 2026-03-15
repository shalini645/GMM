import random

number = random.randint(1, 50)
attempts = 5

print("🎮 Guess the number between 1 and 50")
print("You have 5 attempts!")

while attempts > 0:
    guess = int(input("Enter your guess: "))
    
    if guess == number:
        print("🎉 You guessed it right!")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")

    attempts -= 1
    print("Attempts left:", attempts)

if attempts == 0:
    print("❌ Game Over! The number was:", number)