#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Remplissage d'une zone uniforme du module ig
#
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
from ecran import *
from donnees import *
from base import *
from transfos import *
from segments import *
################################################################################

################################################################################
# Remplissage de zone uniforme
# pos: position
# coul: couleur de remplisage
# fi: fenêtre image pour limiter le remplissage si besoin
# tol: tolérance d'écart à la couleur
################################################################################
def RemplissageUni(pos, coul, fi=None, tol=0):

    # on recupere la couleur du pixel de depart
    CoulARemplacer = CouleurPixel(pos.col, pos.lig, fi)

    # test
    # on colorie en blanc le pixel de depart
    #ColoriePixel(pos.col, pos.lig, Couleur(255, 255, 255))

    # creation de la pile
    pile = []

    # on ajoute le premier pixel
    pile.append(pos)

    # taille de la pile
    #print(len(pile))

    # tant que la pile est pleine, on traite les pixels
    while (len(pile) > 0):
        
        # on recupere le premier pixel de la pile
        pi = pile.pop()

        # on le colorie dans la couleur cible
        ColoriePixel(pi.col, pi.lig, coul)

        # on regarde tous les pixels alentours en 4-connexite
        pi1 = PointImage(pi.col-1, pi.lig)
        pi2 = PointImage(pi.col+1, pi.lig)
        pi3 = PointImage(pi.col, pi.lig-1)
        pi4 = PointImage(pi.col, pi.lig+1)

        # pour chaque point alentours on teste si
        # 1) il est bien dans la fenetre
        # 2) il est de la couleur a remplacer
        # si oui, alors on l'ajoute dans la pile
        if (testPixelInFenetre(pi1, fi)) and (testCouleursEgales(CouleurPixel(pi1.col, pi1.lig, fi),CoulARemplacer)):
            pile.append(pi1)
        if (testPixelInFenetre(pi2, fi)) and (testCouleursEgales(CouleurPixel(pi2.col, pi2.lig, fi),CoulARemplacer)):
            pile.append(pi2)
        if (testPixelInFenetre(pi3, fi)) and (testCouleursEgales(CouleurPixel(pi3.col, pi3.lig, fi),CoulARemplacer)):
            pile.append(pi3)
        if (testPixelInFenetre(pi4, fi)) and (testCouleursEgales(CouleurPixel(pi4.col, pi4.lig, fi),CoulARemplacer)):
            pile.append(pi4)
    return

################################################################################
# fonction qui teste si deux couleurs sont egales

def testCouleursEgales(c1, c2):
    return c1.R==c2.R and c1.V==c2.V and c1.B==c2.B
################################################################################

################################################################################
# fonction qui tests si un pointImage est dans la fenetreImage

def testPixelInFenetre(pi, fi):
    return (pi.col >= fi.bg.col) and (pi.col <= fi.hd.col) and (pi.lig >= fi.hd.lig) and (pi.lig <= fi.bg.lig)
################################################################################
