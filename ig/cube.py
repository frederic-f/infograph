#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin du cube des couleurs du module ig
#
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
from donnees import *
from base import *
################################################################################

################################################################################
# Dessin d'un rectangle uni
################################################################################
def DessineRectangleUni(s1, s2, coul):
    
    for i in range(s1.lig, s2.lig) : # parcourt ligne 
        for j in range(s1.col, s2.col) : # parcours 
            ColoriePixel(i, j, coul)
            

    return
################################################################################

################################################################################
# Dessin d'une face du cube des couleurs à partir de son coin haut-gauche
################################################################################
def DessineFaceCube(pos, coul, baseCol, baseLig):
    
    # debug
    print(pos.col, pos.lig)

    # on fixe R_step V_step et B_step selon valeur de R
    if(coul.R == 0) :
        R_step = 1
    else :
        R_step = -1

    if(coul.V == 0) :
        V_step = 1
    else :
        V_step = -1

    if(coul.B == 0) :
        B_step = 1
    else :
        B_step = -1

    ### 

    R_tmp = coul.R
    V_tmp = coul.V
    B_tmp = coul.B

    # determine les valeurs que i doit parcourir
    # i sont les lignes
    # si 

    for i in range(256) : # on parcourt les lignes

        for j in range(256) : # j c est les colonnes

            # on trace de suite le premier pixel
            # on en determine la couleur
            coul_tmp = Couleur(R_tmp, V_tmp, B_tmp)

            # on ajoute pos.col pour placer le point haut gauche au bon endroit
            # le premier c'est (pos.col + 0, pos.lig + 0)
            ColoriePixel(pos.col + j, pos.lig + i, coul_tmp)

            # modif de la couleur selon colonne : baseCol
            if(baseCol=="R"):
                R_tmp = R_tmp + R_step
            else :
                R_tmp = R_tmp

            if(baseCol=="V"):
                V_tmp = V_tmp + V_step
            else :
                V_tmp = V_tmp

            if(baseCol=="B"):
                B_tmp = B_tmp + B_step
            else :
                B_tmp = B_tmp

        # endfor

        # on remet a zero la couleur de base col
        if (baseCol == "R"):
            R_tmp = coul.R
        if (baseCol == "V"):
            V_tmp = coul.V
        if (baseCol == "B"):
            B_tmp = coul.B

        # on incremente la coul de la ligne
        if (baseLig == "R"):
            R_tmp = R_tmp + R_step
        else:
            R_tmp = R_tmp
        if (baseLig == "V"):
            V_tmp = V_tmp + V_step
        else:
            V_tmp = V_tmp
        if (baseLig == "B"):
            B_tmp = B_tmp + B_step
        else:
            B_tmp = B_tmp

    return
################################################################################

################################################################################
# Dessin des faces du cube des couleurs
################################################################################
def DessineFacesCubeCouleurs():

    # Carré au dessus
    DessineFaceCube(PointImage(256,0), Couleur(0, 255, 255), 'R', 'B')

    # Carré à gauche
    DessineFaceCube(PointImage(0,256), Couleur(0, 255,255), 'B', 'V')

    # Carré au centre
    DessineFaceCube(PointImage(256,256), Couleur(0, 255,0), 'R', 'V')

    # Carré à droite
    DessineFaceCube(PointImage(512,256), Couleur(255, 255, 0), 'B', 'V')

    # Carré derrière (à droite)
    DessineFaceCube(PointImage(768, 256), Couleur(255, 255, 255), 'R', 'V')

    # Carré au dessous
    DessineFaceCube(PointImage(256, 512), Couleur(0, 0, 0), 'R', 'B')

################################################################################
