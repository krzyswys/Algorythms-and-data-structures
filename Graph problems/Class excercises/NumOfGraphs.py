# Złożoność: O(V+E)
import collections


def numOfGraphs(G):
    v = len(G)
    res = 0
    visited = [False for i in range(v)]
    for i in range(v):
        if not visited[i]:
            bfs(G, visited, i)
            res += 1
    return res


def bfs(G, visited, s):
    q = collections.deque()
    q.append(s)  # kladzie z prawej bierze z lewej
    visited[s] = True
    while q:
        parent = q.popleft()
        for neighbour in G[parent]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)


G = [[1, 4],
     [0, 4],
     [3],
     [2],
     [0, 1]]
print(numOfGraphs(G))
