# Złożoność: O(ElogV)
# Zastosowania:
# - Lączenie miast po najmniejszym koszcie
# - Optymalizowanie dystrybucji wody w wiosce: https://github.com/azl397985856/leetcode/blob/master/problems/1168.optimize-water-distribution-in-a-village-en.md
# - Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree: https://zxi.mytechroad.com/blog/graph/leetcode-1489-find-critical-and-pseudo-critical-edges-in-minimum-spanning-tree/
class Node:
    def __init__(self, value):
        self.parent = self
        self.value = value
        self.rank = 0


def find(x):
    if x.parent != x:
        x.parent = find(x.parent)
    return x.parent


def union(x, y):  # mlogn
    x = find(x)
    y = find(y)
    if x == y:
        return
    if x.rank > y.rank:
        y.parent = x
    else:
        x.parent = y
        if x.rank == y.rank:
            y.rank += 1


def make_set(x):
    return Node(x)


def MST(G):  # graf podany w formie listy samych krawędzi
    n = len(G)
    s = [make_set(i) for i in range(n)]
    t = []
    # G.sort(key=lambda x: x[2])
    for p, q, w in G:
        if find(s[p]) != find(s[q]):
            union(s[p], s[q])
            t.append((p, q))
            # if len t ==v-1 return t
    return t
