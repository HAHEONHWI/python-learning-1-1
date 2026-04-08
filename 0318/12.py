use = int(input('전기사용량 입력'))
base = 270

if use>100:
    cost = (use*base)*1.2
else:
    cost = use*base
print('전기 사용량', use, 'KW')
print('전기 요금 : ', cost, '원')