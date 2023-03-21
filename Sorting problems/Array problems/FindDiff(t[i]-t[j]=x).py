def znajdz_roznice(t,x): #O(1)
    n=len(t)
    i=0
    j=0
    while i<=j:
        if(i==n or j==n):
            return None
        if (t[j] - t[i]) == x:
            return i, j
        elif (t[j]-t[i])>x:
            i+=1
        else:
            j+=1


#czesta technika do operowania na dancyh posortowanych, moze byc na kolowkium uzyte