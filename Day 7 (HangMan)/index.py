import random
import os

def generate_random_word():
    words = ["apple", "banana", "cat", "dog", "elephant", "fish", "guitar", "house", "igloo", "jungle", "kangaroo", "lemon", "monkey", "noodle", "ocean", "piano", "queen", "rabbit", "sun", "tiger"]
    rand = random.randint(0, len(words) - 1);
    word = words[rand]    
    return word

def print_hangman_ascii_art():
    print (
        """
             _   _                                              
            | | | |                                             
            | |_| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
            | __| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
            | |_| | | | (_| | | | | (_| | | | | | | (_| | | | |
            \__|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                    __/ |                      
                                    |___/                       

        """
    )

def handle_ascii_hangman(num):
    zero = """
            +---+
            |   |
                |
                |
                |
                |
            =======
    """

    one = """
            +---+
            |   |
            O   |
                |
                |
                |
            =======
    """

    two = """
        +---+
        |   |
        O   |
        |   |
            |
            |
         =======
    """

    three = """
            +---+
            |   |
            O   |
           /|   |
                |
                |
            =======    
    """

    four = """
        +---+
        |   |
        O   |
       /|\  |
            |
            |
        =======
    """

    five = """
        +---+
        |   |
        O   |
       /|\  |
       /    |
            |
        ======= 
    """

    six = """
        +---+
        |   |
        O   |
       /|\  |
       / \  |
            |
        =======
    """
    ascii_array = [zero, one, two, three, four, five, six];
    return ascii_array[num];

# Clear console command based on the operating system
clear_command = "cls" if os.name == "nt" else "clear"
# Function to clear the console
def clear_console():
    os.system(clear_command)


arr = []
def generate_dummy_word_display(array, found_words):
    for letter in array:
        if (len(found_words) <= 0):
            arr.append("_")
        else:
            for found_word in found_words:
                if letter == found_word:
                    indexes = [index for index, letter in enumerate(array) if letter == found_word]
                    
                    if (len(indexes) > 1):
                        for index in indexes:
                            arr[index] = found_word
                    elif (len(indexes) == 1):
                        arr[indexes[0]] = found_word
                else:
                    pass

    print(" ".join(map(str, arr)))

def ending_remarks(win, word):
    if (win):
        print(f"The word was {word}, You won the game!")
    else:
        print(f"The word was {word},Try again next time!")
    

def hangman():
    print_hangman_ascii_art()
    word = generate_random_word()
    print(word)
    print("------ Hello and welcome to the hangman game ------")
    word = list(word)
    gameOver = False
    win = False
    initial_chance = 0
    found = []
    while (not gameOver):
        print (initial_chance)
        init_found = len(found)
        print(
            handle_ascii_hangman(initial_chance)
        )
        generate_dummy_word_display(word, found)
        letter = input("\nEnter the letter that you have guessed: ")
        for rand_letter in word:
            if rand_letter == letter:
                found.append(letter)

        if (len(found) == init_found):
            initial_chance += 1

        if (initial_chance == 7):
            win = False
            gameOver = True
        
        if (''.join(found) == ''.join(word)):
            win = True
            gameOver = True
            print(win)

        # clear_console()
    
    ending_remarks(win, ''.join(word))


hangman()