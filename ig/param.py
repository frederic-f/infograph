#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin de fonction paramétrique du module ig
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
from segments import *
################################################################################

################################################################################
# Paramètres constants du poisson
################################################################################
_a = 15
_k = 1.5

################################################################################
# Fonction paramétrique donnant x(t)
################################################################################
def ParametriqueX(t):
    return _a * (cos(t) + 2 * _k * cos(t/2.) + 2 * _k)
################################################################################

################################################################################
# Fonction paramétrique donnant y(t)
################################################################################
def ParametriqueY(t):
    return _a * sin(t)
################################################################################

################################################################################
# Dessin de la courbe paramétrique pour t dans [tmin, tmax]
# avec le pas constant tpas
################################################################################
def DessineCourbeParametrique(tmin, tmax, tpas, coul, transfo, dicho=False):
    
    #
    # fait
    #

    if dicho:

        # Version récursive
        # Le principe : on divise la distance entre les deux points par deux
        # jusqu'a ce que la distance entre les deux point soit inférieure au pas reel (irA)

        diff = abs(tmax - tmin)
        #print ("diff = ", diff)

        tmilieu = (tmax + tmin)/2
        print ("tmilieu = ", tmilieu)

        print ("dt = ", transfo.irA)
        #print ("tmin = ", tmin, ", tmax = ", tmax)

        #print ("\n")


        # si la difference est superieure, on divise a nouveau par deux
        if diff > transfo.irA:
            DessineCourbeParametrique(tmin, tmilieu, tpas, coul, transfo, True)
            DessineCourbeParametrique(tmilieu, tmax, tpas, coul, transfo, True)
        else:
            # sinon on affiche le segment reel
            pr_precedant = PointReel(ParametriqueX(tmin), ParametriqueY(tmin))
            pr_suivant = PointReel(ParametriqueX(tmax), ParametriqueY(tmax))
            DessineSegmentReel(pr_precedant, pr_suivant, coul, transfo)


    else:

        # Version itérative à pas constant

        # IMPORTANT : un segment est trace entre un point PRECEDANT et un point SUIVANT
        
        # on determine le premier point
        # que l'on nomme point precedant
        # c'est la premiere extremite du premier segment
        pr_precedant = PointReel(ParametriqueX(tmin), ParametriqueY(tmin))
        #__pi_precedant = TransformationRvI(pr_precedant, transfo)
        #__ColoriePoint(pi_precedant, coul)

        t = tmin

        # on parcours le range de tmin a tmax
        # et a chaque fois on trace le segment
        while t <= tmax:
            # calcul du point suivant
            t += tpas
            pr_suivant = PointReel(ParametriqueX(t), ParametriqueY(t))

            # dessin du segment reel
            DessineSegmentReel(pr_precedant, pr_suivant, coul, transfo)
            
            # le point suivant devient le point precedant 
            pr_precedant = PointReel(pr_suivant.x, pr_suivant.y)


################################################################################
