def is_subseqence_slow(s, t):  # raczej longest common subseqence
    nj = len(s) + 1
    ni = len(t) + 1

    if nj - 1 == 0:
        return True
    if ni - 1 == 0:
        return False

    f = [[0 for j in range(nj)] for i in range(ni)]
    for i in range(1, ni):
        for j in range(1, nj):
            if s[j - 1] != t[i - 1]:
                f[i][j] = max(f[i - 1][j], f[i][j - 1])
            elif s[j - 1] == t[i - 1]:
                f[i][j] = max(f[i - 1][j - 1] + 1, f[i - 1][j - 1])

    answer = f[ni - 1][nj - 1]
    if answer == nj - 1:
        return True
    return False


def is_subseqence_fast(s, t):
    i = 0
    if s == "":
        return True
    if len(t) < len(s):
        return False
    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
    return i == len(s)


def is_subseqence_sfast(s, t):
    i = 0
    for c in s:
        if c in t[i:]:
            i = t[i:].index(c) + i + 1
        else:
            return False
    return True



# s = "abc"
# t = "ahbgdc"
# print(is_subseqence_slow(s,t))
# print(is_subseqence_fast(s,t))
# print(is_subseqence_sfast(s,t))
