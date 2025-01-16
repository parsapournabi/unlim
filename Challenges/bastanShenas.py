s = list(input())
t = list(input())

i, j = 0, 0

while i < len(s) and j < len(t):
    if s[i] == t[j]:
        i += 1
    j += 1
print('hoard' if i == len(s) else 'fake')