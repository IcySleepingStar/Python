# -*- coding: utf-8 -*-
"""
Created on Tue May  8 13:48:54 2018

@author: adrie
"""

from math import sqrt,cos



P = [1,3,2,8,9]

def derivpol(P):
    n = len(P)
    sol = []
    i = 1
    while i < n:
        sol.append(P[i]*i)
        i += 1
    return sol

#print(derivpol(P))


def tilde(pol,x):
    n = len(pol)
    i = 0
    sol = 0
    while i < n:
        sol += (pol[i]*(x**i))
        i += 1
    return sol



# f(x,P) revoie sqrt(1 + P'(x)²)

def f(x,P):
    p = derivpol(P)
    sol = sqrt(1 + ((tilde(p,x))**2))
    return sol

#print(f(1,P))



#méthode de Simpson pour un polynome f(x,P)

def m5(f,P,a,b,n):
    S = 0.
    pas = (b-a)/(2*n)
    valgauche = f(a,P)
    x = a
    for i in range(n):
        x += pas
        S += valgauche + 4*f(x,P)
        x += pas
        valgauche = f(x,P)
        S += valgauche
    return (S*pas/3)
     

def arclen(P,a,b,n):
    sol = m5(f,P,a,b,n)
    return sol

print(arclen(P, 0, 10, 100))
    


