# tablica (kolorów) A, n elementowa, każdy element jest ze zbioru od 1 do k i suzkamy indeksów i,j takich że a[i]....a[j]
# zawiera wszystki liczby od 1 do k oraz j-i  jest jak njamnijesze


def find_colors(t,k):
    colors = [0] * (k)
    n=len(t)
    mi=mj=0
    diff=1000
    i=j=0
    s=""
    while(j<n):
        if 0 not in colors:
            if (j-i)<diff:
                diff=j-i
                mi=i
                mj=j
            else:
                colors[t[i] - 1] -= 1

                i += 1
        else:
            colors[t[j] - 1] += 1

            j += 1

        # print(s,colors)
        # s+=" . "

    return mi,mj-1


# t=[1,1,1,1,1,1,1,1,1,1,1,1,5,1,2,3,4,1]
# print(t, len(t))
# print(find_colors(t,5))
