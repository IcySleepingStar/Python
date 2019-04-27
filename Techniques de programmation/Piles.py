# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 16:27:29 2018

@author: adrie
"""

from random import randint
from matplotlib import pyplot as plt




class Cellule:
    def __init__(self,valeur,suivant = None):
        self.val = valeur
        self.next = suivant
    def __str__(self):
        return str(self.val)
    
class Pile:
    def __init__(self):
        self.top = None
        self.len = 0
    def is_empty(self):
        return self.top is None
    def push(self,x):
        c = Cellule(x)
        c.next = self.top
        self.top = c
        self.len += 1
    def pop(self):
        if self.is_empty():
            raise ValueError ("pile vide")
        c = self.top 
        self.top = c.next
        self.len -= 1
        return c.val
    def fold(self, f):
        l = []
        while not self.is_empty():
            a = self.pop()
            l.append(f(a))
        n = len(l)
        i = 0
        while i < n:
            self.push(l[n - 1 - i])
            i += 1
    
def copypile(p):
    l = []
    while not p.is_empty():
        a = p.pop()
        l.append(a)
    n = len(l)
    i = 0
    pp = Pile()
    while i < n:
        p.push(l[n - 1 - i])
        pp.push(l[n - 1 - i])
        i += 1
    return pp


def printpile(p):
    pp = copypile(p)
    while not pp.is_empty():
        a = pp.pop()
        print(a)
    print("fini")
        
    
def lenpile(p):
    a = copypile(p)
    i = 0
    while not a.is_empty():
        x = a.pop()
        i += 1
    return i
    
    
#1

def echange(p):
    a = p.pop()
    b = p.pop()
    p.push(a)
    p.push(b)
    return (a,b)


#2

def appartient(a,y):
    i = 0
    p = copypile(a)
    bol = True
    while (not p.is_empty()) and bol:
        x = p.pop()
        if x == y:
            bol = False
        else:
            i += 1
    if bol == True:
        i = -1
    return i
            

#3

def renverse(p):
    a = copypile(p)
    b = Pile()
    l = []
    while not a.is_empty():
        x = a.pop()
        l.append(x)
    n = len(l)
    i = 0
    while i < n:
        b.push(l[i])
        i += 1
    return b

def renversepile(a):
    l = []
    while not a.is_empty():
        x = a.pop()
        l.append(x)
    n = len(l)
    i = 0
    while i < n:
        a.push(l[i])
        i += 1
    return a



#4

def shuffle(a,b):
    c = Pile()
    while (not a.is_empty()) and (not b.is_empty()):
        n = randint(0,1)
        if n == 0:
            x = a.pop()
            c.push(x)
        else:
            x = b.pop()
            c.push(x)
    while not a.is_empty():
        x = a.pop()
        c.push(x)
    while not b.is_empty():
        x = b.pop()
        c.push(x)
    return c


#5

def depile(p,k):
    i = 0
    while i < k and (not p.is_empty()):
        x = p.pop()
        i += 1
        

#6

def depilpile(p,k):
    renversepile(p)
    depile(p, lenpile(p) - k)
    renversepile(p)


#7

def f(x):
    return x + 1
        

#8

class Point:
    def __init__(self, abscisse,ordonne):
        self.abscisse = abscisse
        self.ordonne = ordonne
        
def vecteur(a,b):
    x = b.abscisse - a.abscisse
    y = b.ordonne - a.ordonne
    return [x,y]


class Triangle:
    def __init__(self,A,B,C):
        self.A = A
        self.B = B
        self.C = C
    def isobarycentre(self):
        x = (1/3)*(self.A.abscisse + self.B.abscisse + self.C.abscisse)
        y = (1/3)*(self.A.ordonne + self.B.ordonne + self.C.ordonne)
        I = Point(x,y)
        return I
        
        
        

def tracepoint(P):
    plt.plot([P.abscisse],[P.ordonne],'.')

def trace(T):
    A = T.A
    B = T.B
    C = T.C
    x1 = A.abscisse
    x2 = A.ordonne
    y1 = B.abscisse
    y2 = B.ordonne
    z1 = C.abscisse
    z2 = C.ordonne
    plt.plot([x1,y1,z1,x1],[x2,y2,z2,x2])
        
        