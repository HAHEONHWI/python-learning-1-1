age = int(input('나이입력'))
cost = 14000
if age >= 60:
    cost = cost*0.7
elif age >= 10:
    cost = cost*0.8
else:
    pass
print('찜질방 이용료 : ', cost)