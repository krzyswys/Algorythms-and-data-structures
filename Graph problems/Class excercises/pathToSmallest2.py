# wartości na krawędziach nie powtarzają się, jeżeli tak to
# trzeba wproadzić ograniczenie relaksacji do K razy,
# gdzie K to max( ilosc wystąpień kazdej liczby)

def pathToSmallest2(E,K): #graf podany jako lista krawędzi
    # edgde=(parent, node, value)
    E=E.sort(key=lambda x: x[2], reverse=True)
    e = len(E)
    visited = [False for i in range(e)]
    distance = [float('inf') for i in range(e)]
    distance[s] = 0

    for _ in range(K):
        for i, list in enumerate(G):
            for travel, neighbour in list:
                if distance[neighbour] > distance[i] + travel:
                    distance[neighbour] = distance[i] + travel

    for i, list in enumerate(G):
        for travel, neighbour in list:
            if distance[neighbour] > distance[i] + travel:
                print("Występuje cykl ujemny")
                return False

    return distance

