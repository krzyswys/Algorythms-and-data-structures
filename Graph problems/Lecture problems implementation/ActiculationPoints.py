# Złożość: O(V+E)
# Zastosowania:
# - Critical Connections

time=0
def DFS(G, u, visited, parent, lowTime, discoveryTime, points):
    global time
    visited[u] = True
    discoveryTime[u] = time
    lowTime[u] = time
    time += 1

    # f=0
    for neighbour in G[u]:
        if not visited[neighbour]:
            # f+=1
            parent[neighbour] = u
            DFS(G, neighbour, visited, parent, lowTime, discoveryTime, points)
            lowTime[u] = min(lowTime[u], lowTime[neighbour])
            # if parent[u]==-1 and f>1:
            #     points.append(u)

            if parent[u] != -1 and lowTime[neighbour] > discoveryTime[u]:
                points.append(u)
        elif neighbour != parent[u]:
            lowTime[u] = min(lowTime[u], discoveryTime[neighbour])
    return points


def bridge(G):
    visited = [False for i in G]
    discoveryTime = [float('inf') for i in G]
    lowTime = [float('inf') for i in G]
    parent = [-1 for i in G]
    points = []
    for i in range(len(G)):
        if not visited[i]:
            points = DFS(G, i, visited, parent, lowTime, discoveryTime, points)
    return points

def matrixToList(M):
    v=len(M)
    G=[[]for i in range(v)]
    for i in range(v):
        for j in range(v):
            if M[i][j]!=0:
                G[i].append(j)
    return G
# G1 = [[1,2,3],[0,2],[0,1],[0,4],[3]]
# G2 = [[1], [0, 2], [1, 3], [2]]
# time = 0
# print(bridge(G2))
G=[[0,1,0],[1,0,1],[0,1,0]]
print(bridge(matrixToList(G)))
