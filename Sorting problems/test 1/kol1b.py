#Krzysztof Wysocki
#Przedstawiony algorytm składa się z 3 części:
#   - Sortowania malejąco według długości przedstawionego na wykładzie: QuickSort, polegającego na wybieraniu elementu i
# przestwaianiu elementow <= na jedna stonę a > na drugą, następnie wywoływanie tegoż sortowania rekurencyjnie na obu powstałych częsciach.
#    - Sprawdzaniu czy dane dwa wyrazy są anaagrami: do jednej tablicy o dlugosci alfabetu zliczana jest ilosc wystąpein danej listery z pierwszego wyrazu, a następnie iterując
# po literach drugiego wyrazu napotkane litery 'sa odejmowane' w tablicy. Jeżlei w tablicy pozostanie 0 to znaczy że wyrazy są anaagramami.
#   - Iterowaniu przez kolejne wyrazy w danej tablicy i wpisywaniu do nowej tablicy liczby anaagramow jaki tworzy ten wyraz. Zwracana jest wartosc max z tejże tablicy

#ZŁOŻONOŚĆ:
#-Czasowa: nlogn + d(dligosc danego wyrazu) + n^2 --> O(n^2)
#-Pamięciowa: n + k (dl alfabetu) + n --> O(n+k), gdzie k to długość alfabetu


from kol1btesty import runtests
# def quick_sort(t,l,r):
#     while(l<r):
#         x=len(t[r])
#         i=l-1
#         for j in range(l,r):
#             if len(t[j])>=x:
#                 i+=1
#                 t[i],t[j]=t[j],t[i]
#         t[i+1],t[r]=t[r],t[i+1]
#         q=i+1
#         quick_sort(t,l,q-1)
#         l=q+1
#     return t
def quick_sort(t,l,r): #z wykładów
    while l<r:

        x = len(t[r]) #pivot section-----------------
        i = l - 1
        for j in range(l, r):
            if len(t[j]) >= x:
                i += 1
                t[i], t[j] = t[j], t[i]
        t[i + 1], t[r] = t[r], t[i + 1]
        q=i+1   # return i + 1 ------------------

        quick_sort(t,l,q-1)
        l=q+1
    return t

def is_anaagram(A,B): #
    k=ord('z')-ord('a')+1
    t=[0]*k
    for j in range(len(A)):
        t[ord(A[j])-ord('a')]+=1
    for j in range(len(A)):
        index=ord(B[j]) -ord('a')
        t[index]-=1
        if t[index]<0:
            return False
    return True

def counting_sort(A):
    n=len(A)
    k=0
    for i in range(n):
        x=len(A[i])
        k=max(x,k)
    C=[0]*(k+1)
    B=[0]*k
    for i in range(n):
        C[len(A[i])]+=1
    for j in range(1,k):
        C[j]=C[j]+C[j-1]
    l=n-1
    while l>=0:
        B[C[len(A[l])]-1]=A[l]
        C[len(A[l])]-=1
        l-=1

def f(T):
    n = len(T)
    # T = quick_sort(T, 0, n - 1)
    T=sorted(T,key=len)
    tab = [0] * n

    for i in range(n):
        for j in range(i,n):
            word1 = T[i]
            word2 = T[j]
            if len(word1) == len(word2):
                if is_anaagram(word1, word2):
                    tab[i] += 1
            else:
                continue
    return max(tab)


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( f, all_tests=True)
