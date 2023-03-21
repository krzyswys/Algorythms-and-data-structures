
def topological_sorting(A):
    n=len(A)
    G=[[] for i in range(n)]

    for i in range(n):
        for e in A[i]:
            G[i].append(("white",i,e))
    V=[]
    L = []
    for list in G:
        print("list", list)
        for c, parent, v in list:
            if c == "white" and v not in V:
                DFS(G, L, (c, parent, v), V)
    L.append(0)
    L.reverse()
    return L


def DFS(G, L, u, V):
    colorNode, parentx, valueNode = u
    V.append(valueNode)
    id = G[parentx].index(u)
    G[parentx][id] = ("grey", parentx, valueNode)
    for color, parent, value in G[valueNode]:
        if value not in V:
            if color == "grey":
                raise Exception("Graph is not a DAG")
            if color == "white":
                DFS(G, L, (color, parent, value), V)
    L.append(valueNode)
    G[parentx][id] = ("black", parentx, valueNode)
    # G = [[("white", 0, 1), ("white", 0, 2), ("white", 0, 3), ("white", 0, 4)], [("white", 1, 3)], [("white", 2, 4)],
    #      [("white", 3, 2)], []]
def isHamiltonInDAG(G):
    l=topological_sorting(G)
    print(l,G)
    for i in range(len(l)-2):
        if not (l[i+1] in G[i]):
            return False
    return True
G=[[1],[2],[3,4],[],[3]]

print(isHamiltonInDAG(G))
