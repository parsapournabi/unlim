n = int(input())
ans = 0

for i in range(n):
    count = input().split()
    matrix = sum(list(map(int, count)))
    if matrix == 2:
        ans += 1
print(ans)