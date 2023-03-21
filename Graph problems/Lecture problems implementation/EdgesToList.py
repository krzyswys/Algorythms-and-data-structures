def EdgesToList(G):  # node=parent->>(weight,parent to-->, node)
    v = max((max(G, key=lambda x: x[1]))[1], (max(G, key=lambda x: x[0]))[0])
    A = [[] for j in range(v + 1)]
    [A[a].append((w, a, b)) for a, b, w in G]
    return A