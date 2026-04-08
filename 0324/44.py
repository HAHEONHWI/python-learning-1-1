a = int(input('행 수 | '))
b = int(input('열 수 | '))

for i in range(1, a + 1):
    for j in range(1, b + 1):
        print(i * j, end=" ")
    print()