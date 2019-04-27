# -*- coding: utf-8 -*-
"""
Created on Fri Jan 18 17:38:56 2019

@author: adrie
"""

import math

def fac(n):
	return math.factorial(n)

def binom(k,n):
	return fac(n)/(fac(k)*fac(n - k))

def S(n):
	s = 0
	for k in range(n + 1):
		s += ((-1)**k)*binom(k,n)*(2/(2*k + 1))
	return s

def S2(n):
	return ((2**(2*n + 1))*(fac(n)**2))/(fac(2*n + 1))


