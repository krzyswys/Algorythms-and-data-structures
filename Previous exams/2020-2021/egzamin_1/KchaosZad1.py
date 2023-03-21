from zad1testy import runtests
from queue import PriorityQueue


def in_sort(t):
    n = len(t)
    for i in range(1, n):
        key = t[i]
        j = i - 1
        while (j >= 0 and key < t[j]):
            t[j + 1] = t[j]
            j -= 1
        t[j + 1] = key
    return t


def bucket_sort(A, y):
    n = len(A)
    buckets_no = 6
    rnge = buckets_no / y

    buckets = []
    for _ in range(buckets_no + 1):
        buckets.append([])

    for element in A:
        integer = int((rnge * element[0]))
        buckets[integer].append(element)

    for i in range(buckets_no + 1):
        if len(buckets[i]) > 1:
            buckets[i] = in_sort(buckets[i])
    x = 0
    for i in range(buckets_no + 1):
        for j in range(len(buckets[i])):
            A[x] = buckets[i][j]
            x += 1
    return A


def chaos_index(T):
    y = max(T)
    T = [(T[i], i) for i in range(len(T))]
    # T.sort(key=lambda x: x[0])
    T = bucket_sort(T, y)
    A = [abs(T[i][1] - i) for i in range(len(T))]
    return max(A)


def chaos_indexx(T):
    q = PriorityQueue()
    [q.put((T[i], i)) for i in range(len(T))]
    ans = 0
    for i in range(len(T)):
        num, id = q.get()
        ans = max(abs(id - i), ans)
    return ans


runtests(chaos_index)
