from zad6ktesty import runtests


def haslo(S):
    if not S:
        return 0
    if S[0] == "0":
        return 0
    n = len(S)
    dp = [0 for x in range(n + 1)]
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if (
            int(S[i - 1 : i]) != 0
        ):  # jak pojedyncza liczba aktualna nie jest 0 to znaczy ze można ja zdekowdowac
            dp[i] += dp[i - 1]
        if (
            10 <= int(S[i - 2 : i]) <= 26
        ):  # jak podwojna aktualna liczba jest <26 i >10 to rowniez mozna ja zdekodowac
            dp[i] += dp[i - 2]  # drugi sposob
    return dp[n]


runtests(haslo)


# def haslo ( S ):
#     print(S)
#     n = len(S)
#     T = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
#     for i in range(n + 1):
#         T[i][i] = 1
#     return sol(S, T, 0, n)
#
# def sol(S, T, b, e):
#     if T[b][e] != 0:
#         return T[e][b]
#     if e - b < 2:
#         return 1
#     if e - b == 2:
#         if int(S[b:e]) < 27:
#             return 2
#         else:
#             return 1
#     x = 0
#     for i in range(b + 1, e):
#         if 0 < int(S[b:i]) < 27:
#             x += sol(S, T, i, e)
#         else:
#             break
#     return x
