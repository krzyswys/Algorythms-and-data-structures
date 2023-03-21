from zad5testy import runtests
import queue


def plan(T):
    n = len(T)
    pending = queue.PriorityQueue()
    fuel = 0
    # stops = [0 for i in range(n)]
    answer = []
    for i in range(n-1):
        if T[i] != 0: pending.put(((-1) * T[i], [i]))
        if fuel == 0:
            refill, index = pending.get()
            fuel += (-1) * refill
            # stops[index] = 1
            answer+=index

        fuel -= 1
    # answer = []
    # [answer.extend(index) for index in range(n) if stops[index] != 0]
    return sorted(answer)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)