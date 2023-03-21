from queue import PriorityQueue


def djisktra(G, s, t):  # graf podany jako lista sąsiadów
    v = len(G)
    visited = [False for _ in range(v)]
    distance = [float('inf') for i in range(v)]
    distance[s] = 0
    q = PriorityQueue()
    q.put(((-1) * distance[s], s))
    lastv = float('inf')
    while not q.empty():
        value, node = q.get()
        value *= (-1)
        if not visited[node]:
            visited[node] = True
            for neighbour, travel in G[node]:
                if distance[neighbour] > distance[
                    node] + travel and travel < lastv:  # warunek relaksacji, działa też f=value+travel i f
                    distance[neighbour] = distance[node] + travel
                    lastv = travel
                    q.put(((-1) * distance[neighbour], neighbour))

    if distance[t] == float('inf'): return False
    return True

# G=[[(1,10)],
#    [(0,10),(2,5)],
#    [(1,5),(3,4)],
#    [(2,4)]
#    ]
# G=[[(1,10)],
#    [(0,10),(2,5)],
#    [(1,5),(3,40)],
#    [(2,40)]
#    ]
# print(djisktra(G,0,3))
