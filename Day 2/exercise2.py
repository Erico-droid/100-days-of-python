age = int(input("What is your current age? "))
threshold = 90

years_to_live = threshold - age

days_to_live = years_to_live * 365

weeks_to_live = years_to_live * 52

months_to_live = years_to_live * 12

print(f"you have {days_to_live} days, {weeks_to_live} weeks and {months_to_live} months to live")
