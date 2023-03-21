#Krzysztof Wysocki
#Zaprezentowny algorytm polega na posrotowaniu danej listy przedziałów malejąco względem rozmiaru obszaru obejmowanyego przez dany przedział. Sortowanie odbywa się za pomocą algorytmu QuickSort wraz z podziałem Hoare'a.
#Algorytm iteruje po najwieszych przedziałach następnie sprawdzając ile podprzedzialów zawiera się w nich. Zwraca liczbę największą

#ZŁOŻONOŚĆ:
#-w przypadku pseymistychnym: tablica posortowana lub żaden przedział nie zawiera się w żadnym: n^2 + n^2 ---> O(n^2)
#-w przypadku większościw wykonań: nlogn + --------- -->-----------

from zad2testy import runtests

def partition(t, l, r):
    pivot = (t[l][1] - t[l][0] + 1)  # pivot
    i=l-1
    j=r+1
    while True:
        i+=1
        while (t[i][1] - t[i][0] + 1) > pivot:
            i+=1
        j-=1
        while (t[j][1] - t[j][0] + 1) < pivot:
            j-=1

        if i>=j:
            return j
        t[i][0], t[j][0] = t[j][0], t[i][0]
        t[i][1], t[j][1] = t[j][1], t[i][1]

def quickSort(t, l, r):
    if l < r:
        pi = partition(t, l, r)
        quickSort(t, l, pi)
        quickSort(t, pi + 1, r)

def depth(L):
    l = len(L)
    quickSort(L, 0, l - 1)
    max = i= 0
    while True:
        x = 0
        for j in range(i + 1, l-i):
            if L[j][0] >= L[i][0]:
                if L[j][1] <= L[i][1]:
                    x += 1
        i += 1
        if x >= max or i>=l:
            max = x
            return max

runtests(depth)
