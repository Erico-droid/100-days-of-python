student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for score in student_scores:
    if student_scores[score] > 91:
        grade = "Outstanding"
    elif student_scores[score] > 80 and student_scores[score] < 91:
        grade = "Exceeds expectations"
    elif student_scores[score] > 70 and student_scores[score] < 81:
        grade = "Acceptable"
    else:
        grade = "Fail"
    
    student_grades[score] = grade
    

# 🚨 Don't change the code below 👇
print(student_grades)





