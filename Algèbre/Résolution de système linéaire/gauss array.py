# -*- coding: utf-8 -*-
"""
Created on Mon Apr 30 10:10:07 2018

@author: adrie
"""

import numpy as np

A = np.array([[1,3,2],[2,1,4],[-1,2,3]])
B = np.array([7,8,3])
#print(A)
#print(B)
#print(len(B))

def augmente(A, B):
    p = len(A)
    i = 0 
    C = np.zeros([p, p + 1])
    while i < p:
        j = 0
        while j < p + 1:
            if j < p:
                C[i,j] = A[i,j]
            else:
                C[i,j] = B[i]
            j += 1
        i += 1
    return C

#print(np.shape(augmente(A,B)))

C = augmente(A, B)
print(C)


def echangeligne(M, i, j):
    p = np.shape(M)[1]
    k = 0
    while k < p:
        (M[i,k],M[j,k]) = (M[j,k],M[i,k])
        k += 1

#echangeligne(C, 0, 1) 
#print(C)


def elimine(M, i, j, l):
    k = 0
    p = np.shape(M)[1]
    while k < p:
        M[j,k] = M[j,k] + (l * M[i,k])
        k += 1

#elimine(C, 0, 1, -1)
#print(C)



def normalise(M, i, l):
    k = 0
    p = np.shape(M)[1]
    while k < p:
        M[i,k] = l * M[i,k]
        k += 1


#normalise(C, 0, -1)
#print(C)

def pivot(M, i):
    k = i
    m = 0
    pivot = -1
    p = np.shape(M)[0]
    while k < p:
        if abs(M[k,i]) > m:
            m = abs(M[k,i])
            pivot = k
        k += 1
    return pivot

def secondmb(M):
    p = np.shape(M)[0]
    j = np.shape(M)[1]
    k = 0
    B = np.zeros([p])
    while k < p:
        B[k] = M[k,j - 1]
        k += 1
    return B

#print(secondmb(C))



def gauss(A, B):
    M = augmente(A, B)
    p = np.shape(M)[0]
    i = 0
    while i < p:
        lpivot = pivot(M, i)
        echangeligne(M, i, lpivot)
        l = 1/M[i,i]
        normalise(M, i, l)
        j = 0
        while j < p:
            if j != i:
                l = -M[j,i]
                elimine(M, i, j, l)
            j += 1
        i += 1
    S = secondmb(M)
    return(S)

print(gauss(A, B))

AA = np.array([[1, 0.25, 1], [1, 1/3, 2],[0, 1, 12]])
BB = np.array([0, 0, 1])

print(gauss(AA, BB))

    












