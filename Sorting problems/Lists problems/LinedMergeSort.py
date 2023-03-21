# ALGORYTM SORTOWANIA MERGESORT
# Algorytm polega na rekurencyjnym rozbijaniu listy na pół aż do elementarnych fragmentów (lista jednoelementowa to posortowana lista),
# oraz na późniejszym scaleniu tychże list w kolejnosci posortwanej.

# ZŁOŻONOŚĆ:  O(nlogn)
# ZŁOŻONOŚĆ PAMIECIOWA: O(n)

# ZLOZONOSC CZASOWA dla:
# k = Θ(1): O(nlogn)
# k = Θ(log n): O(nlogn)
# k = Θ(n): O(nlogn)


class Node():
    def __init__(self):
        self.val=None
        self.next=None


def merge_sort(p):
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
    lewa_strona=merge_sort(p)
    prawa_strona=merge_sort(w_2p)

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





# import random
# def generate_list(n):
#     p=Node()
#     f=p
#
#     p.val = random.randint(1, 100)
#     p.next = Node()
#     for i in range(n-2):
#         p = p.next
#         p.val = random.randint(1, 100)
#         p.next=Node()
#     p.next.val = random.randint(1, 100)
#     return f
#
# def show(l):
#     print("{", l.val, end="")  # pokaz pierwszy element
#     while l.next != None:  # wy[isuj wszystkie elementy dopki ostni niebedzie none
#         print(",", l.next.val, end="")
#         l = l.next
#     print("}")
# t=generate_list(10)
# show(t)
# t=merge_sort(t)
# show(t)
