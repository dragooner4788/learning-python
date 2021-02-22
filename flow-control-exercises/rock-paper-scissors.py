import random
import sys

weclome_message = '''
Welcome to the Rock, Paper, Scissors game! 

How it works:

You will choose either:
1. Rock
2. Paper
3. Scissors

Rules:

* ROCK beats SCISSORS
* SCISSORS beats PAPER
* PAPER beats ROCK

The computer will then take a move and choose it's choice. 

If your choice beats the computer, you win. Else the computer wins. If you both choose the same item it is a tie.

The program will continue to run unil you choose to quit.

Best of luck!
'''

print(weclome_message)

wins = 0
losses = 0
ties = 0

while True:  # main game loop | keeps a user in the game until they press q
    print(f"{wins} Wins, {losses} Losses, {ties} Ties.")
    while True:  # player input loop | we use this to ensure we get player input
        print("Enter your move: (r)ock, (p)aper, (s)cissors, (q)uit.")
        player_move = input("Your choice>")
        if player_move.lower() == 'q' or player_move == 'quit':
            sys.exit()
        if player_move.lower() == 'r' or player_move.lower() == 'rock' or player_move.lower() == 'p' or player_move.lower() == 'paper' or player_move.lower() == 's' or player_move.lower() == 'scissors':
            break  # break out of player input loop

    if player_move == 'r' or player_move == 'rock':
        print("ROCK versus...")
        player_move = 'r'  # convert to single letter
    elif player_move == 'p' or player_move == 'paper':
        print("PAPER versus...")
        player_move = 'p'  # convert to single letter
    elif player_move == 's' or player_move == 'scissors':
        print("SCISSORS versus...")
        player_move = 's'  # convert to single letter

    # Computer Choice
    computer_choice = random.randint(1, 3)

    if computer_choice == 1:
        computer_move = 'r'
        print("ROCK")
    elif computer_choice == 2:
        computer_move = 'p'
        print("PAPER")
    elif computer_choice == 3:
        computer_move = 's'
        print("SCISSORS")

    # Record wins, losses, ties
    if player_move == computer_move:
        print("It's a TIE!")
        ties += 1
    elif player_move == 'r' and computer_move == 's':
        print("Player wins! Rock beats scissors.")
        wins += 1
    elif player_move == 'r' and computer_move == 'p':
        print("Player loses. Paper beats scissors.")
        losses += 1
    elif player_move == 'p' and computer_move == 'r':
        print("Player wins! Paper beats Rock.")
        wins += 1
    elif player_move == 'p' and computer_move == 's':
        print("Player loses. Scissors beats Paper.")
        losses += 1
    elif player_move == 's' and computer_move == 'p':
        print("Player wins! Scissors beats Paper.")
        wins += 1
    elif player_move == 's' and computer_move == 'r':
        print("Player loses. Rock beats Scissors")
        losses += 1
