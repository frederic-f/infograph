#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin de segments du module ig
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
from base import *
from transfos import *
################################################################################

################################################################################
# Dessin d'un segment image en version entière (avec pas de traçage et épaisseur)
# le paramètre optionnel fi permet de limiter le tracé à une fenêtre image
################################################################################
def DessineSegmentImage(p1, p2, coul, pas=1, epaisseur=1, fi=None):
    pi1 = PointImage(p1.col, p1.lig)
    pi2 = PointImage(p2.col, p2.lig)

 
    # variation en lignes et colonnes
    dlig = p2.lig - p1.lig
    dcol = p2.col - p1.col

    absdcol = abs(dcol) # val abs de col
    absdlig = abs(dlig) # pareil lig

    # on commence toujours au point A
    col = p1.col
    lig = p1.lig

    # sens initial de parcours positif
    sensLig = 1
    sensCol = 1

    # Mise a jour sens de parcours des colonnes
    if dcol < 0 :
        sensCol = -1

    if dlig < 0 :
        sensLig = -1

    # parcours des colonnes
    if absdcol >= absdlig :
        
        print("parcours des colonnes")

        cumul = absdcol
        
        while col != p2.col + sensCol :
            
            # prise en compte du pas pour colorier ou pas le pixel
            if col % pas == 0 :
                ColoriePixel(col, lig, coul)
            
            cumul = cumul + 2 * absdlig

            if cumul >= 2 * absdcol :
                lig = lig + sensLig
                cumul = cumul - 2 * absdcol
                     
            col = col + sensCol

    else :  # parcours des lignes
        print(" parcours des lignes")

        cumul = absdlig

        while lig != p2.lig + sensLig :
            
            # prise en compte du pas
            if lig % pas == 0 :
                ColoriePixel(col, lig, coul)
            
            
            cumul = cumul + 2 * absdcol

            if cumul >= 2 * absdlig :
                col = col + sensCol
                cumul = cumul - 2 * absdlig

            lig = lig + sensLig

    # Prise en compte de la fenêtre fi si elle est spécifiée
    if (fi != None):
        pass
        
    # On ne dessine que si le pas d'affichage est non nul
    if (pas > 0):
        pass
################################################################################

################################################################################
# Dessin d'un segment réel
# Le paramètre 'pasHF' peut être omis et représente le pas des pointillés
# pour les parties du segment qui sont hors de la fenêtre
# Le paramètre epaisseur spécifie le nombre de pixels pour l'épaisseur du trait
################################################################################
def DessineSegmentReel(p1, p2, coul, transfo, pasHF=0, epaisseur=1):
    i1, i2 = PointImage(), PointImage()
    r1, r2 = PointReel(), PointReel()
    coulExt = Couleur(255 - coul.R, 255 - coul.V, 255 - coul.B) # Couleur inversée

    #
    # À COMPLÉTER
    #

    # Découpage

    # Si segment en partie dans la fenêtre

    #   Affichage partie p1<->r1 (hors fenêtre)

    #   Affichage partie r1<->r2

    #   Affichage partie r2<->p2 (hors fenêtre)

    # Sinon

    #   Affichage partie p1<->p2 (hors fenêtre)

################################################################################

################################################################################
# Transfert du point p1 à la position "bord" sur l'axe spécifié et info de
# position par rapport à l'autre axe dans l'intervalle [mini:maxi]
################################################################################
def TransfertSurBord(p1, p2, bord, axe, mini, maxi):

    #
    # À COMPLÉTER
    #

    if axe == 'y': # Bord vertical
        pass
        # Calcul des nouvelles coordonnées du point p1

        # Mise à jour des informations de position du point p1 par rapport à l'intervalle [mini:maxi] sur l'autre axe

    else:          # Bord horizontal
        pass
        # Calcul des nouvelles coordonnées du point p1

    # La position relative de p1 n'est plus à l'extérieur par rapport au bord

    return (exterieur, sousmin, surmax) # Variables calculées localement
################################################################################

################################################################################
# Découpage d'un segment réel
################################################################################
def DecoupeSegmentReel(pr1, pr2, fr):

    npr1 = PointReel(pr1.x, pr1.y) # Copie de pr1, éventuellement déplacée sur un bord de la fenêtre
    npr2 = PointReel(pr2.x, pr2.y) # Copie de pr2, éventuellement déplacée sur un bord de la fenêtre

    gauche1  = npr1.x < fr.bg.x
    dessus1  = npr1.y > fr.hd.y
    droite1  = npr1.x > fr.hd.x
    dessous1 = npr1.y < fr.bg.y
    gauche2  = npr2.x < fr.bg.x
    dessus2  = npr2.y > fr.hd.y
    droite2  = npr2.x > fr.hd.x
    dessous2 = npr2.y < fr.bg.y

    #
    # À COMPLÉTER
    #

    # Tests globaux liés aux deux points
    toutDehors = True
    toutDedans = True

    # Boucle des projections sur les bords
    while (not toutDehors) and (not toutDedans):
        pass
        # Mise à jour des positions globales des deux points
                
    # Affectation hors fenêtre si le segment est tout dehors
    if (toutDehors):
        npr1.x = fr.bg.x-1.0
        npr1.y = fr.bg.y-1.0
        npr2.x = fr.bg.x-1.0
        npr2.y = fr.bg.y-1.0

    return (npr1, npr2)
################################################################################

################################################################################
# Dessin d'un ensemble de segments réels issus d'un même point
################################################################################
def DessineFuseau(pr1, pr2, source, coulS, coulP):

    #
    # À COMPLÉTER
    #
    return
    
    # Détermination des points bg et hd

    # Détermination des points de départ et d'arrivée

    # Sens de parcours en X

    # Sens de parcours en Y

    # Boucle des segments balayant l'axe des X

    # Boucle des segments balayant l'axe des Y

################################################################################
