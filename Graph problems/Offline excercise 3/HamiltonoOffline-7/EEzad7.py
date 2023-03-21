#Krzysztof Wysocki
# Zaprezentowany algorytm sprawdzania czy da się przejehac przez każde miasto tylko raz i wrócić do poczatkowego,
# działa na zasadzie szukania cyklu Hamiltona (przebiegający przez kazdy wierzchołek raz). Rozpoczyna się
# wychodzac z dowolnej bramy w 0 mieście, nastepnie w zależności od tego która się 'wjechało' do kolejnego miasta to
# 'wyjeżdża' się z drugiej strony. Algorytm sprawdza każdą zgodna z wymogami drogę (każde miasto raz) z danego wierzchołka na trasie.
# Jeżeli aktualnie rozpatrywana droga nie ma wystarczającej długosći to odwiedzone miasta sa 'usuwane' a droga czyszczona.

#Złożoność pamięciowa: O(n)
#Złożoność czasowa: O(n*n!)?

from zad7testy import runtests

def search(graph,gate, v, visited, path,val):
    if len(path) < len(graph):
        for w in reversed(gate): #odwrocenie jest tylko dlatego że daje lepsze efekty na testach
            if v in (graph[w])[0]:
                out=(graph[w])[1]
            else:
                out=(graph[w])[0]
            if not visited[w]:
                visited[w] = True
                path.append(w)
                val=search(graph, out,w, visited, path,val)

                if len(val)>0:
                    return path
                else:
                    visited[w] = False
                    path.pop()
        return []
    else:
        return path

def droga( G ):
    n=len(G)
    path = [0]
    visited = [False for i in range(n)]
    visited[0] = True
    l=search(G, (G[0])[0], 0, visited, path, [])
    if len(l)==0: return None
    return l
runtests( droga, all_tests = True )