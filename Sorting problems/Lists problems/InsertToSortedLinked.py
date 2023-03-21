class Node:
    def __init__(self, x):
        self.next = None
        self.val = x


def add(l, vall):
    if l.val == None:  # jesli wartosc na1 wszym miejscu ejst pusta to zapisz ja
        l.val = vall
    else:
        while l.next != None:
            l = l.next
        l.next = Node(vall)  # na koncu utworz wezel z wartoscia


def show(l):
    print("[", l.val, end="")  # pokaz pierwszy element
    while l.next != None:
        print(",", l.next.val, end="")
        l = l.next
    print("]")


def insert_to_sorted(first, x):
    if first.next is None:
        first = Node(x)
    p = first
    while p.next != None:  # rysowac przykłady i testować
        if p.next.val > x:
            q = Node(x)
            q.next = p.next
            p.next = q
            return
        p = p.next
    else:
        p.next = Node(x)


# t = Node(9)
# add(t,11)
# add(t, 7)
# add(t, 2)
# add(t, 3)
# add(t, 5)
# add(t, 6)
# show(t)
# insertt(t,4)
# show(t)
# insertt(t,4)
# show(t)
# insertt(t,4)
# show(t)
