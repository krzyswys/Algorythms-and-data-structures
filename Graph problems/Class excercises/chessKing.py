from collections import deque


def chessKing(G, s):  # graf podany jako lista sąsiadów
    v = len(G)
    visited = [[False for _ in range(v)] for i in range(v)]
    distance = [[float('inf') for i in range(v)] for i in range(v)]
    y, x = s
    distance[y][x] = G[0][0]

    q = deque()
    q.append((y, x))
    moves = [(1, 1), (0, 1), (1, 0), (-1, 0), (0, -1), (-1, -1), (-1, 1), (1, -1)]
    while q:
        yo,xo = q.popleft()

        for moveY, moveX in moves:
            x = xo + moveX
            y = yo + moveY
            if x >= 0 and x < v and y >= 0 and y < v:

                if not visited[y][x]:
                    distance[y][x] = distance[yo][xo] + G[y][x]
                    visited[y][x] = True
                    q.append((y, x))

                elif visited[y][x] and distance[y][x] > distance[yo][xo] + G[y][x]:
                    distance[y][x] = distance[yo][xo] + G[y][x]
                    q.append((y, x))

    return distance


M = [
    [2, 0, 0, 4, 5, 2],
    [1, 3, 0, 5, 1, 5],
    [5, 5, 0, 0, 3, 4],
    [4, 2, 3, 0, 0, 1],
    [1, 5, 5, 2, 0, 0],
    [2, 4, 3, 3, 3, 1]
]
d = chessKing(M, (0, 0))
print(*d, sep="\n")


