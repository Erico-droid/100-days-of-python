# find the body mass index of an individual using python

weight = int(input("What is your weight in kgs? "))
height = float(input("What is your height in metres? "))

bmi = weight / height ** 2
print(int(bmi))