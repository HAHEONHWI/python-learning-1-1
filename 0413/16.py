sentence = input()
words = sentence.split()

if len(words) == 0:
	print("")
else:
	longest = words[0]

	for w in words:
		if len(w) > len(longest):
			longest = w

	print(longest)
