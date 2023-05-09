# find the body mass index of an individual using python

weight = int(input("What is your weight in kgs? "))
height = float(input("What is your height in metres? "))

bmi = weight / height ** 2
if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5  and bmi < 25:
    print("You have a normal weight")
elif bmi > 25 and bmi < 30:
    print("You are overweight.")
elif bmi > 30 and bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")
    