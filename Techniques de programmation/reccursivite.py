# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 16:56:09 2018

@author: adrie
"""

def dev(a,b):
    q = a//b
    r = a%b
    if r == 0:
        return [q]
    else:
        return [q] + dev(b,r)



def palindrome(s):
    n = len(s)
    if n == 1 or n == 0:
        return True
    else:
        if s[0] == s[n - 1]:
            return palindrome(s[1:n-1])
        else:
            return False


def binaire(l):
    n = len(l)
    if n == 0:
        return 0
    else:
        x = l.pop(0)
        return ((2**(n - 1))*x) + binaire(l)
    
    

def vers10(l,a):
    n = len(l)
    if n == 0:
        return 0
    else:
        x = l.pop(0)
        return ((a**(n - 1))*x) + vers10(l,a)
    


def maxbiinfn(n,b):
    i = 0
    while (b**i) <= n:
        i += 1
    return i
    
    
def de10(n,b):
    truc = maxbiinfn(n,b)
    def aux(n,b,k):
        if n == 0:
            return []
        else:
            d = b**k
            q = n//d
            r = n%d
            return [q] + aux(r,b,(k - 1))
    return aux(n,b,truc)


def base(l,a,b):
    n = vers10(l,a)
    return(de10(n,b))
        


def horner(l,x):
    a = l.pop(0)
    if l == []:
        return a
    else:
        return a + (x*horner(l,x))


def liste(n):
    l = []
    i = 0
    while i <= n:
        l.append(i)
        i += 1
    return l


def premier(n):
    i = 2
    while (n%i != 0) and (i < n):
        i += 1
    if i == n:
        return True
    else:
        return False
        



def crible(n):
    lili = []
    l = liste(n)
    ln = len(l)
    i = 2
    while i < ln:
        x = l[i]
        if x != -1:
            if premier(x):
                lili.append(x)
                j = 1
                while x*j < n:
                    l[x*j] = -1
                    j += 1
        i += 1
    return lili
   
   
   
print(crible(10000))   






   