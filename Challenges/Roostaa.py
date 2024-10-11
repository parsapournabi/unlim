n, c = list(map(int, input().split()))
m = [int(input()) for _ in range(n)]
ans = 0
plus = 0

for city in sorted(m):
    plus += city
    if plus > c:
        break
    ans += 1
print(ans)
