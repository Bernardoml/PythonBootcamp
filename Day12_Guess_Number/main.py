from random import randint
from os import system

system('clear')

EASY_DIFFICULTY_ATTEMPTS = 10
HARD_DIFFICULTY_ATTEMPTS = 5

def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == 'easy':
        return EASY_DIFFICULTY_ATTEMPTS
    else:
        return HARD_DIFFICULTY_ATTEMPTS
    
def check_answer(guess, num, attempts):
    """Checks guess against the number. Returns the number of attempts remanining."""
    if (guess > num):
        print("Too high.")
        return attempts - 1
    elif (guess < num):
        print("Too low.")
        return attempts - 1
    else:
        print(f"You have correctly guesset the number {num}. Congratulations!")

def guess_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = randint(1, 100)
    print(f"Psst, the number is {num}")
    
    attempts = set_difficulty()
    guess = 0
                   
    while (guess != num and attempts > 0):
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        
        attempts = check_answer(guess, num, attempts)
            
        if attempts == 0:
            print("You've run out of guesses, you lose.")
            print(f"The number was {num}")
            
    restart = input("Would you like to play another game? Type 'y' or 'n': ")
    if (restart == "y"):
        system('clear')
        guess_game()
        
guess_game()