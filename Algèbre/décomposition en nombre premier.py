# -*- coding: utf-8 -*-
"""
Created on Thu Nov 23 18:27:14 2017

@author: adrie
"""

def decomp(n):
    i = 2
    lili = []
    while i <= (n**0.5):
        if (n%i) == 0:
            lili.append(i)
        i += 1
    li = []
    for m in lili:
        li.append(m)
    for h in lili:
        li.append(int(n/h))
    
    fi = []
    t = 0
    while t < len(li):
        i = 2
        while i < li[t] and (li[t]%i) != 0:
            i += 1
        if i == li[t]:
            fi.append(li[t])
        else:
            fi.append(decomp(li[t]))
        t += 1                      
    
    return fi


print(decomp(4002327))


