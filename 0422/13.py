s = 0
def f(n):
    global s
    k = 0
    while k<n:
        k += 1
        s += k
    return s
f(3)

print(s)