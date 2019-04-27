# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:21:33 2019

@author: adrie
"""

import numpy as np
import random as rd
import matplotlib.pylab as plt
from copy import copy

#un labyrinthe est représenté par un graphe dont les aretes sont les chemins et les noeuds les
#cases

#les dimensions de la grille

xmax = 40

ymax = 30

z = xmax*ymax

c = 0

n = 0

# Les noeuds sont numerotés de x allant de 0 à xmax et j = 0 puis on remonte depuis la gauche

# donc dans le tableau la case i,j represente l'arete entre (i%xmax, i//xmax) et 
#(j%xmax, j//xmax)


test = [[0,1,0,0,0,0],
		  [1,0,0,0,1,0],
		  [0,0,0,0,0,1],
		  [0,0,0,0,1,0],
		  [0,1,0,1,0,1],
		  [0,0,1,0,1,0]]


def coordinate(i):
	return i%xmax, i//xmax

def indice(x,y):
	return x + xmax*y

def appartient(x,l):
    for y in l:
        if x == y:
            return True
    return False

def randGraph(n):
	g = np.zeros((z,z), dtype = int)
	for k in range(n):
		i = rd.randint(0, z - 1)
		j = rd.randint(0, z - 1)
		g[i,j] = 1
	return g


# On génère un graphe de la manière suivante:
#    -On crée le graphe vide et on le munit d'un début et d'une fin
#    -On trace un chemin aléatoire entre le début et la fin
#    -On choisit aléatoirement un noeud de la composante connexe du noeud de départ et on cherche 
#    à ajouter une arête depuis ce noeud avec la condition que l'arête ne doit pas pointer 
#    vers un noeud qui appartient déjà à la composante connexe. On répète l'opération
#    jusqu'à ce que touts les noeuds soient dans la composantes connexe


def iniGraph():
    g = np.zeros((z,z), dtype = int)
    ydebut = rd.randint(0, ymax - 1)
    debut = indice(0, ydebut)
    yfin = rd.randint(0, ymax - 1)
    fin = indice(xmax - 1, yfin)
    return g,debut,fin

#Cette fonction prend en argument un noeud et renvoie les noeuds qui sont adjacents

def noeudAdj(i):
    x,y = coordinate(i)
    l = []
    if x != 0:
        l.append(indice(x - 1,y))
    if y != 0:
        l.append(indice(x,y - 1))
    if x != xmax - 1:
        l.append(indice(x + 1,y))
    if y != ymax - 1:
        l.append(indice(x,y + 1))
    return l

# Tant qu'on n'est pas arrivé au noeud de la fin, on conserve la liste ordonné des noeud visités
# On se base sur le principe récursif: 
#     -Si le noeud actuel est le final je renvoie la liste des visités
#     -Sinon, depuis le noeud actuel je forme la liste des noeuds adjacents.
#     Si la liste des adjacents n'est pas vide je l'ajoute à la liste des visités, je la retire
#     de la liste des adjacents et je renvoie la fonction sur la nouvelle liste des visités
#       -Si elle renvoie (-1) je prend un nouveau noeud dans adjacents et on recommence
#       -Si elle renvoie (-1) et que la liste des adjacents est vide je renvoie (-1)

def CreateCheminAux(fin,lv):
    global c
    if c > 1000:
        return "failure"
    c += 1
    i = lv[-1]
    if i == fin:
        return lv
    else:
        adj = noeudAdj(i)
        ladj = priver(adj,lv)
        while ladj != []:
            k = rd.randint(0, len(ladj) - 1)
            j = ladj.pop(k)
            lvn = copy(lv)
            lvn.append(j)
            x = CreateCheminAux(fin,lvn)
            if x == "failure":
                return "failure"
            if x != (-1):
                return x
        return (-1)

def CreateChemin(g,debut,fin):
    lv = CreateCheminAux(fin,[debut])
    if lv == "failure":
        return "failure"
    n = len(lv)
    for k in range(n - 1):
        i = lv[k]
        j = lv[k + 1]
        g[i,j] = 1
        g[j,i] = 1
    return lv

# on veut une fonction qui renvoie une liste privée de l'autre

def priver(ladj,lvprat):
    l = []
    for x in ladj:
        if not appartient(x,lvprat):
            l.append(x)
    return l

def FillGraph(g,lv,lvprat):
    if len(lv) < z:
        k = rd.randint(0,len(lvprat) - 1)
        i = lvprat[k]
        ladj = noeudAdj(i)
        nladj = priver(ladj,lv)
        n = len(nladj)
        if n == 0:
            lvprat.pop(k)
            FillGraph(g,lv,lvprat)
        else:
            p = rd.randint(0,n - 1)
            j = nladj[p]
            lv.append(j)
            lvprat.append(j)
            g[i,j] = 1
            g[j,i] = 1
            FillGraph(g,lv,lvprat)

def FillGraphNeo(g,lv,lvprat):
    if len(lv) < z:
        k = rd.randint(0,len(lvprat) - 1)
        i = lvprat[k]
        ladj = noeudAdj(i)
        nladj = priver(ladj,lv)
        while len(nladj) != 0:
            p = rd.randint(0,len(nladj) - 1)
            j = nladj[p]
            lv.append(j)
            lvprat.append(j)
            g[i,j] = 1
            g[j,i] = 1
            nladj = priver(noeudAdj(j), lv)
            i = j
        FillGraphNeo(g,lv,lvprat)

def CreateGraph():
    global c
    c = 0
    g,debut,fin = iniGraph()
    lv = CreateChemin(g,debut,fin)
    if lv == "failure":
        return "failure"
    gsol = copy(g)
    lvprat = copy(lv)
    FillGraphNeo(g,lv,lvprat)
    return g,debut,fin,gsol



def printArrow(x1,x2,y):
    xm = (x1 + x2)/2
    d = (x1 - x2)/4
    plt.plot([x1,x2],[y,y],'r')
    plt.plot([x2,xm],[y,y + d],'r')
    plt.plot([x2,xm],[y,y - d],'r')

def printGraph(g):
	for i in range(z):
		x,y = coordinate(i)
		plt.plot(x + 0.5, y + 0.5, '.r')
	for j in range(z):
		for i in range(j):
			if g[i][j] == 1:
				x1,y1 = coordinate(i)
				x2,y2 = coordinate(j)
				plt.plot([x1 + 0.5, x2 + 0.5],[y1 + 0.5, y2 + 0.5],'r')

def printLabyrinth(g,debut,fin):
    for y in range(1,ymax):
        for x in range(xmax):
            i = indice(x,y)
            j = indice(x,y - 1)
            if g[i][j] == 0:
                plt.plot([x, x + 1], [y, y], 'k')
    for x in range(1,xmax):
        for y in range(ymax):
            i = indice(x,y)
            j = indice(x - 1,y)
            if g[i][j] == 0:
                plt.plot([x, x], [y, y + 1], 'k')
    xe,ye = coordinate(debut)
    xs,ys = coordinate(fin)
    plt.plot([0,0,xmax,xmax],[ye,0,0,ys],'k')
    plt.plot([0,0,xmax,xmax],[ye + 1,ymax,ymax,ys + 1],'k')
    printArrow(-1,0,ye + 0.5)
    printArrow(xmax,xmax + 1,ys + 0.5)

def printGrid():
	for i in range(xmax + 1):
		plt.plot([i,i],[0,ymax],'--k')
	for j in range(ymax + 1):
		plt.plot([0,xmax],[j,j],'--k')

def printSol(g):
	for j in range(z):
		for i in range(j):
			if g[i][j] == 1:
				x1,y1 = coordinate(i)
				x2,y2 = coordinate(j)
				plt.plot([x1 + 0.5, x2 + 0.5],[y1 + 0.5, y2 + 0.5],'r')

laby = "failure"

while laby == "failure":
	print("failure at trial number " + str(n))
	n += 1
	try:	
		laby = CreateGraph()
	except RecursionError:
		print("maximum recursion depth exceeded at trial number " + str(n))
		n += 1
print("success")
g,i,j,gsol = laby
#printGraph(g)
#printGrid()
printSol(gsol)
printLabyrinth(g,i,j)
