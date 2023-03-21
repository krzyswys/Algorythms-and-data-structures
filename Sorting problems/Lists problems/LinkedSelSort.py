#ALGORYTM SORTOWANIA PORPZEZ WYBIERANIE
#Sortowanie poprzez wyberanie polega na szukaniu najmnijeszego możliwego elementu będącego jednosczesnie większym pod cześci posortowanej
# i zamianie go z tym co jest na niewłaściwym miejscu
#[NIE STABLINY]

#ZŁOŻONOŚĆ CZASOWA:
#- O(n^2)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(1)

class Node():
    def __init__(self):
        self.val=None
        self.next=None



def selSort(l):
    def return_min_and_delete(p):
        min = p
        while p.next != None:
            if p.next.val <= min.next.val:
                min = p
            p = p.next
        node = min.next
        min.next = min.next.next
        return node
    p = Node()
    p.next = l
    new=Node()
    f=new
    while(p.next!=None):
        new.next=return_min_and_delete(p)
        new=new.next
    return f.next


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
# t=selSort(t)
# show(t)