def edit_distance(word1,word2):
    ni=len(word1)+1
    nj=len(word2)+1
    f=[[0 for j in range(nj)] for i in range(ni)]
    for i in range(nj):
        f[0][i]=i
    for i in range(ni):
        f[i][0]=i

    for i in range(1,ni):
        for j in range(1,nj):
            if word1[i-1]==word2[j-1]:
                f[i][j]=f[i-1][j-1]
            else:
                f[i][j]=min(f[i-1][j],f[i][j-1],f[i-1][j-1])+1

    return f[ni-1][nj-1]


# word1 = "intention"
# word2 = "execution"
# word1 = "horse"
# word2 = "ros"
# print(edit_distance(word1,word2))