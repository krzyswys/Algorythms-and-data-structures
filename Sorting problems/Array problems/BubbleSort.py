#ALGORYTM SORTOWANIA BĄBELKOWEGO:
#Sortowanie bąbelkowe polega na iterowaniu przez tablicę n*n razy i zamieniania ze sobą elementów w nieodpowiedniej kolejności.
#Przechodzenie przez drugą pętle można robić do n-itego elemntu ponieważ elementy najdalje będą już posortowane w dobrej kolejności.
#Jeżeli nie dokonano żadnych podczas przejścia przez 2 petlę (flaga) to znaczy że całość jest już posortowana i można wyjśc z pęl
#[STABILNY]

#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna i średnia : O(n^2)
#-optymistyczna: O(n) - kiedy tablica jest już posortowana

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(1)

def bubble_sort(t):
    n=len(t)
    for i in range(n):
        flag=0
        for j in range(n-i-1):
            if t[j]>t[j+1]:
                t[j],t[j+1]=t[j+1],t[j]
                flag=1
        if flag==0:
            break
    return t




# import random
# t = [random.randint(0,100) for i in range(10)]
# print(t)
# print(bubble_sort(t))