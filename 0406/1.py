student = int(input("학생수: "))
score = []
for i in range(student):
    score.append(int(input()))

print("평균: ", sum(score) / student)
print("총점: ", sum(score))
print("최고점: ", max(score))
print("최저점: ", min(score))  