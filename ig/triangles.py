#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin de triangles pleins du module ig
#
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
from donnees import *
from base import *
from segments import *
################################################################################

################################################################################
# Dessin d'un triangle image vide avec pas de traçage et épaisseur
################################################################################
def DessineTriangleImage(pi1, pi2, pi3, coul, pas=1, epaisseur=1):

    DessineSegmentImage(pi1, pi2, coul, pas, epaisseur)
    DessineSegmentImage(pi2, pi3, coul, pas, epaisseur)
    DessineSegmentImage(pi1, pi3, coul, pas, epaisseur)

################################################################################
# Dessin d'un triangle réel vide avec pas de traçage hors fenêtre
################################################################################
def DessineTriangleReel(pr1, pr2, pr3, coul, transfo, pasHF=0):

    DessineSegmentReel(pr1, pr2, coul, transfo, pasHF)
    DessineSegmentReel(pr2, pr3, coul, transfo, pasHF)
    DessineSegmentReel(pr1, pr3, coul, transfo, pasHF)

################################################################################
# Dessin d'un triangle plein
################################################################################
def DessineTrianglePlein(pi1, pi2, pi3, coul):

    # Calcul des vecteurs correspondant aux côtés du triangles
    AB = PointImage(pi2.col - pi1.col, pi2.lig - pi1.lig)
    AC = PointImage(pi3.col - pi1.col, pi3.lig - pi1.lig)
    P = PointImage()

    # Récupération de la boîte englobante du triangle

    # calcul du delta necessaire pour parcourir AB
    mAB = max(abs(AB.col), abs(AB.lig))

    dAB = 1

    if mAB != 0:
        dAB = 1.0 / mAB

    # calcul du delta necessaire pour parcourir AC
    mAC = max(abs(AC.col), abs(AC.lig))
    dAC = 1

    if mAC != 0:
        dAC = 1.0 / mAC

    # Parcours de la boîte englobante

    # double boucle de parcours
    a = 0.0

    while a <= 1.0 :

        b = 0.0

        while a + b <= 1.0 :
            P.x = int(round(pi1.col + a * AB.col + b * AC.col))
            P.y = int(round(pi1.lig + a * AB.lig + b * AC.lig))
            ColoriePixel(P.x, P.y, coul)
            b = b + dAC

        a = a + dAB

################################################################################
