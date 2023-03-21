from zad3testy import runtests
from zad3EK    import edmonds_karp
from math import inf

def Floyd_Warshall(G):
    n = len(G)
    for t in range(n): # na wykladzie (1,n+) inna numeracja wierzchołkow
        for u in range(n):
            for w in range(n):
                G[u][w] = min(G[u][w], G[u][t] + G[t][w])

def BlueAndGreen(T, K, D):
    n = len(T)
    for i in range(n):
        for j in range(n):
            if i!=j and T[i][j] == 0:
                T[i][j] = inf
    Floyd_Warshall(T)
    #print(T)
    for i in range(n):
        for j in range(n):
            '''if j>=n//2:
                T[i][j] = 0'''

            if T[i][j] < D:
                T[i][j] = 0

            elif K[i] == 'G' and K[j] == 'B':
                T[i][j] = 1

            else:
                T[i][j] = 0

    T.append([0]*(n+2))
    T.append([0]*(n+2))

    for i in range(n):
        T[i].append(0)
        T[i].append(0)

    for i in range(n):
        if K[i] == 'G':
            T[n][i] = 1
        else:
            T[i][n+1] = 1
    print(T)
    return edmonds_karp(T,n,n+1)

# runtests( BlueAndGreen )
T = [
[0, 1, 1, 0, 1],
[1, 0, 0, 1, 0],
[1, 0, 0, 0, 1],
[0, 1, 0, 0, 1],
[1, 0, 1, 1, 0],
]
K = ['B', 'B', 'G', 'G', 'B']
D = 2
print(BlueAndGreen(T,K,D))

