n = list(map(int, input().split()))

stack = []
maximum = 0

for i, l in enumerate(n):
    st_index = i
    while stack and stack[-1][1] > l:
        idx, level = stack.pop()
        maximum = max(maximum, level * (i - idx))
        st_index = idx
    stack.append((st_index, l))

for i, lvl in stack:
    maximum = max(maximum, lvl * (len(n) - i))
print(maximum)
