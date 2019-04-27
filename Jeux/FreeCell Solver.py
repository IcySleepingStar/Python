# -*- coding: utf-8 -*-
"""
Created on Mon Jan 28 20:59:08 2019

@author: adrie
"""

# on cherche à résoudre le jeu de FreeCell avec un algorithme DFS

# après chaque coup on établit la liste des coups jouables
# on donne la priorité aux coups vers la fondation

# Quand on descend on se souvient de la liste des derniers coups joué jusqu'au dernier
# coup vers la fondation car un coup vers la fondation ne peut pas appartenir à un cycle

# A chaque coup on vérifie que le coup joué n'a pas déja été joué dans la même configuration
# Si c'est le cas on passe au coup suivant
# Le coup suivant est le coup suivant dans la liste des coups ou si touts les coups à
# ce niveau on déjà été essayé, on remonte au niveau précédent pour jouer le prochain
# coup

# On s'arrête dès que les cascades et les freecells sont vides


# IMPLEMENTATION

# Le plateau est représenté par une liste contenant
# _ Une liste a 4 élément representant la fondation
# _ Une liste a 4 élément representant les freecells
# _ 8 Listes représentant les cascades

# Les cartes les plus en bas sont à droite

# Une carte est représenté par un couple (numéro, couleur)
# 1 -> Coeur
# 2 -> Carreau
# 3 -> Pique
# 4 -> Tréfle

# Un coup est représenté par un couple [début,fin]
# début = [n dans [0,9], i dans [0,3] ou -1 si on joue sur une cascade]
# pareil pour fin


Exemple = [[0,0,0,0],[],[(2,1),(1,1)],[(1,3)],[(2,3)],[(3,3)],[],[],[],[]]


def JeuVersFondation(C,rg,B):
	if len(B[C]) > 0:
		num,coul = B[C][rg]
		if B[0][coul - 1] == (num - 1):
			return [C,rg,coul]
		else:
			return -1
	else:
		return -1
	

def JeuVersFreeCell(C,rg,B):
	if len(B[C]) > 0:
		if len(B[1]) < 5:
			return [C,rg]
		else:
			return -1
	else:
		return -1

def JeuVersCascade(C,rg,B):
	if len(B[C]) > 0:
		l = []
		num,coul = B[C][rg]
		for k in range(2,10):
				if len(B[k]) > 0:
					numk,coulk = B[k][-1]
					if k != C and num == (numk - 1):
						if coulk == 1 or coulk == 2:
							if coul == 3 or coul == 4:
								l.append([C,rg,k,-1])
						if coulk == 3 or coulk == 4:
							if coul == 1 or coul == 2:
								l.append([C,rg,k,-1])
				else:
					l.append([C,rg,k,-1])
		return l
	else:
		return -1
	
			
def appendcond(l,x):
	if x != -1:
		l.append(x)
		
def concatcond(l1,l2):
	if l2 != -1:
		return l1 + l2
	else:
		return l1


def ListeCoups(B):
	lFondation = []
	lFreeCell = []
	lCascade = []
	n = len(B[1])
	for k in range(n):
		appendcond(lFondation,JeuVersFondation(1,k,B))
		appendcond(lFreeCell,JeuVersFreeCell(1,k,B))
		lCascade = concatcond(lCascade,JeuVersCascade(1,k,B))
	for k in range(2,10):
		appendcond(lFondation,JeuVersFondation(k,-1,B))
		appendcond(lFreeCell,JeuVersFreeCell(k,-1,B))
		lCascade = concatcond(lCascade,JeuVersCascade(k,-1,B))
	return lFondation + lCascade + lFreeCell


# Joue(Board,coup) renvoie le board obtenu à partir de Board après avoir joué le
# coup "coup"
# On fera bien attention à effectuer un copy


# over(Board) vérifie si les cascades et les freecells sont vides



#def Solvaux(Board,Liste_coups_joués):
#	if over(Board):
#		return Liste_coups_joués
#	else:
#		Liste_coups_possibles = ListeCoups(B)
#		for coup in Liste_coups_possibles:
#			if not cycle(Liste_coups_joués,coup):
#				NewBoard = Joue(Board,coup)
#				NextStep = Solvaux(NewBoard,Liste_coups_joués + [coup])
#				if NextStep != -1:
#					return NextStep
#		return -1
