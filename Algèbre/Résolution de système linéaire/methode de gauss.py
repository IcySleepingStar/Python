# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 16:05:15 2018

@author: adrie
"""

from copy import deepcopy

A = [[1, 3], [1, 7]]

B = [2, 6]

S2 = [-1, 1]



M = [[3, 3, -4], [2, 6, 1], [-1, 1, 0]]

C = [-2, 10, 0]

S = [1, 1, 2]

def indicepivot(M, i):
    p = len(M)
    k = i
    pivot = 0
    ipivot = i
    while k < p:
        if abs(M[k][i]) > pivot:
            ipivot = k
            pivot = abs(M[k][i])
        k += 1
    return ipivot

#print(indicepivot(M, 0))


def permutation(M, i, j):
    (M[i], M[j]) = (M[j], M[i])

#permutation(M, 0, 1)
#print(M)

    

#nettoyage de M avec la ligne i
def nettoyage(M, i):
    p = len(M)
    k = i + 1
    pivot = M[i][i]
    while k < p:
        a = (M[k][i])/pivot
        j = i
        while j < p:
            M[k][j] = M[k][j] - (a*M[i][j])
            j += 1
        k += 1


def nettoyageSM(M, S, i):
    p = len(M)
    k = i + 1
    pivot = M[i][i]
    while k < p:
        a = (M[k][i])/pivot
        S[k] = S[k] - (a*S[i])
        k += 1


#nettoyageSM(M, C, 0)
#print(C)

#nettoyage(M, 1)
#print(M)


def remonter(M, S):
    p = len(M)
    i = p - 1
    sol = []
    while i >= 0:
        b = 0
        k = 0
        while k < p - i - 1:
            b = b + (sol[k]*M[i][p - 1 - k])
            k += 1
        a = (S[i] - b)/(M[i][i])
        sol.append(a)
        i -= 1
    sol.reverse()
    return sol

        
#print(remonter([[1, 3],[0, 4]], [2, 4])) 
        
        


def triangularisation(M):
    i = 0
    p = len(M)
    while i < p:
        ipivot = indicepivot(M, i)
        permutation(M, ipivot, i)
        nettoyage(M, i)
        i += 1
    return M




#print(triangularisation(M))

    
def resoudre(M, S):
    i = 0
    p = len(M)
    while i < p:
        ipivot = indicepivot(M, i)
        permutation(M, i, ipivot)
        permutation(S, i, ipivot)
        N = deepcopy(M)
        nettoyage(M, i)
        nettoyageSM(N, S, i)
        i += 1
    sol = remonter(M, S)
    return sol


print(resoudre(M, C))
        
        











print("done")
        