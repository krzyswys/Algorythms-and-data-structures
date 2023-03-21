
t=0
def dfs(G, s):
    v = len(G)
    visited = [False for i in range(v)]
    timeTable = [0 for _ in range(len(G))]
    parent = [-1 for _ in range(len(G))]
    path = [s]

    DFS(G, s, visited, timeTable,  parent, path)

    traversalTime = [(timeTable[i], i) for i in range(len(timeTable))]
    # traversalTime.sort(reverse=True)
    print(path)
    print(traversalTime)


def DFS(G, u, visited, timeTable, parent, path):
    global t
    t += 1  # czas wejscia
    visited[u] = True
    for v in G[u]:
        if not visited[v]:
            path.append(v)
            DFS(G, v, visited, timeTable, parent, path)
            if len(path)==len(G)-1:
                # print(path)
                return path
            else:
                visited[v]=False
                path.pop()

    t += 1  # czas przetworzenia
    timeTable[u] = t

G=[[1,2],
   [0,2],
   [0,1,3],
   [2,4,5],
   [3,5],
   [3,4]]
print(dfs(G,0))
