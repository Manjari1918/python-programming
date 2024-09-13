import random

options = ("rock","paper","scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options: 
     player = input("enter a choice: ")
     
    print(f"Player:{player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("it is a tie!!")
    elif player == "rock" and computer == "scissors":
        print("you win!!")
    elif player == "paper" and computer == "rock":
        print("you win!!")
    elif player == "scissors" and computer == "paper":
        print("you win!!")
    else:
        print("you lose!")
    Play_again = input("Play again? (y/n): ").lower()
    if not Play_again == "y": 
         running = False
    print("thanks for playing!")
     
