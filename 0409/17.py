
a = input().split()
a = set(a)
for i in a:
    if a.count(i) == 1:
        print(i)
