from zad3testy import runtests


# 1. Dodajemy do tablicy oryginalny index
# 2. Sortujemy tablicę malejąco według końca
# 3. Wybieramy po jednym elemencie z tablicy: i,dodajemy index do nowo utworzonej tablicy ans
# 4. Sprawdzamy dla każdego innego elementu j czy poczatek elementu i-tego zachodzi na jakiś element j
# 5. Jeśli tak to dodajemy ideks elementu j do ans
# 6. Gdzy jest k alementów to sprawdzamy czy ich zakres jest wiekszy niż aktualny
# 7. Jeśli tak to go aktualizujemy i do X dodajemy elemety z ans
def kintersect( A, k ):
    n=len(A)
    A=[(A[i][0],A[i][1],i) for i in range(n)]
    A.sort(key=lambda x:x[1], reverse=True)
    maxlen=0
    X=[]
    #dodac warunek ze co jak k==1
    for i in range(n):
      ans=[]
      ans.append(A[i][2])
      for j in range(n):
        if i!=j:
          if A[j][0]<=A[i][0]<=A[j][1]:
            ans.append(A[j][2])
            if len(ans)==k:
              l=min(A[j][1]-A[i][0],A[i][1]-A[i][0])
              if maxlen<l:
                maxlen=l
                X=ans.copy()
    return X
A=[(2,100),(97,99),(97,98),(30,90),(3,50)]

print(kintersect(A,3))
# runtests( kintersect )