def print_star(n):
    if n == 1:
        print('*')
        return
    print('*'*n)
    print_star(n-1)

print_star(int(input()))