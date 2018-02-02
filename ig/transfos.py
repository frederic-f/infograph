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
    
    #
    # À COMPLÉTER
    #

    return pi # Renvoie le point image obtenu par la transformation du point réel
################################################################################

################################################################################
# Transformation image vers réel
################################################################################
def TransformationIvR(pi, transfo):
    pr = PointReel() # Point réel résultant de la transformation
    
    #
    # À COMPLÉTER
    #

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
    # À COMPLÉTER
    #

    # Transfo réel -> image

    # Transfo image -> réel

    return transfo # Renvoie la structure de transformation
################################################################################

################################################################################
# Dessin d'un point réel
################################################################################
def DessinePointReel(pr, coul, transfo):

    #
    # À COMPLÉTER
    #
    return
################################################################################
