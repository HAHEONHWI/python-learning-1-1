n = int(input())
count = 0

for i in range(1, n + 1):
	if n % i == 0:
		count += 1

if count == 2:
	print("소수입니다")
else:
	print("소수가 아닙니다")
