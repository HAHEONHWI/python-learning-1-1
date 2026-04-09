
words = input().split()
print("리스트:", words)
print("튜플:", tuple(words))
print("세트:", set(words))
word_dict = {word: len(word) for word in words}
print("딕셔너리:", word_dict)