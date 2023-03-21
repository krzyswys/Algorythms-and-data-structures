#ALGORTM SORTOWANIA POPRZEZ WSTAWINIE
#Sortowanie przez wstawianie polega na wybieraniu kolenego elementu z części nie posortowanej i wsatwianiu go na odpowiednie mijejsce w części posortowanej.
#Iterujemy przez cześć posortowaną (jednoelementowa listato lista posortowana), następnie dla kolejnego elementu który chcemy wstawić (klucz)
#trzeba zrobić miejsce i przesunać liczby wieksze do przodu w drugiej pętli. Następnie wystarczy wstawić pożądany elemen w zrobione miejsce
#[STABILNY]

#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna i średnia : O(n^2)
#-optymistyczna: O(n) - kiedy tablica jest już posortowana

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(1)


def insertion_sort(t):
    n=len(t)
    for i in range(1,n):
        klucz1=t[i]
        j=i-1
        while(j>=0 and klucz1 > t[j]):
            t[j+1]=t[j]
            j-=1
        t[j+1]=klucz1
    return t




# import random
# t = [random.randint(0,100) for i in range(10)]
# print(t)
# print(bubble_sort(t))