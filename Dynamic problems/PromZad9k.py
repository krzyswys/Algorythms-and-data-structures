from zad9ktesty import runtests
from math import inf
def F(T,f,i,l1,l2):
    if i>len(T)-1:
        return 0
    if f[i][l1][l2] !=-1:
        return f[i][l1][l2]
    if T[i]>l1 and T[i]>l2:
        f[i][l1][l2]=0
        return 0
    if T[i]>l1:
        f[i][l1][l2]=F(T,f,i+1,l1,l2-T[i])+1
    elif T[i]>l2:
        f[i][l1][l2]=F(T,f,i+1,l1-T[i],l2)+1
    else:
        x=F(T,f,i+1,l1,l2-T[i])+1
        y=F(T,f,i+1,l1-T[i],l2)+1
        f[i][l1][l2]=max(x,y)
    return f[i][l1][l2]
def prom(P, g, d):
    f=[[[-1 for i in range(d+1)] for j in range(g+1)] for k in range(len(P))]
    w=F(P,f,0,g,d)
    # print(w)
    i=0
    l1=g
    l2=d
    sol=[]
    sol2=[]
    while i<len(P) and (l1>=P[i] or l2 >=P[i]):
        if P[i]>l1:
            w1=0
            w2=1
        elif P[i]>l2:
            w1=1
            w2=0
        else:
            w2=F(P,f,i+1,l1,l2-P[i])
            w1=F(P,f,i+1,l1-P[i],l2)
        if w1>w2:
            sol.append(i)
            l1=l1-P[i]
        else:
            sol2.append(i)
            l2=l2-P[i]
        i+=1
    if w-1 in sol:
        return sol
    else:
        return sol2



    return [0,w-1]

runtests ( prom )


# def prom(P, g, d):
#     x, y = sol(P, g, d, 0, [], [], 0)
#     return y
#
# def sol(P, g, d, i, L, R, last):
#     if i == len(P) or (P[i] > g and P[i] > d):
#         if last == 0:
#             return 0, L
#         else:
#             return 0, R
#     if g >= P[i] and d >= P[i]:
#         x, y = max(sol(P, g, d - P[i], i + 1, L, R + [i], 1), sol(P, g - P[i], d, i + 1, L + [i], R, 0))
#         x += 1
#         return x, y
#     elif g < P[i]:
#         x, y = sol(P, g, d - P[i], i + 1, L, R + [i], 1)
#         x += 1
#         return x, y
#     elif d < P[i]:
#         x, y = sol(P, g - P[i], d, i + 1, L + [i], R, 0)
#         x += 1
#         return x, y