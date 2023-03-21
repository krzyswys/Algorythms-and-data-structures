from zad7ktesty import runtests


def odlegosci(T, x, depth, width):
    y = 0
    l, r = x - 1, x + 1
    while y < depth:
        if l - 1 >= 0 and T[y][l - 1] != 0:
            l -= 1
        if r + 1 < width and T[y][r + 1] != 0:
            r += 1
        y += 1
    return l, r


def suma(T, x, depth, width):
    l, r = odlegosci(T, x, depth, width)
    SUM = 0
    for i in range(depth):
        for j in range(l, r + 1):
            SUM += T[i][j]
    return SUM


def ogrodnik(T, D, Z, l):  # pole, lokalizacje, zysk, litry
    depth = len(T)
    width = len(T[0])
    trees = len(D)

    weight = [0 for i in range(trees)]
    f = [[0 for i in range(l + 1)] for j in range(trees)]
    m = 0
    for i in range(width):
        if T[0][i] != 0:
            weight[m] = suma(T, i, depth, width)
            m += 1
    # print(weight)
    # print(l)
    for i in range(trees):
        for j in range(l + 1):
            if j >= weight[i]:
                f[i][j] = max(Z[i] + f[i - 1][j - weight[i]], f[i - 1][j])
            else:
                f[i][j] = f[i - 1][j]

    return f[trees - 1][l]


runtests(ogrodnik, all_tests=True)


# def ogrodnik (T, D, Z, l):
#     for i in range(len(T)):
#         print(T[i])
#     print(D)
#     print(Z)
#     print(l)
#     S = [[0 for _ in range(l + 1)] for _ in range(len(D))]
#     return sol(T, D, Z, l, 0, len(T), len(T[0]), S)
#
# def sol(T, D, Z, l, a, n, m, S):
#     if S[l] != 0:
#         return S[l]
#     if a == len(D):
#         return 0
#     toVis = [D[a]]
#     cost = 0
#     for el in toVis:
#         for i in range(n):
#             if T[i][el] == 0:
#                 continue
#             if el - 1 >= 0 and T[i][el - 1] != 0 and el - 1 not in toVis:
#                 toVis.append(el - 1)
#             if el + 1 < m and T[i][el + 1] != 0 and el + 1 not in toVis:
#                 toVis.append(el + 1)
#             cost += T[i][el]
#     if cost <= l:
#         x = max(sol(T, D, Z, l - cost, a + 1, n, m, S) + Z[a], sol(T, D, Z, l, a + 1, n, m, S))
#         # S[l] = x
#         # print(S)
#         return x
#     else:
#         x = sol(T, D, Z, l, a + 1, n, m, S)
#         # S[l] = x
#         # print(S)
#         return x
