# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 15:17:13 2017

@author: adrien
"""
i = 0
n = 483
d = 2
while d < n:
    if (n % d) == 0:
        i += 1
        print(d)
        d += 1
    if (n % d) != 0:
        d += 1
if i == 0:
    print("premier")   
if i != 0:
    print("nombre de diviseur:",i)