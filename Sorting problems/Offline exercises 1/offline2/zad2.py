#Krzysztof Wysocki
#Zaprezentowny algorytm znajduje przedział który jest najwieszy pod względem obejmowanego obszaru i zwraca jego indeks w fundki find_max. Następnie począwszy od tegoż elementu sprawdza ile
#przedziałów zawiera się w nim. Trzeba ustawić sprawdzony element na [0,0] co spowoduje brak potrzeby późniejszego sprawdzania tego elementu poniewaz zaden mniejszy przedzial nie będzie nigdy zawierać większego od siebie
#Wartość najwieksza jest zwracana (max).

#ZŁOŻONOŚĆ:
#- w przypadku pesymistycznym, tj. kiedy żaden przedział nie będzie zawierać się w sobie: n(n+n) --> O(n^2)
#- w pozostałych przypadkach: najczęsciej przedział który będzie najwieszy będzie zawierać najwięcej podprzedziałów, więc znalezienie go będzie liniowe. Następnie kolejny przedział pod względem wielkosci itd az to przypadku pesymistycznego.
#- Złożonośc pamięciowa: O(1)
from zad2testy import runtests


def find_max(t,l):
   max=1
   max_i=0
   for i in range(l):
      if t[i][1]-t[i][0]+1>max:
         max=t[i][1]-t[i][0]+1
         max_i=i
   return max_i

def depth(L):
      l = len(L)
      max = 0
      for m in range(l):
          x = 0
          start=find_max(L,l)

          a,b=L[start][0],L[start][1]
          L[start][1] = L[start][0] = 0

          for j in range(l):
             if L[j][1] !=0:
                 if L[j][0] >= a and L[j][1] <= b:
                            x += 1
          if x > max:
                max = x
                break

      return max

runtests( depth )
