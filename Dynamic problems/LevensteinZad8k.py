from zad8ktesty import runtests 

def napraw ( s, t ):
    ni=len(s)+1
    nj=len(t)+1
    print(s,t,ni,nj)
    f=[[0 for j in range(nj)] for i in range(ni)]
    for i in range(nj): f[0][i] = i
    for i in range(ni): f[i][0] = i
    for i in range(1,ni):
        for j in range(1,nj):
            if s[i-1]==t[j-1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j]=min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1
    # print(f)
    return f[ni-1][nj-1]
runtests ( napraw )


# def napraw ( s, t ):
#     print(s)
#     print(t)
#     n = len(s)
#     m = len(t)
#     R = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
#     return sol(s, t, n, m, R)
#
# def sol(s, t, n, m, R):
#     if R[m][n] >= 0:
#         return R[m][n]
#     if m == 0:
#         return n
#     if n == 0:
#         return m
#     if s[0] == t[0]:
#         x = sol(s[1:], t[1:], n - 1, m - 1, R)
#         R[m][n] = x
#         return x
#     x = min(sol(s[1:], t, n - 1, m, R) + 1, sol(s, t[1:], n, m - 1, R) + 1, sol(s[1:], t[1:], n - 1, m - 1, R) + 1)
#     R[m][n] = x
#     return x