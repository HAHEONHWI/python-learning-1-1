#여러 단어를 입력받아 길이를 key로 하고 그 길이를 가진 단어들의 리스트를 value로 하는 딕셔너리를 만들어 출력하기
words = input("단어들을 입력하세요: ").split()
length_dict = {}
for word in words:
    length = len(word)
    if length in length_dict:
        length_dict[length].append(word)
    else:
        length_dict[length] = [word]
print(length_dict)