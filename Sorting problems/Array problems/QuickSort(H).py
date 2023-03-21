#ALGORYTM SORTOWANIA SZYBKIEGO - QUICKSORT
#Sortowanie QuickSort polega na rekurencyjnym wywoływaniu się tka aby przekszałcać tablicę w następujący sposób;
#wybiera się dowolny element: pivot, według którego ustawia się elementy tak aby polewejs tronie tego elementu były elementy o wartości mniejszej niz wartośc pivot'u
#natomiast po stronie prawej ustawiane są elementy o wartościach większych niż wartośc pivot'u



#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna: O(n^2) - kiedy tablica jest posortowana, wybierze się naj-wiekszy/mnijeszy pivot, elementy są takie same
#-optymistyczna i średnia : O(nlogn)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(n)


def quickSortH(t, l, r): #podział Hoare'a
    if l < r:

        pivot = (t[l])  # pivot section--------
        i = l - 1
        j = r + 1
        while True:
            i += 1
            while (t[i]) < pivot:
                i += 1
            j -= 1
            while (t[j]) > pivot:
                j -= 1
            if i >= j:
                pi= j #return j
                break
            t[i], t[j] = t[j], t[i] #----------

        quickSort(t, l, pi)
        quickSort(t, pi + 1, r)
    return t


def quickSort(t,l,r): #z wykładów
    while l<r:

        x = t[r] #pivot section-----------------
        i = l - 1
        for j in range(l, r):
            if t[j] <= x:
                i += 1
                t[i], t[j] = t[j], t[i]
        t[i + 1], t[r] = t[r], t[i + 1]
        q=i+1   # return i + 1 ------------------

        quickSort(t,l,q-1)
        l=q+1
    return t






import random
t = [random.randint(0,100) for i in range(10)]
print(t)
print(quickSort(t,0,(len(t)-1)))