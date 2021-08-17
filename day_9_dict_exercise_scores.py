student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

for key, value in student_scores.items():
  if value <=100 and value >= 91:
    student_grades[key] = "Outstanding"
  elif value < 91 and value >=81:
    student_grades[key] = "Exceeds Expectations"
  elif value < 81 and value >= 71:
    student_grades[key] = "Acceptable"
  elif value < 71:
    student_grades[key] = "Fail"

print(student_grades)



