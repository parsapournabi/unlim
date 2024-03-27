n, m = list(map(lambda x: int(x, 2), input().split()))
print(int(str(bin(m - n))[2:], 2))
