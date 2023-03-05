import os
from day9_blind_auction_art import logo

print(logo)

auction_bids = {}

def enter_bid(bidder_name, bid_value):
    auction_bids[bidder_name] = bid_value
    
def winner_bid():
    winner = ""
    winning_bid = 0
    for key in auction_bids:
        if auction_bids[key] > winning_bid:
            winner = key
            winning_bid = auction_bids[key]
    
    print(f"The winner is {winner} with a bid of $ {bid}")

another_bidder = True

while (another_bidder):
    print("Welcome to the secret auction program.")
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    enter_bid(bidder_name=name, bid_value=bid)

    new_bidder = input("Are there any other bidders? Type 'yes' or 'no'.")

    if (new_bidder == "no"):
        os.system('clear')
        winner_bid()
        another_bidder = False
    else:
        os.system('clear')


