import random, time

n = int(input())
ages = list(map(int, input().split()))
# ages = [random.randint(0, 2000) for i in range(n)]
coins = [1 for c in range(n)]

# print(ages)

for i, age in enumerate(ages):
    if i == 0:
        if age > ages[i + 1]:
            coins[i] += 1
    elif i == len(ages) - 1:
        if age > ages[i - 1]:
            coins[i] += 1
    else:
        if age > ages[i + 1]:
            coins[i] += 1
        # if age > ages[i - 1]:
        #     coins[i] += 1

print(' '.join(list(map(str, coins))))
