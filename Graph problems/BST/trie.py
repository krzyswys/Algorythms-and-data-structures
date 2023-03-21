
class T:
    def __init__(self):
        self.children = [None] * 4
        self.isleaf = False
        self.num=0

def charTonum(ch):
    # return ord(ch)-ord('a')
    # print(ch)
    x=ord(ch)
    if x==97: return 0
    if x==99: return 1
    if x==116: return 2
    if x==122: return 3
def insert(root,key):
    p=root
    for i in range(len(key)):
        index=charTonum(key[i])
        if index != None:
            print(index)

            if  not p.children[index]:
                p.children[index]=T()
            p=p.children[index]
    p.isleaf=True
    p.num+=1

def search(root, key):
    p = root
    for i in range(len(key)):
        index = charTonum(key[i])
        if not p.children[index]:
            return False
        p = p.children[index]
    print(p.num, p.children)
    return p.isleaf

tree=T()
insert(tree,"aact")
insert(tree,"ttc")
insert(tree,"ggtc")
insert(tree,"cgc")
insert(tree,"ttc")
print(ord('a'),ord('c'),ord('t'),ord('g'),ord('z')) #25, 23, 6,19
print(search(tree,"ttc"))