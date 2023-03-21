#ALGORYTM SORTOWANIA PORPZEZ WYBIERANIE
#Sortowanie poprzez wyberanie polega na szukaniu najmnijeszego możliwego elementu będącego jednosczesnie większym pod cześci posortowanej
# i zamianie go z tym co jest na niewłaściwym miejscu
#[NIE STABLINY]

#ZŁOŻONOŚĆ CZASOWA:
#- O(n^2)

#ZŁOŻONOŚĆ PAMIĘCIOWA:
#O(1)

def selection_sort(t):
    n=len(t)
    for i in range(n):
        min=t[i]
        index_min=i

        for j in range(i,n):
            if t[j]<min:
                min=t[j]
                index_min=j
        t[i],t[index_min]=t[index_min],t[i]
    return t

# import random
# t = [random.randint(0,100) for i in range(10)]
# print(t)
# print(selection_sort(t))