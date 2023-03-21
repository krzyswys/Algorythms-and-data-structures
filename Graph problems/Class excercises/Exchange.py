import math
from queue import PriorityQueue


def BellmanFord(G, s):
    v = len(G)
    visited = [False for i in range(v)]
    distance = [float('inf') for i in range(v)]
    distance[s] = 0

    # parent = [-1 for i in range(v)]
    # parent[s] = s
    for _ in range(v - 1):
        for i, list in enumerate(G):
            for travel, neighbour in list:
                if distance[neighbour] > distance[i] + travel:
                    distance[neighbour] = distance[i] + travel
                    # parent[neighbour] = node #[]

    for i, list in enumerate(G):
        for travel, neighbour in list:
            if distance[neighbour] > distance[i] + travel:
                # print("Występuje cykl ujemny")
                return False

    return True


def exchange(A):
    v = len(A)
    G = [[] for i in range(v)]
    for i, list in enumerate(A):
        for e, w in list:
            l = (-1) * math.log(w, 10)
            G[i].append((l, e))
    for i in range(v):
        if not BellmanFord(G, i):
            return True
    return False

# G=[
#     [(1,0.2),(3,0.75)],
#     [(2,0.1)],
#     [(0,2),(3,0.25)],
#     [(2,2),(0,0.15),(1,0.15)]
# ] #T
# G=[
#     [(1,0.2),(3,0.75)],
#     [(2,0.1)],
#     [(0,0.2),(3,0.25)],
#     [(2,0.2),(0,0.15),(1,0.15)]
# ] #F
# print(exchange(G))
