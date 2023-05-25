import os

def determine_winner(bidders):
    maxi = 0
    winner = {}
    for bidder in bidders:
        if (bidder["bid"] > maxi):
            winner = bidder
    print(f"Winner {bidder['name']} has won!")


def clear_console():
    os.system('clear')  # For Linux/macOS
    # Alternatively, you can use 'cls' for Windows:
    # os.system('cls')


def private_bid():
    bid_over = False
    bidders = []

    while (not bid_over):
        individual_bid = {}
        name = input("Welcome To the Private auctioneers site! What is your name")
        bid = int(input("What is your bid? $"))
        individual_bid["name"] = name
        individual_bid["bid"] = bid

        line = input("Are there other people on the line to bid? (Y/N): ")
        if (line == "Y"):
            bid_over = False
        else:
            bid_over = True

        bidders.append(individual_bid)
        clear_console()

    
    determine_winner(bidders)
        
private_bid()