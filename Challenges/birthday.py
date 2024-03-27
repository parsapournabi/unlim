m, n = list(map(int, input().split()))
b, a = list(map(int, input().split()))

months = [list(range(31)) for _ in range(6)] + [list(range(30)) for _ in range(5)] + [list(range(29)) for _ in
                                                                                      range(1)]

days = 0

idx = m - 1

while True:
    if m == b and n == a:
        print(0)
        break

    if idx >= len(months):
        idx = 0
    for day in months[idx]:
        if idx == b - 1 and day == a - 1:
            if (ret := days - n) < 0:
                print(365 + ret + 1)
            else:
                print(days - n + 1)
            exit()
        days += 1
    idx += 1
