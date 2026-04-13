nums = list(map(int, input().split()))

result = []
for n in nums:
	if n not in result:
		result.append(n)

result.sort()
print(result)
