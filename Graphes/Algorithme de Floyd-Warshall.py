# -*- coding: utf-8 -*-
"""
Created on Wed Nov 28 16:17:22 2018

@author: adrie
"""

import numpy as np
from copy import deepcopy
np.set_printoptions(threshold=1000)


dico={'Paris':0,'Marseille':1,'Lyon':2,'Toulouse':3,'Nice':4,'Nantes':5,'Bordeaux':6,'Lille':7,'Strasbourg':8,
'Montpellier':9,'Brest':10,'Nancy':11,'Rouen':12,'Orléans':13,'Tours':14,'Dijon':15,'Besançon':16, 
'Grenoble':17,'Clermont-Ferrand':18,'Rennes':19,'Poitiers':20,'Amiens':21}

revdico = { dico[x] : x for x in dico}

distances = [(0,2,465),(2,1,314),(2,18,164),(15,2,194),(2,17,112),(11,2,404),(11,15,214),(11,8,159),(11,0,385),
             (1,4,199),(1,9,169),(3,6,245),(3,9,247),(6,20,258),(20,5,219),(20,18,319),(20,14,105),(14,5,216),
             (14,13,117),(14,19,257),(14,18,240),(13,0,132),(13,12,252),(13,19,305),(13,5,335),(13,18,300),
             (13,11,449),(21,0,145),(21,11,420),(21,7,145),(21,12,120),(21,8,526),(12,0,136),(12,19,311),(12,14,310),
             (19,5,113),(19,10,242),(19,0,349),(5,10,295),(5,6,347),(7,0,225),(12,7,256),(11,7,418),(7,8,525),
             (7,15,502),(7,2,691),(2,9,303),(16,15,92),(16,2,255),(16,8,243),(16,11,206),(16,0,410),(17,1,306),
             (17,9,295),(0,3,679),(0,6,584),(18,9,332)]


# le plus court chemin ne passant que par des sommets jusqu'a k - 1 reliant i et j est le minimum de 
   # le plus court chemin ne passant que par des sommets jusqu'a k - 2
   # le plus court chemin de i vers k - 1 + le plus court chemin de k - 1 vers j

A = np.array([[0,2,4,np.inf],
			   [2,0,1,5],
			   [4,1,0,3],
			   [np.inf,5,3,0]])

# distance a une complexité en O(n**3)

def distance(A):
	B = deepcopy(A)
	n = len(B)
	for k in range(1,n + 1):
		nB = deepcopy(B)
		for i in range(n):
			for j in range(n):
				nB[i][j] = min(B[i][j], B[i][k - 1] + B[k - 1][j])
		B = deepcopy(nB)
	return B


# le predecesseur de j dans le plus court chemin reliant i a j avec des sommets d'indices 
# entre 0 et k - 1 est
	# soit le predecesseur de j dans le plus court chemin reliant i a j avec des sommets 
	# d'indices entre 0 et k - 1 si le meilleur chemin ne passe pas par k - 1
	
	# soit le predecesseur de j dans le plus court chemin reliant k - 1 a j avec des 
	# sommets d'indices entre 0 et k - 2 si le meilleur chemin passe par k - 1

def construitP(A):
	n = len(A)
	P = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if A[i][j] == np.inf:
				P[i][j] = -1
			else:
				P[i][j] = i
	return P


# distancepred a une complexité en O(n**3)


def distancepred(A):
	Po = construitP(A)
	n = len(A)	
	B = deepcopy(A)
	P = deepcopy(Po) 
	for k in range(1, n + 1):
		Pk = np.zeros((n,n))
		Bk = np.zeros((n,n))
		for i in range(n):
			for j in range(n):
				if B[i][j] <= B[i][k - 1] + B[k - 1][j]:
					Bk[i][j] = B[i][j]
					Pk[i][j] = P[i][j]
				else:
					Bk[i][j] = B[i][k - 1] + B[k - 1][j]
					Pk[i][j] = P[k - 1][j]
		B = deepcopy(Bk)
		P = deepcopy(Pk)
	return B,P


def intmat(P):
	n = len(P)
	Po = np.zeros((n,n), dtype = np.int)
	for i in range(n):
		for j in range(n):
			Po[i][j] = int(P[i][j])
	return Po

def renverse(l):
	n = len(l)
	L = []
	for i in range(n):
		L.append(l[n - i - 1])
	return L


def chemin(A,i,j):
	B,Pi = distancepred(A)
	P = intmat(Pi)
	l = [j]
	while i != j:
		j = P[i][j]
		l.append(j)
	return renverse(l)


# il y a n villes numeroté de 0 a n - 1

def la_to_matadj(la,n):
	mat = np.full((n,n),np.inf)
	for t in la:
		i,j,d = t
		mat[i][j] = d
		mat[j][i] = d
	for i in range(n):
		mat[i][i] = 0
	return mat


def trajet(depart,arrive,dico,la):
	n = len(dico)
	mat = la_to_matadj(la,n)
	i = dico[depart]
	j = dico[arrive]
	lc = chemin(mat,i,j)
	rdico = { dico[x] : x for x in dico }
	L = [rdico[x] for x in lc]
	d = int(distance(mat)[i][j])
	return d,L
	


