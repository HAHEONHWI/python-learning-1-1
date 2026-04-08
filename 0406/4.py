seats = [
    ("김민준",(1,1)),
    ("이서연",(1,2)),
    ("박지후",(1,1)),
    ("최하은",(2,1))
]

result = {}

for name, sit in seats:
    if sit not in result:
        result[sit] = []
    result[sit].append(name)

print(result)

for sit, names in result.items():
    if len(names) >= 2:
        print(names, sit)