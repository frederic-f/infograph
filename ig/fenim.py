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

    #print("fenim.py > ligne ",fi.hd.lig)

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


    #print("DessineAxes called")
    #print("Transfo", pas)
    

    if (haut != None):
        taille = haut

    # AXE HORIZONTAL

    # on trace l' axe horizontal
    # p1 a gauche
    # y = 0 pour les deux points (c' est laxe horizontal)
    # c' est la valeur par defaut quand un point reel est cree
    # on ne modifie donc que x
    p1.x = transfo.fr.bg.x
    p2.x = transfo.fr.hd.x
    DessineSegmentReel(p1, p2, couleur, transfo)
 
    # Graduations de l'axe horizontal
    
    # VERS LA DROITE

    # on part de zero et on ajoute le pas
    x = pas
    p1.y = 0
 
    while(x < transfo.fr.hd.x): # tant que l' on n est pas sorti de la fenetre
  
        # on recupere le point image correspondant
        p1.x = x
        i1 = TransformationRvI(p1, transfo)
        ColoriePixel(i1.col, i1.lig, Couleur(255, 255, 255))

        # on trace un segment
        # ici segment vertical col = i1.col
        # 
        iHaut = PointImage(i1.col, i1.lig-3)
        iBas = PointImage(i1.col, i1.lig+3)
        DessineSegmentImage(iHaut, iBas, couleur)

        x = x+pas

    # VERS LA GAUCHE

    # on part de zero et on soustrait le pas
    x = - pas
    p1.y = 0

    while(x > transfo.fr.bg.x): # tant que l' on n est pas sorti de la fenetre
 
        # on recupere le point image correspondant
        p1.x = x
        i1 = TransformationRvI(p1, transfo)
        ColoriePixel(i1.col, i1.lig, Couleur(255, 255, 255))

        # on trace un segment
        # ici segment vertical col = i1.col
        # 
        iHaut = PointImage(i1.col, i1.lig-3)
        iBas = PointImage(i1.col, i1.lig+3)
        DessineSegmentImage(iHaut, iBas, couleur)

        x = x - pas


    # AXE VERTICAL

    # inverse de precedemment, x = 0 et on ne modifie que y
    p1.x = 0
    p2.x = 0
    p1.y = transfo.fr.hd.y
    p2.y = transfo.fr.bg.y
    DessineSegmentReel(p1, p2, couleur, transfo)


    # Graduations de l'axe vertical
    
    # VERS LE HAUT
    
    # on part de zero et on ajoute le pas
    y = pas
    p1.x = 0
 
    while(y < transfo.fr.hd.y): # tant que l' on n est pas sorti de la fenetre
  
        # on recupere le point image correspondant
        p1.y = y
        i1 = TransformationRvI(p1, transfo)
        ColoriePixel(i1.col, i1.lig, Couleur(255, 255, 255))

        # on trace un segment
        # ici segment horizontal (lig ne change pas)
        # 
        iGauche = PointImage(i1.col-3, i1.lig)
        iDroite = PointImage(i1.col+3, i1.lig)
        DessineSegmentImage(iGauche, iDroite, couleur)

        y = y + pas

    # graduations 
        
    # VERS LE BAS
    
    # on part de zero et on soustrait le pas
    y = - pas
    p1.x = 0
 
    while(y > transfo.fr.bg.y): # tant que l' on n est pas sorti de la fenetre
  
        # on recupere le point image correspondant
        p1.y = y
        i1 = TransformationRvI(p1, transfo)

        # on trace un segment
        # ici segment horizontal (lig ne change pas)
        # 
        iGauche = PointImage(i1.col-3, i1.lig)
        iDroite = PointImage(i1.col+3, i1.lig)
        DessineSegmentImage(iGauche, iDroite, couleur)

        y = y - pas        


    # faisons apparaitre l' origine en blanc

    p = PointReel()
    DessinePointReel(p, Couleur(255,255,255), transfo)

################################################################################
