from queue import PriorityQueue

def djikstra(G,s,t):
    v=len(G)
    distance=[[float('inf'),float('inf')]for i in range(v)] #tablica na przyjście z użyciem butów i bez użycia
    distance[s][0]=0 #zaczynamy bez użycia
    # distance[s][1]=0
    visited = [[False,False] for i in range(v)]
    # visited[s][0]=True
    visited[s][0]=True
    q=PriorityQueue()
    used=0 #parametr mowi o tym czy użyliśmy czy nie
    q.put((distance[s][0],s,used))
    while not q.empty():
        travel,node, used=q.get()
        for i in range(v): # w tej pętli wrzucamy do kolejki jak w zwyklej djikstrze, tj bez użycia butów
            if G[node][i]!=0:
                if distance[i][0]>travel+G[node][i]:
                    distance[i][0] = travel + G[node][i]
                    q.put((distance[i][0], i, 0))

        if used==0: #oraz ttuaj jeżeli wcześniej nie zostało użyte to wrzucamy wszystkei możliwsci z użyciem butów
            for i in range(v):
                if G[node][i] != 0:
                    for j in range(v):
                        if G[i][j]!=0:
                            k=max(G[node][i],G[i][j])
                            if distance[j][1]>travel+k:
                                distance[j][1] = travel + k
                                q.put((distance[j][1],j,1))
    return min(distance[t][0],distance[t][1])







G = [
    [0,1,0,0,0],
    [1,0,1,0,0],
    [0,1,0,7,0],
    [0,0,7,0,8],
    [0,0,0,8,0],
     ]
print(djikstra(G,0,4))