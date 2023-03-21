from zad2ktesty import runtests

def palindrom( S ):
    n=len(S)
    print(S)
    maxp=""
    for i in range(n):
        l,r=i,i
        while l>=0 and r<n and S[l]==S[r]:
            pal=S[l:r+1]
            if len(pal)>len(maxp):
                maxp=pal
            l-=1
            r+=1
        l, r = i, i+1
        while l>=0 and r<n and S[l]==S[r]:
            pal = S[l:r+1]
            if len(pal) >=len(maxp):
                maxp = pal
            l -= 1
            r += 1


    return maxp

runtests ( palindrom )