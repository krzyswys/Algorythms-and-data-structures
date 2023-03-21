#ALGORTM SORTOWANIA POPRZEZ WSTAWINIE NA LISATCH JEDNOKIERUNKOWYCH6
#Sortowanie przez wstawianie polega na wybieraniu kolenego elementu z części nie posortowanej i dopinaniu go do listy posortowanej.

#[STABILNY]

#ZŁOŻONOŚĆ CZASOWA:
#-pesymistyczna i średnia : O(n^2)
#-optymistyczna: O(n) - kiedy tablica jest już posortowana

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(1)

class Node:
    def __init__(self):
        self.val = None # przechowywana liczba rzeczywista
        self.next = None # odsyłacz do nastepnego elementu

def in_to_Slink(posortowana_lista,przekazany_wezel_do_doloczenia): #funkcja przepina zadanego Nodea do odpowiedniego miejsca

    if (posortowana_lista == None or posortowana_lista.val >= przekazany_wezel_do_doloczenia.val): #rozwazenie pierwszego elementu

        przekazany_wezel_do_doloczenia.next = posortowana_lista
        posortowana_lista = przekazany_wezel_do_doloczenia

    else:
        rozwazany_wezel_przy_iteracji = posortowana_lista

        while (rozwazany_wezel_przy_iteracji.next != None): #lokalizuje mijesce gdzie nalezy wstawić przekazanego Nodea
           if ( rozwazany_wezel_przy_iteracji.next.val >= przekazany_wezel_do_doloczenia.val):
               break
           rozwazany_wezel_przy_iteracji = rozwazany_wezel_przy_iteracji.next

        przekazany_wezel_do_doloczenia.next = rozwazany_wezel_przy_iteracji.next
        rozwazany_wezel_przy_iteracji.next = przekazany_wezel_do_doloczenia

    return posortowana_lista

def inSort(f):
    posortowane = None #inicjalizacja posortowanej linked listy #tworzymy sobie pierwszy wskaznik do 'nowej listy' kora bedzie posortowana i tam bedziemy przepinać każdy Node z tej oficjalnej
    obecny_wezel = f #//obecny wezel to takie p

    while (obecny_wezel != None):
        kolejny=obecny_wezel.next #
        posortowane = in_to_Slink(posortowane, obecny_wezel) #sorted --//--, obecny wezel to kolejny node ktory bedizemy wstawiac w odpowiedniej kolejnosci do sorted
        obecny_wezel = kolejny

    return posortowane







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
# t=inSort(t)
# show(t)