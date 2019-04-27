# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 15:02:28 2018

@author: adrie
"""

def pgcd(a,b):
    while b != 0:
        r = a%b
        a = b
        b = r
    return a


def est_premier(p):
    i = 2
    b = True
    while (i < (p**(1/2)) + 0.5) and b :
        if p%i == 0:
            b = False
        i += 1
    return b

def decomp(n):
    i = 2
    lili = []
    while n > 1:
        if est_premier(i):
            if n%i == 0:
                n = n//i
                lili.append(i)
            else:
                i += 1
        else:
            i += 1
    return lili
                
"""
i = 23
b = True
while b:
    if est_premier(i):
        M = (2**i) - 1
        if not est_premier(M):
            b = False
        else:
            i += 1
    else:
        i += 1
print(i)
"""


i = 0
while i < 6:
    F = (2**(2**i)) + 1
    print(F, est_premier(F))
    i += 1

