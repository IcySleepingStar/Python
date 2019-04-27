# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 16:20:16 2017

@author: adrie
"""

def easy():
    from numpy.random import randint
    print("Un ensemble de 20 allumettes sont disposées devant vous.")
    print("A chaque étapes vous pouvez retirer entre 1 et 4 allumettes.")
    print("le joueur qui prend la dernière allumette a perdu.")
    print("Vous jouez contre l'ordinateur et vous jouez en premier.")
    a = 20
    k = 0
    while a > 0:
        if k == 0:
            print("A votre tour")
            print("nombre d'allumettes restantes:", a*"|")
            n = int(input("Combien d'allumettes voulez-vous retirer ?"))
            while n > 4 or n < 1:
                print("TRICHEUR")
                n = int(input("Combien d'allumettes voulez-vous retirer tricheur ?"))
            a = a - n
            k = 1
        else:
            n = randint(1, 4)
            a = a - n
            print("L'ordinateur a pris", n, "allumettes")
            k = 0
        
    if k == 0:
        print("Vous avez gagné")
    else:
        print("Vous avez perdu")
 




       
        
def hard():
    from numpy.random import randint
    print("Un ensemble de 20 allumettes sont disposées devant vous.")
    print("A chaque étapes vous pouvez retirer entre 1 et 4 allumettes.")
    print("le joueur qui prend la dernière allumette a perdu.")
    print("Vous jouez contre l'ordinateur et vous jouez en premier.")
    a = 20
    k = 0
    while a > 0:
        if k == 0:
            print("A votre tour")
            print("Nombre d'allumettes restantes:")
            print(a)
            n = int(input("Combien d'allumettes voulez-vous retirer ?"))
            while n > 4 or n < 1:
                print("TRICHEUR")
                n = int(input("Combien d'allumettes voulez-vous retirer tricheur ?"))
            a = a - n
            k = 1
        else:
            n = 1
            while ((a-n)%5) != 1:
                n += 1
            if n == 5:
                n = randint(1, 4)
            a = a - n
            print("L'ordinateur a pris", n, "allumettes")

            k = 0
        
    if k == 0:
        print("Vous avez gagné")
    else:
        print("Vous avez perdu")
        
        
        
        
        
print("choisissez un mode:")
print("pour facile tapez 1")
print("pour difficile tapez 2")
h = int(input("difficulté"))
if h == 1:
    easy()
else:
    hard()
