def stock(prices):
    n = len(prices)
    maxv = 0
    f = [0 for i in range(n)]
    i = 0
    j = 0
    while (j < n):
        profit = prices[j] - prices[i]
        maxv = max(profit, maxv, f[j - 1])
        f[j] = profit
        if profit < 0:
            i += 1
            j -= 1
        j += 1

    return max(f)
def stock_On(prices):
    minbuy, maxprofit=prices[0],0
    for price in prices:
        minbuy=min(minbuy, price)
        profit=price-minbuy
        maxprofit=max(maxprofit, profit)
    return maxprofit

# t = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
# print(stock(t))
