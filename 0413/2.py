num = list(map(int, input().split()))
hol = 0
zak = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        zak += num[i]
    else:
        hol += num[i]
print("홀수 합:", hol)
print("짝수 합:", zak)