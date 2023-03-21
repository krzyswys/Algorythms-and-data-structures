from collections import deque


def BFS(G, s, t, val):
    v = len(G)
    q = deque()
    q.append(s)
    visited = [False for i in range(v)]
    visited[s] = True
    while q:
        u = q.popleft()
        for n, w in G[u]:
            if not visited[n] and w >= val:
                visited[n] = True
                q.append(n)
    return visited[t]


def guide(G):
    maximum = 0
    for list in G:
        for u, v in list:
            maximum = max(maximum, v)
    for val in range(maximum):
        w = maximum - val
        if BFS(G, 0, 1, w):
            return w
    return False


# G = [
#     [(1, 10), (2, 8)],
#     [(0, 10), (3, 3), (4, 5)],
#     [(0, 8), (5, 7)],
#     [(1, 3), (4, 1), (5, 5)],
#     [(1, 7), (3, 1), (5, 1)],
#     [(4, 1), (3, 5), (2, 7)]
# ]
G=[
[(4, 5), (3, 8), (5, 10)],
[(6, 4), (2, 9), (4, 11)],
[(5, 5), (1, 9), (3, 20)],
[(4, 20), (0, 8), (2, 20)],
[(0, 5), (3, 20), (1, 11)],
[(0, 10), (2, 5), (6, 7)],
[(5, 7), (1, 4)]
]
print(guide(G))
