#Krzysztof Wysocki
#Zaprezentowany algorytm korzysta z sortowania przez kubełkowanie. Zakres każdego kubkna jest obliczany według wzoru: (a,b)-najwiekszy możliwy przedział wyrbany z tablicy P
#buckets_no - liczba wykorzystywanych kubełków: [(b-a)//buckets_no]. Każdy kubełek jest następnie uzupełaniany o odpowiadające mu wartości.
#Następnym krokiem jaki należy wykonać jest posortowanie każdego z kubełków. Po wykonaniu tejże operacji wystarczy połączyć kubełki w kolejności rosnącej w jedą listę.
#ZŁOŻONOŚĆ CZASOWA:
# O(n) [w najgorszym przypadku: O(n^2)
#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(n)


from zad3testy import runtests

def InSort(t):
    n=len(t)
    for i in range(1,n):
        key=t[i]
        j=i-1
        while (j>=0 and key<t[j]):
            t[j+1]=t[j]
            j-=1
        t[j+1]=key
    return t

def BucketSort(A,P):
    n=len(A)
    buckets_no=(n//8)
    max_v=max(A)

    buckets=[]
    for _ in range(buckets_no+1):
        buckets.append([]) #dodac 'dno' do kubka

    for element in A:
        integer=int(buckets_no*element/max_v)
        buckets[integer].append(element)

    for i in range(buckets_no+1):
        if len(buckets[i])>1:
            buckets[i]=InSort(buckets[i])
    k=0
    for i in range(buckets_no+1):
        for j in range (len(buckets[i])):
            A[k]=buckets[i][j]
            k+=1
    return A

def SortTab(T,P):
    T=BucketSort(T,P)

    return T

runtests( SortTab )
