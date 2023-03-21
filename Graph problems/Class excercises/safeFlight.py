import collections


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


def safeTravel(G,s,t,k,p):
    q = collections.deque()
    v = len(G)
    visited = [False for i in range(v)]
    # parents = [0 for i in range(v)]
    q.append(s)  # kladzie z prawej bierze z lewej
    visited[s] = True
    while q:
        parent = q.popleft()
        # if parent==t: break
        for neighbour, val in G[parent]:

            if not visited[neighbour] and (p-k<=val and val <=p+k):
                visited[neighbour] = True
                q.append(neighbour)
                # parents[neighbour] = parent
    return visited

G=[
    [(1,20),(4,10)],
    [(0,20),(2,12),(3,15)],
    [(1,12),(3,40),(4,13)],
    [(1,15),(2,40),(5,10)],
    [(0,10),(2,13),(5,5)],
    [(4,5),(3,10)]
]
k=5
s=0
t=5
p=10
print(safeTravel(G,s,t,k,p))
