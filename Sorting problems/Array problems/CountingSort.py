#SORTOWANIE PRZEZ ZLICZANIE (COUNTING SORT):
#Sortowanie przez zliczanie polega na wyznaczeniu dla każdeg elementu w danej tablicy A liczby elementów mniejszych od niego.
#Nastepnie wstawiamy liczby na odpowiednie indeksy;  tj. liczba mniejszych elementów lub równych. Po każdej operacji należy zmniejszyć liczbę <= o 1.
#Zakładamy że liczby są z przedziału od 0 do k, więc aby poznac przedział można znaleźć maksymalna wartośc w tab i uznac ją jako zakonczenie zbioru.

#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna: O(n+k)
#-optymistyczna i średnia : O(n) (dla k=O(n))

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(n+k)

def counting_sort(A):
    n=len(A)
    k=max(A)+1 #zakres
    C=[0]*(k+1) #zawierać będzie liczbę elemenów mniejszych lub równych elementowi
    B=[0]*(n) #tablca na dane wyjsciowe

    for i in range(n): #ile razy kazdy element występuje
        C[A[i]]+=1

    for j in range(1,k): #suma poprzednich
        C[j]=C[j]+C[j-1]

    l=n-1
    while (l>=0):
        B[C[A[l]]-1]=A[l]
        C[A[l]]-=1
        l-=1
    return B



# import random
# t = [random.randint(0,100) for i in range(10)]
# print(t)
# print(counting_sort(t))