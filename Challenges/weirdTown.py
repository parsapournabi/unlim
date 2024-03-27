n = int(input())
ni = list(map(int, input().split()))

ans = 0

for i in range(n):
    if ni.count(ni[i]) > 1:
        while True:
            if not ni.count(ni[i]) > 1:
                break
            ans += 1
            ni[i] += 1
print(ans)
