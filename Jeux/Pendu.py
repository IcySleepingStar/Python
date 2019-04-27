# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 15:10:05 2017

@author: adrie
"""

E = 10


def initialisation():
    print("entrez un mot:")
    mot = input()
    if not mot.isalpha():
        print("ce n'est pas un mot")
    else:
        mot = mot.lower()
        li = []
        for k in mot:
            li.append(k)
    return li


        
def varint():
    print("entrez une lettre:")
    test = input()
    if not test.isalpha():
        print("ce n'est pas une lettre")
    elif len(test) != 1:
        print("il y a trop de lettre")
    return test
  


def verif(li, t):
    b = -1
    i = 0
    while i < len(li) and b == -1:
        if li[i] == t:
            b = i
        else:
            i += 1
    return b
    



def main():
    l = initialisation()
    aux = []
    n = 0
    i = 0
    while i < len(l):
        aux.append("?")
        i += 1
    print(aux)
    i = 0
    while i < E and n != len(l):
        c = varint()
        j = verif(l, c)
        if j == -1:
            print("mauvaise lettre")
            i += 1
            print(E - i, "essais restants")
            print(aux)
        else:
            print("bonne lettre")
            aux[j] = c
            l[j] = 6
            print(aux)
            n += 1
    if i == 10:
        print("vous avez perdu et vous ne connaitrez jamais la solution car ce programme l'a effacé (parce que le programmeur est un flemmard)")
    else:
        print("vous avez gagné")
            



main()
