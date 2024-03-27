n = int(input())

foods = ['pizza', 'burger', 'fries potato', 'hotdog']

idx = 0
cnt = 0
ans = []

for i in range(n):
    if cnt >= len(foods):
        idx = 0
        cnt = 0
    ans.append(foods[idx])
    cnt += 1
    idx += 1
print('\n'.join(ans))
