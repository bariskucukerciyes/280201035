grade_list = []

num_student = int(input("Enter number of students: "))
for i in range(num_student) :
  print("Student ",i+1 )
  mid1 = int(input("Midterm 1: " ))
  mid2 = int(input("Midterm 2: " ))
  final = int(input("Final: " ))
  grade_list.append([mid1,mid2,final])
print(grade_list)

avg_grades = []

for grade in grade_list:
  avg_grades.append( grade[0]*0.3 + grade[1]*0.3 + grade[2]*0.4 )
print(avg_grades)
  
  


