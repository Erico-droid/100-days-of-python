#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
totals = nr_letters + nr_numbers + nr_symbols
generated = []
for number in range(totals):
    if (nr_letters > 0):
        let_random = random.randint(0, len(letters) - 1)
        generated.append(letters[let_random])
        nr_letters -= 1

    if (nr_symbols > 0):
        sym_random = random.randint(0, len(symbols) - 1)
        generated.append(symbols[sym_random])
        nr_symbols -= 1

    if (nr_numbers > 0):
        num_random = random.randint(0, len(numbers) - 1)
        generated.append(numbers[num_random])
        nr_numbers -= 1;

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
final_result = ""
for num in range(len(generated)):
    ran = random.randint(0, len(generated) - 1)
    final_result += generated[ran]
    generated.pop(ran)
print(final_result)

