word = input()
reverse_word = ""

for ch in word:
	reverse_word = ch + reverse_word

if word == reverse_word:
	print("회문입니다")
else:
	print("회문이 아닙니다")
