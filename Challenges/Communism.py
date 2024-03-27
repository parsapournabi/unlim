n, x = list(map(int, input().split()))
A = list(map(int, input().split()))

ans = 0

for i in range(n - 1):
    if not A[i] + A[i + 1] > x:
        continue
    if A[i] > x:
        ans += A[i] - x
        A[i] -= A[i] - x
    if A[i + 1] > x:
        ans += A[i + 1] - x
        A[i + 1] -= A[i + 1] - x
    if A[i] + A[i + 1] > x:
        if A[i] > A[i + 1]:
            ans += A[i] + A[i + 1] - x
            A[i] -= A[i] + A[i + 1] - x
        elif A[i + 1] > A[i]:
            ans += A[i] + A[i + 1] - x
            A[i + 1] -= A[i] + A[i + 1] - x
        else:
            ans += A[i] + A[i + 1] - x
            A[i + 1] -= A[i] + A[i + 1] - x

print(ans)
