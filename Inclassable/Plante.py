# -*- coding: utf-8 -*-
"""
Created on Mon Jun 18 15:27:15 2018

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt

plt.axis('equal')

alpha = (np.pi/180)*22.5

E = [1,0,0,0]


def l(E):
    EE = [0,0,E[2],E[3]]
    EE[0] = np.cos(alpha)*E[0] - np.sin(alpha)*E[1]
    EE[1] = np.sin(alpha)*E[0] + np.cos(alpha)*E[1]
    return EE

def r(E):
    EE = [0,0,E[2],E[3]]
    EE[0] = np.cos(alpha)*E[0] + np.sin(alpha)*E[1]
    EE[1] = - np.sin(alpha)*E[0] + np.cos(alpha)*E[1]
    return EE

def a(E):
    EE = [E[0],E[1],0,0]
    EE[2] = E[2] + E[0]
    EE[3] = E[3] + E[1]
    return EE

func_dic = {'a':a,'l':l,'r':r}

init = 'allalla'

motif = 'arallara'

def affiche(L):
    n = len(L)
    i = 0
    lx = [0]
    ly = [0]
    E = [1,0,0,0]
    while i < n:
        cara = L[i]
        E = func_dic[cara](E)
        lx.append(E[2])
        ly.append(E[3])
        i += 1
    plt.plot(lx,ly)
    return lx,ly
        
        
def assigne(n,init,motif):
    i = 0
    L = init
    while i < n:
        L = L.replace('a',motif)
        i += 1
    return L

new = assigne(4,init,motif)


#affiche(new)
    

def a2(lE):
    E = lE.pop()
    E = a(E)
    lE.append(E)
    return E
    
def l2(lE):
    E = lE.pop()
    E = l(E)
    lE.append(E)
    return E

def r2(lE):
    E = lE.pop()
    E = r(E)
    lE.append(E)
    return E
    
def e(lE):
    n = len(lE)
    new = list(lE[n - 1])
    lE.append(new)
    return E

def m(lE):
    E = lE.pop()
    return E

def x(lE):
    return E

    
    

func_dic2 = {'a':a2,'l':l2,'r':r2,'(':e,')':m,'x':x}


def affiche2(L):
    n = len(L)
    i = 0
    lx = [0]
    ly = [0]
    lE = [[0,1,0,0]]
    while i < n:
        cara = L[i]
        e = func_dic2[cara](lE)
        if cara == '(' or ')' or 'x':
            nn = len(lE)
            lx.append(lE[nn - 1][2])
            ly.append(lE[nn - 1][3])
            i += 1
    plt.plot(lx,ly)
    return lx,ly


new2 = assigne(4,'a','a(la)a(ra)a')

#affiche2(new2)


def assigne2(n,init,motif):
    L = init
    i = 0
    while i < n:
        L = L.replace('a','aa')
        L = L.replace('x',motif)
        i += 1
    return L

new3 = assigne2(6,'x','ar((x)lx)la(lax)rx')

affiche2(new3)
        

