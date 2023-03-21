# Złożoność: O(ElogV) - da nam odległość od s do kazdego punktu
# Zastosowania:
# - najkrotsze sciezki
# - ilosc najkrotszych sciezek
# - network delay time


from queue import PriorityQueue


def restorePath(parents, s, t):
    cost = 1
    parent = parents[t]
    shortestPath = [t]
    while parent != s:
        shortestPath.append(parent)
        parent = parents[parent]
        cost += 1
    shortestPath.append(parent)

    return shortestPath[::-1]


def djisktra(G, s):  # graf podany jako lista sąsiadów
    v = len(G)
    visited = [False for _ in range(v)]
    distance = [float('inf') for i in range(v)]
    distance[s] = 0
    q = PriorityQueue()
    q.put((distance[s], s))

    # counts = [0 for i in range(v)]
    # counts[s] = 1
    parent = [-1 for i in range(v)]
    parent[s] = s

    while not q.empty():
        value, node = q.get()
        if not visited[node]:
            visited[node] = True
            for neighbour, travel in G[node]:

                if distance[neighbour] > distance[node] + travel:  # warunek relaksacji, działa też f=value+travel i f
                    distance[neighbour] = distance[node] + travel
                    q.put((distance[neighbour], neighbour))

                #     counts[neighbour] = counts[node]
                    parent[neighbour] = node #[]
                #
                # elif distance[neighbour]==distance[node]+travel:
                #     counts[neighbour] += counts[node]
                #     parent[neighbour].append(node)


    return distance,restorePath(parent,0,5)


def EdgesToList(G):  # node=parent->>(weight,parent to-->, node)
    v = max((max(G, key=lambda x: x[1]))[1], (max(G, key=lambda x: x[0]))[0])
    A = [[] for j in range(v + 1)]
    for a, b, w in G:
        A[a].append((w, b))
        A[b].append((w, a))
    return A


# A=[(0, 1, 4),(0, 7, 8),(1, 2, 8),(1, 7, 11),(2, 3, 7),(2, 8, 2),(2, 5, 4),(3, 4, 9),(3, 5, 14),(4, 5, 10),(5, 6, 2),(6, 7, 1),(6, 8, 6),(7, 8, 7)]
s = 0
A = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5],
     [4, 6, 2]]  # [0, 2, 5, 5, 5, 6, 7] [None, 0, 1, 1, 0, 2, 0]
G = [
    [[1, 1], [7, 2]],
    [[0, 1], [4, 3], [2, 2]],
    [[1, 2], [3, 5]],
    [[2, 5], [6, 1]],
    [[1, 3], [5, 3], [7, 1]],
    [[4, 3], [6, 8], [8, 1]],
    [[3, 1], [5, 8], [8, 4]],
    [[0, 2], [4, 1], [8, 7]],
    [[7, 7], [5, 1], [6, 4]],
]
def addedges(G,A):
   for i, price in enumerate(A):
      for j in range(len(A)):
         # G[i].append((j,A[i]))
         G[j].append((i,A[j]))
   return G
G=[[(1,3),(3,2)],
   [(0,3),(2,20)],
   [(1,20),(5,1),(3,6)],
   [(0,2),(2,6),(4,1)],
   [(3,1),(5,7)],
   [(4,7),(2,1)]
   ]
A=[50,100,1,20,2,70]

# [0, 1, 3, 8, 3, 6, 9, 2, 7]
# G=EdgesToList(A)
print(djisktra(addedges(G,A),s), s)
