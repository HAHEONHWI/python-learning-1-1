gas = [10, 7, 8, 6, 15]
all = []

for i in range(len(gas)):
    calc = 50000 + (gas[i] * 3000)
    print(i+1, '호의 관리비는', calc, '원')