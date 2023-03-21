def isTwoColorable(G):
    v = len(G)
    colors = [-1 for i in range(v)]
    result = True
    c = 0

    for i in range(v):
        if colors[i] == -1:
            result = DFS(G, colors, i, 1 - c)
        return result


def DFS(G, colors, i, c):
    colors[i] = c
    result = True
    print(colors)
    # for i, list in enumerate(G):
    for u in G[i]:
        if colors[u] == c:
            print(colors[u], u, c)
            return False
        elif colors[u] == -1:
            result = DFS(G, colors, u, 1 - c)
    print(colors)
    return result

# G = [[1],
#      [0],
#      [3],
#      [2],
#     ]
# G = [[1, 4],
#      [0, 4],
#      [3],
#      [2],
#      [0, 1]]
# G=[[1,3],
#    [0,2],
#    [1,3],
#    [0,2],
#    ]
# print(isTwoColorable(G))
