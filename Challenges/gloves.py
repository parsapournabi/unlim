gloves = list(map(int, input().split()))
gloves.remove(min(gloves))
print(sum(gloves) + 2)
