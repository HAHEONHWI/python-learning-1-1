# 2번

data = ["A", "B", "A", "C", "B", "D", "A"]
result = []

for i in data:
    if not(i in result):
        result.append(i)
print(result)