#ALGORYTM SORTOWANIA WYRAZÓW RADIX:
#Sortowanie radix wyrazow odbywa sie porpez sortowanie przez zliczanie wg. ostatniej litery wszystkich wyrazów, nastpnie 1 przed ostania itd.

#ZŁOŻONOŚĆ CZASOWA:
#-O(d*(n+k)); d-dlugosc wyrazu, k-zakres wartosci (np alfabet-26)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(n+k)

def count_sort_letters(A, column, max_len):
  alf_size=26
  n=len(A)

  B   = [0] * n
  C    = [0] * (alf_size + 1)
  min_base = ord('a') - 1 #litery alfabetu + '0'

  for item in A: # policz wystapienia
    if column < len(item): #jak kolumna znajduje sie w stringu to wykonaj operacja a jak nie to dej 0
        letter = ord(item[column]) - min_base #zlicz wg ascii do odpowiedniego mijesca, odejmij min prog aby było min=0
    else:
        letter = 0
    C[letter] += 1

  for i in range(len(C)-1):   #zlicz wyrazy <=
      C[i + 1] += C[i]

  for item in reversed(A):

    if column < len(item):
        letter = ord(item[column]) - min_base
    else:
        letter = 0

    B[C[letter] - 1] = item
    C[letter] -= 1

  return B



def radix_sort_words(A):
    n=len(A)
    max_len = len(max(A, key=len))-1  # zwraca najwieksza dlugosc najdluszego wyrazu-1

    for i in range(max_len, -1, -1):  # max_len-1, max_len-2, ...0
        A = count_sort_letters(A, i, max_len)
    return A




# t = ['aa', 'a', 'ab', 'abs', 'asd', 'avc', 'axy', 'abid']
# print(t)
# print(radix_sort_words(t))





