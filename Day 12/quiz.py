from art import art
import random
#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
print(art)
print("Welcome to the number guessing game \nI'm thinking of a number between 1 and 100.")
difficulty = input("choose the difficulty, easy or hard: ")

attempts = 0
if (difficulty == "easy"):
    attempts = 10
else:
    attempts = 5
 
def playGame():
    correct_number = random.randint(1, 100)
    global attempts 
    while attempts > 0:
        print(f"You have {attempts} remaining attempts to guess the number.")
        guess = int(input("Make a guess: "))
        if guess > correct_number:
            if attempts > 1:
                print("Too high.\nGuess again.")
            else:
                print("Too high.")
        elif guess < correct_number:
            if attempts > 1:
                print("Too low.\nGuess again.")
            else:
                print("Too low.")
        else:
            print(f"You got it! The answer was {correct_number}")
            return False

        if attempts <= 1:
            print(f"You are out of attempts. The correct answer was {correct_number}. You lose.")
            return False
        attempts -= 1

playGame()