# -*- coding: utf-8 -*-
"""
Created on Thu Sep 20 18:40:03 2018

@author: adrie
"""

# dans Z/22Z

def ordre(a,n):
	i = 1
	while ((a**i)%n) != 1:
		i += 1
	return i



for i in [3,5,7,9,13,15,17,19,21]:
	print(ordre(i,22))