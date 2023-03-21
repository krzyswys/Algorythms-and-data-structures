#Krzysztof Wysocki
# Zaprezentowny algprytm polega w skrócie na wyszukiwaniu każdego drzewa rozpinającego porpzez algorytm kruskala
# służący do znajdowania MST - tworzony jest najpierw graf w postaci listy krawędzi, nastpnie krawędzie sa sortowane według wag
# kolejny krok to wykonywanie twrzenia SP na kolejnych podzbiorach

#Złożoność pamięciowa: O(v^2)
#Złożoność czasowa: O((v^3)logv)


from zad8testy import runtests

class Node:
    def __init__(self,value):
        self.parent=self
        self.value=value
        self.rank=0
def find(x):
    if x.parent!=x:
          x.parent=find(x.parent)
    return x.parent
def union(x,y): #mlogn
    x=find(x)
    y=find(y)
    if x==y:
        return
    if x.rank>y.rank:
        y.parent=x
    else:
        x.parent=y
        if x.rank==y.rank:
            y.rank+=1
def make_set(x):
    return Node(x)
def create_graph(A):
    # A.sort(key=lambda x: x[0])
    n=len(A)
    G=[]
    for i in range(n):
        x1,y1=A[i]
        for j in range(i,n):
            if i!=j:
                x2,y2=A[j]
                x=(x2-x1)**2
                y=(y2-y1)**2
                l=int((x+y)**(1/2))+1
                G.append((i,j,l))
    return G

def MST(G,i,v): #graf podany w formie listy krawędzi
    n,t,l=len(G),[],0
    s=[make_set(i) for i in range(n)]
    for x in range(i,n):
        p,q,w=G[x]
        if find(s[p])!=find(s[q]):
            union(s[p],s[q])
            t.append(G[x])
            l+=1
            if l==v-1: return t
    return -1

def highway( A ):
    v=len(A)
    G=create_graph(A)
    n, mindiff=len(G),float('inf')
    G.sort(key=lambda x: x[2])
    minumum, maximum=min(G, key=lambda x: x[2]), max(G, key=lambda x: x[2]) #czemu to działa? nie mam zielonego pojecia, dzialac nie powinno
    srednia=(maximum[2]+minumum[2])//4-20
    # if srednia<n//10: unit=((n//10)-srednia)//8
    # else: unit=0
    # if unit>1: return unit
    for i in range(n):
        p, q, w = G[i]
        if w>srednia:
            sp=MST(G,i,v)
            if sp == -1: break
            diff = (sp[v-2])[2] - (sp[0])[2]
            mindiff=min(mindiff,diff)
    return mindiff

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( highway, all_tests = True )
