class Node:
    def __init__(self,x):
        self.next=None
        self.val=x

def add(l, vall):
    if l.val == None:  # jesli wartosc na1 wszym miejscu ejst pusta to zapisz ja
        l.val = vall
    else:  # w przeciwnym wypadku iteruj po liscie do poku nie bedzie na koncu
        while l.next != None:
            l = l.next
        l.next = Node(vall)  # na koncu utworz wezel z wartoscia
def show(l):
    print("[", l.val, end="")  # pokaz pierwszy element
    while l.next != None:  # wy[isuj wszystkie elementy dopki ostni niebedzie none
        print(",", l.next.val, end="")
        l = l.next
    print("]")



def del_max(p):
    if p.next == None:
        return
    f=p
    previous=None
    max=p

    while p.next != None:
        # print(p.val, max.val)
        if p.next.val>max.val:
           previous=p
           max=p.next
        p=p.next
    if previous == None:
        f=f.next
    else:
        previous.next=max.next
    return f


# t = Node(9)
# add(t,11)
# add(t, 7)
# add(t, 2)
# add(t, 3)
# add(t, 5)
# add(t, 6)
# show(t)
# t=del_max(t)
# show(t)
# t=del_max(t)
# show(t)
# t=del_max(t)
# show(t)