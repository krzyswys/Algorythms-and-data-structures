# Krzysztof Wysocki
# Aby unikąć przepisywania do tablic, zaprezentowany algorytm sortowania dla listy odsylaczowej k-chaotycznej sklada się z 2 algorytmow:
# sortowania przez scalanie(MereSort) oraz sortowania poprzez wybieranie (SelSort).
# Pierwszy wykorzystany algorytm polega na rekurencyjnym rozbijaniu listy na pół aż do elementarnych fragmentów (lista jednoelementowa to posortowana lista),
# oraz na późniejszym scaleniu tychże list w kolejnosci posortwanej.
# Drugi użyty algorytm działa na zasadzie przepinania (polacz z nowa oraz usun ze starej) wezla zawierajacego najmniejsza wartosc do nowej listy.
# Dla wartosci K<=5, wysraczy przejsc przez liste do k tego elementu aby znaleźc najmnijesza wartość jako ze ona może być maksymalnie na k-tym miejscu.

# ZŁOŻONOŚĆ:  O(nlogn) [dla k<=5: O((nk))^2)]
# ZŁOŻONOŚĆ PAMIECIOWA: O(n) [dla k<=5: O(1)]

# ZLOZONOSC CZASOWA dla:
# k = Θ(1): O(nlogn)
# k = Θ(log n): O(nlogn)
# k = Θ(n): O(nlogn)

from zad1testy import Node, runtests

def MergeSort(p):
    # ------------------------------------------------------zlapanie wskazika na srodek
    if p.next == None:
        return p
    el=p
    p1 = el
    p2 = el.next
    while (p2 != None and p2.next != None):  # drugi wskaznik porusza się 2 razy szybciej od pierwszego, co w konsekwecji odpowie na pytanie gdzie jest srodek listy
        p1 = p1.next
        p2 = p2.next.next

    w_srodek=p1 #wskazanie na ostatni element z 1 polowy
    w_2p=w_srodek.next #wskazanie na poczatek 2 polowy
    w_srodek.next=None #rozpięcie 2 polowek

    #---------------------------------------------------------------------rekurencyjnie podzielenie na fragmenty elementarne listy
    lewa_strona=MergeSort(p)
    prawa_strona=MergeSort(w_2p)


    #--------------------------------------------------------------------------------- \/ fragment ponizej odpowiada za laczenie  POSORTOWANYCH list
    p_lista = Node()  # przygotowywuje nowa, polaczona liste do ktorej będzie sie przepinac kolejne wezly
    f = p_lista  # przechowuje wskazanie na 1 element listy
    while p_lista != None:
        # kiedy ktoras z list bedzie juz pusta, wtedy laczy poprostu te listy ze soba
        if prawa_strona == None:
            p_lista.next = lewa_strona
            break
        if lewa_strona == None:
            p_lista.next = prawa_strona
            break
            # porownuje kolejne wartosci i przepina zgodne z wynikiem
        if lewa_strona.val <= prawa_strona.val:
            p_lista.next = lewa_strona
            lewa_strona = lewa_strona.next
        else:
            p_lista.next = prawa_strona
            prawa_strona = prawa_strona.next
        p_lista = p_lista.next


    posortowana_lista=f.next
    return posortowana_lista

def SelSort(p,k):

    def w_min_usun(p,k): #znajduje, usuwa i zwraca wskaznik na najmnijsza wartosc
        krok = 0
        min_wart = p
        while p.next != None and krok<=k:
            if p.next.val <= min_wart.next.val:
                min_wart = p
            p = p.next
            krok+=1

        w = min_wart.next
        min_wart.next = min_wart.next.next
        return w

    v = Node()
    v.next = p
    new=Node()
    f=new
    while(v.next!=None): #przepina najmniejsza wartosc do nowej listy
        new.next=w_min_usun(v,k)
        new=new.next
    return f.next

def SortH(p,k):
    if k>5:
        p=MergeSort(p)
    elif k<=5:
        p=SelSort(p,k)
    else:
        return p #lista juz posortowana
    return p

runtests( SortH )