n = int(input())
birds = list(map(int, input().split()))
used = []
ans = 0

for bird in birds:
    if birds.count(bird) > 1 and bird not in used:
        if birds.count(bird) == 2:
            ans += 1
        elif birds.count(bird) == 3:
            ans += 3
        else:
            ans += sum([i for i in range(3, birds.count(bird))]) + 3
        used.append(bird)

print(ans)
