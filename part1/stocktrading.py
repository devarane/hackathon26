def maxProfit(prices):
    if len(prices) < 2:
        return 0
    min_price = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] - min_price > profit:
            profit = prices[i] - min_price
        if prices[i] < min_price:
            min_price = prices[i]
    return profit


print(maxProfit([7, 1, 5, 3, 6, 4]) == 5)
print(maxProfit([7, 6, 4, 3, 1]) == 0)
print(maxProfit([1, 2, 3, 4, 5]) == 4)
print(maxProfit([1, 2]) == 1)
print(maxProfit([2, 1]) == 0)
print(maxProfit([3, 8, 1]) == 5)
