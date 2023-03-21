def canpartition(nums): #partition equal subset sum
    val=(sum(nums)//2)+1
    n=len(nums)
    suma=sum(nums)
    if suma%2!=0: return False
    f=[[0 for i in range(val)] for i in range(n)]
    f[0][0]=0
    for i in range(n):
        for j in range(val):
            if nums[i]<=j:
                f[i][j]=max(f[i-1][j],f[i-1][j-nums[i]]+nums[i])
            else:
                f[i][j]=f[i-1][j]
            if f[i][j]==suma-val+1:
                return True
    return (suma-f[n-1][val-1]==val-1)


# t=[5,1,11,5]
# print(canpartition(t))