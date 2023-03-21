from zad12ktesty import runtests

def sum(arr, start, to):
    total = 0
    for i in range(start, to + 1):
        total += arr[i]
    return total

def findMax(arr, n, k):
    dp = [[0 for i in range(n + 1)]
          for j in range(k + 1)]
    for i in range(1, n + 1):
        dp[1][i] = sum(arr, 0, i - 1)
    for i in range(1, k + 1):
        dp[i][1] = arr[0]
    for i in range(2, k + 1):
        for j in range(2, n + 1):
            best = 100000000
            for p in range(1, j + 1):
                best = min(best, max(dp[i - 1][p],
                                     sum(arr, p, j - 1)))
            dp[i][j] = best
    return dp[k][n]
def autostrada( T, k ):
    #Tutaj proszę wpisać własną implementację
    return findMax(T,len(T),k)

runtests ( autostrada,all_tests=True )