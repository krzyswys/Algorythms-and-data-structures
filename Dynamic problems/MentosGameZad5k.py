from zad5ktesty import runtests
import time


def garek(A):
    n = len(A)
    f = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j: f[i][j] = A[i]
    for skos in range(n):
        for j in range(skos, n):
            i = j - skos
            a = 0
            b = 0
            c = 0
            if i + 2 < n:
                a = f[i + 2][j]
            if i + 1 < n and 0 <= j - 1:
                b = f[i + 1][j - 1]
            if 0 <= j - 2:
                c = f[i][j - 2]
            f[i][j] = max(A[i] + min(a, b), A[j] + min(b, c))

    return f[0][n - 1]


runtests(garek)
