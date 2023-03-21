from egz1btesty import runtests
#Krzysztof Wysocki
# Rozważanie ktore krawędzie należy wyłączyć aby uzyskac najwieksze ładne drzewo można rozpocząć poprzez:
# 1. Ponumerowanie w x poziomów każdego węzła
# 2. Sprawdzenie czy obecnie drzewo nie jest już ładne
# 3. Odcinanie kolejnych krawędzi od liści które znajdują się na najniższych poziomach
# 3.5 Jeżeli odcinamy jakieś krawędzie i przedtem na tej zamej dordze również to zrobiliśmy to wystarczy zaktaulizaowac odpowienio licznyk usuniętyhc krawędzei
# 4. wracamy do 2

#Złożoność czasowa: O(n^2)

maxlevel=0
class Node:
  def __init__( self ):
    self.left = None    # lewe poddrzewo
    self.right = None   # prawe poddrzewo
    self.x = 0       # pole do wykorzystania przez studentow

def level(root,level): #nadaje wartości poziomów
    if root is not None:
        print(level)
        root.x=level
        level(root.left,level+1) and level(root.right,level+1)
def isPreety(root, level): #sprawedza czy drzwe jest ładne
    if root is None:
        return True
    if root.left is None and root.right is None:
        return level == root.x
    return (isPreety(root.left, level + 1) and isPreety(root.right, level + 1))

def removeLowestLeaf(root): #usuwa najzniższy liść
    global maxlevel
    if root is None:
        return None
    if root.left.left is None and root.left.right is None:
        if root.left.x>maxlevel:
            maxlevel=root.left.x
            root.left=None
    elif root.right.left is None and root.right.right is None:
        if root.right.x>maxlevel:
            maxlevel=root.right.x
            root.right=None
    return removeLowestLeaf(root.left) and removeLowestLeaf(root.right)

def wideentall( T ):
    global maxlevel
    level(T,0)
    ans=0
    if isPreety(T):
        return 0
    else:
        while not isPreety(T) and T!=None:
            removeLowestLeaf(T)
            ans+=1

    return ans

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( wideentall, all_tests = False )