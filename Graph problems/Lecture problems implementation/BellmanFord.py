# Złożoność: O(V*E)
# Zastosowania:
# - najkrótsze scieżki ale z dostępnymi wagami ujemnymi
# - najkrotsze sciezki
# - ilosc najkrotszych sciezek
# - network delay time


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
                print("Występuje cykl ujemny")
                return False

    return distance


G = [
    [(1, 2), (2, 4)],
    [(0, 2), (3, 11), (4, 3)],
    [(0, 4), (3, 13)],
    [(1, 11), (2, 13), (5, 17), (6, 1)],
    [(1, 3), (5, 5)],
    [(3, 17), (4, 5), (7, 7)],
    [(3, 1), (7, 3)],
    [(5, 7), (6, 3)],

]
s = 0
A = [(0, 1, -1), (0, 2, 4), (1, 2, 3), (1, 3, 2), (1, 4, 2), (3, 2, 5), (3, 1, 1), (4, 3, -3)]
# A=[(0, 1, 5),(0, 2, 4),(1, 3, 3),(2, 1, 6),(3, 2, 2)]
A = [(0, 1, 2), (1, 2, -10), (2, 3, -10), (3, 1, -10), (2, 4, 2)]


def EdgesToList(G):  # node=parent->>(weight,parent to-->, node)
    v = max((max(G, key=lambda x: x[1]))[1], (max(G, key=lambda x: x[0]))[0])
    A = [[] for j in range(v + 1)]
    print(v + 1)
    for a, b, w in G:
        A[a].append((w, b))
        # A[b].append((w, a))
    return A


print(BellmanFord(EdgesToList(A), s))
# 0		0
# 1		-1
# 2		2
# 3		-2
# 4		1

# 0		0
# 1		5
# 2		4
# 3		8
# 4		inf
