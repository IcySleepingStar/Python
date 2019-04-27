# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 18:55:05 2019

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt
import random as rd

# Le plan contient des charges ponctuelles dans chacune des cases de la matrice
# La valeur de la case est la charge de la charge ponctuelle

# La dimension du plan

xmax = 1000
ymax = 1000

x = np.linspace(0,xmax - 1,xmax)
y = np.linspace(0,ymax - 1,ymax)

X,Y = np.meshgrid(x,y)

def distance(x1,y1,x2,y2):
	return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# renvoie un plan contenant n1 charges ponctuelles de charge +q1 et n2 charges ponctuelles de charge -q2
# réparties aléatoirement

def ChargePlane(M,q):
	x = rd.randint(0, xmax - 1)
	y = rd.randint(0, ymax - 1)
	if M[x,y] == 0:
		M[x,y] = q
	else:
		ChargePlane(M,q)

def ChargedPlane(n1,q1,n2,q2):
	P = np.zeros((xmax, ymax))
	for k in range(n1):
		ChargePlane(P, q1)
	for k in range(n2):
		ChargePlane(P, -q2)
	return P

# renvoie le plan en rajoutant un disque de charge q de rayon r centré en (x,y)

def ChargePlaneWithDisc(M,x,y,r,q):
	for i in range(xmax):
		for j in range(ymax):
			if distance(x,y,i,j) < r:
				M[i,j] = q



def Champ(P,lc,x,y):
	Ex,Ey = 0,0
	for (i,j) in lc:
		if x != i and y != j:
			Ex += (P[i,j]/(distance(x,y,i,j)**3))*(x - i)
			Ey += (P[i,j]/(distance(x,y,i,j)**3))*(y - j)
	return Ex,Ey

# Etant donné la liste des points contenants des charges et la matrice qui représente le plan,
# cette fonction renvoie la composante du champs selon x et selon y

def NewChamp(P,lc):
	U,V = np.zeros((xmax,ymax)),np.zeros((xmax,ymax))
	for x in range(xmax):
		for y in range(ymax):
			Ex,Ey = Champ(P,lc,x,y)
			U[x,y] = Ex
			V[x,y] = Ey
	return U,V

def ListCharges(P):
	l = []
	for i in range(xmax):
		for j in range(ymax):
			if P[i,j] != 0:
				l.append((i,j))
	return l


fig,ax = plt.subplots()
ax.set_title("Lignes de champs éléctrostatique")

Ptest = np.zeros((xmax,ymax))

ChargePlaneWithDisc(Ptest,500,250,5,-1)
ChargePlaneWithDisc(Ptest,300,750,5,1)
ChargePlaneWithDisc(Ptest,700,750,5,1)

#ChargePlaneWithDisc(Ptest,50,25,5,1)
#ChargePlaneWithDisc(Ptest,30,75,5,-1)
#ChargePlaneWithDisc(Ptest,70,75,5,-1)

#ChargePlaneWithDisc(Ptest,50,50,5,1)


LcPtest = ListCharges(Ptest)

Plane = ChargedPlane(2, 4, 3, 2)

AbsPlane = abs(Plane)
AbsPtest = abs(Ptest)

ax.imshow(AbsPtest, cmap = 'gray_r')

V,U = NewChamp(Ptest,LcPtest)

ax.streamplot(X,Y,U,V)