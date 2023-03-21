# Złożoność: O(ElogV)
# Zastosowania:
# - Lączenie miast po najmniejszym koszcie
# - Optymalizowanie dystrybucji wody w wiosce: https://github.com/azl397985856/leetcode/blob/master/problems/1168.optimize-water-distribution-in-a-village-en.md
# - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree: https://zxi.mytechroad.com/blog/graph/leetcode-1489-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
from queue import PriorityQueue


def primMST(G):  # n,p,v graf podany w formie listy sasiadów, lub macierzowej (potrzebny traversal)
    v = len(G)
    q = PriorityQueue()
    visited = [False for i in range(v)]
    tree = []
    visited[0] = True
    for n, p, vx in G[0]:
        q.put((vx, p, n))
    while len(tree) < v - 1:
        val, parent, neigbour = q.get()
        if not visited[neigbour] and neigbour != parent:
            tree.append((parent, neigbour, val))
            visited[neigbour] = True
            for n, p, va in G[neigbour]:
                q.put((va, p, n))
    return sorted(tree)

# def traverse(M):
#     v=len(M)
#     A=[[]for i in range(v)]
#     for i in range(v):
#         for j in range(v):
#             if M[i][j]!=0:
#                 A[i].append((j,i,M[i][j]))
#     return A
# M = [[0, 2, 0, 6, 0],
#     [2, 0, 3, 8, 5],
#     [0, 3, 0, 0, 7],
#     [6, 8, 0, 0, 9],
#     [0, 5, 7, 9, 0]]
# G = [[0, 9, 75, 0, 0],
#      [9, 0, 95, 19, 42],
#      [75, 95, 0, 51, 66],
#      [0, 19, 51, 0, 31],
#      [0, 42, 66, 31, 0]]
# A = [
#     [[1,0, 1], [2,0, 2]],
#     [[0,1, 1], [3,1, 1], [4,1, 3]],
#     [[0,2, 2], [3,2, 3]],
#     [[1,3, 1], [2,3, 3], [4,3, 1], [5,3, 2]],
#     [[1,4, 3], [3,4, 1], [5,4, 4]],
#     [[3,5, 2], [4,5, 4], [6,5, 1], [7,5, 5]],
#     [[5,6, 1], [7,6, 2]],
#     [[5,7, 5], [6,7, 2]],
# ]
#
# print(primMST(A))
# print(primMST(traverse(M)))
# print(primMST(traverse(G)))
