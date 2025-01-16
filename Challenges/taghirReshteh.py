def print_matrix(matrix: list[list]):
    print(''.join('\n'.join(map(str, matrix))))


w1 = input()
w2 = input()

cache = [[float("inf")] * (len(w2) + 1) for _ in range(len(w1) + 1)]

for j in range(len(w2) + 1):
    cache[len(w1)][j] = len(w2) - j
for i in range(len(w1) + 1):
    cache[i][len(w2)] = len(w1) - i

for i in range(len(w1) - 1, -1, -1):
    for j in range(len(w2) - 1, -1, -1):
        if w1[i] == w2[j]:
            cache[i][j] = cache[i + 1][j + 1]
            continue
        cache[i][j] = min(cache[i + 1][j], cache[i][j + 1], cache[i + 1][j + 1]) + 1
print_matrix(cache)
print(cache[0][0])
