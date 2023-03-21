from egz1atesty import runtests

# Zaprezentowany algorytm polega na wybieraniu i obaszrów z njawiększą ilością sniegu, i - ilość dni dopóki nie roztopi się ostatni:
# Każda operacja to jeden dzień --> n operacji to n dni czyli -n sniegu w każdym obszarze.
# Pwooduje to brak potrzeby wybierania między danymi obszarami: w momencie jak bierzemy jeden - drugi stopnieje,
# dlatego w odwrotenj kolejnosci to suma sumarum wyniku nei zminei


# Złozonsoc czasowa: O(nlogn) Pamięcowa:O(n)
def snow(S):
    n = len(S)
    ans = 0
    S.sort()
    S = S[::-1]
    for i in range(n):
        el = S[i]
        if el - i >= 0:
            ans += el - i
        else:
            break
    return ans


# Krzysztof Wysocki
# Algorytm ktory został wykorzystany to algorytm dynamiczny uzależniający funckję wykonującą liczby dni i dostępnych elementów:
# f(i,d)=max(f(i-1,d),f(i,d-1),f(i-1,d-1)+S[i]-d+1), gdzie d to liczba max dni do wykorzystania, i to max element do ktorego możemy dojść.
# //f(i-1,d-1)+S[i]-d+1 -> w tym miejscu nalezy odjac liczbe dni-1 od ilości śniegu ponieważ on topnieje//
# f(i,0)=0, f(0,i)=S[0], f(0,0)=0
# f- maxymalna liczba snigu zebrana w cigau d dni do i-tego elementu
# wynik nie zmienia się jeżeli rozpatrujemy tylko z jednej strony ponieważ przejechane elementy ze sniegeim sa zerowane

# Złożoność czasowa: O(n^2) Złożoność pamięciowa: O(n^2)

# def snow( S ):
#     n=len(S)
#     f1=[[0 for i in range(n)]for j in range(n)]
#     for i in range(n): f1[0][i]=0
#     for i in range(n): f1[i][0]=S[0]
#     f1[0][0]=0
#     for days in range(1,n):
#         for num in range(days,n):
#             f1[days][num]=max(f1[days][num-1],f1[days-1][num-1]-days+1+S[num],f1[days-1][num])
#     # print(f1[n-1][n-1])
#     return f1[n-1][n-1]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests(snow, all_tests=True)
