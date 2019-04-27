# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 15:17:08 2018

@author: adrie
"""

from random import random
from scipy.integrate import quad 
import matplotlib.pyplot as plt
from math import exp, tan, pi, sqrt
 


#décentré à gauche
def m1(f,a,b,n):
    S = 0.
    x = a
    pas = (b-a)/n
    for i in range(n):
        S += f(x)
        x += pas
    return (S*pas)


#décentré à droite
def m2(f,a,b,n):
    S = 0.
    pas = (b-a)/n
    x = a + pas
    for i in range(n):
        S += f(x)
        x += pas
    return (S*pas)
     

#centré
def m3(f,a,b,n):
    S = 0.
    pas = (b-a)/n
    x = a + pas/2
    for i in range(n):
        S += f(x)
        x += pas
    return (S*pas)
     

#méthode des trapèzes
def m4(f,a,b,n):
    S = f(a) + f(b)
    pas = (b-a)/n
    x = a + pas
    for i in range(n-1):
        S += 2*f(x)
        x += pas
    return (S*(b-a)/(2*n))


#méthode de Simpson
def m5(f,a,b,n):
    S = 0.
    pas = (b-a)/(2*n)
    valgauche = f(a)
    x = a
    for i in range(n):
        x += pas
        S += valgauche + 4*f(x)
        x += pas
        valgauche = f(x)
        S += valgauche
    return (S*pas/3)
     



def Graphe(f,a,b,n):
    abscisse=[]
    ordonne=[]
    x=a
    pas=(b-a)/n
    for i in range(n+1):
        abscisse.append(x)
        ordonne.append(f(x))
        x+=pas
    plt.plot(abscisse,ordonne)
    plt.show()
    return (abscisse,ordonne)











































print("fin")