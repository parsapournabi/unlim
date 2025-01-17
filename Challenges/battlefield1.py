n, m = tuple(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(n)]

squares = []
for i in range(n):
    row = [(board[i][j], i, j) for j in range(m)]
    row.sort()
    squares += row[-3:]

squares = sorted(squares, reverse=True)
mx = -float("inf")

for a, x1, y1 in squares[:9]:
    for b, x2, y2 in squares:
        if x1 == x2 or y1 == y2:
            continue
        for c, x3, y3 in squares:
            if x3 in {x1, x2} or y3 in {y1, y2}:
                continue
            mx = max(mx, a + b + c)
            break
print(mx)
