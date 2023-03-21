def cmp(coins, amount):
    f = [amount + 1 for i in range(amount + 1)]
    f[0] = 0
    for i in range(amount + 1):
        for j in range(len(coins)):
            if i >= coins[j]:
                f[i] = min(f[i - coins[j]] + 1, f[i])
    if f[amount] == amount + 1:
        return -1
    return f[amount]

# t = [1, 2, 5]
# amount = 11
# print(cmp(t, amount))
