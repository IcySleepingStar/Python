# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 15:12:17 2017

@author: adrie
"""

from numpy.random import randint


lili = []
i = 0
while i <100:
    lili.append(randint(0, 99))
    i += 1

def genlili():
	return [randint(0, 99) for i in range(100)]
		   	   
def nonpresent(t):
    i = 0
    k = 0
    while i < 100:
        if i in t:
            k += 1
        i += 1
    n = 100 - k
    return n

def experience(p):
    i = 0
    s = 0
    while i < p:		   
        l = genlili()
        s = s + nonpresent(l)
        i += 1
    m = s / p
    return m

l = experience(100000)
print(l)



def eq2(a ,b, c):
    d = (b**2)-(4*a*c)
    if d > 0:
        m = (-b -(d**0.5))/(2*a)
        n = (-b +(d**0.5))/(2*a)
        print("deux racines réelles distinctes:", m, n)
    elif d == 0:
        m = (-b)/(2*a)
        print("une racine double:", m)
    else:
        m = complex((-b)/(2*a), -((-d)**0.5)/(2*a))
        n = complex((-b)/(2*a), ((-d)**0.5)/(2*a))
        print("deux racines complexes:", m, n)
    
print(eq2(1, 0, 1))



def formecreuse(a, b, c, d):
   print(a)
   print()
   print(b)
   print()
   print(c)
   print()
   print(d)
   print()
   i = 0
   chaine = ""
   while i < a:
       chaine = chaine + "X"
       i += 1
   print(chaine)
   print()
   ligne = ""
   i = 0
   while i < c:
       ligne = ligne + "#"
       i += 1
   print(ligne)
   ligne2 = "#"
   i = 2
   while i < c:
       ligne2 = ligne2 + " "
       i += 1
   ligne2 = ligne2 + "#"
   i = 2
   while i < b:
       print(ligne2)
       i += 1
   print(ligne)
   print()
   i = 0
   p = (d-2)
   print("@")
   while i < p:
       k = 0
       chaine = "@"
       while k < i:
           chaine = chaine + " "
           k += 1
       chaine = chaine + "@"
       print(chaine)
       i += 1
   print(d*"@")
        
        
    
        
    
    
    
#formecreuse(6, 35, 24, 28)



