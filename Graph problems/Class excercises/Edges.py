from queue import PriorityQueue

import collections


# pusic bfs
# odzyskać scieżkę
# jeżeli naścieżce jest jakas krawędź z wagą 1 to usunąć ją z grafu
# odplaic jeszcze raz bfs
# jak da się do końca przejsc to usuwać kolejne krawędzie z wagą dopóki nie będzie braku możliwsci przejscia
def smallestAmount(G, s, t):
    path, c = bfs(G, s, t)  # path= parent, node, weight

    while len(path) > 0 and c != 0:
        for i, (parent, neigbour, w) in enumerate(path):

            if w[0] == 1:
                G[parent].pop(G[parent].index((neigbour, w[0])))
                path, c = bfs(G, s, t)
                print(c)
                print(path)


def restorePath(parents, s, t):
    cost = 0
    parent, c = parents[t]
    shortestPath = [(parent, t, [c])]
    if c == 1: cost += 1
    while parent != s:
        shortestPath.append(((parents[parent])[0], parent, [parents[parent][1]]))
        parent, c = parents[parent]
        if c == 1: cost += 1

    return shortestPath[::-1], cost


def bfs(G, s, t):
    q = collections.deque()
    v = len(G)
    visited = [False for i in range(v)]
    parents = [0 for i in range(v)]
    q.append(s)  # kladzie z prawej bierze z lewej
    visited[s] = True
    while q:
        parent = q.popleft()
        if parent == t: break
        for neighbour, val in G[parent]:
            if not visited[neighbour]:
                visited[neighbour] = True
                q.append(neighbour)
                parents[neighbour] = (parent, val)

    if visited[t]: return restorePath(parents, s, t)
    return []


G = [
    [(1, 0), (4, 1)],
    [(2, 0), (3, 1)],
    [(4, 0)],
    [(2, 1), (5, 0)],
    [(5, 0)],
    []
]
print(smallestAmount(G, 0, 5))
