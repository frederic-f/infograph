#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Gestion des transformations entre fenêtres du module ig
#
################################################################################

################################################################################
# Chargement des modules standards
################################################################################
from math import *
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
from donnees import *
from base import ColoriePixel
################################################################################

################################################################################
# Transformation réel vers image
################################################################################
def TransformationRvI(pr, transfo):
    pi = PointImage() # Point image résultant de la transformation
    
    # col = riA * x + riB

    pi.col = int(round(transfo.riA * pr.x + transfo.riB))
    pi.lig = int(round(transfo.riC * pr.y + transfo.riD))

    #debug 
    #print("transfo.py > TransformationsRvI > transfo ", transfo);
    
    return pi # Renvoie le point image obtenu par la transformation du point réel
################################################################################

################################################################################
# Transformation image vers réel
################################################################################
def TransformationIvR(pi, transfo):
    pr = PointReel() # Point réel résultant de la transformation
    
    pr.x = transfo.irA * pi.col + transfo.irB
    pr.y = transfo.irC * pi.lig + transfo.irD


    return pr # Renvoie le point réel obtenu par la transformation du point image
################################################################################

################################################################################
# Calcul de coefficients de transformations réel <-> image
################################################################################
def CalculTransfosFenetres(fr, fi):
    transfo = TransfosFenetres()          # Structure de transformation
    dcol, dlig = int(0), int(0)           # Variations en colonnes et lignes
    dx, dy = float(0.0), float(0.0)       # Variations en x et y
    dxbis, dybis = float(0.0), float(0.0) # Idem pour égalisation des ratios des fenêtres

    transfo.fr = fr # Recopie de la fenêtre réel
    transfo.fi = fi # Recopie de la fenêtre image

    #
    # FAIT
    #

    # A = dcol / dx
    #print("fi.hd.col :", fi.hd.col)
    #print("fi.bg.col :", fi.bg.col)
    dcol = fi.hd.col - fi.bg.col

    #print("fr.hd.x :", fr.hd.x)
    #print("fr.bg.x :", fr.bg.x)
    dx = fr.hd.x - fr.bg.x
    
    # Transfo réel -> image
    transfo.riA = dcol / dx
    
    #print("riA :", transfo.riA) # 28.13636

    transfo.riB = fi.bg.col - (transfo.riA * fr.bg.x)

    #print("riB :", transfo.riB) # 682.5

    # C = - dlig / dy
    #print("fi.bg.lig :", fi.bg.lig)
    #print("fi.hd.lig :", fi.hd.lig)
    dlig = fi.bg.lig - fi.hd.lig

    #print("fr.hd.y :", fr.hd.y)
    #print("fr.bg.y :", fr.bg.y)
    dy = fr.hd.y - fr.bg.y

    transfo.riC = - dlig / dy
    #print("riC :", transfo.riC) # -28.09

    # D 

    transfo.riD = dlig - (transfo.riC * fr.bg.y) + fi.hd.lig
    #print("riD :", transfo.riD) # 384
    #print("\n")

    # Transfo image -> réel

    # on renvoie les inverses
    transfo.irA = 1 / transfo.riA
    transfo.irB = 1 / transfo.riB
    transfo.irC = 1 / transfo.riC
    transfo.irD = 1 / transfo.riD


    return transfo # Renvoie la structure de transformation
################################################################################

################################################################################
# Dessin d'un point réel
################################################################################
def DessinePointReel(pr, coul, transfo):

    #
    # FAIT
    #
    i1 = PointImage()

    i1 = TransformationRvI(pr, transfo)
    ColoriePixel(i1.col, i1.lig, coul)

    return
################################################################################
