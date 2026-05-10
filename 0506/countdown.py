
def countdown(n):
    if n == 0:
        print("발사!")
        return
    print(n)
    n -= 1
    countdown(n)
countdown(int(input()))