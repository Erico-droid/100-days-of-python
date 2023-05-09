print("welcome to the python pizza deliveries")
size = input("What size of pizza do you want? S, M or L: ")
add_pepperoni= input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0;
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if bill == 15:
        bill += 2
    if bill == 20 or bill == 25:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: {bill}")


