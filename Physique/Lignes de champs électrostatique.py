# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 15:38:51 2019

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

dx = 50

dy = 50


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

def InPlane(x,y):
	return (0 <= x < xmax and 0 <= y < ymax)

def LigneDeChamp(P,lc,x,y,n):
	lx = [x]
	ly = [y]
	i = 0
	while InPlane(int(x),int(y)) and P[int(x),int(y)] == 0 and i < n:
		Ex,Ey = Champ(P,lc,int(x),int(y))
		x += Ex*dx
		y += Ey*dy
		lx.append(x)
		ly.append(y)
		i += 1
	return lx,ly
		
def ListNextToPlus(M):
	l = []
	for i in range(xmax):
		for j in range(ymax):
			if M[i,j] == 0 and (M[min(i + 1,xmax - 1),j] == 0 or M[max(i - 1,0),j] == 0 or M[i,min(j + 1,ymax - 1)] == 0 or M[i, max(j - 1,0)] == 0) and (M[min(i + 1,xmax - 1),j] > 0 or M[max(i - 1,0),j] > 0 or M[i,min(j + 1,ymax - 1)] > 0 or M[i, max(j - 1,0)] > 0):
				l.append((i,j))
	return l

def ListCharges(P):
	l = []
	for i in range(xmax):
		for j in range(ymax):
			if P[i,j] != 0:
				l.append((i,j))
	return l

def PlotLigneDeChamp(P,n):
	lc = ListCharges(P)
	lntp = ListNextToPlus(P)
	for (x,y) in lntp:
		lx,ly = LigneDeChamp(P,lc,x,y,n)
		plt.plot(lx,ly,'r')
	

Ptest = np.zeros((xmax,ymax))

ChargePlaneWithDisc(Ptest,500,250,5,-1)
ChargePlaneWithDisc(Ptest,300,750,5,1)
ChargePlaneWithDisc(Ptest,700,750,5,1)

LcPtest = ListCharges(Ptest)

Plane = ChargedPlane(2, 4, 3, 2)

AbsPlane = abs(Plane)
AbsPtest = abs(Ptest)

plt.imshow(AbsPtest.T, cmap = 'gray_r')

#lx,ly = LigneDeChamp(Ptest,LcPtest,30,30,1000)
#plt.plot(lx,ly)

PlotLigneDeChamp(Ptest,100000)