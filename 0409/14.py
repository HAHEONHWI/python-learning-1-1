
sentence1 = input()
sentence2 = input()
set1 = set(sentence1.split())
set2 = set(sentence2.split())
common_words = set1 & set2
print(common_words)  