from queue import PriorityQueue


def restorePath(parents, s, t):
    shortestPath = []
    stops = [0 for i in range(len(parents))]
    parent = parents[t][0]
    while parent != (-1,-1):
        node, fuel = parent
        stops[node] += 1
        parent = parents[node][fuel]

    for i in range(len(parents)):
        if stops[i] != 0:
            shortestPath.append((i, stops[i] - 1))
    return shortestPath


def travel(G, s, t, prices, tankCapacity):  # graf podany jako lista sąsiadów
    v = len(G)
    visited = [[False for _ in range(tankCapacity + 1)] for j in range(v)]
    parents = [[(-1,-1) for _ in range(tankCapacity + 1)] for j in range(v)]
    distance = [[float('inf') for i in range(tankCapacity + 1)] for j in range(v)]
    distance[s][0] = 0
    q = PriorityQueue()
    q.put((distance[s][0], s, 0))  # dystans od punktu 's' do s, aktualnie rozwazany punkt, aktualnie paliwa w baku

    while not q.empty():

        distanceToS, node, fuel = q.get()
        if not visited[node][fuel]:
            visited[node][fuel] = True

            # rozważyć trzeba tankowanie --> przejscie w 'górę' po wierzchołku
            for i in range(fuel + 1, tankCapacity + 1):
                if distance[node][i] > distance[node][i - 1] + prices[node]:  # relasacja ale w tym przypadku dystancem jest cena za litr
                    distance[node][i] = distance[node][i - 1] + prices[node]
                    parents[node][i] = (node, i - 1)
                q.put((distance[node][i], node,i))
                         # na kolejke trzeba odlożyć każde przejscie ponieważ nadal jestesmy w tym samym punktcie, tlyko "idziemy do góry'

            # teraz rozważamy standardowo jak w djistrze miasta ktore sasiaduja z node
            for neigbour, travel in G[node]:
                if fuel >= travel:  # czyli jak mozna przejchać to
                    if distance[neigbour][fuel - travel] > distance[node][fuel]:  # relaksuję ale zamiast dodawać > +w to funkcję to spełnia [][f-w]
                        distance[neigbour][fuel - travel] = distance[node][fuel]
                        parents[neigbour][fuel - travel] = (node, fuel)

                    q.put((distance[neigbour][fuel - travel], neigbour, fuel - travel))

    print("distance: ", *distance, sep="\n")
    print("")
    print("parents: ", *parents, sep="\n")
    print("")
    print("visited: ", *visited, sep="\n")
    print("")
    return distance[t][0], parents
# G=[
#     [(1,7),(2,2)],
#     [(4,5),(3,6)],
#     [(3,10)],
#     [],
#     []
# ]
# prices=[5.5,9.8,2.6,7.1,8.2]
# capacity=7
# t=4


G = [
    [[1, 1], [2, 4]],
    [[0, 1], [3, 8]],
    [[0, 4], [4, 3]],
    [[1, 8], [4, 9]],
    [[2, 3], [3, 9], [5, 2]],
    [[4, 2]],
]
prices = [3, 8, 4, 2, 9, 100]
capacity = 5
t= 5

d, p=travel(G,0,t,prices,capacity)
print(d,restorePath(p,0,t))
