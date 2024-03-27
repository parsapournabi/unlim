n, m = list(map(int, input().split()))
gp = [input().split() for _ in range(n)]

def movement(i, y, x):
    """If val: 0 -> moveUp, 1 -> moveDown, 2 -> moveLeft 3 -> moveRight"""
    y, x = y, x

    if i == 0:
        y -= 1
        if y < 0:
            y = 0
    elif i == 1:
        y += 1
        if y > n - 1:
            y = n - 1
    elif i == 2:
        x -= 1
        if x < 0:
            x = 0
    elif i == 3:
        x += 1
        if x > m - 1:
            x = m - 1
    return y, x

mdays = (n * m) - 1
days = 0
positions = []
ans = []

for d in range(mdays):
    if [g for g in gp if 'H' in g] == []:
        print(days)
        break
    for y in range(n):
        for x in range(m):
            if 'C' == gp[y][x]:
                for i in range(4):
                    yy, xx = movement(i, y, x)
                    if 'E' not in gp[yy][xx]:
                        positions.append((yy, xx))

    for (py, xy) in positions:
        gp[py][xy] = 'C'
    days += 1
else:
    print('not bad')
