from queue import PriorityQueue

#minimum time it takes for all the n nodes to receive the signal
def NDT(G, s):  # graf jako lista sasiadów
    v = len(G)
    visited = [False for _ in range(v)]
    distance = [float('inf') for i in range(v)]
    distance[s] = 0
    q = PriorityQueue()
    q.put((distance[s], s))
    while not q.empty():
        weight, node = q.get()
        if not visited[node]:
            visited[node]=True
            if False not in visited:
                return weight
            for currWeight, v in graph[node]:
                if distance[node] + currWeight < distance[v]: # and not visited[v]:
                    distance[v] = distance[node] + currWeight
                    q.put((distance[v], v))
    return -1
