import random


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def generate_list(n):
    p = Node()
    f = p

    p.val = random.randint(1, 100)
    p.next = Node()
    for i in range(n - 2):
        p = p.next
        p.val = random.randint(1, 100)
        p.next = Node()
    p.next.val = random.randint(1, 100)
    return f


def show(l):
    print("{", l.val, end="")  # pokaz pierwszy element
    while l.next != None:
        print(",", l.next.val, end="")
        l = l.next
    print("}")


t = generate_list(10)
show(t)
