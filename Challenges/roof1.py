n = int(input())
t = list(map(int, input().split()))

ans = []
for i, tt in enumerate(t):
    for j in t[i+1:]:
        if j > tt:
            ans.append(str(j))
            break
    else:
        ans.append('-1')

print(' '.join(ans))
