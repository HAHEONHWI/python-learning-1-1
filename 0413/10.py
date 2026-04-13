n = int(input())

students = []
total = 0

for _ in range(n):
	name, score = input().split()
	score = int(score)
	students.append([name, score])
	total += score

avg = total / n

for student in students:
	if student[1] >= avg:
		print(student[0], "---", student[1])
