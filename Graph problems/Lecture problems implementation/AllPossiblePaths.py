# Złożoność O(v^v)

def allPaths(G, u, d, visited, path):
    visited[u] = True
    path.append(u)
    if u == d:
        print(path)
    else:
        for i in G[u]:
            if not visited[i]:
                allPaths(G, i, d, visited, path)
    path.pop()
    visited[u] = False


def printpaths(G, s, d):
    visited = [False for i in range(len(G))]
    path = []
    allPaths(G, s, d, visited, path)


# G=[[1,2],[0,2,3,4],[0,1],[1,4],[1,3]]
# G = [[1, 2, 3], [3], [0, 1, 3], []]
# s, d = 2, 3
# printpaths(G, s, d)
# [2, 0, 1, 3]
# [2, 0, 3]
# [2, 1, 3]
