# -*- coding: utf-8 -*-
"""
Created on Sun May  6 21:48:10 2018

@author: adrie
"""

import matplotlib.pylab as plt
from math import sqrt
from random import randint,random
from copy import deepcopy


#les points de controles sont representé par une liste de liste à deux element
#splinecub prend en argument la liste de n [abscisse,ordonne,derive]
#splinecub renvoie la liste de n - 1 [a,b,c,d] qui represente le polynome Yi
#on suppose que les triplet sont ordonnes par leur premier element

liste = [[0,0,3],[2,5,1],[5,4,2],[6,8,7],[8,2,5],[10,4,0]]
liste2 = [[0,3],[2,2],[5,8],[6,1],[8,4],[10,5]]


"""

ne marche pas

def splinecub(lili): 
    n = len(lili)
    i = 0
    sol = []
    while i < (n - 1):
        l = []
        yi = lili[i][1]
        yii = lili[i + 1][1]
        di = lili[i][2]
        dii = lili[i + 1][2]
        l.append(yi)
        l.append(di)
        l.append((-2*di) - dii + (3*(yi + yii)))
        l.append(dii + di + (2*(yi - yii)))
        sol.append(l)
        i += 1
    return sol

#print(splinecub(liste))

#extrait la colonne i de la matrice lili

def extract(lili,i):
    n = len(lili)
    k = 0
    sol = []
    while k < n:
        sol.append(lili[k][i])
        k += 1
    return sol

#print(extract(liste,0))

def tilde(pol,x):
    n = len(pol)
    i = 0
    sol = 0
    while i < n:
        sol += (pol[i]*(x**i))
        i += 1
    return sol

#poly = [2,6,1,2]
#print(tilde(poly,0))


def tab(Y,xi,xii,n):
    i = 0
    h = (1/n)
    tabx = []
    taby = []
    while i <= 1:
        a = tilde(Y, ((i - xi)/(xii - xi)))
        taby.append(a)
        tabx.append((i*(xii - xi)) + xi)
        i += h
    return [tabx,taby]
        



def printpol(lili,n):
    pol = splinecub(lili)
    absi = extract(lili,0)
    i = 0
    n = len(lili)
    while i < (n - 1):
        Yi = pol[i]
        xi = absi[i]
        xii = absi[i + 1]
        t = tab(Yi,xi,xii,n)
        plt.plot(t[0],t[1])
        i += 1
        
#printpol(liste,1000)
        
"""

def maxi(liste, i):
    n = len(liste)
    m = liste[0][i]
    k = 1
    while k < n:
        a = liste[k][i]
        if a > m:
            m = a
        k += 1
    return m



def mini(liste, i):
    n = len(liste)
    m = liste[0][i]
    k = 1
    while k < n:
        a = liste[k][i]
        if a < m:
            m = a
        k += 1
    return m



#print(mini(liste, 1))



#ajoute a la liste la derivé telle que la tangente en un point soit parralele a la droite reliant les points encadrant ce point

def ajoutderiv(liste):
    n = len(liste)
    i = 1
    liste[0].append(0)
    while i < (n - 1):
        p = (liste[i + 1][1] - liste[i - 1][1])/(liste[i + 1][0] - liste[i - 1][0])
        liste[i].append(p)
        i += 1
    liste[n - 1].append(0)


#ajoute les derivé au pif

def ajoutderand(liste):
    a = mini(liste, 1)
    b = maxi(liste, 1)
    n = len(liste)
    i = 0
    while i < n:
        x = (b - a)*random() + a
        liste[i].append(x)
        i += 1
    





#print(liste2)
#ajoutderand(liste2)
#print(liste2)




#renvoie la liste des polynomes generé par les points de controles de lili

def spline(lili):
    n = len(lili)
    i = 0
    sol = []
    while i < (n - 1):
        xi = lili[i][0]
        xii = lili[i + 1][0]
        yi = lili[i][1]
        yii = lili[i + 1][1]
        di = lili[i][2]
        dii = lili[i + 1][2]
        A = (-0.5*(xii**3)) + (0.5*(xi**3)) - ((3/2)*xii*(xi**2)) + ((3/2)*xi*(xii**2))
        B = yii - yi + ((1/2)*(xi - xii)*(di + dii))
        d = B/A
        c = (dii - di - (3*((xii**2) - (xi**2))*d))/(2*(xii -xi))
        b = di - (3*(xi**2)*d) - (2*xi*c)
        a = yi - (d*(xi**3)) - ((xi**2)*c) - (xi*b)
        l = [a,b,c,d]
        sol.append(l)
        i += 1
    return sol



#print(spline(liste))


def tilde(pol,x):
    n = len(pol)
    i = 0
    sol = 0
    while i < n:
        sol += (pol[i]*(x**i))
        i += 1
    return sol


poly = [1,3,8,3]
#print(tilde(poly, 1))


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


#extrait la colonne i de la matrice lili

def extract(lili,i):
    n = len(lili)
    k = 0
    sol = []
    while k < n:
        sol.append(lili[k][i])
        k += 1
    return sol


#print(extract(liste, 0))


#print(tabpol(poly, 0, 1, 100))




def printpoint(liste):
    n = len(liste)
    i = 0
    while i < n:
        plt.plot(liste[i][0], liste[i][1], 'kD')
        i += 1


#printpoint(liste)



def printspline(liste, N):
    printpoint(liste)
    n = len(liste)
    listpoly = spline(liste)
    absi = extract(liste, 0)
    i = 0
    while i < (n - 1):
        xi = absi[i]
        xii = absi[i + 1]
        pi = listpoly[i]
        couple = tabpol(pi, xi,xii, N)
        plt.plot(couple[0], couple[1], 'k')
        i += 1

#ajoutderiv(liste2)
#printspline(liste2, 100)




def derivpol(P):
    n = len(P)
    sol = []
    i = 1
    while i < n:
        sol.append(P[i]*i)
        i += 1
    return sol

#print(derivpol(P))




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


#cette fonction prend en argument la liste des points sans les derivées et les ajoute avec ajoutderiv

def arclenspline(liste,N):
    ajoutderiv(liste)
    lp = spline(liste)
    n = len(lp)
    i = 0
    sol = 0
    while i < n:
        xi = liste[i][0]
        xii = liste[i + 1][0]
        P = lp[i]
        arci = arclen(P,xi,xii,N)
        sol += arci
        i += 1
    return sol

#print(arclenspline(liste2, 1000))

#pour cette fonction la derivée est deja en argument

def arclenspline2(liste,N):
    lp = spline(liste)
    n = len(lp)
    i = 0
    sol = 0
    while i < n:
        xi = liste[i][0]
        xii = liste[i + 1][0]
        P = lp[i]
        arci = arclen(P,xi,xii,N)
        sol += arci
        i += 1
    return sol


#print(arclenspline2(liste, 1000))



#cette fonction compare la longueur pour des choix different de derivé
#les arguments ne comportent donc pas la derivée

def compare(liste,N):
    l1 = deepcopy(liste)
    sol1 = arclenspline(l1,N)
    m = -1
    for i in range(10000):
        l = deepcopy(liste)
        ajoutderand(l)
        a = arclenspline2(l,N)
        if ((a < m) or (m == -1)):
            m = a
    return sol1,m

print(compare(liste2, 100))




