n = list(map(int, input().split()))
length = len(n)

days = [0] * length
stack = []

for i in range(length):
    while stack and stack[-1][1] < n[i]:
        index, _ = stack.pop()
        days[index] = i - index
    stack.append((i, n[i]))
print(' '.join(map(str, days)))