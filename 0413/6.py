pw = input()
for ch in pw:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        has_english = True
        break
if len(pw) >= 8:
    if has_english == True:
        if (1, 2, 3, 4, 5, 6, 7, 8, 9 ,0) in pw:
            print('사용 가능')
        else:
            print('사용 불가능')
    else:
        print('사용 불가능')
else:
    print('사용 불가능')