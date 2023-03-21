def logicFloydWarshall(G):
    v = len(G)
    M = G.copy()
    for t in range(v):
        for i in range(v):
            for j in range(v):
                M[i][j] = (M[i][j] or (M[i][t] and M[t][j]))
    return M


def traverse(G):
    v = len(G)
    M = [[False for i in range(v)] for i in range(v)]
    for i, list in enumerate(G):
        for e in list:
            M[i][e] = True
    print(M)
    return M

# G1=[[1,3],[0],[3],[2,0]]
# G2=[[3],[0],[3],[]]
# print(logicFloydWarshall(traverse(G2)))
