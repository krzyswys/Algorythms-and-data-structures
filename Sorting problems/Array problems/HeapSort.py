#ALGORYTM SORTOWANIA PRZEZ KOPCOWANIE
#Sortowanie przez kopcowanie polega na wykożystaniu funckji heapify do utworzenia kopca MAX - elementy w tablicy przekłądadne są w taki sposób
#aby otrzymać docelowo relację el poprzedni>= elementom poniżej jego. Nastepnie brana jest pierwsza wartosc i kopiec jest naprwaianywzględem tej wielkości tak aby znalazła się ona najżniżej jak
#jest możliwe. Wykonywac aż nie bedzize spełniona relacje że elementy od prawej do lewej, oraz od gory do dołu są <= elementom dalej.


#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna i średnia : O(nlogn)
#-optymistyczna: O(n)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(1)

def heapify(t,n,i):
    l=2*i+1
    r=2*i +2
    max_ind=i
    if l<n and t[max_ind]<t[l]:
        max_ind=l
    if r<n and t[r]>t[max_ind]:
        max_ind=r
    if max_ind != i:
        t[i],t[max_ind]=t[max_ind], t[i]
        heapify(t,n,max_ind)

def heap_sort(t):
    n=len(t)
    x=(n//2)-1
    for i in range(x, -1, -1):
        heapify(t, n, i)
    for i in range(n-1,0,-1):
        t[i],t[0]=t[0],t[i]
        heapify(t,i,0)
    return t

# import random
# t = [random.randint(0,100) for i in range(10)]
# print(t)
# print(heap_sort(t))