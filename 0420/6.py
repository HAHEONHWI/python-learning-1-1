def add(*paras):
    print(paras)
    total = 0
    for para in paras:
        total += para
    return total

print(add(10))
print(add(10, 100))
print(add(10, 100, 1000))