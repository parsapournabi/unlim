n = list(map(int, input()))

length = len(n)

for i in range(length):
    even = True if n[i] % 2 == 0 else False
    for j in range(i + 1, length):
        if even and n[j] % 2 == 0:
            if n[j] > n[i]:
                n[i], n[j] = n[j], n[i]

        elif not even and n[j] % 2 == 1:
            if n[j] > n[i]:
                n[i], n[j] = n[j], n[i]

print(''.join(map(str, n)))