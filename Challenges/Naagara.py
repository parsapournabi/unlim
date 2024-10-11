def ave(x):
    return sum(x) // len(x)


n = int(input())
m = [ave(list(map(int, input().split()))) for _ in range(n)]
minimum = min(m)
print(minimum, m.index(minimum) + 1)
