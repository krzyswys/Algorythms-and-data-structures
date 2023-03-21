X=[(7, 3, 4, 7), (7, 1, 3, 19), (2, 14, 15, 3), (3, 3, 5, 3), (3, 6, 7, 3), (3, 5, 7, 19), (3, 1, 17, 19), (4, 7, 8, 7), (3, 10, 14, 11), (2, 9, 10, 11)]
P=20 #48
# X=[(2, 1, 5, 3), (3, 7, 9, 2), (2, 8, 11, 1)]
# P=5 #14
# X=[(3, 1, 2, 7), (2, 1, 7, 19), (3, 1, 4, 3), (2, 5, 6, 11), (3, 1, 10, 3)]
# P=40 #27
# X=[(7, 3, 4, 27), (2, 23, 32, 19), (3, 2, 19, 67), (3, 1, 27, 75), (3, 66, 70, 99), (2, 1, 34, 59), (3, 1, 10, 79), (2, 59, 68, 27), (3, 12, 26, 63), (3, 31, 39, 75), (2, 34, 79, 51), (3, 1, 38, 51), (2, 12, 23, 83), (3, 1, 25, 47), (2, 26, 62, 19), (3, 7, 18, 31), (4, 38, 51, 43), (3, 25, 34, 63), (3, 58, 69, 39), (2, 1, 20, 15), (3, 24, 30, 43), (2, 45, 68, 15), (3, 16, 29, 87), (2, 1, 82, 87), (3, 68, 69, 95), (3, 1, 69, 95), (2, 22, 50, 39), (3, 45, 79, 91), (3, 1, 42, 23), (2, 13, 17, 83), (3, 96, 98, 71), (2, 29, 47, 95), (3, 14, 105, 35), (4, 47, 53, 39), (3, 10, 39, 67), (4, 27, 73, 3), (3, 34, 35, 43), (2, 59, 81, 15), (3, 32, 43, 83), (4, 51, 96, 47), (3, 60, 85, 43), (4, 27, 41, 15), (3, 38, 44, 71), (3, 1, 14, 75), (3, 82, 152, 11), (4, 51, 56, 31), (3, 58, 87, 55), (4, 33, 59, 51), (3, 88, 118, 87), (2, 1, 54, 99), (3, 1, 85, 31), (2, 61, 68, 43), (3, 86, 118, 95), (2, 49, 93, 7), (3, 52, 55, 55), (4, 65, 101, 11), (3, 58, 62, 7), (3, 61, 65, 3), (4, 58, 59, 47), (3, 25, 43, 27), (3, 34, 58, 55), (3, 53, 74, 67), (3, 54, 66, 75), (2, 117, 190, 31), (3, 74, 104, 15), (4, 57, 70, 11), (3, 62, 68, 51), (4, 79, 98, 59), (3, 118, 130, 15), (4, 61, 68, 83), (3, 80, 147, 27), (4, 67, 80, 15), (3, 66, 68, 7), (3, 67, 69, 43), (2, 58, 79, 95), (3, 105, 191, 75), (2, 82, 150, 83), (3, 103, 108, 79), (3, 34, 47, 59), (3, 115, 119, 75), (3, 68, 94, 51), (4, 123, 126, 79), (3, 86, 106, 63), (4, 103, 162, 11), (3, 76, 78, 43), (4, 47, 61, 39), (3, 56, 77, 43), (3, 129, 132, 23), (3, 96, 108, 95), (4, 139, 184, 47), (3, 114, 145, 63), (2, 55, 118, 95), (3, 184, 279, 51), (4, 125, 146, 91), (3, 98, 134, 75), (4, 83, 158, 63), (3, 88, 134, 55), (2, 59, 94, 31), (3, 116, 121, 31), (4, 69, 74, 71)]
# P=200 #853
X=[(3, 3, 4, 19), (3, 11, 17, 7), (4, 8, 15, 15), (3, 1, 7, 15), (4, 12, 17, 7), (3, 1, 7, 3), (4, 8, 9, 7), (3, 11, 18, 15), (4, 20, 31, 19), (3, 17, 26, 7)]
P=20

def countbuildings(b,m,t):
    lb=len(b)
    lm=len(m)
    answer=[]
    for i in range(lm):
        for j in range(lb):
            if m[i]==t[b[j]]:
                answer.append(i)
    return answer
def ks(t, P):
    n = len(t)
    f = [[0 for i in range(P + 1)] for j in range(n)]
    buildings = [[[] for i in range(P + 1)] for j in range(n)]
    num =[0 for i in range(n)]

    m=t.copy()
    t = sorted(t, key=lambda x: x[2])
    maxv=0
    maxi=0
    for i in range(n):
        h, a, b, w = t[i]

        v= h * (b - a)
        for j in range(P + 1):
            for k in range(n):
                if w <= j:
                    if  f[i - k][j - w] + v>=f[i][j] and (t[i-k])[2]<a:
                        f[i][j]=f[i - k][j - w] + v

                        buildings[i][j] = buildings[i - k][j - w].copy()
                        if i not in buildings[i][j]:
                                buildings[i][j].append(i)
                    elif v>f[i][j]:
                        f[i][j]=v

                        buildings[i][j]=buildings[i][j].copy()
                        if i not in buildings[i][j]:
                            buildings[i][j].append(i)
        if f[i][P]>maxv:
            maxi=i
            maxv=f[i][P]
    print(maxi)




    for i in range(n):
        for j in range(P+1):
           print("[", end="")
           print(f[i][j], end="] ")
        print("")


    answer=countbuildings(buildings[maxi][P],m,t)
    # buildings2 = [[[] for i in range(P + 1)] for j in range(n)]
    # for i in range(n):
    #     for j in range(P+1):
    #         buildings2[i][j].append(countbuildings(buildings[i][j],m,t))

    # maximum=max(f)
    # maxi=f.index(maximum)
    # # print(maximum)
    # maxval=0
    # for i in range(len(f[maxi])):
    #
    #     if f[maxi][i]>maxval:
    #         maxj=i
    #         maxval=f[maxi][i]

    # print(f[99][maxj])
    # print(buildings[maxi][maxj])

    return f,buildings[n-1][P],answer,m,t, buildings,0


a,b,c,d,e,f,g=ks(X,P)
print(X)
# print(sorted(X, key=lambda x: x[1]))
# print(a)
# print( a.index(0)  )
# print(b)
print(c)
# print(d)
# print(e)
# print(f)
# print(g)
# print(X)


# def canUse(t,el):
#     if len(t)!=0 and len(el)!=0:
#         h,a,b,w=el
#         for i in range(len(t)):
#             h2,a2,b2,w2=t[i]
#             if (a2 <= a and a <= b2) or (a2 <= b and b<= b2):
#                 return False
#         return True
#     return False
#
# def val(t):
#     val=0
#     for h,a,b,w in t:
#         val+=h * (b - a)
#     return val
# def ks(t,P):
#     n=len(t)
#     m=t
#     f=[[[(0,0,0,0)] for i in range(P+1)] for j in range(n)]
#     t=sorted(t,key=lambda x:(x[0]*(x[2]-x[1])))
#     q = max(t, key=lambda x: x[2])
#
#     for i in range(n):
#         h, a, b, w = t[i]
#         p = h * (b - a)
#
#
#         for j in range(P+1):
#             t1 = f[i - 1][j]
#             t2 = f[i - 1][j - w]
#             if w<=j:
#                 if val(t1)<=((val(t2))+p):
#
#                     if canUse(t2,t[i]):
#                         t2.append(t[i])
#                         f[i][j] = t2
#                     else:
#                         f[i][j] = t1
#
#                 else:
#                     f[i][j] = t1
#             else:
#                 f[i][j]=t1
#     c=[]
#     for i in range(len(f[n-1][P])-1):
#         for j in range(len(m)):
#             if m[j]==f[n-1][P][i+1]:
#                 c.append(j)
#     c=sorted(c)
#     # print(c)
#     return  c
# def canUse(builings,i,t):
#     b=len(builings)
#     n=len(t)
#     ai,bi,ci,di=t[i]
#     for j in range(b):
#         ab, bb, cb, db =t[builings[j]]
#         if (bb<=bi<=cb) or(bb<=ci<=cb): #jak zachodzi
#             return False
#     return True
# def countbuildings(b,m,t):
#     lb=len(b)
#     lm=len(m)
#     answer=[]
#     for i in range(lb):
#         for j in range(lm):
#             if m[j]==t[b[i]]:
#                 answer.append(j)
#     return sorted(answer)
# def ks(t, P):
#     n = len(t)
#     f = [[0 for i in range(P + 1)] for j in range(n)]
#     buildings = [[[] for i in range(P + 1)] for j in range(n)]
#     buildings2 = [[[] for i in range(P + 1)] for j in range(n)]
#     m=t.copy()
#     t = sorted(t, key=lambda x: x[0]*(x[1]-x[2]))
#
#     for i in range(n):
#         h, a, b, w = t[i]
#         v = h * (b - a)
#
#         for j in range(P + 1):
#             if w <= j:
#                 if (f[i - 1][j] <= f[i - 1][j - w] + v) and (canUse(buildings[i - 1][j - w],i,t)):
#                     f[i][j] = f[i - 1][j - w]+v
#                     buildings[i][j]=buildings[i - 1][j - w].copy()
#                     if i not in buildings[i][j]:
#                         buildings[i][j].append(i)
#                 else:
#                     f[i][j] = f[i - 1][j]
#                     buildings[i][j] = buildings[i - 1][j].copy()
#             else:
#                 f[i][j] = f[i - 1][j]
#                 buildings[i][j] = buildings[i - 1][j].copy()
#
#     answer=countbuildings(buildings[n-1][P],m,t) #-18 na 6
#
#     for i in range(n):
#         for j in range(P+1):
#             buildings2[i][j].append(countbuildings(buildings[i][j],m,t))
#
#
#
#     return answer

# def ks(t, P):
#     n = len(t)
#     f = [[0 for i in range(P + 1)] for j in range(n)]
#     buildings = [[[] for i in range(P + 1)] for j in range(n)]
#
#     m=t.copy()
#     t = sorted(t, key=lambda x: x[1])
#
#     for i in range(n):
#         h, a, b, w = t[i]
#
#         v = h * (b - a)
#         for j in range(P + 1):
#             for k in range(1,n):
#                 if w <= j:
#                     if (f[i - k][j] <= f[i - k][j - w] + v) and (a<(t[i-1])[2]):
#                         f[i][j] = f[i - k][j - w]+v
#                         buildings[i][j]=buildings[i - 1][j - w].copy()
#                         if i not in buildings[i][j]:
#                             buildings[i][j].append(i)
#                     else:
#                         f[i][j] = f[i - k][j]
#                         buildings[i][j] = buildings[i - k][j].copy()
#                 else:
#                     f[i][j] = f[i - k][j]
#                     buildings[i][j] = buildings[i - 1][j].copy()
#
#
#
#     answer=countbuildings(buildings[n-1][P],m,t)
#     return answer