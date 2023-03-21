# Krzysztof Wysocki
# Algorytm wyznaczania budynków najbardzije odpowiednich do budowy bazuje na zmodyfikowanej idei problemu plecakowego. Na początku tablica zawierającac budynki jest sortowana według parametru b,
# W ten sposób aby sprawdzić czy dany budynek może zostac użyty wystarczy sprawdzić czy zaczyna się dalej niż konczy poprzedni. Tablica f, w domyśle funkcja, przechowuje wartości odpowiadające równaiu rekurencyjnemu:
# f(i,j)=max(f[i-k][i-w[i]]+v[i] {gdy budynku t[i-k] można użyć},v[i]) , gdzie k należy do (1,...,i), i należy do (0,..n-1), oraz i to każdy koleny budynek w tablicy t,
# j należy do (0,...,P) oraz j to maxymalna możliwa suma cen budynków aktualnie rozpatrywanych, w[i],v[i] to odpowiednio cena wybodowania i-tego budynku oraz jego 'pojemność'.
# Inaczej niż w problemie plecakowym, w tym przypadku przepisywanie wartosci poprzedniej (f[i-1][j]) nie może zostac zastosowane ponieważ trzeba byłoby przechowywac w osobnej tablicy indexy budyknków dla każdego okienka i za
# każdym razem sprawdzać czy można tego użyć. W tym przypadku wystarczy sprawdzić budynek na danym indexie i ponieważ każdy poprzedni nie będzie przeszkadzał jako że budynki zostały posortowane według parametru końcowego.

# ZŁOŻONOŚĆ CZASOWA: nlogn + (n^2)*p + n
# ZŁOŻONOŚĆ PAMIĘCIOWA: p*n

from zad4testy import runtests

# def countbuildings(b,m,t):
#     lb=len(b)
#     lm=len(m)
#     answer=[]
#     for i in range(lm):
#         for j in range(lb):
#             if m[i]==t[b[j]]:
#                 answer.append(i)
#     return answer

def ks(t, P):
    n = len(t)
    f = [[0 for i in range(P + 1)] for j in range(n)]  # pamięć p*n
    buildings = [[[] for i in range(P + 1)] for j in range(n)]  # pamięć p*n
    m = t.copy()  # czas: n
    t = sorted(t, key=lambda x: x[2])  # czas: nlogn
    maxv = maxi = 0
    for i in range(n):
        h, a, b, w = t[i]
        v = h * (b - a)
        for j in range(w, P + 1):
            for k in range(1, i + 2):  # czas: n*p*n
                if f[i - k][j - w] + v >= f[i][j] and (t[i - k])[2] < a:
                    f[i][j] = f[i - k][j - w] + v
                    buildings[i][j] = buildings[i - k][j - w].copy()
                    if i not in buildings[i][j]:
                        buildings[i][j].append(i)
                elif v > f[i][j]:
                    f[i][j] = v
                    buildings[i][j] = buildings[i][j].copy()
                    if i not in buildings[i][j]:
                        buildings[i][j].append(i)
        if f[i][P] > maxv:
            maxi = i
            maxv = f[i][P]
    # for i in range(n):
    #     for j in range(P + 1):
    #         print("[", end="")
    #         print(f[i][j], end="] ")
    #     print("")

    answer = []
    b = buildings[maxi][P]
    for j in range(len(b)):
        ind = m.index(t[b[j]])
        answer.append(ind)
    return answer

    # answer = countbuildings(buildings[maxi][P], m, t) #czas: n
    # return answer

def select_buildings(T, p):
    x = ks(T, p)
    return x


runtests(select_buildings)
