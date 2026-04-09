a = input().split()
a = set(a)

longest = ""
for i in a:
    if len(i) > len(longest):
        longest = i
print(longest)