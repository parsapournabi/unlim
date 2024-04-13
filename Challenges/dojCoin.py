n = int(input())
prices = []

for _ in range(n):
    week_prices = list(map(int, input().split()))
    prices.extend(week_prices)


def max_profit(prices):
    n = len(prices)
    if n == 0:
        return 0

    max_profit = [0] * n
    min_price = [0] * n
    min_price[0] = prices[0]

    for i in range(1, n):
        min_price[i] = min(min_price[i - 1], prices[i])
        max_profit[i] = max(max_profit[i - 1], prices[i] - min_price[i])

    return max_profit[-1]


max_profit = max_profit(prices)
if max_profit > 0:
    print(max_profit)
else:
    print("No profit no loss")
