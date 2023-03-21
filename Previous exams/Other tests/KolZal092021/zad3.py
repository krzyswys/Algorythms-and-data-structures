from zad3testy import runtests
from queue import PriorityQueue


def restorePath(parents, s, t):
        parent = parents[t]
        shortestPath = [(parent,t)]
        while parent != s:
            shortestPath.append((parents[parent], parent))
            parent = parents[parent]

        shortestPath.append((parents[parent], parent))

        return shortestPath[::-1]


def djisktra(G, s,t):  # graf podany jako lista sąsiadów
    v = len(G)
    visited = [False for _ in range(v)]
    distance = [float('inf') for i in range(v)]
    distance[s] = 0
    q = PriorityQueue()
    q.put((distance[s], s))

    while not q.empty():
        value, node = q.get()
        if not visited[node]:
            visited[node] = True
            for neighbour, travel in G[node]:

                if distance[neighbour] > distance[node] + travel:  # warunek relaksacji, działa też f=value+travel i f
                    distance[neighbour] = distance[node] + travel
                    q.put((distance[neighbour], neighbour))

    return distance
def paths(G,s,t):
    ans=0
    dst1=djisktra(G,s,t)
    if dst1[t]==float('inf'): return 0
    dst2=djisktra(G,t,s)
    for u,egdes in enumerate(G):
        for v, val in egdes:
            if dst1[u]+val+dst2[v]==dst1[t]:
                ans+=1
    return ans

# G=[ [(1,2),(2,4)],
#       [(0,2),(3,11),(4,3)],
#       [(0,4),(3,13)],
#       [(1,11),(2,13),(5,17),(6,1)],
#       [(1,3),(5,5)],
#       [(3,17),(4,5),(7,7)],
#       [(3,1),(7,3)],
#       [(5,7),(6,3),]]
# print(djisktra(G,0,7))
runtests( paths )


