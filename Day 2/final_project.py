print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? "))
tip = int(input("What percantage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people are splitting the bill? "))

print(f"Each person should pay {round((bill + bill * tip/100)/people, 2)}")
