import sys 

#change in the maximum recursion level allowed
sys.setrecursionlimit(10**6) 


def subconjuntos(s):
    return subconjuntosBase("", s).split() #P(n) + c4
def subconjuntosBase(base, t):
    if(t == ""): #c1
        return base #c2
    return subconjuntosBase(base + t[0], t[1:]) + " " + subconjuntosBase(base, t[1:]) # P(n) = P(n-1) + P(n-1) 

#P(n) = c1 + c2 if n = 0
#P(n) = c3*2**n-1

def subCadenaMax(s1,s2):
    lst1 = subconjuntos(s1) #P(n) + c4
    lst2 = subconjuntos(s2) #P(m) + c4
    lst1.sort(key = len, reverse = True) #G(n) = nlog( n*(n+1)/2) + c5 <--- timsort
    lst2.sort(key = len, reverse = True) #G(m) = mlog( m*(m+1)/2) + c5 <--- timsort
    for subS1 in lst1: #c6*n
        if (subS1 in lst2): # c7*n*m
            return subS1 #c8*n
        
#We get T(n,m) =
# c3*2**n-1 + c4 + c3*2**m-1 + c4 + nlog( n*(n+1)/2)  + c5 + mlog( m*(m+1)/2) + c5 + c6*n + c7*n*m + c8*n
# so T(n,m) = O(2**n + 2**m)
#With n being the lenght of s1 and m the lenght of s2
print(subCadenaMax(input(), input()))

#----------------------------------------------------------#

"""
Title: Python Program for Longest Common Subsequence
Author: contributed by multiple authors from GeeksforGeeks
Date: 18 Apr, 2020
Code version: last updated in 18 Apr, 2020
Availability: https://www.geeksforgeeks.org/python-program-for-longest-common-subsequence/
"""
def lcsAux(X, Y, m, n): 
  
    if m == 0 or n == 0: #c1
       return 0; #c2
    elif X[m-1] == Y[n-1]: #c3
       return 1 + lcsAux(X, Y, m-1, n-1); #c4 + P(p-2)
    else: #c5
       return max(lcsAux(X, Y, m, n-1), lcsAux(X, Y, m-1, n)); # c5 + P(p-1) + P(p-1)

def lcs(str1, str2): 
    return lcsAux(str1, str2, len(str1), len(str2)) #P(p) + c6

#We get 
# T(p) = P(p) + c6
# worst case
#P(p) = c5 + P(p-1) + P(p-1)
#With p being the sum of the lenght of the two strings
