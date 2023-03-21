#ALGORYTM SORTOWANIA KUBEŁKOWEGO:
#Sortowanie kubełkowe n elementowej tablicy polega na utworzeniu k+1 ilości kubełków; kazdy kubełek będzie przyjmoać wartosci w zakresie = k/max_value.
#Podczas iteracji przez tablicę, elementy wkąłdamy do odpowiadających im kubełków: indeks kubełka= zakres*element
#Następnie każdy kubełek o długości więszej niż 1, jest sortowany przez wstawianie. Po tym kroku kubełki są 'łączone' po kolei.
#[STABILNY]

#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna: O(n^2) - kiedy wszytkie elementy trafią do jednego kubełka - wtedy sortowanie przejdzie na insortra
#-średnia (gdy k=O(n)): O(n+n^2/k+k)=O(n)
#-optymistyczna: O(n+k)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(n+k)

def in_sort(t):
    n=len(t)
    for i in range(1,n):
        key=t[i]
        j=i-1
        while (j>=0 and key<t[j]):
            t[j+1]=t[j]
            j-=1
        t[j+1]=key
    return t

def bucket_sort(A):
    n=len(A)
    buckets_no=6
    rnge=buckets_no/(max(A))

    buckets=[]
    for _ in range(buckets_no+1):
        buckets.append([]) #dodac 'dno' do kubka

    for element in A:
        integer=int((rnge*element))
        buckets[integer].append(element)

    for i in range(buckets_no+1):
        if len(buckets[i])>1:
            buckets[i]=in_sort(buckets[i])
    x=0
    for i in range(buckets_no+1):
        for j in range (len(buckets[i])):
            A[x]=buckets[i][j]
            x+=1
    return A


# import random
# t = [random.randint(11,100) for i in range(10)]
# print(t)
# print(bucket_sort(t))