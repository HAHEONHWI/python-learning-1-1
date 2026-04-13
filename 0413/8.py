a = int(input())
score = 0
pas = 0
for i in range(1, a + 1):
    score += int(input())
    if score >= 80:
        pas += 1
    else:
        pass
print('합격자 수 ', pas-1)
print(score/a)