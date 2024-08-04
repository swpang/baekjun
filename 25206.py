grades = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

lines = []
for i in range(20):
    lines.append(input().split(' '))

num_courses = 0
total_grades = 0.0
for course in lines:
    if course[2] == 'P':
        continue
    else:
        total_grades += grades[course[2]] * float(course[1])
        num_courses += float(course[1])

print(total_grades / num_courses)