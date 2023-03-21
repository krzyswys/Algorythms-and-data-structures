#ALGORYTM SORTOWANIE PRZEZ SCLANAIE:
#Sortowanie poprzez scalanie polega na rekurencyjnym rozłożeniu tablicy na podtablice posortowane (tj. jednoelementowe).
#Następnie wystarczy te tablice połączyć ze sobą w kolejnosći posortowanej.
#[STABILNY]

#ZŁOŻONOŚĆ CZASOWA:
#- O(nlogn)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#-O(nlogn)

def merge_sort(t):
    n=len(t)
    if n>1:
        srodek=n//2
        lewa_czesc=[]
        prawa_czesc=[]
        for i in range(srodek): #od zera do polowy
            lewa_czesc.append(t[i])
        for i in range(srodek, n): #od polowy do konca
            prawa_czesc.append(t[i])

        #podzial
        merge_sort(prawa_czesc)
        merge_sort(lewa_czesc)

        #merge
        i=j=k=0 #indeks lewej tablicy | indeks prawej tablicy | index polaczonej tablicy
        while i<len(lewa_czesc) and j< len(prawa_czesc):
            if lewa_czesc[i]<prawa_czesc[j]:
                t[k]=lewa_czesc[i]
                i+=1
            else:
                t[k]=prawa_czesc[j]
                j+=1
            k+=1

        #cos co porona ostatni element z tej wiekszej czesci co pozostanie
        while i<len(lewa_czesc):
            t[k]=lewa_czesc[i]
            i+=1
            k+=1

        while j<len(prawa_czesc):
            t[k]=prawa_czesc[j]
            j+=1
            k+=1

        return t


# import random
# t = [random.randint(0,100) for i in range(10)]
# print(t)
# print(merge_sort(t))