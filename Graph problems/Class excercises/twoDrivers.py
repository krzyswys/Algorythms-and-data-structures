from queue import PriorityQueue

def djistra(G,s,t):
    v=len(G)
    visited=[False for i in range(v)]
    distance=[float('inf') for i in range(v)]
    distance[s]=0
    q=PriorityQueue()
    q.put((distance[s],s))
    while not q.empty():
        value, node = q.get()
        if not visited[node]:
            visited[node]=True
            for neigbour, travel in G[node]:
                if distance[neigbour]>distance[node]+travel:
                    distance[neigbour]=distance[node]+travel
                    q.put((distance[neigbour], neigbour))
    print(distance)
    if visited[t]: return distance[t]
    return -1

def procreate(A,num):
    v=len(A)
    G=[[] for i in range(num*v)]
    for i, list in enumerate(A):
        for u, value in list:
            G[i].append((v+u,value))
            G[v+i].append((u,value))

    return G
def driver(G,drivers):
    n=len(G)
    G=procreate(G,drivers)
    v=len(G)
    for i in range(drivers):
        for j in range(drivers):
            val=djistra(G,i*n,v-j*n-1)
            print(val)
            print(i*n,v-j*n-1 )


G=[
    [(1,3),(3,7)],
    [(2,8)],
    [(4,4)],
    [(2,2)],
    []
]
print(driver(G,2))
