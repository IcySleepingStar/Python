# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 15:53:34 2018

@author: adrien
"""




import numpy as np
from scipy.optimize import fsolve
import pylab as plt

def Dichotomie(f, a, b, e):
    while abs(f(a) - f(b)) > e and f(a)*f(b) < 0:
        c = (a + b)/2
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return b

def g(x):
    return x**3 - 1



def Lagrange(f, a, b, n):
    i = 0
    while i < n:
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
        i += 1
    return c

def Newton(f, a, n):
    i = 0
    while i < n:
        d = ( f(a + 0.00001) - f(a))/0.00001
        a = a - (f(a)/d)
        i += 1
    return a
        


a=25
b=22
L=75
c=75
d=40

def f(theta5):
    return (a*np.sin(theta5)+c+b*np.sin(theta3))**2+(-a*np.cos(theta5)+d-b*np.cos(theta3))**2-L**2



abscisse = np.linspace(-0.8, 0.8, 100)

#résolution par scipy
ordonnee_scipy=[]
for theta3 in abscisse:
    ordonnee_scipy.append(Newton(f, 0, 10))


plt.plot(abscisse, ordonnee_scipy,label='fsolve')
plt.legend()
plt.xlabel('$\Theta 3$ en rad')
plt.ylabel('$\Theta 5$ en rad')
plt.title('loi entree sortie')
plt.grid(True)
plt.show()
print("fin")