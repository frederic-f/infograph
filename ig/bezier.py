#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin de courbes de Bézier de degré 1 à 3 du module ig
#
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
# Définition des courbes paramétriques de Bezier pour degrés 1 à 3
################################################################################
def B1(t, vals):
    return (1.0 - t) * vals[0] + t * vals[1]

def B2(t, vals):
    return ((1.0 - t)**2) * vals[0] + 2 * (1.0 - t) * t * vals[1] + (t**2) * vals[2]

def B3(t, vals):
    return ((1.0 - t)**3) * vals[0] + 3 * ((1.0 - t)**2) * t * vals[1] + 3 * (1.0 - t) * t * t * vals[2] + (t**3) * vals[3]
################################################################################

################################################################################
# Dessin d'une courbe de Bezier de degré 1 à 3 (2 à 4 pts de contrôle)
################################################################################
def DessineBezier(pts, pas, coul, transfo, tgtes = False, coulFin = None, epaisseur=1, epFin=None):
    t = 0.0 # Paramètre réel évoluant entre 0 et 1
    degre = len(pts) - 1

    # Récupération des fonctions adéquates et des listes de chaque coordonnées
    # On considère le degré 1 par défaut
    B = B1
    lstx = [pts[0].x, pts[1].x]
    lsty = [pts[0].y, pts[1].y]

    #
    # À COMPLÉTER
    #

################################################################################
