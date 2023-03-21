# Krzysztof Wysocki
# Przedstawiony algorytm w pierwszej kolejnosci szuka najkrótszej drogi z s do t wykorzsytując algorytm BFS,
# następnie iteruje przez każdą krawędź w tejże ścieżce i usuwa ją z całego grafu. Kolejnie ponownie uruchamia algorytm BFS,
# i porównuje otrzymaną długość ścieżki z 'oryginalną' długością. Jeżeli ta jest wieksza to znaczy ze usunięcie danej krawędzi spowodowało wydłużenie najkrótszej ścieżki.
# Jeżeli po usunięciu ścieżki nie została ona wydłużona i graf dalej jest spójny oznacza to ze nie ma potrzeby jej spowrotem dodawać.
# W przypadku jeżeli szukanie najkrótszej ściżeszki zwróci -10 to oznacza ze usuneicie krawędzi spowowało rozspójnienie grafu i również wydłużenie ścieżki.

# Złożoność czasowa: O(q(V+E)) gdzie q to długość najkrótszej ścieżki
# Złożoność pamięciowa: O(V+E)


from zad6testy import runtests
import collections


def shortest_path_BFS(G, s, t):
    v = len(G)
    visited = [False for i in range(v)]  # wartosc dla rodzica i kosztu dojścia
    parents = [0 for i in range(v)]
    queue = collections.deque()
    queue.append(s)

    while queue:
        parent = queue.popleft()
        if parent == t: break
        for neighbour in G[parent]:
            if not visited[neighbour]:
                visited[neighbour] = True
                parents[neighbour] = parent
                queue.append(neighbour)

    if not visited[t]: return ([], -10)

    cost = 1
    parent = parents[t]
    shortestPath = [t]
    while parent != s:
        shortestPath.append(parent)
        parent = parents[parent]
        cost += 1
    shortestPath.append(parent)
    return (shortestPath, cost)


def longer(G, s, t):
    Gn = len(G)
    if Gn == 1 or Gn == 2 or Gn == 0:
        return None
    path, cost = shortest_path_BFS(G, s, t)
    n = len(path)
    for e in range(n - 1):
        ip = G[path[e]].index(path[e + 1])
        G[path[e]].pop(ip)
        ie = G[path[e + 1]].index(path[e])
        G[path[e + 1]].pop(ie)
        pathX, costX = shortest_path_BFS(G, s, t)
        # G[path[e]].append(ip)
        # G[path[e+1]].append(ie)
        if costX > cost or costX == -10:
            return (path[e], path[e + 1])
    return None


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(longer, all_tests=True)
