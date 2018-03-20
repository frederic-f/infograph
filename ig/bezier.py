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
   
    if (degre == 1) :
        B = B1
        lstx = [pts[0].x, pts[1].x]
        lsty = [pts[0].y, pts[1].y]
    elif (degre == 2) :
        B = B2
        lstx = [pts[0].x, pts[1].x, pts[2].x]
        lsty = [pts[0].y, pts[1].y, pts[2].y] 
    elif (degre == 3) :
        B = B3
        lstx = [pts[0].x, pts[1].x, pts[2].x, pts[3].x]
        lsty = [pts[0].y, pts[1].y, pts[2].y, pts[3].y] 

    #
    # fait
    #

    DessinePointReel(pts[0], coul, transfo)
        
    # calcul du premier point precedant, cad t=0
    pr_precedant = PointReel()
    pr_precedant.x = B1(t, lstx)
    pr_precedant.y = B1(t, lsty)

    while (t <= 1) :
        # incrementation du pas pour calculer le point suivant
        t += pas
        pr_suivant = PointReel()
        pr_suivant.x = B(t, lstx)
        pr_suivant.y = B(t, lsty)

        # on trace le segment
        DessineSegmentReel(pr_precedant, pr_suivant, coul, transfo)

        # point suivant devient point precedant
        pr_precedant.x = pr_suivant.x
        pr_precedant.y = pr_suivant.y


    # courbes de degre 1 pour le pot
    # courbes de degre 2 pour le pistil
    # courbes de degre 3 pour la tige, les feuilles et les petales

################################################################################
