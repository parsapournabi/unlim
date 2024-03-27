g, y, r = list(map(int, input().split()))
n = int(input())

times = (list(range(g)), 'green'), (list(range(g, g + y)), 'yellow'), (list(range(g + y, g + y + r)), 'red')
length = len(list(range(g)) + list(range(g, g + y)) + list(range(g + y, g + y + r)))

ans = 'green'
cnt = 0

if n > length:
    if n % length == 0:
        n = length
    else:
        n = n % length
while True:
    for tme, color in times:
        for t in tme:
            if cnt == n - 1:
                ans = color
                print(ans)
                exit()
            cnt += 1
