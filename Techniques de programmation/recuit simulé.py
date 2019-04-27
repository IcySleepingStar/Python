# -*- coding: utf-8 -*-
"""
Created on Wed Dec 12 16:11:45 2018

@author: adrie
"""

import numpy as np
import random
from copy import copy

xt = 0.001

# distance entre deux points: sqrt((xi - xj)² + (yi - yj)²)
# il faut donc 6 opérations elementaires pour calculer une distance

# il y a N² valeur dans la matrice donc il faut 6N² operations pour former la matrice

# il y a N! parcours possibles
# le calcul d'un parcours coute N operations elementaires

# donc le cout total est de N*N!

def factoriel(n):
	if n == 0:
		return 1
	else:
		return factoriel(n - 1)*n
	

# 3GHz donc 3 000 000 000 operations par secondes
# donc 16219346721 secondes
# donc 514 années et 4 mois


def distance(x1,y1,x2,y2):
	return (((x1 - x2)**2) + ((y1 - y2)**2))**(0.5)

def separe(V):
	n = len(V)
	I,J = [],[]
	for i in range(n):
		I.append(V[i][0])
		J.append(V[i][1])
	return I,J

def dismat(V):
	n = len(V)
	mat = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			mat[i][j] = distance(V[i][0],V[i][1],V[j][0],V[j][1])
	return mat


V1 = [[0,0],[3,2],[5,8],[2,4]]
V2 = [[0,0],[3,2],[5,8],[2,4],[9,3],[23,8],[12,0],[34,78],[3,4],[4,8]]
V3 = [[4,9],[12,98],[45,76],[23,0],[67,81],[90,21],[3,32],[54,83]]
V4 = [[0,0],[3,2],[5,8],[2,4],[9,3],[23,8],[12,0],[34,78],[3,4],[4,8],[4,9],[12,98],[45,76],[23,0],[67,81],[90,21],[3,32],[54,83],[3,234],[324,987],[894,236],[324,863],[112,323]]

mat1 = dismat(V1)
mat2 = dismat(V2)
mat3 = dismat(V3)
mat4 = dismat(V4)

# un trajet est une permutation
# c'est a dire une liste des entiers de 0 a N - 1 dans N cases
# donc trajet est une liste

def energie(trajet,distmatrice):
	n = len(trajet)
	E = 0
	for i in range(n):
		E += distmatrice[trajet[i - 1]][trajet[i]]
	return E

def newpermutation(l):
	n = len(l)
	i = random.randint(1,n)
	j = random.randint(1,n)
	if i == j:
		return newpermutation(l)
	else:
		if j > i:
			return [l[k] for k in range(i)] + [l[i + j - k - 1] for k in range(i,j)] + [l[k] for k in range(j,n)]
		else:
			i,j = j,i
			return [l[k] for k in range(i)] + [l[i + j - k - 1] for k in range(i,j)] + [l[k] for k in range(j,n)]		
		

def recuitsim(villes,gen,T0):
	n = len(villes)
	x = [i for i in range(n)]
	T = T0
	mat = dismat(villes)
	E0 = energie(x,mat)
	bestx = x
	minE = E0
	for k in range(1,gen):
		y = newpermutation(x)
		E1 = energie(y,mat)
		D = E1 - E0
		T = (1 - xt)*T
		if D < 0:
			x = y
			if E1 < minE:
				minE = E1
				bestx = x
		else:
			p = random.random()
			lim = np.exp(-(D/T))
			if p < lim:
				x = y
				if E1 > minE:
					minE = E1
					bestx = x
		E0 = E1
	return minE



def perm(n):
	if n == 1:
		return [[0]]
	else:		
		res = []
		l = perm(n - 1)
		for i in range(n):
			for lili in l:
				li = copy(lili)
				li.insert(i,(n - 1))
				res = res + [li]
		return res
		
	

def calcul_total(villes):
	n = len(villes)
	mat = dismat(villes)
	lp = perm(n)
	Emin = np.inf
	for l in lp:
		E = energie(l,mat)
		if E < Emin:
			x = l
			Emin = E
	return Emin,x


def permalea(l):
	n = len(l)
	if n == 0:
		return []
	else:
		i = random.randint(0, n - 1)
		x = l.pop(i)
		return [x] + permalea(l)


def randsol(villes,k):
	n = len(villes)
	mat = dismat(villes)
	Emin = np.inf
	for i in range(k):
		y = permalea([i for i in range(n)])
		E = energie(y,mat)
		if E < Emin:
			Emin = E
			x = y
	return Emin

def randvilles(n):
	return [[random.randint(1,10000),random.randint(1,10000)] for k in range(n)]

V0 = randvilles(100)

