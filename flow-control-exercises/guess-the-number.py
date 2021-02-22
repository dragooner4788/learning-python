import random

welcome_message = '''
Welcome to \'Guess the Number\' game!

You will be attempting to guess a number between 1 and 20. 

You have 6 guesses before the game ends.
'''

print(welcome_message)

secret_number = random.randint(1,20)

for guessesTaken in range(1,7):
    guess = int(input("Take a guess> "))

    if guess < secret_number:
        print(f"{guess} is too low! Try again.")
    elif guess > secret_number:
        print(f"{guess} is too high! Try again.")
    else:
        break

if guess == secret_number:
    print(f"That's right! The secret number was {secret_number}. You got this in {guessesTaken} attempts!")

else:
    print(f"You have guessed {guessesTaken} times and have not gotten the secret number. The secret number was {secret_number}")

