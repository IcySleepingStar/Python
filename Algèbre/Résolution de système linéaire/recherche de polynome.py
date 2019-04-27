# -*- coding: utf-8 -*-
"""
Created on Mon May  7 15:52:29 2018

@author: adrie
"""

#on donne une liste de n + 1 points et on cherche le polynome de degré n qui passe par ces points

lili = [[2,4],[4,1],[8,0],[6,8],[3,7]]

import numpy as np
from copy import deepcopy
import matplotlib.pylab as plt



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
#print(C)


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


#print(gauss(A,B))




def givemat(liste):
    n = len(liste)
    i = 0
    A = []
    B = []
    while i < n:
        j = 1
        l = [1]
        while j < n:
            l.append((liste[i][0])**j)
            j += 1
        A.append(l)
        i += 1
    i = 0
    while i < n:
        B.append(liste[i][1])
        i += 1
    return[A,B]



#print(givemat(lili))


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


def tilde(pol,x):
    n = len(pol)
    i = 0
    sol = 0
    while i < n:
        sol += (pol[i]*(x**i))
        i += 1
    return sol




def tabpol(P,xi,xii,N):
    h = (xii - xi)/N
    tabx = []
    taby = []
    i = xi
    while i <= xii:
        tabx.append(i)
        v = tilde(P,i)
        taby.append(v)
        i += h
    return [tabx,taby]





def trouvepol(liste):
    A = givemat(liste)[0]
    B = givemat(liste)[1]
    S = resoudre(A,B)
    return S

#print(trouvepol(lili))



def printpol(P, x1, x2, N):
    t = tabpol(P, x1, x2, N)
    plt.plot(t[0],t[1])


printpol(trouvepol(lili),2,8, 100)



