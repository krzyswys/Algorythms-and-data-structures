from queue import PriorityQueue
from zad2testy import runtests

# Zaczynamy z 0 czasem, następnie sprawdzamy czy dana komórka została dowiedzona jak nie to sprawdzamy czy czas obecny poprawi ten poprzedni,
# jeśli tak to aktualizuemy wartość oraz wrzucamy do kolejki:
# - Wartości związane z obrotem, tj:
#       czas+45, aktualny x,y bo nie przemieszczamy się, kierunek w -90^ i 90^, stan predkosci(0) - bo stoi
# - Wartości związane z poruszaniem się w przód, tj:
#       jak poprzednia predkosc to stan 0, to znaczy ze 1 etap rozpędzania, jak 1> to znaczy ze rozpedzony więc: czas+rozpędzanie, nowy xy, kierunek, kolejny stan predkosci
# Na końcu wystarczy przejrzeć wszystkie możliwe stany końcowe: stany predkosci*kierunki


def robot(L, A, B):
    distance = [[[[float('inf') for i in range(3)] for m in range(4)] for j in range(len(L[0]))] for k in range(len(L))]
    visited = [[[[False for i in range(3)] for m in range(4)] for j in range(len(L[0]))] for k in range(len(L))]
    # tablica na każdy stan predkości | tablica na każdy kierunek | kolumn | wierszy

    vector = {0: (1, 0), 1: (0, 1), 2: (-1, 0), 3: (0, -1)}
    moves = {(1, 0): 1, (0, 1): 2, (-1, 0): 3, (0, -1): 0}
    speed = [60, 40, 30]

    startX, startY = A
    endX, endY = B

    q = PriorityQueue()
    q.put((0, startX, startY, 0, 0))

    while not q.empty():
        time, x, y, direction, lastSpeed = q.get()
        if not visited[y][x][direction][lastSpeed] and L[y][x] != 'X':
            visited[y][x][direction][lastSpeed] = True

            if distance[y][x][direction][lastSpeed] > time:
                distance[y][x][direction][lastSpeed] = time

                # obrót:
                vec = vector[direction]
                q.put((time + 45, x, y, moves[vec], 0))
                q.put((time + 45, x, y, moves[((-1) * vec[0], (-1) * vec[1])], 0))

                # jazda do przodu:
                x, y = x + vec[0], y + vec[1]
                if lastSpeed == 0:
                    q.put((time + speed[lastSpeed], x, y, direction, 1))
                else:
                    q.put((time + speed[lastSpeed], x, y, direction, 2))
    # print(*distance, sep="\n")
    # tab=[[0 for i in range(len(L[0]))]for j in range(len(L))]
    # for k in range(len(L)):
    #     for m in range(len(L[0])):

    ans = float('inf')
    for i in range(4):
        for j in range(3):
                ans = min(ans, distance[endY][endX][i][j])

            # tab[k][m]=ans
    # print(*tab,sep="\n")
    if ans == float('inf'): return None
    return ans


runtests(robot)
