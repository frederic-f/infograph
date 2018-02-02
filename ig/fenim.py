#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin des contours et des axes d'une fenêtre image du module ig
#
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
from donnees import *
from base import *
from segments import *

################################################################################
# Dessin du contour de la fenêtre image
################################################################################
def DessineContours(fi, coul):

    print("ligne ",fi.hd.lig)

    # Coin haut gauche a calculer
    coin_hg = PointImage(fi.bg.col, fi.hd.lig)

    # Coin haut droit = fi.hd
    coin_hd = fi.hd

    # coin bas droite
    coin_bd = PointImage(fi.hd.col, fi.bg.lig)

    # coin bas gauche = fi.bg
    coin_bg = fi.bg

    # segment dessus
    DessineSegmentImage(coin_hg, coin_hd, coul)
    # cote droit
    DessineSegmentImage(coin_hd, coin_bd, coul)
    # dessous
    DessineSegmentImage(coin_bd, coin_bg, coul)
    # cote gauche
    DessineSegmentImage(coin_bg, coin_hg, coul)

    return
################################################################################

################################################################################
# Fonction de dessin des axes avec graduations selon le pas
################################################################################
def DessineAxes(pas, transfo, couleur, nbInter = None, haut = None):
    p1, p2 = PointReel(), PointReel()   # Points pour le dessin des axes
    i1, i2 = PointImage(), PointImage() # Points image pour les graduations
    taille = 3                          # Taille des graduations en pixel au-dessus et au-dessous des axes

    if (haut != None):
        taille = haut

    #
    # À COMPLÉTER
    #

    # Axe horizontal

    # Graduations de l'axe horizontal

    # Axe vertical

    # Graduations de l'axe vertical

################################################################################
