def longestPalindrom(s):
    n = len(s)
    f = 0
    for i in range(n - 1):
        if s[i] != s[i + 1]:
            f = 1
    if f == 0:
        return s
    res = ""
    length = 0
    for i in range(n):
        l, r = i, i
        while r < n and l >= 0 and s[l] == s[r]:
            if length < (r - l + 1):
                res = s[l : r + 1]
                length = r - l + 1
            r += 1
            l -= 1

        l, r = i, i + 1
        while r < n and l >= 0 and s[l] == s[r]:
            if length < (r - l + 1):
                res = s[l : r + 1]
                length = r - l + 1
            r += 1
            l -= 1

    return res


def longestPalindrom_fast(s):
    if not s:
        return ""
    maxlen, start = 1, 0
    for i in range(len(s)):
        step2 = i - maxlen - 1
        step1 = i - maxlen
        if step2 >= 0 and s[step2 : i + 1] == s[step2 : i + 1][::-1]:
            start = step2
            maxpen += 2
            continue
        if step1 >= 0 and s[step1 : i + 1] == s[step1 : i + 1][::-1]:
            start = step1
            maxlen += 1
    return s[start : start + maxlen]


# word="cbbd"
# word="babad"
# word = "abb"
# print(longestPalindrom(word))
