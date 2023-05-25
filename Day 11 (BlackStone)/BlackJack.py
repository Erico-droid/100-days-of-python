############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def print_art():
    print(
        """
        .------.            _     _            _    _            _    
        |A_  _ |.          | |   | |          | |  (_)          | |   
        |( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
        | \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
        |  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
        `-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
              |  \/ K|                            _/ |                
              `------'                           |__/       
        
        
        """
    )

def get_initial_random_cards():
    initial_start= 2;
    player_cards = []
    for i in range(initial_start):
        rand = random.randint(0, len(cards) - 1)
        player_cards.append(cards[rand])
    return player_cards

def get_score(ls):
    count = 0
    for i in ls:
        count += i
    if len(ls) == 2 and count == 21:
        return 0
    return count

def append_card(ls):
    rand = random.randint(0, len(cards) - 1);
    ls.append(cards[rand])
    return ls

def determine_result(current_score):
    if current_score > 21:
        return False
    
def show_message(message):
    print(message)

def manage_dealer(dealer_cards):
    if (get_score(dealer_cards) < 17):
        append_card(dealer_cards)
    else: 
        pass

    if (get_score(dealer_cards) > 21):
        return False
    else:
        return True

def compare_players(player, dealer):
    if get_score(player) > get_score(dealer):
        return "You won"
    elif get_score(player) < get_score(dealer):
        return "You lost"
    elif get_score(player) == get_score(dealer):
        return "You had a draw"
    else:
        return "Failure"

firstStart = True
choice = input("welcome to blackjack would you like to begin(y/n)?: ")
if choice.lower() == "y":
    choice = True
else: 
    choice = False


if choice:
    print_art()
    while (choice):
        if firstStart:
            firstStart = False
        else:
            choice = input("\n\nwelcome to blackjack would you like to begin(y/n)?: ")
            if choice.lower() == "y":
                choice = True
            else: 
                choice = False
        
        if choice:
            player = get_initial_random_cards()
            dealer = get_initial_random_cards()
            play = True  
            while play: 
                if (get_score(player) == 0):
                    message = "You just had a blackjack!"
                    show_message(message)
                elif (get_score(dealer) == 0):
                    message = "Dealer just had a blackjack!"
                    show_message(message)
                else:
                    print(f"Your cards: {player}, current score: {get_score(player)} \nComputer's first card: {dealer[0]}")
                    get_card = input("Type 'y' to get another card, type 'n' to pass: ")
                    if get_card == "y":
                        play = True
                        player = append_card(player)
                        print(player)
                        if determine_result(get_score(player)) == False:
                            get_card = "n"
                            message = f"You went over board. You Lost! Your cards are: {player} with score {get_score(player)}. Dealers cards are {dealer} with score {get_score(dealer)}"
                            show_message(message)

                    if get_card == "n":
                        if (manage_dealer(dealer) == False):
                            message = f"You won. Your cards are: {player} with score {get_score(player)}. Dealers cards are {dealer} with score {get_score(dealer)}"
                            show_message(message)
                        elif manage_dealer(dealer) == True:
                            winner = compare_players(player=player, dealer=dealer)
                            message = f"{winner} Your cards are: {player} with score {get_score(player)}. Dealers cards are {dealer} with score {get_score(dealer)}"
                            show_message(message)
                        play = False
        else:
            print("Thank you for an amazing time!")
else:
    print("You quit the program without playin the game.")
            
