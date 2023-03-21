class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


# add(first arr, value)
def add(l, val):
    if l.data == None:  # jesli wartosc na1 wszym miejscu ejst pusta to zapisz ja
        l.data = val
    else:  # w przeciwnym wypadku iteruj po liscie jak nie bedzie na koncu
        while l.next != None:
            l = l.next
        #     if l.data==val:
        #         return
        # if l.data==val:   #DLA DODAWANIA BEZ POWTORZEN
        #     return
        l.next = Node(val)  # na koncu utworz wezel z wartoscia


# show(rem(arr, value))
def rem(l, val):
    if l.data == None:
        print("Lista jest pusta")
    if l.data == val:
        l = l.next
        return l
    else:
        f = l
        while l.next != None:
            prev = l
            l = l.next
            if l.data == val:
                prev.next = l.next
                return f
    print("Brak takiego elementu")


# show(arr)
def show(l):
    print("[", l.data, end="")  # pokaz pierwszy element
    while l.next != None:
        print(",", l.next.data, end="")
        l = l.next
    print("]")


# show(rem_ind_x(arr, index))
def rem_ind_x(l, x):
    leng = lenght(l)
    # if x > leng or x < leng:
    #     print("zły index")
    if l.data == None:
        print("Lista jest pusta")
    if x == 0:
        l = l.next
        return l
    else:
        couter = 0
        f = l
        while l.next != None:
            prev = l
            l = l.next
            couter += 1
            if x == couter:
                prev.next = l.next
                return f


# print(val_ind_x(arr,index))
def val_ind_x(l, x):
    leng = lenght(l)
    # if x > leng or x < leng:
    #     print("zły index")
    if l.data == None:
        print("Lista jest pusta")
    if x == 0:
        return l.data
    else:
        counter = 0
        while l.next != None:
            l = l.next
            counter += 1
            if x == counter:
                return l.data
    if counter > leng:
        print("brak takiej wartosci")


def insert_val_ind_x(l, x, val):
    new_value = Node(val)
    leng = lenght(l)
    # if x > leng or x < leng:
    #     print("zły index")
    if l.data == None:
        print("Lista jest pusta")
    else:
        counter = 0
        while counter != x:
            prev = l
            l = l.next
            counter += 1
        prev.next = new_value
        new_value.next = l.next


# print(is_in(arr, value)
def is_in(l, val):
    if l.data == val:
        return True
    else:
        while l.next != None:
            l = l.next
            if l.data == val:
                return True
    return False


# print(lenght(arr))
def lenght(l):
    counter = 1
    while l.next != None:
        l = l.next
        counter += 1
    return counter


# examples: ---------
t = Node()
add(t, 0)
add(t, 1)
add(t, 2)
add(t, 3)
add(t, 4)
add(t, 5)
print(lenght(t))
# print(len(t))
# show(t)
# insert_val_ind_x(t,2,56)
# show(t)
# # print(is_in(t,0))
# # show(rem(t,1))
# show(rem_ind_x(t, 2))
