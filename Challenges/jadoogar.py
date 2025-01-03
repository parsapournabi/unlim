N, L, R = tuple(map(int, input().split()))

pages = list(range(1, N + 1))

print(' '.join(map(str, pages[:L - 1] + pages[L - 1:R][::-1] + pages[R:])))
