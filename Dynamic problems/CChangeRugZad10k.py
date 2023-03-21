from zad10ktesty import runtests


def answer(iteracje):
    ans = []

    def rek(index):
        i, value = index
        if i != -1:
            rek(iteracje[i])
            ans.append(value)

    rek(iteracje[-1])
    return ans


def dywany(N):
    print(N)
    f = [N + 1 for i in range(N + 1)]
    iteracje = [[-1, -1] for i in range(N + 1)]
    f[0] = 0
    for i in range(N + 1):
        s = 1
        while i - s * s >= 0:
            if f[i - s * s] < f[i]:  # +1
                f[i] = f[i - s * s] + 1
                iteracje[i] = [i - s * s, s]  # [a,value]
            s += 1
    print(f)

    return answer(iteracje)  # Tutaj proszę wpisać własną implementację


runtests(dywany)
