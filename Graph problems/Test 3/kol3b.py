# Krzszysztof Wysocki
# Algorytm szukania ceny trasy polega na wpierw znalezieniu trasy przez drogi od A do B,
# następnie sprawdzanie są kolejne połączenia lotnicze między koljennymi miastami: A-->B----lot----C->D
# zwracany jest minnimalny koszt podróży.
# Wysraczy rozpatrywac tylko takie przelowty ponieważ jak chcemy poleciec ABC to taniej wyjdzie AC.

# Złożoność pamięciowa: O(n)
# Złożoność czasowa: O(n^2+mlogn)


from kol3btesty import runtests
from queue import PriorityQueue


def djisktra(G, s, t):
    v = len(G)
    visited = [False for _ in range(v)]
    distance = [float('inf') for i in range(v)]
    distance[s] = 0
    q = PriorityQueue()
    q.put((distance[s], s))

    while not q.empty():
        value, node = q.get()
        if node == t: break
        if not visited[node]:
            visited[node] = True
            for neighbour, travel in G[node]:
                if distance[neighbour] > distance[node] + travel:
                    distance[neighbour] = distance[node] + travel
                    q.put((distance[neighbour], neighbour))

    return distance


def airports(G, A, s, t):
    distanceST = djisktra(G, s, t)
    distanceTS = djisktra(G, t, s)
    miniumum = distanceST[t]

    for i in range(len(A)):
        for j in range(len(A)):
            miniumum = min(miniumum, (distanceST[j] + A[i] + A[j] + distanceTS[i]))
    return miniumum


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(airports, all_tests=True)
