import random
import os
from day11_blackjack_art import logo

def draw(list, score, n=1):
    cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    for i in range(n):
        x = random.choice(cards)
        list.append(x)
        if (x == "J" or x == "Q" or x == "K"):
            score.append(10)
        elif (sum(score) > 10 and x == "A"):
            score.append(1)
        elif (x == "A"):
            score.append(11)
        else:
            score.append(x)
            
def print_hand(person):
    if (person == "player"):
        print(f"Your cards: {p_cards} - Total: {sum(p_score)}")
    else:
        print(f"Computer's cards: {c_cards} - Total: {sum(c_score)}")
        
def results():
    print_hand("player")
    print_hand("computer")
    if (sum(p_score) <= 21 and sum(p_score) > sum(c_score)):
        print("You Win. Congratulations!!!")
    else:
        print("You lose. Try Again next time.")

def reset():
    p_cards.clear()
    c_cards.clear()
    p_score.clear()
    c_score.clear()    
        
def black_jack():  
    print(logo)
    draw(p_cards, p_score, 2)
    draw(c_cards, c_score, 2)
        
    if (sum(c_score) == 21):
        print_hand("player")
        print_hand("computer")
        print("The Computer got a Blackjack and have won the game!")
    elif (sum(p_score) == 21):
        print_hand("player")
        print_hand("computer")
        print("You got a Blackjack and have won the game! Congratulations!")
    else:
        print_hand("player")
        print(f"Computer's first card: {c_cards[0]}")
        
        ask_card = True
                
        while (ask_card):
            n_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if (n_card == "y"):
                draw(p_cards, p_score)
                print_hand("player")
                if (sum(p_score) > 21):
                    print("You busted, sorry.")
                    return
            elif (n_card == "n"):
                ask_card = False
                
        while (sum(c_score) < 16):
            draw(c_cards, c_score)
            
        results()
        play_again = input("Would you like to play another game? Type 'y' or 'n': ")

        if (play_again == "y"):
            reset()
            os.system('clear')
            black_jack()
            

p_cards = []
c_cards = []
p_score = []
c_score = []
            
black_jack()