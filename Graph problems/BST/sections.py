COUNT=[10]
class BSTNode:
    def __init__(self,key):
        self.key=key
        self.parent=None
        self.left=None
        self.right=None
        self.max=key[1]


def print2DUtil(root, space):
    global COUNT
    if (root == None):
        return
    space += COUNT[0]

    print2DUtil(root.right, space)

    print()
    for i in range(COUNT[0], space):
        print(end=" ")
    print((root.key,root.max))

    print2DUtil(root.left, space)
def print2D(root):

    print2DUtil(root, 0)

def giveMax(node):
    if node.left != None and  node.right!=None:
        return max(node.left.max,node.right.max,(node.key)[1])
    elif node.left != None and  node.right==None:
        return max(node.left.max,  (node.key)[1])
    elif node.left == None and node.right != None:
        return max( node.right.max, (node.key)[1])
    else:
        return (node.key)[1]

def find(root,key):
    while root!=None:
        if root.key==key:
            return root
        elif (key[0])<(root.key)[0]:
            root=root.left
        else:
            root=root.right
    return None

def insertKey(root, key):
    f=root
    if root==None:
        return BSTNode(key)
    if (root.key)[0]<(key)[0]:
        #if intesect : split
        root.right=insertKey(root.right, key)
        root.right.parent=root
        root.max=giveMax(root)

    elif (root.key)[0]>(key)[0]:

        root.left=insertKey(root.left,key)
        root.left.parent=root
        root.max=giveMax(root)

    return f
def intersect(root,x):
    p=root
    while p!=None and not ((p.key)[0]<x[0]<(p.key)[1] and (p.key)[0]<x[1]<(p.key)[1]):
        if p.left!=root and p.left.max>=x[0]:
            p=p.left
        else:
            p=p.right
    return p.key
tree=BSTNode([16,21])
insertKey(tree,[8,9])
insertKey(tree,[5,8])
insertKey(tree,[0,3])
insertKey(tree,[6,10])
insertKey(tree,[15,23])
insertKey(tree,[25,30])
insertKey(tree,[17,19])
insertKey(tree,[25,30])
insertKey(tree,[26,26])
insertKey(tree,[19,20])
print2D(tree)
print(intersect(tree, [26,29]))
