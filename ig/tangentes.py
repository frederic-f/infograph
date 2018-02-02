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
    # À COMPLÉTER
    #

    dt = 0.01
    if (typeC == "f"): # Tangente d'une fonction analytique
        pass
    else:              # Tangente d'une fonction paramétrique
        pass

################################################################################
