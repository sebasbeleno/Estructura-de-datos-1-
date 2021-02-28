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

import random, string

def lcs(i, j, x, y):
    if(i<0 or j<0):#c0
        return -1 #c1
    if(x[i:i+1] == y[j:j+1]): #c2
        return lcs(i-1, j-1, x, y) + 1 #T(p-2)
    return max(lcs(i-1, j, x, y), lcs(i, j-1, x, y)) #T(p-1) + T(p-1)
#we get 
#Worst case:
# T(p) = T(p-1) + T(p-1) + c3 =  c3((2**p)-1) + c4*2**p-1
#then
#T(p) = O(2**p) with p being the sum of the length of the two strings

x ="ABCD"
y ="ABCD"
#print(lcs(len(x),len(y),x,y))
