def merge1(Node1, Node2):
    #node1 i node2 = none?
    p=Node
    if (Node1 is None):
        return Node2
    if (Node2 is None):
        return Node1

    if (Node1.val >= Node2.val):
        Node2.next=merge(Node1, Node2.next)
        return Node2
    else:
        Node1.next=merge(Node1, Node2)
        return Node1