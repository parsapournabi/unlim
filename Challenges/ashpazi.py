H, M = tuple(map(int, input().split()))
X = int(input())

hour = X // 60
minute = X % 60

if not hour:
    minute = X
for m in range(1, minute + 1):
    M += 1
    if M >= 60:
        hour += 1
        M = 0
for h in range(1, hour + 1):
    H += 1
    if H >= 24:
        H = 0

print(H, M)
