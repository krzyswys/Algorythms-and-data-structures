# Złożoność: O(V+E)
# Jak sprawdzić czy istnieje to w nieskierowanym: stopnie kazdego wierzchoła |2
# a w skieroawnym: taka sama liczba krawędzi wchodzących i wychodzacych z każdego wierzchołka


def eulerCycle(G):
    C = []
    for list in G:
        for u in list: DFS(G, C, u)
    return C


def DFS(G, C, u):
    for v in G[u]:
        id = G[u].index(v)
        G[u].pop(id)
        id = G[v].index(u)
        G[v].pop(id)

        DFS(G, C, v)
        C.append(u)


# G = [[1, 2], [0, 2, 3, 4], [0, 1], [1, 4], [1, 3]]
#
# print(eulerCycle(G))
