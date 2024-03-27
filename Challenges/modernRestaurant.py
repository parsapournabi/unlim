n = int(input())

foods = ['burger', 'fries potato', 'hotdog', 'pizza']

idx = 0
ans = []
for i in range(n):
    if i + n >= len(foods):
        ans.append(foods[idx])
        idx += 1
        if idx >= len(foods):
            idx = 0


    else:
        ans.append(foods[i + n])

print('\n'.join(ans))
