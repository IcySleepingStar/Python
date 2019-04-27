# -*- coding: utf-8 -*-
"""
Created on Tue Dec 11 22:32:17 2018

@author: adrie
"""

import matplotlib.pylab as plt
import numpy as np


def arcpara(f,T,n):
	lx,ly = f(np.linspace(0,T,n))
	plt.plot(lx,ly)


def cyclo(t):
	return [t - np.sin(t), 1 - np.cos(t)]

def cardioide(t):
	return [2*np.cos(t) - np.cos(2*t), 2*np.sin(t) - np.sin(2*t)]

def astroide(t):
	return [np.sin(t)**3, np.cos(t)**3]

def gribouillage(t):
	return [np.cos(t)**2 - np.tan(3*t), np.sin(3*t**2)]

def dieu_et_infini(t):
	return [np.cos(t)**3 , np.sin(5*t)]

def boucle_cosmique(t):
	return [np.sin(t)**3, 2*np.sin(t) - np.sin(2*t)]

def montagne_russe(t):
	return [t**2 - np.sin(t), (t**2)*np.log(t + 1)*np.cos(t)]

def garde_ton_calme(t):
	return [2*np.cos(t) - np.cosh(t**0.5), 2*np.sin(t**2) - np.sin(2*t)]

def forme_universel(t):
	return [np.cos(t)**7 , np.sin(np.sin(t))]

def the_world(t):
	return [np.cos(t**t) , np.sin(t**t)]

def randonneur_spectral(t):
	return [np.cos(t + np.sin(3*t)) + t ,1 + 4*t**0.5 + np.sin(np.sin(t))]

def aurore_dimensionelle(t):
	return [(t**0.9)*np.cos(t)**4, t + np.cos(t**3)*np.sin(np.log(t + 1))]

def cercle01(t):
	return [0.5*(1 + np.cos(t)), 0.5*(1 + np.sin(t))]

def lemniscate(t):
	return [(abs(np.cos(2*t))**0.5)*np.cos(t), (abs(np.cos(2*t))**0.5)*np.sin(t)]

def soleil_galactique(t):
	return [4.3*np.cos(t) - np.cos(4.3*t), 4.3*np.sin(t) - np.sin(4.3*t)]

def triphroide(t):
	return [4*np.cos(t) - np.cos(4*t), 4*np.sin(t) - np.sin(4*t)]
