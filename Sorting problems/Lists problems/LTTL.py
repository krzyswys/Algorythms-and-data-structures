def linked_to_arr(p):
    f=p
    l=1
    i = 0
    while p.next != None:
        l+=1
        p = p.next

    t=[0 for i in range(l)]

    while f.next != None:
        t[i]=f.val
        f=f.next
        i+=1
    t[i] = f.val
    return t


def arr_to_linked(t):
    p = Node()
    f = p

    p.val = t[0]
    p.next = Node()
    for i in range(1,len(t)-1):
        p = p.next
        p.val = t[i]
        p.next = Node()

    p.next.val=t[len(t)-1]
    return f

# def funktion(p):
#     t = linked_to_arr(p)
#     # heap_sort(t)
#     p = arr_to_linked(t)
#     return p