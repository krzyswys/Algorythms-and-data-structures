from zad1testy import runtests

def lnds(t):
    n=len(t)
    f=[1 for i in range(n)]
    p = [-1 for i in range(n)]
    maxi=0
    for i in range(n):
        for j in range(i):
            if t[i]>t[j] and f[i]<f[j]+1:
                # f[i]=max(f[i],f[i-j]+1)
                f[i]=f[j]+1
                p[i]=j
        if f[i]>f[maxi]:
            maxi=i
    x = []
    def printSol(t,p,i,x):
            if p[i]!=-1:
                printSol(t,p,p[i],x)
            x.append(t[i])
    printSol(t,p,maxi,x)
    return f[maxi],x

def intuse( I, x, y ):
    # x=djisktra(I,x,y)
    x=[]
    return x

# I=[[3, 4], [2, 5], [1, 3], [4, 6], [1, 4]]
# x=1
# y=6
# print(intuse(I,x,y))
runtests( intuse )


