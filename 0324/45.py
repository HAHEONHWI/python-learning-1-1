a = int(input('수 입력 : '))
x = 1
for i in range (1, a+1, 2):
    if i%2 == 0:
        print(' '*(a-i+1), '*'*(x))
else:
    print(' '*(a-i), '*'*(x))
    x += 2
