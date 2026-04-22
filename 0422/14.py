def f(n):
    s = 0
    for k in range(1, n+1):
        s += k
    return s

n = int(input())
print(f(n))