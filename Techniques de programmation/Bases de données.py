# -*- coding: utf-8 -*-
"""
Created on Thu Dec 27 23:25:18 2018

@author: adrie
"""

vehicule1 = [["98300", "Bus", "IBUS"],
			["1562", "TGV", "SNCF"],
			["30990", "A320", "Hop!"],
			["78234", "Bus", "IBUS"],
			["27364", "Bus", "IBUS"],
			["39827", "Navette spatiale", "ESA"],
			["00000", "à pied", "SNCF"],
			["23784", "Métro", "SNCF"],
			["24873", "Taxi", "G7"],
			["23782", "Bus", "IBUS"],
			["1093", "TGV", "SNCF"],
			["mystère", "???", "???"]]

trajet1 = [["trajet1", "Lille", "Rennes", "5 oct. 2016", "09h00", "30990"],
		  ["trajet2", "Lille", "Rennes", "5 oct. 2016", "10h00", "98300"],
		  ["trajet3", "Lille", "Rennes", "5 oct. 2016", "14h00", "1562"],
		  ["trajet4", "Paris", "Lille", "4 oct. 2016", "19h00", "1093"],
		  ["trajet5", "Rennes", "Paris", "2 oct. 2016", "23h00", "23782"]]



# PARTIE I


def SelectionConstante(t,i,c):
	l = []
	for e in t:
		if e[i] == c:
			l.append(e)
	return l

# SelectionConstante a une complexité en O(n) ou n est le nombre d'enregistrements:
# on parcours touts les enregistrements de la table et on effectue sur chaque une
# opération à coût constant


def SelectionEgalite(t,i,j):
	l = []
	for e in t:
		if e[i] == e[j]:
			l.append(e)
	return l


def ProjectionEnregistrement(e,li):
	return [e[i] for i in li]

def Projection(t,li):
	return [ProjectionEnregistrement(e,li) for e in t]


def ProduitCartesien(t1,t2):
	l = []
	for e1 in t1:
		for e2 in t2:
			l.append(e1 + e2)
	return l


def JointEnregistrement(e1,e2,i1,i2):
	if e1[i1] == e2[i2]:
		l = [x for x in e1]
		k2 = len(e2)
		for i in range(k2):
			if i != i2:
				l.append(e2[i])
		return l
	else:
		return -1

def Jointure(t1,t2,i1,i2):
	l = []
	for e1 in t1:
		for e2 in t2:
			e = JointEnregistrement(e1,e2,i1,i2)
			if e != -1:
				l.append(e)
	return l

# la complexité de JointEnregistrement est O(k1 + k2)

# Jointure appelle n1*n2 fois JointEnregistrement donc sa complexité totale est
# O(n1*n2*(k2 + k2))


def EgaliteListe(e1,e2):
	n = len(e1)
	for i in range(n):
		if e1[i] != e2[i]:
			return False
	return True

def AppartientListe(e,l):
	for ee in l:
		if EgaliteListe(e,ee):
			return True
	return False

def SupprimerDoublons(t):
	l = []
	for e in t:
		if not AppartientListe(e,l):
			l.append(e)
	return l

# EgaliteListe a une complexité O(k)

# AppartientListe appelle au pire n fois EgaliteListe donc a une complexité O(n*k)

# SupprimerDoublons appelle n fois AppartientListe donc a une complexité O(n²*k)



# Partie II

Vehicule = [["30990", "A320", "Hop!"],
			["98300", "Bus", "IBUS"],
			["1562", "TGV", "SNCF"]]

Trajet = [["trajet1", "Lille", "Rennes", "30990"],
		  ["trajet2", "Lille", "Rennes", "98300"],
		  ["trajet3", "Lille", "Rennes", "1562"],
		  ["trajet4", "Paris", "Lille", "1562"],
		  ["trajet5", "Rennes", "Paris", "1562"]]

Ticket = [["23982", "trajet1", "32", "5 oct. 2016", "09h00", "56"],
		  ["22382", "trajet1", "36", "5 oct. 2016", "09h00", "50"],
		  ["21282", "trajet1", "42", "5 oct. 2016", "09h00", "54"],
		  ["93022", "trajet2", "98", "5 oct. 2016", "10h00", "50"],
		  ["26382", "trajet3", "382", "5 oct. 2016", "14h00", "398"],
		  ["87382", "trajet2", "378", "5 oct. 2016", "10h00", "78"]]

Hotel = [["8372", "****", "Rennes"],
			["3672", "**", "Lille"],
			["6737", "***", "Paris"],
			["3892", "*****", "Paris"],
			["7287", "***", "Paris"]]

Chambre = [["83729","8372", "5 oct. 2016", "100"],
			["29829","3672", "5 oct. 2016", "213"],
			["23729","6737", "5 oct. 2016", "100"],
			["24729","3892", "5 oct. 2016", "100"],
			["13729","7287", "5 oct. 2016", "118"],
			["78729","6737", "2 oct. 2016", "423"],
			["75729","3892", "4 oct. 2016", "329"],
			["46729","7287", "6 oct. 2016", "318"]]


# 1

resultat1 = SelectionConstante(Trajet,1,"Rennes")


# 2

resultat2 = ProduitCartesien(Trajet,Vehicule)


# 3

r3 = ProduitCartesien(Trajet,Vehicule)
resultat3 = SelectionEgalite(r3,3,4)


# 4

r4 = Jointure(Hotel,Chambre,0,1)
resultat4 = Projection(r4,[1,2,4,5])


# 5

r5 = ProduitCartesien(ProduitCartesien(Hotel,Trajet),Ticket)
rr5 = SelectionEgalite(r5,2,5)
rrr5 = SelectionEgalite(rr5,3,8)
rrrr5 = SelectionConstante(rrr5,12,"50")
resultat5 = Projection(rrrr5,[0])


# 6

r6 = SelectionConstante(Chambre,3,"100")
resultat6 = []
for idhotel in SupprimerDoublons(resultat5):
	resultat6 += SelectionConstante(r6,1,idhotel[0])



# Partie III

Test = [["1234", "Bus", "IBUS"],
			["1562", "TGV", "SNCF"],
			["1678", "A320", "Hop!"],
			["1789", "Bus", "IBUS"],
			["1789", "Navette spatiale", "ESA"],
			["1983", "à pied", "SNCF"],
			["1985", "Métro", "SNCF"],
			["1985", "Taxi", "G7"],
			["1985", "Bus", "IBUS"],
			["2009", "TGV", "SNCF"],
			["9003", "???", "???"]]

Test2 = [["1234","30%"],
		 ["1562","50%"],
		 ["2009","40%"]]


def VerifieTrie(t,i):
	n = len(t)
	for j1 in range(n):
		for j2 in range(j1 + 1,n):
			if t[j1][i] > t[j2][i]:
				return False
	return True


def IndiceGauche(t,i,c):
	n = len(t)
	i1 = 0
	i2 = n - 1
	while i2 != i1:
		j = int((i2 + i1)/2)
		if t[j][i] < c:
			i1 = j + 1
		else:
			i2 = j
	return i1

def IndiceDroite(t,i,c):
	n = len(t)
	i1 = 0
	i2 = n - 1
	while i2 != i1:
		j = int((i2 + i1)/2) + 1
		if t[j][i] > c:
			i2 = j - 1
		else:
			i1 = j
	return i1

def SelectionConstanteTrie(t,i,c):
	i1 = IndiceGauche(t,i,c)
	i2 = IndiceDroite(t,i,c)
	if t[i1][i] == t[i2][i] == c:
		return [t[j] for j in range(i1, i2 + 1)]
	else:
		return []


def JointureTrie(t1,t2,i1,i2):
	l = []
	for e1 in t1:
		t = SelectionConstanteTrie(t2,i2,e1[i1])
		if len(t) == 1:
			e2 = t[0]
			e = [x for x in e1]
			k2 = len(e2)
			for i in range(k2):
				if i != i2:
					e.append(e2[i])
			l.append(e)
	return l

# IndiceGauche et IndiceDroite vérifient l'equation de complexité T(n) = T(n/2) + O(1)
# leurs complexité est donc O(log(n2))

# La complexité de SelectionConstanteTrie est donc aussi O(log(n2))

# JointureTrie effectue n1 fois un appel de SelectionConstanteTrie puis une operation
# de cout k1 + k2 donc sa complexité totale est O(n1*(log(n2) + k1 + k2))

# Cette approche est particulièrement performante quand une des tables contient 
# beaucoup plus d'enregistrement que l'autre car on peut alors minimiser son impact
# sur la complexité en la passant en 2e argument car son influence est alors
# reduite par le log

# Cette approche sera dans touts les cas toujours plus performante


def CreerDictionnaire(t,i):
	dico = {}
	n = len(t)
	for j in range(n):
		e = t[j]
		if e[i] in dico:
			dico[e[i]].append(j)
		else:
			dico[e[i]] = [j]
	return dico


def SelectionConstanteDictionnaire(t,i,c,dico):
	return [t[j] for j in dico[c]]

# SelectionConstanteDictionnaire effectue autant d'opérations que d'enregistrement 
# verifiant la condition alors que SelectionConstante effectue toujours n opérations
# La complexité de SelectionConstanteDictionnaire est donc toujours meilleure que 
# celle de SelectionConstante

# Si touts les enregistrements vérifient la condition, SelectionConstanteDictionnaire
# n'est pas plus performante


def JointureDictionnaire(t1,t2,i1,i2,dico2):
	l = []
	for e1 in t1:
		for i in dico2[e1[i1]]:
			e2 = t2[i]
			e = [x for x in e1]
			for j in range(len(e2)):
				if j != i2:
					e.append(e2[j])
			l.append(e)
	return l

# Soit m la somme des arités des tables t1 et t2
# JointureDictionnaire effectue n1 fois (itération sur t1) k2 fois (itération 
# sur dico[e1[i]]) m opérations donc la complexité totale est O(n1*k2*m)

# On souhaite choisir t1 et t2 pour que n1*k2 soit minimal