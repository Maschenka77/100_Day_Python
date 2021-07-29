#Find Maximum of a list without max() function

#Mit split kann man eine Liste erstellen aus Eingaben
student_highscore = input("List of student high-scores: ").split()
for n in range(0, len(student_highscore)):
  student_highscore[n] = int(student_highscore[n])
print(student_highscore)

max_score = student_highscore[0]
for i in student_highscore:
 
 if max_score < i:
   max_score = i


 
print(max_score)
  