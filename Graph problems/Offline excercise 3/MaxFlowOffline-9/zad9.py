# Krzysztof Wysocki
# Zaprezentowany algorytm jest w zasadzie implementajcą algrorytmu Edmondsa-Karpa (modyfikacja forda fulkersona). Algorytm tworzy siec residualną, nastepnie szuka najkrótszej scieżki
# i wybiera bottleneck, następnie aktualizuje wartosci w sieci. Wykonywane jest to dopóki istnije ścieżka: tj. da sie przejsc po wartoscach >0 w seci od startu do końca.
# Całość jest uruchamian przy wybieraniu każdej pary wierzchołków i twrozenia z nimi superujścia i sprawdzania która para da najlepszy rezultat.

# Złożoność pamięciowa: O(V^2)
# Złożoność czasowa: O(V^3*E^2)


from zad9testy import runtests
import collections


def residualNetwork(G: list[list[tuple[int, int, int, int, int]]]):  # [parent]->>(residual capacity, flow, capacity,parent, node)
    v = max((max(G, key=lambda x: x[1]))[1], (max(G, key=lambda x: x[0]))[0])
    A = [[] for j in range(v + 1)]
    [A[a].append((w, 0, w, a, b)) for a, b, w in G]
    return A


def restorePath(s: int, t: int, parents: list):
    rc, f, value, parent, neighbour = parents[t]
    minimum, n = rc, 1
    shortestPath = [(rc, f, value, parent, neighbour)]
    while parent != s:
        shortestPath.append((rc, f, value, parent, neighbour))
        rc, f, value, parent, neighbour = parents[parent]
        minimum = min(minimum, rc)
        n += 1

    shortestPath.append((rc, f, value, parent, neighbour))
    return shortestPath[::-1], minimum, n


def BFS(G: list[list[tuple[int, int, int, int, int]]], s: int, t: int):
    if s == t: return (False, float('inf'), [], 0)
    q, v = collections.deque(), len(G)
    q.append(s)
    parents = [-1 for _ in range(v)]
    visited = [False for _ in range(v)]
    visited[s] = True

    while q:
        parent = q.popleft()
        if parent == t: break
        for rc, f, value, prev, neighbour in G[parent]:
            if not visited[neighbour] and rc > 0:
                visited[neighbour] = True
                q.append(neighbour)
                parents[neighbour] = (rc, f, value, parent, neighbour)

    if visited[t]:
        shortestPath, minimum, n = restorePath(s, t, parents)
        return (True, minimum, shortestPath, n)
    else:
        return (False, float('inf'), [], 0)


def EdmundsKarp(G: list[list[tuple[int, int, int, int, int]]], s: int, t: int):
    v, flow, val = len(G), 0, True
    while val:
        val, minimum, path, n = BFS(G, s, t)
        if minimum != float('inf'): flow += minimum

        for i in range(n):
            rc, f, value, parent, neighbour = path[i]
            if path[i] in G[parent]:
                id = G[parent].index(path[i])
                G[parent][id] = (rc - minimum, minimum, value, parent, neighbour)

    return flow


def maxflow(G: list[list[tuple[int, int, int, int, int]]], s: int):
    flowGaph = residualNetwork(G)
    v, flow = len(flowGaph), 0
    for i in range(v):
        for j in range(i + 1, v):
            if i != s:
                A = [flowGaph[i][:] for i in range(v)]
                A.append([])
                A[i].append((float("inf"), 0, float("inf"), i, v))
                A[j].append((float("inf"), 0, float("inf"), j, v))
                flow = max(flow, EdmundsKarp(A, s, v))
                A[i].pop()
                A[j].pop()
    return flow


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(maxflow, all_tests=True)
