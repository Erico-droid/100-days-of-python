import random;

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___) 
'''

#Write your code below this line 👇
ls = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for rock, type 1 for paper, type 2 for scissors: "))
computer_choice = random.randint(0,2)
if (choice > 2 or choice < 0):
    print("You typed an invalid number")
else:
    print(f"Your choice: \n {ls[choice]}")
    print(f"Computer's choice: \n {ls[computer_choice]}")

    if (computer_choice == choice):
        print("It's a draw")
    if (choice == 0 and computer_choice == 2):
        print("You win!")
    if (choice == 2 and computer_choice == 0):
        print("You lose!")
    if (choice == 2 and computer_choice == 1):
        print("you win!")
    if (choice == 1 and computer_choice == 2):
        print("you lose!")
    if (choice == 1 and computer_choice == 0):
        print("you win!")
    if (choice == 0 and computer_choice == 1):
        print("you lose!")
        
