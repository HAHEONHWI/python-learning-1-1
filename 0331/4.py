a = int(input())
for i in range(a):
    print(' '*(a-i), end='')
    print('*', end='')
    print('*'*i*2)