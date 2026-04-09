#두 문장에서 공통단어 빈도수 구하기, 각 단어의 빈도수는 딕셔너리로 저장하기, 대소문자 구분 안함
sentence1 = input().lower()
sentence2 = input().lower()
set1 = set(sentence1.split())
set2 = set(sentence2.split())
common_words = set1 & set2
frequency_dict = {}
for word in common_words:
    frequency_dict[word] = sentence1.split().count(word) + sentence2.split().count(word)
print(frequency_dict)