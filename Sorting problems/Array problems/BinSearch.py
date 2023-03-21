#Algorytm wyszukiwania dzialającyw czasie O(logn)
#Działa na posortowanej tablicy; dzili na poł i potem szuka w tej połówce co jest element


def bin_search(t,x):
    start=0
    end=len(t)-1
    while (start<=end):
        middle=(end+start)//2
        val=t[middle]
        if val==x:
            return True
        elif val>x:
            end=middle-1
        elif val<x:
            start=middle+1
    return False


# t=[1,2,3,4,5,6,7,8]
# print(bin_search(t,2))