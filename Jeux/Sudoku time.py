# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 17:20:53 2018

@author: adrie
"""

import time
import numpy as np
from copy import deepcopy
np.set_printoptions(threshold=100)


m1 = np.array([[0,1,0,0,5,2,0,0,7],
			  [0,8,0,7,0,0,0,1,0],
			  [9,0,2,0,6,1,5,0,0],
			  [4,0,0,2,0,0,7,0,0],
			  [8,0,1,0,7,0,2,0,4],
			  [0,0,7,0,0,5,0,0,9],
			  [0,0,6,5,3,0,9,0,8],
			  [0,9,0,0,0,4,0,5,0],
			  [2,0,0,9,8,0,0,7,0]])


m2 = np.array([[0,6,0,0,0,0,9,8,5],
         [0,0,5,6,0,9,0,0,0],
         [0,0,7,0,0,0,0,4,0],
         [0,2,0,9,0,0,0,0,8],
         [0,7,0,5,0,1,0,6,0],
         [1,0,0,0,0,3,0,9,0],
         [0,1,0,0,0,0,4,0,0],
         [0,0,0,3,0,6,8,0,0],
         [6,5,9,0,0,0,0,1,0]])

m3 = np.array([[0,0,0,3,0,1,0,0,0],
         [0,0,0,0,0,0,3,7,0],
         [2,0,8,0,9,0,0,5,0],
         [6,9,0,0,0,2,0,0,0],
         [4,0,1,0,3,0,2,0,7],
         [0,0,0,9,0,0,0,1,5],
         [0,1,0,0,7,0,8,0,3],
         [0,4,6,0,0,0,0,0,0],
         [0,0,0,4,0,3,0,0,0]])

mc =np.array([[4,0,0,0,0,0,0,0,9],
           [9,0,3,0,0,0,4,0,1],
           [0,0,0,0,9,0,3,0,0],
           [3,0,0,0,6,0,1,9,7],
           [0,0,0,1,0,7,0,0,0],
           [0,8,7,0,0,0,6,2,0],
           [0,1,0,0,0,0,0,3,0],
           [0,0,0,0,1,0,0,0,0],
           [0,0,0,9,0,3,0,0,0]])


# pas dans colonne renvoie true si x n est pas dans la colonne j

def pas_dans_colonne(x,m,j):
	for i in range(9):
		if m[i][j] == x:
			return False
	return True

def pas_dans_ligne(x,m,i):
	for j in range(9):
		if m[i][j] == x:
			return False
	return True

def pas_dans_carre(x,m,i,j):
	ii = i - (i%3)
	jj = j - (j%3)
	for p in range(ii, ii + 3):
		for q in range(jj, jj + 3):
			if m[p][q] == x:
				return False
	return True

# test renvoie true si la valeur peut etre mise dans la case

def test(x,m,i,j):
	return pas_dans_colonne(x,m,j) and pas_dans_ligne(x,m,i) and pas_dans_carre(x,m,i,j)


def trouve_zero(m):
	for i in range(9):
		for j in range(9):
			if m[i][j] == 0:
				return (i,j)
	return (-1,-1)


def sudoku(m):
	(i,j) = trouve_zero(m)
	if (i,j) == (-1,-1):
		return m
	else:
		x = 1
		while x < 10:
			if test(x,m,i,j):
				mnew = deepcopy(m)
				mnew[i][j] = x
				res = sudoku(mnew)
				if type(res) != int:
					return res
			x += 1
		return 0

def sudoku_time(m):
	t1 = time.time()
	sol = sudoku(m)
	t2 = time.time()
	print(t2 - t1)
	print(sol)


def voisins(i,j):
	l = []
	for x in [-1,1]:
		for y in [-2,2]:
			if 8 >= (x + i) >= 0 and 8 >= (j + y) >= 0:
				l.append((x + i, y + j))
	for x in [-2,2]:
		for y in [-1,1]:
			if 8 >= (x + i) >= 0 and 8 >= (y + j) >= 0:
				l.append((x + i, y + j))
	return l

def pas_dans_voisins(x,m,i,j):
	for (ii,jj) in voisins(i,j):
		if x == m[ii][jj]:
			return False
	return True

def test_cavalier(x,m,i,j):
	return pas_dans_colonne(x,m,j) and pas_dans_ligne(x,m,i) and pas_dans_carre(x,m,i,j) and pas_dans_voisins(x,m,i,j)

def sudoku_cavalier(m):
	(i,j) = trouve_zero(m)
	if (i,j) == (-1,-1):
		return m
	else:
		x = 1
		while x < 10:
			if test_cavalier(x,m,i,j):
				mnew = deepcopy(m)
				mnew[i][j] = x
				res = sudoku_cavalier(mnew)
				if type(res) != int:
					return res
			x += 1
		return 0


# Bonus

# fonction qui valide une solution

def valide_dans_colonne(x,i,j):
	for ii in range(9):
		if m[i][j] == m[ii][j] and ii != i:
			return False
	return True


"""
def est_sol(m):
	for i in range(9):
		for j in range(9):
			"""



# a 2 solutions

m4 = np.array([[6, 1, 3, 4, 5, 2, 8, 9, 7],
       [5, 8, 4, 7, 9, 3, 6, 1, 2],
       [9, 7, 2, 8, 6, 1, 5, 4, 3],
       [4, 6, 9, 2, 1, 8, 7, 3, 5],
       [8, 5, 1, 3, 7, 9, 2, 6, 4],
       [3, 2, 7, 6, 4, 5, 1, 8, 9],
       [1, 4, 0, 5, 3, 7, 9, 2, 0],
       [7, 9, 0, 1, 2, 4, 3, 5, 0],
       [2, 3, 5, 9, 8, 6, 4, 7, 1]])


	
# on calcule qu il a 9 solutions
	
m5 = np.array([[0,1,0,0,5,2,0,0,7],
			  [0,0,0,7,0,0,0,1,0],
			  [0,0,2,0,0,0,5,0,0],
			  [4,0,0,2,0,0,7,0,0],
			  [8,0,1,0,7,0,2,0,4],
			  [0,0,0,0,0,5,0,0,9],
			  [0,0,6,5,3,0,0,0,8],
			  [0,9,0,0,0,4,0,5,0],
			  [0,0,0,9,8,0,0,7,0]])

	

def aux(m,lzero):
	if len(lzero) == 0:
		return [m]
	else:
		(i,j) = lzero[0]
		newlzero = lzero[1:]
		lsol = []
		for x in range(1,10):
			if test(x,m,i,j):
				mnew = deepcopy(m)
				mnew[i][j] = x
				mm = aux(mnew,newlzero)
				lsol = lsol + mm
		return lsol


def liste_zero(m):
	l = []
	for i in range(9):
		for j in range(9):
			if m[i][j] == 0:
				l.append((i,j))
	return l 


def liste_solutions(m):
	lzero = liste_zero(m)
	return aux(m,lzero)

def nombre_solutions(m):
	return len(liste_solutions(m))
