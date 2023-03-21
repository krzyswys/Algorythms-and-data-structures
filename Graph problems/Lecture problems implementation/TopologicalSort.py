# Złożność: O(V+E)
# Zastosowanie:
# - układanie kolejnośći zadań
# - szukanie (czy istnieje) scieszki hamiltona?
# - "sentence ordering"
# - sprawdzanie czy graf zawiera JAKIS cykl

def topSortEdges(E):
    def topological_sorting(G):
        L = []
        V=[False for i in range(len(G))]
        for list in G:
            for parent, v in list:
                if not V[v]:
                    DFS(G, L, (parent, v), V)
        L.append(0)
        L.reverse()
        return L


    def DFS(G, L, u, V):
        parentx, valueNode = u
        V[valueNode]=True
        for parent, value in G[valueNode]:
            if not V[value]:
                    DFS(G, L, (parent, value), V)
        L.append(valueNode)


    G = [[(0, 1), (0, 2), (0, 3), (0, 4)], [(1, 3)], [(2, 4)],
         [(3, 2)], []]
    # V = []
    #[0, 1, 3, 2, 4]
    print(topological_sorting(G))

def topSortList(G):
    def DFS(G):
        n = len(G)
        visited = [False for _ in range(n)]
        topSort = []
        for i in range(n):
            if not visited[i]:
                DFSh(G, i, visited, topSort)
        return topSort

    def DFSh(G, i, vis, top):
        vis[i] = True
        for j in G[i]:
            if not vis[j]:
                DFSh(G, j, vis, top)
        top += [i]

    def reverse(T):
        n = len(T)
        S = [0 for _ in range(n)]
        for i in range(n):
            S[i] = T[n - i - 1]
        return S

    return reverse(DFS(G))

    G = [
        [1, 2, 3, 4],
        [3],
        [4],
        [2],
        []
    ]
    print(topologicSort(G))

def topSrotEdgesColors(Ec):
    def topological_sorting(G):
        L = []
        V = [False for i in range(len(G))]
        for list in G:
            print("list", list)
            for c, parent, v in list:
                if c == "white" and not V[v]:
                    DFS(G, L, (c, parent, v), V)
        L.append(0)
        L.reverse()
        return L

    def DFS(G, L, u, V):
        colorNode, parentx, valueNode = u
        V[valueNode] = True
        id = G[parentx].index(u)
        G[parentx][id] = ("grey", parentx, valueNode)
        for color, parent, value in G[valueNode]:
            if not V[value]:
                if color == "grey":
                    raise Exception("Graph is not a DAG")
                if color == "white":
                    DFS(G, L, (color, parent, value), V)
        L.append(valueNode)
        G[parentx][id] = ("black", parentx, valueNode)

    G = [[("white", 0, 1), ("white", 0, 2), ("white", 0, 3), ("white", 0, 4)], [("white", 1, 3)], [("white", 2, 4)],
         [("white", 3, 2)], []]
    # V = []
    # [0, 1, 3, 2, 4]
    print(topological_sorting(G))





