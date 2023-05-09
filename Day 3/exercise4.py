# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

concat_names = name1 + name2

string = "True Love" 
count = 0
score = 0
while count < len(string):
    number = concat_names.lower().count(string[count])
    score += number
    if count < 5:
        first = str(score)
        print(first + " " + concat_names[count] + " " + string[count])
    if count == 5:
        score = 0
    if count > 5:
        second = str(score)
    count += 1

score = first + second
print(score)

# wrong sln