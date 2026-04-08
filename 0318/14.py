kind = input('승객 유형 입력 [임산부, 노약자, 일반] \n ==')
if kind == '임산부' or '노인':
    print('이용가능')
else:
    print('이용불가능')