# Złożoność O(v^3)
# Zastosowania:
# - szukanie najrótszych scieżek pomiędzy wszystkimi parami wraz z ich odtworzeniem


def constructPath(parent, a, b):
    if parent[a][b] == -1:
        return []
    path = [a]
    while a != b:
        a = parent[a][b]
        path.append(a)
    return path


def FloydWarshall(M):  # graf podany jako reprezentacja macierzowa
    v = len(M)
    # parent=[[-1 for i in range(v)] for j in range(v)]
    # for i in range(v):
    #     for j in range(v):
    #         if M[i][j]==float('inf'):
    #             parent[i][j]=-1
    #         else:
    #             parent[i][j]=j

    for t in range(v):
        for i in range(v):
            for j in range(v):
                if M[i][j] > M[i][t] + M[t][j]:
                    M[i][j] = M[i][t] + M[t][j]
                    # parent[i][j]=parent[i][t]
    # shortestPath=constructPath(parent,u,v)
    return M


# INF = float('inf')
# A = [[0, 5, INF, 10],
#      [INF, 0, 3, INF],
#      [INF, INF, 0, 1],
#      [INF, INF, INF, 0]
#      ]  # [[0, 5, 8, 9], [inf, 0, 3, 4], [inf, inf, 0, 1], [inf, inf, inf, 0]]
# M = [[0, 3, INF, 7],
#      [8, 0, 2, INF],
#      [5, INF, 0, 1],
#      [2, INF, INF, 0]]  # [[0, 3, 5, 6], [5, 0, 2, 3], [3, 6, 0, 1], [2, 5, 7, 0]]
# print(FloydWarshall(A))
