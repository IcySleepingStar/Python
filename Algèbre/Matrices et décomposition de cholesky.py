# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 09:41:24 2019

@author: adrie
"""

import numpy as np

A = np.array([[2,5,1],[5,4,9],[1,9,7]])

B = np.array([[2,4,9],[8,2,5]])

I = np.eye(3)

def Nilpotente(n):
	M = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			if j == i + 1:
				M[i,j] = 1
	return M

def MatMin(n):
	M = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			M[i,j] = min(i,j) + 1
	return M

MMin = MatMin(3)

def MatHilbert(n):
	M = np.zeros((n,n))
	for i in range(n):
		for j in range(n):
			M[i,j] = 1/(i + j + 1)
	return M

def Mult(A,B):
	n,p = np.shape(A)
	pp,m = np.shape(B)
	if p != pp:
		return "mauvaise dimension"
	else:
		M = np.zeros((n,m))
		for i in range(n):
			for j in range(m):
				s = 0
				for k in range(p):
					s += A[i,k]*B[k,j]
				M[i,j] = s
		return M

def Transpose(A):
	n,m = np.shape(A)
	M = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			M[i,j] = A[j,i]
	return M

def Cholesky(S):
	n,n = np.shape(S)
	T = np.zeros((n,n))
	for j in range(n):
		for i in range(j,n):
			if i == j:
				s = 0
				for k in range(i):
					s += T[i,k]**2
				T[i,j] = (S[i,j] - s)**0.5
			else:
				s = 0
				for k in range(j):
					s += T[i,k]*T[j,k]
				T[i,j] = (S[i,j] - s)/T[j,j]
	return T
					
			