people = int(input())
for i in range(people):
    student_dict = {}
    name, score = input().split()
    score = int(score)
    student_dict[name] = score
    if score >= 60:
        print(f"{name} 합격")
    else:
        print(f"{name} 불합격")