sen = input()
result = 0
for i in range(len(sen)):
    if sen[i] in "aeiouAEIOU":
        result += 1
print('모음개수:', result   )