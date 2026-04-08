import random as r

a = list(map(int, input().split()))
b = [r.randint(1, 6), r.randint(1, 6)]

print(f'com : {b} user : {a}')

if a[0] == b[0] or a[0] == b[1]:
    if a[1] == b[0] or a[1] == b[1]:
        print('1등')
    else:
        print('2등')
elif a[1] == b[0] or a[1] == b[1]:
    if a[0] == b[0] or a[0] == b[1]:
        print('2등')
else:
    print('3등')