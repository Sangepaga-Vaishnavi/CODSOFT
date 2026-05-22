import random

print("====================================")
print("   ROCK PAPER SCISSORS GAME ✊📄✂️")
print("====================================")

choices = ["rock", "paper", "scissors"]

user = input("Enter rock, paper, or scissors: ").lower()

computer = random.choice(choices)

print("\nYou chose:", user)
print("Computer chose:", computer)

if user == computer:
    print("\nIt's a Tie 🤝")

elif (
    (user == "rock" and computer == "scissors") or
    (user == "paper" and computer == "rock") or
    (user == "scissors" and computer == "paper")
):
    print("\nYou Win 🎉")

elif user in choices:
    print("\nComputer Wins 😎")

else:
    print("\nInvalid Input ❌")

print("====================================")
print("      Thanks for Playing ❤️")
print("====================================")