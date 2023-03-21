# Złożoność: O(V+E)
# Zastosowania:
# - sprawdzanie spójności grafu
# - sprawdzanie dwudzielnosci
# - wykrywanie cykli (jak??)
# - sortowanie topologiczne
# - cykl eulera
# - scc
# - mosty i pkt artykulacji


def dfs(G, s):
    v = len(G)
    visited = [False for i in range(v)]
    timeTable = [0 for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    path = []

    DFS(G, s, visited, timeTable, timeTable, parent, path)

    traversalTime = [(timeTable[i], i) for i in range(len(timeTable))]
    traversalTime.sort(reverse=True)


def DFS(G, u, visited, timeTable, parent, path):
    global t
    t += 1  # czas wejscia
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            # path.append(v)
            DFS(G, v, visited, timeTable, parent, path)
            # if len(val)>0:
            #     return path
            # else:
            #     visited[v]=False
            #     path.pop()

    t += 1  # czas przetworzenia
    timeTable[u] = t
