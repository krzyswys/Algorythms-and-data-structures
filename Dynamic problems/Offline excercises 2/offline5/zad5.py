# Krzysztof Wysocki
#     Zaprezzentowny algrytm rozwiązujący problem podany w zadaniu działa w sposób nastepnujący: przesuwamy się po trasie i każdą, niepustą,
#     plamę zapisujemy do kolejki prorytetowej w taki sposób aby plama o najwiekszej pojemnosci zawsze była jako pierwsza.
#     W momencie kiedy skończy się paliwo pobieramy pierwsza stację i jej index konkatenujemy do answer.
#     Na końcu wystarczy posortować answer.

# Złożoność pamięciowa: O(n)
# Złożoność czasowa: n*logn--> O(nlogn)

from zad5testy import runtests
import queue

def plan(T):
    pending,fuel, answer, n = queue.PriorityQueue(), 0, [], len(T)
    for i in range(n):
        if fuel==0 and i==n-1:
            break
        if T[i] != 0: pending.put(((-1) * T[i], [i]))
        if fuel == 0:
            refill, index = pending.get()
            fuel += (-1) * refill
            answer+=index
        fuel -= 1
    answer=sorted(answer)
    return answer

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(plan, all_tests=True)
