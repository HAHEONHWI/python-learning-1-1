#5번문제

point = 0
for i in range(1, 201, 1):
    if i%28 == 0:
        pass
    elif i%4 == 0:
        point = point+4
    elif i%7 == 0:
        point = point+7
    else:
        pass
print('총 에코 포인트 : ', point)