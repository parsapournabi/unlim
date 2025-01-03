nums = int(input())
n = input()

ans = ''
for i in range(nums):
    if i == 0:
        ans += n[i]
        continue
    if ans[-1] == n[i]:
        continue
    ans += n[i]
print(ans)
