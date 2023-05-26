import random;
from game_data import data;
from art import logo, vs;
import os


def print_art():
    print(logo)

final_score = 0

print(data[0]["name"])

def get_correct_data(random1, random2):
    name1 = data[random1]["name"]
    description1 = data[random1]["description"]
    country1 = data[random1]["country"]
    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(vs)
    name2 = data[random2]["name"]
    description2 = data[random2]["description"]
    country2 = data[random2]["country"]
    print(f"Compare B: {name2}, a {description2}, from {country2}.")

    if data[random1]["follower_count"] > data[random2]["follower_count"]:
        return "A";
    else:
        return "B"

def handle_loss():
    print_art()
    print(f"You lost the game. Your final score is {final_score}.")

# Clear console command based on the operating system
clear_command = "cls" if os.name == "nt" else "clear"
# Function to clear the console
def clear_console():
    os.system(clear_command)

def game():
    failed = False
    global final_score
    first_time = True
    while not failed:
        print_art()
        if not first_time:
            print(f"You are right! Current score is {final_score}")
        random1 = random.randint(0, len(data) - 1)
        random2 = random.randint(0, len(data) - 1)
        correct_answer = get_correct_data(random1, random2).lower()
        answer = input("Who has more followers? Type 'A' or 'B': ").lower()
        if correct_answer == answer:
            first_time = False
            final_score += 1;
        else:
            failed = True
        clear_console()
    handle_loss();

game()