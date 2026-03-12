import random

print("🎮 Welcome to Rock Paper Scissors Game")

choices = ["rock", "paper", "scissors"]

# User choice
user = input("Enter rock, paper, or scissors: ").lower()

# Computer choice
computer = random.choice(choices)

print("Computer chose:", computer)

# Game logic
if user == computer:
    print("It's a tie!")

elif user == "rock" and computer == "scissors":
    print("🎉 You win!")

elif user == "paper" and computer == "rock":
    print("🎉 You win!")

elif user == "scissors" and computer == "paper":
    print("🎉 You win!")

elif user in choices:
    print("😢 You lose!")

else:
    print("Invalid input! Please choose rock, paper, or scissors.")