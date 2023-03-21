def lnds(t):
    n = len(t)
    f = [1 for i in range(n)]
    p = [-1 for i in range(n)]
    maxi = 0
    for i in range(n):
        for j in range(i):
            if t[i] > t[j] and f[i] < f[j] + 1:
                # f[i]=max(f[i],f[i-j]+1)
                f[i] = f[j] + 1
                p[i] = j
        if f[i] > f[maxi]:
            maxi = i
    x = []

    def printSol(t, p, i, x):
        if p[i] != -1:
            printSol(t, p, p[i], x)
        x.append(t[i])

    printSol(t, p, maxi, x)
    return f[maxi], x


# rozwiazanie nlogn - kopia do podgladu z gfg
def CeilIndex(A, l, r, key):
    while r - l > 1:
        m = l + (r - l) // 2
        if A[m] >= key:
            r = m
        else:
            l = m
    return r


def LongestIncreasingSubsequenceLength(A, size):
    tailTable = [0 for i in range(size + 1)]
    len = 0
    tailTable[0] = A[0]
    len = 1
    for i in range(1, size):
        if A[i] < tailTable[0]:
            tailTable[0] = A[i]
        elif A[i] > tailTable[len - 1]:
            tailTable[len] = A[i]
            len += 1
        else:
            tailTable[CeilIndex(tailTable, -1, len - 1, A[i])] = A[i]
    return len


# t=[-1,3,4,5,2,2,2,2]
# t=[2,1,4,3,4,8,5,7,2,0]
# print(lnds(t))
