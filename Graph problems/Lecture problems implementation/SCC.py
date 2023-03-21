# Strongly connected component (silnie spojne skladowe)
# Złożoność: O(V+E)
# Zastosowania szukania silnie spójnych składowych:
# - Minimum Number of Days to Disconnect Island
# - Upadające domino

# Algorytm:
# 1. DFS na grafie zapamiętując czasy przetrwarzania.
# 2. Odwrócenie kierunku wszystkich krawędzi
# 3. DFS w kolejnosci malejących czasów przetwarzania
t = 0


def DFS(G, v, visited):
    visited[v] = True
    print(v, end=" ")
    for neigbour in G[v]:
        if not visited[neigbour]:
            DFS(G, neigbour, visited)


def DFS2(G, v, visited, timeTable):
    global t
    t += 1
    visited[v] = True
    for neigbour in G[v]:
        if not visited[neigbour]:
            DFS2(G, neigbour, visited, timeTable)
    t += 1
    timeTable[v] = t


def SCC(G):
    visited = [False for i in range(len(G))]
    timeTable = [0 for _ in range(len(G))]
    for i in range(len(G)):
        if not visited[i]:
            DFS2(G, i, visited, timeTable)

    traversalTime = [(timeTable[i], i) for i in range(len(timeTable))]
    traversalTime.sort(reverse=True)

    G = reverse(G)
    visited = [False for i in range(len(G))]

    while len(traversalTime) > 0:
        timee, i = traversalTime.pop(0)
        if not visited[i]:
            DFS(G, i, visited)
            print(" ")


def reverse(G):
    v = len(G)
    A = [[] for i in range(v)]

    for i, list in enumerate(G):
        for neigbour in list:  # color, time, timef,neigbour,parentorg,parent
            A[neigbour].append(i)
    return A


# 0 2 1
# 9 7 8 10
# 5 6 4 3

# G = [[1], [2, 3], [0, 9], [5], [3, 6], [4], [5], [9], [4, 7], [10], [5, 8]]
# print(G)
# print(reverse(G))
# print(SCC(G))
