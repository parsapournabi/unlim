n = int(input())
ck = []
k: dict = {}
sum = 0

for _ in range(n):
    _c, _k = input()
    ck.append(_c + _k)
    k[_k] = set()

for i in range(n):
    color = ck[i][0]
    column = ck[i][1]
    k[column].add(color)

for value in k.values():
    if len(value) == 3:
        sum += 1

print(sum)