def znajdz_sume(t,x): #O(1) #posotrowane
    n=len(t)
    i=0
    j=n-1
    while i<=j:
        if(i==n or j==n):
            return None
        if (t[j] + t[i]) == x:
            return i, j
        elif (t[j]+t[i])<x:
            i+=1
        else:
            j-=1

x=[1,1,1,3,4,90,91]
print(znajdz_sume(x,95))