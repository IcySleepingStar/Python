# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 16:26:05 2018

@author: adrie
"""

import numpy as np
import random as rand
import math

p = 2

m1 = [[39,94],[23,84]]
m2 = [[2,4],[2,1]]

def encodage(c):
	return [(ord(i) - 32) for i in c]

def decodage(l):
	if len(l) == 0:
		return ""
	else:
		return(chr(l[0] + 32) + decodage(l[1:]))

message = "Mathematics has always benefited from its involvement with developing sciences. Each successive interaction revitalises and enhances the field. Biomedical science is clearly the premier science of the foreseeable future. For the continuing health of their subject, mathematicians must become involved with biology. With the example of how mathematics has benefited from and influenced physics, it is clear that if mathematicians do not become involved in the biosciences they will simply not be a part of what are likely to be the most important and exciting scientific discoveries of all time."

#print(message)
#print(encodage(message))
#print(decodage(encodage(message)))

def asciitomat1(msg,p):
	l = encodage(msg)
	mat = []
	i = 0
	ltemp = []
	for x in l:
		if i == (p - 1):
			ltemp.append(x)
			mat.append(ltemp)
			ltemp = []
			i = 0
		else:
			ltemp.append(x)
			i += 1
	n = len(ltemp)
	if n > 0:
		while len(ltemp) < p:
			ltemp.append(0)
		mat.append(ltemp)
	return mat

def asciitomat2(mat):
	matrice = []
	i = 0
	ltemp = []
	for x in mat:
		if i == (p - 1):
			ltemp.append(x)
			matrice.append(ltemp)
			ltemp = []
			i = 0
		else:
			ltemp.append(x)
			i += 1
	n = len(ltemp)
	if n > 0:
		while len(ltemp) < p:
			ll = [0 for i in range(p)]
			ltemp.append(ll)
		matrice.append(ltemp)
	return matrice

def asciitomat(msg,p):
	return asciitomat2(asciitomat1(msg,p))

#print(asciitomat(message,p))

def mattoascii(mat):
	l = []
	for x in mat:
		for y in x:
			for u in y:
				l.append(u)
	return l

#print(decodage(mattoascii(asciitomat(message,p))))

def bezout(a,b):
	la = np.array([1,0,a])
	lb = np.array([0,1,b])
	while lb[2] != 0:
		 q = la[2]//lb[2]
		 la,lb = lb,la - q*lb
	return la 


#print(bezout(21,12))

def inv95(n):
	return bezout(n,95)[0]

#print(inv95(3))

def det(mat):
	return(((mat[0][0]*mat[1][1]) - (mat[0][1]*mat[1][0])) % 95)

def comatrice(mat):
	return ([[mat[1][1], - mat[0][1]],[- mat[1][0],mat[0][0]]])

def invmat(mat):
	d = inv95(det(mat))
	return([[((mat[1][1])*d)%95, - ((mat[0][1])*d)%95],[- ((mat[1][0])*d)%95,((mat[0][0])*d)%95]])

def randmat():
	m = [[rand.randint(0,94),rand.randint(0,94)],[rand.randint(0,94),rand.randint(0,94)]]
	if math.gcd(det(m),95) == 1:
		return m
	else:
		return randmat()

a = randmat()

def produit(m,a):
	return([[(m[0][0]*a[0][0] + m[0][1]*a[1][0])%95, 
			  (m[0][0]*a[0][1] + m[0][1]*a[1][1])%95],
				[(m[1][0]*a[0][0] + m[1][1]*a[1][0])%95,
				(m[1][0]*a[0][1] + m[1][1]*a[1][1])%95]])

def matchiffrement(M,A):
	return produit(A,M)
	
def matdechiffrement(N,A):
	AA = invmat(A)
	return produit(AA,N)

#print(a)

#print(m1)

#print(matchiffrement(m1,a))

#print(matdechiffrement((matchiffrement(m1,a)),a))

def chiffrement(msg,a):
	n = len(msg)
	lmat = asciitomat(msg,p)
	lfinal = []
	for m in lmat:
		mm = matchiffrement(m,a)
		lfinal.append(mm)
	lf = mattoascii(lfinal)
	return(decodage(lf),n)

code,long = chiffrement(message,a)

print(code)

print("\n")
 
def dechiffrement(msg,a,long):
	c,n = chiffrement(msg,invmat(a))
	return c[0:long]

decode = dechiffrement(code,a,long)

print(decode)