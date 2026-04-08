import random as r
print('컴퓨터를 이겨라 가위바위보')
me = input('나의 선택 가위바위보 : ')
list = ['가위', '바위', '보']
com = r.choice(list)

print('컴퓨터의 선택 :', com)
if me == '가위':
    if com == '가위':
        print('비김')
    elif com == '바위':
        print('짐')
    elif com == ('보'):
        print('이김')
elif me == '바위':
    if com == '가위':
        print('이김')
    elif com == '바위':
        print('비김')
    elif com == ('보'):
        print('짐')
elif me == '보':
    if com == '가위':
        print('짐')
    elif com == '바위':
        print('이김')
    elif com == ('보'):
        print('비김')