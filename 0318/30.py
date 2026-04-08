num = int(input('수입력:'))
odd = 0
even = 0
for i in range (1, num+1):
    if i%2 == 0:
        even += i
    else:
        odd += i
print('1부터', num, '까지의 홀수 합은 ', odd)
print('1부터', num, '까지의 짝수 합은 ', even)