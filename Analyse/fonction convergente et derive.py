# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 01:56:22 2018

@author: adrie
"""

import numpy as np
import matplotlib.pylab as plt

n = 10000
T = 10
h = T/n

lt = []
i = 0
while i < n:
	lt.append(i*h)
	i += 1

#print(lt)

def xa(lt,a):
	l = []
	for x in lt:
		l.append(x**a)
	return l

def exp(lt):
	l = []
	for x in lt:
		l.append(np.exp(x))
	return l


def creneau(lt):
	l = []
	for x in lt:
		if x % 2 > 1:
			l.append(-1)
		else:
			l.append(1)
	return l

def creneaurapide(lt):
	l = []
	for x in lt:
		if np.exp(x) % 2 > 1:
			l.append(-1)
		else:
			l.append(1)
	return l




#plt.plot(lt,xa(lt,1))
#plt.plot(lt,xa(lt,2))
#plt.plot(lt,exp(lt))

#plt.plot(lt,creneaurapide(lt))

def prim0(lt,lf):
	l = []
	i = 0
	n = len(lt)
	F = 0
	while i < n - 1:
		F += (lf[i] + lf[i + 1])*(h/2)
		l.append(F)
		i += 1
	l.append(l[n - 2])
	return l

plt.plot(lt,prim0(lt,creneaurapide(lt)))
	

		