from os import system
from random import choice
from day14_higherlower_art import logo, vs

# TODO generate a list on another file with the persons
from day14_higherlower_data import data

# TODO function to get record
def get_account(y=-1):
    """Get a random account different from y (optional)"""
    x = choice(data)
    while (x == y):
        x = choice(data)
    return x

def format_data(account):
    """Format the account data into a printable format."""
    return f"{account['name']}, a {account['description']}, from {account['country']}"

# TODO function to print the persons it wants to compare
def print_info(account_a, account_b):
    """Print the information from the accounts in a formated setting."""
    print(f"Compare A: {format_data(account_a)}.")
    print(vs)
    print(f"Against B: {format_data(account_b)}.")
 
# TODO function to compare and return the higher   
def compare(guess, account_a, account_b):
    """Takes tue user guess and the accounts and returns if they got it right"""
    if (account_a['follower_count'] > account_b['follower_count']):
        return guess == "A"
    else:
        return guess == "B"

# TODO make a function to run the game
def game():
    """Starts the game"""
    score = 0
    game_stop = False
    account_a = get_account()
    
    # TODO make it loop while guess is right
    while (not game_stop):
        system('clear')
        print(logo)
        account_b = get_account(account_a)
        
        if score > 0:
            print(f"You're right! Current score: {score}.")
    
        # TODO print the records to the screen
        print_info(account_a, account_b)
        
        # TODO ask player input and check if they got it right
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if (compare(guess, account_a, account_b)):
            # TODO when the player guess it right, update score
            score += 1
            
            # TODO if guess == 'B' , shift the account to 'A'
            if (guess == "B"):
                account_a = account_b
            
        else:
            # TODO when the player get it wrong, exit the loop and print the result
            game_stop = True
            system('clear')
            print(logo)
            print(f"Sorry, that's wrong. Final score: {score}")
            
            # TODO ask if he wants to play the game again
            play_again = input("Would you like to play another game? Type 'Y' or 'N': ").upper()
            if (play_again == "Y"):
                game()
            
game()