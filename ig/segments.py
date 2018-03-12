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

    # On ne dessine que si le pas d'affichage est non nul
    if (pas > 0):

        pi1 = PointImage(p1.col, p1.lig)
        pi2 = PointImage(p2.col, p2.lig)


        # VERSION PERSONNELLE DE LA FONCTION

        # variation en lignes et colonnes
        dlig = p2.lig - p1.lig
        dcol = p2.col - p1.col

        absdcol = abs(dcol) # val abs de col
        absdlig = abs(dlig) # pareil lig

        # on commence toujours au point p1
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

        # debug
        #print("Sens des colonnes:", sensCol)
        #print("Sens des lignes:", sensLig)

        # parcours des colonnes pour le traçage (car y'a plus de differentiel en colonnes qu'en lignes)
        if absdcol >= absdlig :

            #print("parcours des colonnes")

            cumul = absdcol

            while col != p2.col + sensCol :

                # prise en compte du pas pour colorier ou pas le pixel
                if col % pas == 0 :

                    for i in range(epaisseur) :
                        ColoriePixel(col +i , lig, coul)

                cumul = cumul + 2 * absdlig

                if cumul >= 2 * absdcol :
                    lig = lig + sensLig
                    cumul = cumul - 2 * absdcol

                col = col + sensCol

        else :  # parcours des lignes pour le traçage car il y a plus de differentiel en lignes qu'en colonnes

            #print(" parcours des lignes")

            cumul = absdlig

            while lig != p2.lig + sensLig :

                # prise en compte du pas
                if lig % pas == 0 :

                    for i in range(epaisseur) :
                        ColoriePixel(col, lig +i, coul)


                cumul = cumul + 2 * absdcol

                if cumul >= 2 * absdlig :
                    col = col + sensCol
                    cumul = cumul - 2 * absdlig

                lig = lig + sensLig

        # Prise en compte de la fenêtre fi si elle est spécifiée
        if (fi != None):
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

    r1, r2 = DecoupeSegmentReel(p1, p2, transfo.fr)

    # on verifie que le segment est a tracer
    # cad que les coordonnees sont a l interieur de la fenetre
    if (r1.x >= transfo.fr.bg.x):
        # on trace
        # images des extremites DANS fenetre
        i1 = TransformationRvI(r1, transfo)
        i2 = TransformationRvI(r2, transfo)
        DessineSegmentImage(i1, i2, coul)
# images des extremites HORS fenetre


  


    # si au moins une des extremites est HORS fenetre, on trace trois segments
"""
    gauche1 = p1.x < fr.bg.x
    dessus1 = p1.y > fr.hd.y
    droite1 = p1.x > fr.hd.x
    dessous1 = p1.y < fr.bg.y
    gauche2 = p2.x < fr.bg.x
    dessus2 = p2.y > fr.hd.y
    droite2 = p2.x > fr.hd.x
    dessous2 = p2.y < fr.bg.y
"""
    # si tout dehors
    #if (r1.x = transfo.fr.bg.x - 1.0) and (r1.y = transfo.fr.bg.y - 1.0) and (r2.x = transfo.fr.bg.x - 1.0) and (r2.y = transfo.fr.bg.y - 1.0):
        # segment completement en dehors
        # on trace p1 <-> p2 avec un pas de 2
    # sinon
        # on trace les 3 portions de segment avec des pas différents pour les identifier




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



    #
    # À COMPLÉTER
    #

    # on met tout a faux pour entrer dans la boucle
    # sinon il faudrait copier tous les tests avant la boucle et ça fait moche
    toutDedans = toutDehors = gauche1 = gauche2 = droite1 = droite2 = dessus1 = dessus2 = dessous1 = dessous2 = False

    gauche1 = npr1.x < fr.bg.x
    dessus1 = npr1.y > fr.hd.y
    droite1 = npr1.x > fr.hd.x
    dessous1 = npr1.y < fr.bg.y
    gauche2 = npr2.x < fr.bg.x
    dessus2 = npr2.y > fr.hd.y
    droite2 = npr2.x > fr.hd.x
    dessous2 = npr2.y < fr.bg.y

    # pente constante quoi qu'il arrive
    dx = pr2.x - pr1.x
    dy = pr2.y - pr1.y
    if (dx != 0) :
        pente = dy / dx
    else:
        pente = 0

    # on va utiliser pente et 1/pente par la suite

    # TANT QUE JE N'AI PAS TOUT-DEHORS OU TOUT-DEDANS
    # Boucle des projections sur les bords
    # a chaque passage dans la boucle une coordonnées peut changer (sauf peut etre au premier passage, dans ce cas, passage unique)
    while (not toutDehors) and (not toutDedans): # ou bien :  not (toutDehors or toutDedans)

        #_ print("Entrée dans la boucle")

        # RIEN A CHANGER QUE CE SOIT DROITE1 ou DROITE2
        # on considera le differentiel dx ou dy TOUJOURS positif

        # on fait une projection
        if(gauche1): # projection du point gauche sur le bord gauche
            #_ print("in gauche1") # OK
            # on deplace d'abord sur l'axe des x PUIS on calcule le decalage y
            dx1 = fr.bg.x - npr1.x # le x est a decaler de dx1 (il est a gauche de bg)
            dy1 = pente * dx1 # on calcule le decalage en y en consequence

            npr1.x = fr.bg.x # le nouveau x est le bord gauche
            npr1.y = npr1.y + dy1 # le nouveau y est l'ancien y ajouté du dy1
        elif(gauche2):
            #dbg print("in gauche2") # OK
            # on deplace d'abord sur l'axe des x PUIS on calcule le decalage y
            dx1 = fr.bg.x - npr2.x # le x est a decaler de dx1 (il est a gauche de bg)
            dy1 = pente * dx1 # on calcule le decalage en y en consequence

            npr2.x = fr.bg.x # le nouveau x est le bord gauche
            npr2.y = npr2.y + dy1 # le nouveau y est l'ancien y ajouté du dy1

        elif(droite1):
            #dbg print("in droite1") # OK
            # on deplace d'abord sur l'axe des x PUIS on calcule le decalage y
            dx1 = fr.hd.x - npr1.x   # le x est a decaler de dx1 (il est a droite de hd)
            dy1 = pente * dx1  # on calcule le decalage en y en consequence

            npr1.x = fr.hd.x  # le nouveau x est le bord gauche
            npr1.y = npr1.y + dy1  # le nouveau y est l'ancien y ajouté du dy1
        elif(droite2):
            #dbg print("in droite2") # OK
            # on deplace d'abord sur l'axe des x PUIS on calcule le decalage y
            dx1 = npr2.x - fr.hd.x  # le x est a decaler de dx1 (il est a droite de hd)
            dy1 = pente * dx1  # on calcule le decalage en y en consequence

            npr2.x = fr.hd.x  # le nouveau x est le bord gauche
            npr2.y = npr2.y - dy1  # le nouveau y est l'ancien y ajouté du dy1


        elif(dessus1):
            #dbg print("in dessus1")
            # on deplace d'abord sur l'axe des Y PUIS on calcule le decalage x
            dy1 = npr1.y - fr.hd.y # le y est a decaler de dy1 (il est au dessus de hd)
            dx1 = (1/ pente) * dy1 # on calcule le decalage en x en consequence

            npr1.y = fr.hd.y # le nouveau y est le bord haut
            npr1.x = npr1.x - dx1 # le nouveau x est l'ancien x ajouté du dx1

        elif(dessous1):
            #dbg print("in dessous1")
            # on deplace d'abord sur l'axe des Y PUIS on calcule le decalage x
            dy1 = npr1.y - fr.bg.y  # le y est a decaler de dy1 (il est en-dessous de bg)
            dx1 = (1 / pente) * dy1  # on calcule le decalage en x en consequence

            npr1.y = fr.bg.y  # le nouveau y est le bord bas
            npr1.x = npr1.x - dx1  # le nouveau x est l'ancien x ajouté du dx1


        elif(dessus2):
            #dbg print("in dessus2")
            # on deplace d'abord sur l'axe des Y PUIS on calcule le decalage x
            dy1 = npr2.y - fr.hd.y # le y est a decaler de dy1 (il est au dessus de hd)
            dx1 = (1/ pente) * dy1 # on calcule le decalage en x en consequence

            npr2.y = fr.hd.y # le nouveau y est le bord haut
            npr2.x = npr2.x - dx1 # le nouveau x est l'ancien x ajouté du dx1
        elif(dessous2):
            #dbg print("in dessous2")
            # on deplace d'abord sur l'axe des Y PUIS on calcule le decalage x
            dy1 = npr2.y - fr.bg.y  # le y est a decaler de dy1 (il est en-dessous de bg)
            dx1 = (1 / pente) * dy1  # on calcule le decalage en x en consequence

            npr2.y = fr.bg.y  # le nouveau y est le bord bas
            npr2.x = npr2.x - dx1  # le nouveau x est l'ancien x ajouté du dx1


        gauche1 = npr1.x < fr.bg.x
        dessus1 = npr1.y > fr.hd.y
        droite1 = npr1.x > fr.hd.x
        dessous1 = npr1.y < fr.bg.y
        gauche2 = npr2.x < fr.bg.x
        dessus2 = npr2.y > fr.hd.y
        droite2 = npr2.x > fr.hd.x
        dessous2 = npr2.y < fr.bg.y

        # projection est faite
        # on regarde ce que ça donne

        # TOUT DEDANS ?
        # Si oui on renvoie directement
        if (not (gauche1) and not (gauche2) and not (droite1) and not (droite2) and not (dessus1) and not (
        dessus2) and not (dessous1) and not (dessous2)):
            toutDedans = True
        else:
            toutDedans = False

        # TOUT DEHORS
        if ((gauche1 and gauche2) or (droite1 and droite2) or (dessus1 and dessus2) or (dessous1 and dessous2)):
            toutDehors = True
        else:
            toutDehors = False

        # mis au depart pour ne faire qu'un seul passage dans la boucle
        # chaque segment a couper des deux cotes n'etait donc coupe que d'un seul cote
        #toutDedans = True




    # Affectation hors fenêtre si le segment est tout dehors
    if (toutDehors):
        npr1.x = fr.bg.x - 1.0
        npr1.y = fr.bg.y - 1.0
        npr2.x = fr.bg.x - 1.0
        npr2.y = fr.bg.y - 1.0

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
