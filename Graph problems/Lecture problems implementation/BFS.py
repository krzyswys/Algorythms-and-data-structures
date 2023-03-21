# Złożoność: O(V+E)
# Zastosowania:
# - najkrotsze scieszki bez wag
# - spójność grafu
# - wykrywanie cykli (jak??)
# - sprawdzanie dwudzielności


import collections


def restorePath(parents, s, t):
    cost = 1
    parent = parents[t]
    shortestPath = [t]
    while parent != s:
        shortestPath.append(parent)
        parent = parents[parent]
        cost += 1
    shortestPath.append(parent)

    return shortestPath[::-1]


def bfs(G, s):
    q = collections.deque()
    v = len(G)
    visited = [False for i in range(v)]
    # parents = [0 for i in range(v)]
    q.append(s)  # kladzie z prawej bierze z lewej
    visited[s] = True
    while not q.empty():
        parent = q.popleft()
        # if parent==t: break
        for neighbour in G[parent]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)
                # parents[neighbour] = parent
G=[[1]]
print(bfs(G,0))