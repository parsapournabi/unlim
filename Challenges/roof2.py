n, m = map(int, input().split())
a = []
ans = ['-1'] * (n * m)
ans_idx = []
for _ in range(n):
    A = list(map(int, input().split()))
    a.extend(A)

for i, aa in enumerate(a):
    if i == len(a) - 1:
        continue
    ans_idx.append((i, aa))
    while ans_idx and a[i + 1] > ans_idx[len(ans_idx) - 1][1]:
        ans[ans_idx[len(ans_idx) - 1][0]] = str(a[i + 1])
        ans_idx.pop()

print(' '.join(ans))
