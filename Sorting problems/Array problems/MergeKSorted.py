def merge_k(t, k):
    merged = []
    for i in range(k):
        for j in range(len(t[i])):
            merged.append(t[i][j])
    return sorted(merged)


# t=[[5,10,11,13],
#    [1,3,5,6,],
#    [4,5,6,10]]
# print(t)
# print(merge_k(t,3))
