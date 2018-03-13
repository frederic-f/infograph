#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Calcul et dessin de tangentes du module ig
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
from fonction import *
from param import *
################################################################################

################################################################################
# Dessin de la tangente à la courbe de type typeC au point t
################################################################################
def DessineTangente(t, typeC, coul, transfo):
    
    #
    # done
    #

    dt = 0.01
    if (typeC == "f"): # Tangente d'une fonction analytique
        #print("tangente parametriquw")
        # coordonnees de A
        A = PointReel(t, FonctionF(t))
        #print("coord A (", A.x, ",", A.y)

        # coordonnees de B
        B = PointReel(t-dt, FonctionF(t-dt))
        #print("coord B (", B.x, ",", B.y)

        # coordonnees de C
        C = PointReel(t+dt, FonctionF(t+dt))
        #print("coord C (", C.x, ",", C.y)

        # calcul du vecteur BC
        # on utilise un point reel pour stocker le vecteur
        BC = PointReel(C.x - B.x, C.y - B.y)
        
        alpha = 1000

        # calcul des coord de B_ (A - alpha * vectBC)
        B_ = PointReel(A.x - alpha*BC.x, A.y - alpha*BC.y)
        # calcul des coord de C_ (A + ....
        C_ = PointReel(A.x + alpha*BC.x, A.y + alpha*BC.y)

        # tracage de B_C_
        DessineSegmentReel(B_, C_, coul, transfo)
        

    else:              # Tangente d'une fonction paramétrique
                # coordonnees de A
        A = PointReel(ParametriqueX(t), ParametriqueY(t))
        #print("coord A (", A.x, ",", A.y)

        # coordonnees de B
        B = PointReel(ParametriqueX(t - dt), ParametriqueY(t - dt))
        #print("coord B (", B.x, ",", B.y)

        # coordonnees de C
        C = PointReel(ParametriqueX(t + dt), ParametriqueY(t + dt))
        #print("coord C (", C.x, ",", C.y)

        # calcul du vecteur BC
        # on utilise un point reel pour stocker le vecteur
        BC = PointReel(C.x - B.x, C.y - B.y)
        
        alpha = 1000

        # calcul des coord de B_ (A - alpha * vectBC)
        B_ = PointReel(A.x - alpha*BC.x, A.y - alpha*BC.y)
        # calcul des coord de C_ (A + ....
        C_ = PointReel(A.x + alpha*BC.x, A.y + alpha*BC.y)

        # tracage de B_C_
        DessineSegmentReel(B_, C_, coul, transfo)

################################################################################
