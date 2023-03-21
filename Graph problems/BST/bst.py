COUNT = [10]


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None
        self.elleft = 0
        self.elright = 0


def print2DUtil(root, space):
    global COUNT
    if (root == None):
        return
    space += COUNT[0]

    print2DUtil(root.right, space)

    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print((root.elleft, root.key, root.elright))

    print2DUtil(root.left, space)


def print2D(root):
    print2DUtil(root, 0)


def find(root, key):
    while root != None:
        if root.key == key:
            return root
        elif key < root.key:
            root = root.left
        else:
            root = root.right
    return None


def insertKey(root, key):
    f = root
    if root == None:
        return BSTNode(key)
    if root.key < key:

        root.right = insertKey(root.right, key)
        root.right.parent = root
        root.elright += 1
    elif root.key > key:

        root.left = insertKey(root.left, key)
        root.left.parent = root
        root.elleft += 1

    return f


def findMin(root):
    while root.left != None:
        root = root.left
    return root


def findMax(root):
    while root.right != None:
        root = root.right
    return root


def findparent(root, val):
    node = find(root, val)
    return node.parent.key


def deleteVal(root, key):
    f = root
    node = find(root, key)
    if node is None: return None
    if node.left is None and node.right is None:
        if node != root:
            if node.parent.left == node:
                node.parent.left = None
            else:
                node.parent.right = None
    elif node.left is None and node.right is not None:
        if node != root:
            tmp = node.key
            node.right = None
            node.key = tmp
    elif node.left is not None and node.right is None:
        if node != root:
            tmp = node.left.key
            node.left = None
            node.key = tmp
    elif node.left is not None and node.right is not None:
        succ = findMin(node.right)
        tmp = succ.key
        deleteVal(f, succ.key)
        node.key = tmp

    return root



def sumTree(root):
    if root == None:
        return 0
    return (root.key + sumTree(root.left) + sumTree(root.right))


def kLargest(root, k):
    if k > 0:
        r = root.elleft + 1
        if k == r:
            return root.key
        elif k < r:
            return kLargest(root.left, k)
        else:
            return kLargest(root.right, k - r)


def whichK(root, key):
    x = find(root, key)
    r = x.elleft + 1
    y = x
    while y != root:
        if y == y.parent.right:
            r = r + y.parent.elleft + 1
        y = y.parent
    return r


tree = BSTNode(10)
# print2D(tree)
insertKey(tree, 9)
insertKey(tree, 1)
insertKey(tree, 15)
insertKey(tree, 12)
insertKey(tree, 11)
insertKey(tree, 20)
insertKey(tree, 17)
insertKey(tree, 25)
print2D(tree)
print("----")
# print(findMin(tree).key)
# print(findMax(tree).key)
# print(findparent(tree,15))
deleteVal(tree, 10)
print2D(tree)
# print(sumTree(tree))
# print(kLargest(tree,4))
# print(whichK(tree,11))
