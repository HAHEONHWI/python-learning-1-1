text = input().split()

for word in text:
	dup = set()

	for ch in word:
		if word.count(ch) > 1:
			dup.add(ch)

	print(dup)
