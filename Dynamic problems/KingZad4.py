from zad4ktesty import runtests


def king(T):
    n = len(T)
    f = [[0 for i in range(n)] for j in range(n)]
    for i in range(1, n):
        f[i][0] = f[i - 1][0] + T[i][0]
        f[0][i] = f[0][i - 1] + T[0][i]

    for i in range(1, n):
        for j in range(1, n):
            f[i][j] = min(f[i - 1][j] + T[i][j], f[i][j - 1] + T[i][j])

    return f[n - 1][n - 1]


runtests(king)
