from zad3testy import runtests

def change(color):
    if color=="green":
        return "red"
    elif color=="red":
        return "blue"
    elif color=="blue":
        return "green"

def lamps( n,T ):
    tab=["green" for i in range(n)]
    m=0
    x=0
    for a,b in T:
        for i in range(a,b+1):
            color=tab[i]
            if color == "green":
                tab[i]= "red"
            elif color == "red":
                tab[i]= "blue"
                m+=1
            elif color == "blue":
                tab[i]= "green"
                m-=1
        x=max(x,m)

    return x

    
runtests( lamps )


