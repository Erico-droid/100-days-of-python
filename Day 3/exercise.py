year = int(input("which year do you want to enter? "))
leap_year = False
if year % 4 == 0:
    leap_year = True
    if year % 100 == 0:
        leap_year = False
        if year % 400 == 0:
            leap_year = True
        
print(f"{year} is a leap year? {leap_year}")