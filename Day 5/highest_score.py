# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maxNum = 0
for score in student_scores:
    if (score > maxNum):
       maxNum = score

print(f"The Highest Score is {maxNum}")
# 
# [78, 65, 89, 86, 55, 91, 64, 89]