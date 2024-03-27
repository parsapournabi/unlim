n = int(input())
prices = []

for i in range(n):
    # price = list(map(int, input().split()))
    if i < 1999:
        price = [10 for w in range(7)]
    else:
        print(i)
        prices = [70 for w in range(7)]
    for p in price:
        prices.append(p)

if sum(prices) // len(prices) == prices[0]:
    print('No profit no loss')
    exit()

print(prices)

if prices.index(max(prices)) == 0:
    for ii in range(2000):
        if prices.index(max(prices)) != 0:
            break
        else:
            prices.pop(0)

if not prices:
    print('No profit no loss')
    exit()

max_price_idx = prices.index(max(prices))
if prices.count(max(prices)) > 1:
    max_price_idx = (len(prices) - 1) - prices[::-1].index(max(prices))
sort_prices = sorted(prices[:max_price_idx + 1])
if profit := (sort_prices[-1] - sort_prices[0]):
    print(profit)
else:
    print('No profit no loss')
