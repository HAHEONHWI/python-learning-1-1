def hanoi(n, start, end, temp):
    if n == 1:
        print(f"{start} -> {end}")
        return

    hanoi(n - 1, start, temp, end)
    print(f"{start} -> {end}")
    hanoi(n - 1, temp, end, start)

