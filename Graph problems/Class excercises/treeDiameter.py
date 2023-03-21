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
    parents = [0 for i in range(v)]
    distance=[-1 for i in range(v)]
    q.append(s)  # kladzie z prawej bierze z lewej
    visited[s] = True
    distance[s]=0
    while q:
        parent = q.popleft()
        # if parent==t: break
        for neighbour,val in G[parent]:
            if not visited[neighbour]:
                visited[neighbour] = True
                distance[neighbour]=distance[parent]+val
                q.append(neighbour)
                parents[neighbour] = parent
    return distance, parents
G=[
    [(2,7)],
    [(2,5)],
    [(0,7),(1,5),(3,18)],
    [(2,18),(4,2)],
    [(3,2),(5,10),(6,9)],
    [(4,10)],
    [(4,9),(7,8)],
    [(6,8)]
]

G=[
    [(1,1)],
    [(0,1),(2,2)],
    [(1,2),(3,1),(5,3)],
    [(2,1)],
    [(5,1),(7,4)],
    [(2,3),(4,1),(6,3),(8,2)],
    [(5,3),(9,1)],
    [(4,4)],
    [(5,2),(10,2)],
    [(6,1)],
    [(8,2)]
]
# L = [ [ (2,1) ],
# [ (2,1) ],
# [ (0,1), (1,1), (3,1)],
# [ (2,1), (4,1) ],
# [ (3,1), (5,1), (6,1) ],
# [ (4,1) ],
# [ (4,1) ] ]

def diameter(G):
    distance1, parent1=bfs(G,0)
    end=distance1.index(max(distance1))
    distance2, parent2=bfs(G,end)
    start=distance2.index(max(distance2))
    path=restorePath(parent1, start, end)
    minimum=float("inf")
    l=0
    for ind in path:
        if abs(distance2[ind]-distance1[ind])<minimum:
            minimum=abs(distance2[ind]-distance1[ind])
            l=ind
    return l
print(diameter(L))


