# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 14:56:24 2018

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt
import random

N = 1000
a = -4
b = 4
h = (b - a)/N
tabt = np.linspace(a,b,N)



def creneau(i,j):
	l = []
	for t in tabt:
		if i < t < j:
			l.append(1)
		else:
			l.append(0)
	return l

def square():
	return [t**2 for t in tabt]

def randfunc(v):
	x = 0
	l = []
	for i in range(N):
		l.append(x)
		x += v * h * (0.5 - random.random())
	return l

def gaussienne():
	return [np.exp(-(t**2)) for t in tabt]

# calcule la primitive nulle en a

def primitive_euler(l):
	s = 0
	n = len(l)
	pri = []
	for i in range(n):
		s += (l[i] * h)
		pri.append(s)
	return pri

def primitive_simpson(l):
	s = 0
	n = int(len(l)/2)
	pri = []
	for i in range(n - 1):
		s += (h/3)*(l[2*i] + 4*l[2*i + 1] + l[2*i + 2])
		pri.append(s)
	for i in range(n - 1):
		pri.insert(2*i + 1, pri[2*i])
	while len(pri) < len(l):
		pri.append(pri[-1])
	return pri

def primitive(l):
	s = 0
	n = len(l)
	pri = []
	for i in range(n - 1):
		s += (h/2)*(l[i] + l[i + 1])
		pri.append(s)
	pri.append(s)
	return pri


def plotnprim(l,n):
	plt.plot(tabt,l)
	for i in range(n):
		l = primitive(l)
		plt.plot(tabt,l)


# calcul de l'integrale entre a et b de f

def integrale(l):
	s = 0
	n = len(l)
	for i in range(n - 1):
		s += (h/2)*(l[i] + l[i + 1])
	return s

# la convolution tant attendue

# pour t, l'indice correspondant est N*(t - a)/(b - a)

def convolution(l1,l2,tab):
	at = tab[0]
	bt = tab[-1]
	nt = len(tab)
	ht = (bt - at)/nt
	newtabt = np.linspace(2 * at, 2 * bt, 2 * nt)
	c = max(at, 2*at - bt)
	d = min(bt, 2*bt - at)
	tab_integration = np.linspace(c,d, int(((d - c)/(bt - at)) * nt))
	lconv = []
	for x in newtabt:
		xint = int((2*nt*(x - 2*at))/(2*bt - 2*at))
		s = 0
		for t in tab_integration:
			tint = int((nt*(t - at))/(bt - at))
			if 0 <= tint < nt and 0 <= (xint - tint) < nt:
				s += ht*l1[xint - tint]*l2[tint]
		lconv.append(s)
	return lconv,newtabt
				

def plotnconvo(f,tabt,n):
	plt.plot(tabt,f)
	for i in range(n):
		f,tabt = convolution(f,f,tabt)
		plt.plot(tabt,f)


def aplatit(F,f):
	a = max(f)
	b = min(f)
	A = max(F)
	B = min(F)
	c = ((b - a)/(B - A))
	l = [c*x for x in F]
	return l

def plotnconvoap(f,tabt,n):
	F = f
	plt.plot(tabt,f)
	for i in range(n):
		F,tabt = convolution(F,F,tabt)
		F = aplatit(F,f)
		plt.plot(tabt,F)

f = randfunc(1000)

#plt.plot(tabt,creneau(-1,1))

#plt.plot(ntabt,lc)

#plt.plot(tabt,f)

#plt.plot(tabt,primitive(f))
