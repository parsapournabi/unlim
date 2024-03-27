import math

n = int(input())
cost = list(map(int, input().split()))

new_cost = []
discount = []

value = 0

ans = []

for i in range(n):
    if len([c for c in cost if sum(cost) / len(cost) == c]) == len(cost) and i == 0:
        new_cost = cost
        discount = [20 for i in range(9, len(new_cost))] + [40, 40, 40, 30, 30, 30, 30, 30, 10]
        break
    if i < 3:
        value = max(cost)
        discount.append(40)
    elif 3 <= i < 8:
        value = max(cost)
        discount.append(30)
    elif 8 <= i < n -1:
        value = max(cost)
        discount.append(20)
    else:
        value = max(cost)
        discount.append(10)

    new_cost.append(value)
    cost.pop(cost.index(value))

for c, d in zip(new_cost, discount):
    ans.append(math.ceil(c - ((c * d) / 100)))
print(''.join(list(map(lambda x: f'{x} ', sorted(ans)))))
