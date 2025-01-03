n, a, b = tuple(map(int, input().split()))

if not a:
    print(0)
    exit()

sum_ab = a + b

nums = n // sum_ab

remain = n % sum_ab

last = a

if remain < last:
    last = remain

ans = (nums * a) + last
print(ans)
