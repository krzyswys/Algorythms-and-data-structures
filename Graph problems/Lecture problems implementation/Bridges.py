# Złożość: O(V+E)
# Zastosowania:
# - Critical Connections


def bridgeuntill(G, u, visited, parent, lowTime, discoveryTime, bridges):
    global time
    visited[u] = True
    discoveryTime[u] = time
    lowTime[u] = time
    time += 1
    for neighbour in G[u]:
        if not visited[neighbour]:
            parent[neighbour] = u
            bridgeuntill(G, neighbour, visited, parent, lowTime, discoveryTime, bridges)
            lowTime[u] = min(lowTime[u], lowTime[neighbour])
            if lowTime[neighbour] > discoveryTime[u]:
                bridges.append((u, neighbour))
        elif neighbour != parent[u]:
            lowTime[u] = min(lowTime[u], discoveryTime[neighbour])
    return bridges


def bridge(G):
    visited = [False for i in G]
    discoveryTime = [float('inf') for i in G]
    lowTime = [float('inf') for i in G]
    parent = [-1 for i in G]
    bridges = []
    for i in range(len(G)):
        if not visited[i]:
            bridges = bridgeuntill(G, i, visited, parent, lowTime, discoveryTime, bridges)
    return bridges

# G1 = [[1, 2, 3], [0, 2], [0, 1], [0, 4], [3]]
# G2 = [[1], [0, 2], [1, 3], [2]]
# time = 0
# print(bridge(G1))
