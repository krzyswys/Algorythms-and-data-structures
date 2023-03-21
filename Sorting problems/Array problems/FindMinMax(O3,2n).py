
#max na 0 i przechodzimy po kolejnych komorkach i porownójemy z maxem
#bierzemy 1 pare le i je porwonujemy w sordu i na mniejsza poronowjemy z min gloablnym i zapisujemy,
# tak samo z max. Potem druga para itd-> jedno porownanie dla pare, 1 dla min, jedno dla min -> co najmniej jedno dale kazdej komwokri i par: n/n+n =3/2n

def min_max(t):
    n=len(t)
    min=max=t[n-1]
    i=0
    while(i<n-1):
        if (t[i]>=t[i+1]):
            if(t[i]>max):
                max=t[i]
            elif(t[i+1]<min):
                min=t[i+1]
        else:
            if (t[i+1] > max):
                max = t[i+1]
            elif (t[i] < min):
                min = t[i]
        i+=2
    return min,max

# import random
#t=[3,8,2,1,7,10]
#t=[random.randint(1,100) for i in range(10000001)]
#print(min_max(t))