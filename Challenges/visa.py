ans = ''
n, m = list(map(int, input().split()))
for i in range(m):
    a, b, c = list(map(int, input().split()))
    if b - a != c:
        ans = 'No'

if ans != 'No':
    ans = 'Yes'
print(ans)

# def solve(n, m, a, b, c):
#     pos = [0] * (n + 1)
#     for i in range(m):
#         if pos[a[i]] and pos[b[i]] and pos[b[i]] - pos[a[i]] != c[i]:
#             return "No"
#         if pos[a[i]]:
#             pos[b[i]] = pos[a[i]] + c[i]
#         else:
#             pos[a[i]] = 1
#             pos[b[i]] = 1 + c[i]
#     return "Yes"
#
# n, m = map(int, input().split())
# a, b, c = [], [], []
# for i in range(m):
#     abc = list(map(int, input().split()))
#     a.append(abc[2])
#     b.append(abc[1])
#     c.append(abc[0])
# print(solve(n, m, a, b, c))