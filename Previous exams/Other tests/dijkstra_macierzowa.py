
from math import inf

def dijkstra(G,v):

    n = len(G)
    visited = [False] * n
    distance = [inf] * n
    parent = [-1] * n
    distance[v] = 0
    inx = v

    while True:
        print(inx)
        visited[inx] = True
        next_id = -1
        min_d = inf

        # znajdowanie krawędzi kolejnej
        for i in range(n):
            if not visited[i]:
            # aktualizcja minimalnje odlegosci sasiadow
                if G[inx][i] != -1 and distance[i]>distance[inx]+ G[inx][i]:
                    distance[i] = distance[inx] + G[inx][i]
                    parent[i] = inx
                # wybranie nastepengeo rozpatrywanego wierzcholka (takiego z min odlegloscia)
                if min_d>distance[i]:
                    next_id = i
                    min_d = distance[i]

        if next_id == -1: # jezeli jest -1 to wszystkie wierzcholki dostpene z v sa odwiedzone( nie sprawdza spojnosci)
            #return distance, parent
            return distance

        inx = next_id




'''G = [[-1, 6,-1, 5, 2],
[-1,-1, 1, 2,-1],
[-1,-1,-1,-1,-1],
[-1,-1, 4,-1,-1],
[-1,-1, 1,-1,-1]]'''
G = [
     [-1,4,-1,-1,6,2,-1],
     [4,-1,2,-1,-1,-1,-1],
     [-1,2,-1,2,-1,-1,-1],
     [-1,-1,2,-1,3,1,-1],
     [6,-1,-1,3,-1,5,2],
     [2,-1,-1,1,5,-1,7],
     [-1,-1,-1,2,7,-1]]
print(dijkstra(G,0))