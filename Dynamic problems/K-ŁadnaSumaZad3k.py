
from zad3ktesty import runtests

"""
f(i) - najmniejsza suma oraz biezemy i-tą liczbę
f(i) = T[i] + min[j po k](f(i-j))
"""


def ksuma(T, k):
    n = len(T)
    F = [float("inf") for _ in range(n)]

    for i in range(k):
        F[i] = T[i]

    for i in range(k, n):
        best = float("inf")
        for j in range(i - k, i):
            best = min(best, F[j])

        F[i] = T[i] + best

    return min(F[-k:])


runtests(ksuma)