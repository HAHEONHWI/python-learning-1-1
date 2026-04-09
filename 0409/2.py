list = input().split()
even = []
odd = []
for i in list:
    if int(i) % 2 == 0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)