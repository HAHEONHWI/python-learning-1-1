#학생 수를 입력받아 딕셔너리에 이름=점수 저장한 후 최고 점수와 학생 이름을 출력하라
people = int(input("학생 수: "))
student_dict = {}
for i in range(people):
    name, score = input("이름과 점수: ").split()
    score = int(score)
    student_dict[name] = score
max_score = max(student_dict.values())
top_students = [name for name, score in student_dict.items() if score == max_score]
print(max_score, top_students)
