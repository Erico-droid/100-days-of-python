def is_leap(year):
  if year % 4 == 0:
    if year % 100 == 0:
      if year % 400 == 0:
        return ("Leap year.")
      else:
        return ("Not leap year.")
    else:
      return ("Leap year.")
  else:
    return ("Not leap year.")

def days_in_month(month, year):
  month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  
  leap = is_leap(month)
  for days in range(len(month_days)):
    if year == days + 1:
      if (leap == "Leap year." and  month_days[days] == 28):
        return 29
      else:
        return month_days[days]
  
  
#🚨 Do NOT change any of the code below 
year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)












