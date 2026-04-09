#영어 리스트 단어들 입력받아 각 단어의 모음 개수를 출력하기
words = input().split() 
vowels = "aeiouAEIOU"
for word in words:
    count = 0
    for char in word:
        if char in vowels:
            count += 1
    print(f"{word}: {count}")  