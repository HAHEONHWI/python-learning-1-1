

num_students = int(input("학생 수: ")) 
grades = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
for _ in range(num_students):
    name, score = input("이름과 점수: ").split()
    score = int(score)
    if score >= 90:
        grades['A'] += 1
    elif score >= 80:
        grades['B'] += 1
    elif score >= 70:
        grades['C'] += 1
    else:
        grades['D'] += 1
print(grades)