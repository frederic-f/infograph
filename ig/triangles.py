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

    #
    # À COMPLÉTER
    #
    return

    # Calcul des vecteurs correspondant aux côtés du triangles

    # Récupération de la boîte englobante du triangle

    # Parcours de la boîte englobante

################################################################################
