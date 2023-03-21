


def anagram(A,B): #O(n+k)
    k = ord('z') - ord('a') + 1
    t=[0]*k
    for j in range(len(A)): t[ord(A[j])-ord('a')]+=1
    for j in range(len(A)):
        index=ord(B[j])-ord('a')
        t[index]-=1
        if t[index]<0:
            return False
    return True



def anagram2(A,B,t): #O(n), pamiec: n+k
    for j in A: t[ord(j)-ord("a")]=0
    for j in B: t[ord(j) - ord("a")] = 0
    for j in A: t[ord(j) - ord("a")] +=1
    for j in B:
        index=ord(j)-ord('a')
        t[index]-=1
        if t[index]<0:
            return False
    return True

# import random
# t=[random.randint(123,34234) for _ in range(44)]
# print(anagram("aabx","abxa"))