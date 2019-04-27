# -*- coding: utf-8 -*-
"""
Created on Sun Feb 08 19:10:41 2015

@author: Antoine
"""
#################################################
#           Outils pour la résolution           #
#################################################

import numpy as np
from scipy.optimize import fsolve
import pylab as plt


###################################    
#Différentes méthodes de résolution
###################################

#Dichotomie (à compléter)

#def Dichotomie...

def Dichotomie(f, a, b, e):
    while abs(f(a) - f(b)) > e and f(a)*f(b) < 0:
        c = f(a)*f(b)
        if f(c)*f(a) < 0:
            b = c
        else:
            a = c
    return a

def f(x):
    a = 2*(x**2) + 2*x - 1
    return a



#Lagrange (à compléter)

#def Lagrange...    
       
#Newton (à compléter)

#def Newton...


##################################################
#      Résolution 1 : Mécanisme de direction     #
##################################################

########################
# Paramètres du problème
########################

#Données géométriques
a=25
b=22
L=75
c=75
d=40

#fonction à résoudre
def f(theta5):
    return (a*np.sin(theta5)+c+b*np.sin(theta3))**2+(-a*np.cos(theta5)+d-b*np.cos(theta3))**2-L**2

  

#######################################
#Calcul de theta5 en fonction de theta3
#######################################
      
#liste de valeurs pour theta3  
abscisse = np.linspace(-0.8, 0.8, 100)

#résolution par scipy
ordonnee_scipy=[]
for theta3 in abscisse:
    ordonnee_scipy.append(fsolve(f,0))

#résolution par dichotomie (à compléter)

    
#résolution par Lagrange (à compléter)

    
#résolution par Newton (à compléter)



##################
#Tracé des courbes
##################
plt.plot(abscisse, ordonnee_scipy,label='fsolve')
plt.legend()
plt.xlabel('$\Theta 3$ en rad')
plt.ylabel('$\Theta 5$ en rad')
plt.title('loi entree sortie')
#plt.grid(True)
plt.show()
print("fin")