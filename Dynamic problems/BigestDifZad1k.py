from zad1ktesty import runtests

def roznica( S ):
    n=len(S)
    if '0' not in S: return -1
    s=[1 if S[i]=='1' else 0 for i in range(n)]
    f=[[0 for i in range(n)] for j in range(n)]
    maxt=0
    for i in range(n):
        for j in range(i+1,n):
            if s[j]==1:x=-1
            elif s[j]==0:x=1
            f[i][j]=f[i][j-1]+x
            maxt=max(maxt,f[i][j])
    return maxt

runtests ( roznica )

# def roznica( S ):
#     n = len(S)
#     T = [[-2 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         T[i][i] = -1
#     return sol(S, T, 0, n - 1)
#
# def sol(S, T, b, e):
#     if T[b][e] != -2:
#         return T[b][e]
#     c = 0
#     for i in range(b, e + 1):
#         if S[i] == '0':
#             c += 1
#         else:
#             c -= 1
#     if c < 0:
#         T[b][e] = -1
#     else:
#         T[b][e] = c
#     return max(T[b][e], sol(S, T, b, e - 1), sol(S, T, b + 1, e))