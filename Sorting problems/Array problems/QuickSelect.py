# znajdowwanie k tego elementu: w najgorszym przypadku jest O(n^2), ale takoto dla srednich i opytmistycznych dziala w n*k
# Wybieramy pivot, robimy quicksorta ale do poki pivot nie jest szukanym k tym elementem
# i rekurencyje wywolumeny nie wszystko ale jedna czesc wedlug pozycji pivotu


def partition(A, left, right):
    pivot = A[right]
    i = left
    for j in range(left, right):
        if A[j] <= pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[i], A[right] = A[right], A[i]
    return i


def findK(A, left, right, k):
    if k >= 0 and k <= right - left + 1:
        q = partition(A, left, right)
        if q - left == k:
            return A[q]
        if q - left > k:
            return findK(A, left, q - 1, k)
        return findK(A, q + 1, right, k - q + left - 1)


# t=[52,52,525,52,6,44,23,8,11,12] #6,8,11,12,23,44
# n=len(t)
# print(findK(t,0,n-1,2))
# print(t)
