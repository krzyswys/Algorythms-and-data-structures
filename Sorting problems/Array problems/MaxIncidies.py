def max_incidies(t):
    n = len(t)
    new = []

    for i in range(n - 1):
        if t[i] == t[i + 1]:
            new.append(t[i])

    max_v = max(new)
    count = [0] * (max_v + 1)
    for i in range(len(new)):
        count[new[i]] += 1

    max_vC = max(count)
    for i in range(len(count)):
        if count[i] == max_vC:
            index = i

    return count, new, index


# t=[5,6,2,2,8,2,3,35,5,5,5,5,5,5,5,2,2,2,3,2,2,2,3,2,5,5,5,5,5,3,3,3,3,3,3,3,1]
# print(t)
# print(max_incidies(t))
