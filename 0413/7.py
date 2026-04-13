nums = list(map(int, input().split()))

max_num = nums[0]
min_num = nums[0]

for n in nums[1:]:
	if n > max_num:
		max_num = n
	if n < min_num:
		min_num = n

print("최댓값:", max_num)
print("최솟값:", min_num)
