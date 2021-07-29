#Mit split kann man eine Liste erstellen aus Eingaben
student_heigths = input("List of student height in cm: ").split()
for n in range(0, len(student_heigths)):
  student_heigths[n] = int(student_heigths[n])
print(student_heigths)

av_heigth = 0
for i in student_heigths:
  av_heigth = av_heigth + i

av_heigth = round(av_heigth/len(student_heigths))
print(av_heigth)
  