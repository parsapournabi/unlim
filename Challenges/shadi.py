n = int(input())
a = list(map(int, input().split()))

ans = 1
answers = {1}

for i in range(n):
    if i == 0:
        continue
    if a[i] > a[i - 1]:
        ans += 1
        if i == n - 1:
            answers.add(ans)
        continue
    answers.add(ans)
    ans = 1
print(max(answers))
