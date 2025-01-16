n, m = list(map(int, input().split()))
t = list(map(int, input().split()))

dp = [n + 1] * (n + 1)
dp[0] = 0

for i in range(1, n + 1):
    for tt in t:
        if i - tt < 0:
            continue
        dp[i] = min(dp[i], 1 + dp[i - tt])
print(dp[n] if dp[n] != n + 1 else "failed")
