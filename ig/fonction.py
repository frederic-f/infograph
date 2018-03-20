#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Dessin de fonction analytique du module ig
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
# Fonction f(x)
################################################################################
def FonctionF(x):
    #return sin(x)
    return 2.75*cos(7*x)/(1+x*x)
################################################################################

################################################################################
# Fonction de dessin d'une fonction y=f(x)
################################################################################
def DessineFonction(coul, transfo):
    x =  0.0
    dx = 1.0
    pr = PointReel()
    pi = PointImage()
    
    #
    # FAIT
    #

    # d'abord : calcul de longueur d'un pas reel (l'équivalent d'un pixel image)

    # on prend deux points image (0,0) et (1,0)
    # on les rapporte en points reels et on en deduit le pas reel

    pi1 = PointImage(0,0)
    pi2 = PointImage(1,0)

    pr1 = TransformationIvR(pi1, transfo)
    pr2 = TransformationIvR(pi2, transfo)

    pasReel = pr2.x - pr1.x
    print("Mon Pas reel = ", pasReel) # 0.0096930
    print("Pas reel de la transfo = ", transfo.irA) # 0.0096930 C'EST LE MEME
    # on va tracer la fonction
    # ce qui revient a tracer des segments successifs entre deux points : un point nouvellement calculé et le point précédent

    # le "premier" point précédent est le point de départ
    # on connait son x (bord gauche)
    # on calcule son y
    # et on le colorie

    pr_precedant = PointReel()
    pr_precedant.x = transfo.fr.bg.x
    pr_precedant.y = FonctionF(pr_precedant.x)

    pi_precedant = PointImage()
    pi_precedant = TransformationRvI(pr_precedant, transfo)
    ColoriePixel(pi_precedant.col, pi_precedant.lig, coul)

    # on parcourt les x
    # depuis transfo.fr.bg.x
    # jusqu'a transfo.fr.hd.x
    # par pas de pasReel

    # on s'attaque au point courant avant de rentrer dans la boucle de parcours des x reels
    pr_courant = PointReel()
    pr_courant.x = transfo.fr.bg.x + pasReel

    while(pr_courant.x < transfo.fr.hd.x) :

        # pour chaque x
        # on calcule le y correspondant
        pr_courant.y = FonctionF(pr_courant.x)

        # on trace le segment reel
        DessineSegmentReel(pr_precedant, pr_courant, coul, transfo)

        # cela fait,
        # le point courant devient le point precedent
        pr_precedant = PointReel(pr_courant.x, pr_courant.y)
        # et le point courant avance d'un pas
        pr_courant.x = pr_courant.x + pasReel

################################################################################
