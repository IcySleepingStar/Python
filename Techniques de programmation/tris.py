# -*- coding: utf-8 -*-
"""
Created on Wed Oct  3 15:22:04 2018

@author: adrie
"""

import time
import random



lili = [random.randint(0, 100000) for i in range(100000)]
l = [8,3,0,9,1,0,8,3,10]


# ne marche pas
def insertion(l):
	a = time.time()
	n = len(l)
	i = 1
	while i < n:
		k = 0
		x = l[i]
		while k < i and l[k] <= x:
			k += 1
		while k < i:
			(l[k],l[k + 1]) = (l[k + 1],l[k])
			k += 1
		i += 1
	b = time.time()
	return (b - a)

#print(insertion(l))

#print(l)


def bulle(l):
	n = len(l)
	aux(l,n - 1)

def aux(l,i):
	j = 0
	while j < i:
		if l[j] > l[j + 1]:
			(l[j],l[j + 1]) = (l[j + 1],l[j])
		j += 1
	if i > 0:
		aux(l,i - 1)
		

def compte(ch, mot):
	n = len(ch)
	m = len(mot)
	i = 0
	c = 0
	while i < n - m + 1:
		j = 0
		while j < m and ch[i + j] == mot[j]:
			j += 1
		if j == m:
			c += 1
		i += 1
	return(c)
			



def remonte(tas,i):
	j = int((i - 1)/2)
	if tas[j] < tas[i]:
		(tas[j],tas[i]) = (tas[i],tas[j])
		remonte(tas,j)
			

def descend(tas,i,n):
	if 2*i + 2 <= n:
		if tas[i] < tas[2*i + 1] and tas[2*i + 2] <= tas[2*i + 1]:
			(tas[2*i + 1],tas[i]) = (tas[i],tas[2*i + 1])
			descend(tas,2*i + 1 ,n)
		else:
			if tas[i] < tas[2*i + 2] and tas[2*i + 2] > tas[2*i + 1]:
				(tas[2*i + 2],tas[i]) = (tas[i],tas[2*i + 2])
				descend(tas,2*i + 2,n)
	else:
		 if 2*i + 1 <= n and tas[i] < tas[2*i + 1]:
			 (tas[2*i + 1],tas[i]) = (tas[i],tas[2*i + 1])
			 descend(tas,2*i + 1 ,n)

	
def tasser(l):
	tas = []
	n = len(l)
	i = 0
	while i < n:
		tas.append(l[i])
		remonte(tas, i)
		i += 1
	return(tas)

def reconstituer(tas,n):
	descend(tas,0,n)
	
	
l = [0, 8, 6, 7, 7, 0, 1, 2, 7, 5, 0]

def heapsort(l):
	tas = tasser(l)
	n = len(tas)
	i = n - 1
	while i > 0:
		(tas[0],tas[i]) = (tas[i],tas[0])
		reconstituer(tas, i - 1)
		i -= 1
	return(tas)


def separe(x,l):
	g = []
	d = []
	for a in l:
		if x < a:
			d.append(a)
		else:
			g.append(a)
	return (g,d)

def rapid(l):
	if len(l) <= 1:
		return (l)
	else:
		pivot = l.pop(0)
		(g,d) = separe(pivot,l)
		return rapid(g) + [pivot] + rapid(d)

def trie(l):
	def auxtri(i,l,n):
		if i == n - 1:
			return True
		else:
			if l[i] <= l[i + 1]:
				return auxtri(i + 1,l,n)
			else:
				return False
	n = len(l)
	return auxtri(0, l, n)

def trie2(l):
	i = 0
	n = len(l)
	while i < n - 1:
		if l[i] > l[i + 1]:
			return False
		i += 1
	return True




def fusion(l1,l2):
	if l1 == []:
		return l2
	if l2 == []:
		return l1
	x = l1.pop(0)
	y = l2.pop(0)
	if x > y:
		return [y] + fusion([x] + l1, l2)
	else:
		return [x] + fusion(l1, [y] + l2)
		
		
def fusion2(l1,l2):
	if l1 == []:
		return l2
	if l2 == []:
		return l1
	if l1[0] > l2[0]:
		return [l1[0]] + fusion2(l1[1:], l2)
	else:
		return [l2[0]] + fusion2(l1, l2[1:])

# cette fonction est iterative pour etre plus python-friendly

def fusion3(ll,lll):
	l1 = ll
	l2 = lll
	l = []
	while not ((l1 == []) or (l2 == [])):
		if l1[0] < l2[0]:
			x = l1.pop(0)
			l.append(x)
		else:
			x = l2.pop(0)
			l.append(x)
	return (l + l1 + l2)
	
	


def trifusion(l):
	n = len(l)
	if n <= 1:
		return l
	else:
		k = int(n/2)
		return fusion3(trifusion(l[0:k]), trifusion(l[k:n]))
		
		



print(" ")

print("comparaison")

print(" ")

print("rapid")
t = time.time()
l = rapid(lili)
print("temps de calcul :",time.time() - t)
print("liste trié :",trie2(l))

print(" ")

print("heapsort")
t = time.time()
ll = heapsort(lili)
print("temps de calcul :",time.time() - t)
print("liste trié :",trie2(ll))

print(" ")

print("trifusion")
t = time.time()
lll = trifusion(lili)
print("temps de calcul :",time.time() - t)
print("liste trié :",trie2(lll))

print(" ")

"""

print("bubulle")
t = time.time()
bulle(lili)
print("temps de calcul :",time.time() - t)
print("liste trié :",trie2(lili))

"""
