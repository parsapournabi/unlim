import time
import random

n, m = list(map(int, input().split()))
t = list(map(int, input().split()))

primes = [2, 3, 5, 7]


def set_zero_with_lowest_movements(numbers, n):
    st = time.time()




numbers = [random.randint(1, 10) for _ in range(10)]
print(numbers)
result = set_zero_with_lowest_movements(numbers, n)
print(result)
