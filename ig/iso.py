#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Fonctions de dessin en 3D isométrique du module ig
#
################################################################################

################################################################################
# Chargement des modules standards
################################################################################
import pygame
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
from donnees import *
from base import *
from segments import *
################################################################################

################################################################################
# Calcul la boîte englobante de d'un objet 3D
################################################################################
def BoiteObj(obj):
    mins = Point3D(obj.pts[0].x, obj.pts[0].y, obj.pts[0].z)
    maxs = Point3D(obj.pts[0].x, obj.pts[0].y, obj.pts[0].z)

    for pt in obj.pts:
        # Axe des x
        if (pt.x < mins.x):
            mins.x = pt.x
        if (pt.x > maxs.x):
            maxs.x = pt.x
        # Axe des y
        if (pt.y < mins.y):
            mins.y = pt.y
        if (pt.y > maxs.y):
            maxs.y = pt.y
        # Axe des z
        if (pt.z < mins.z):
            mins.z = pt.z
        if (pt.z > maxs.z):
            maxs.z = pt.z

    return (mins, maxs)
################################################################################

################################################################################
# Calcul du repère isométrique adapté à l'objet recentré à l'origine
################################################################################
def CalculeRepereIso(obj, fi):
    # Calcul de la boîte englobante de l'objet
    mins, maxs = BoiteObj(obj)

    # Calcul des variations
    dcol = (fi.hd.col - fi.bg.col)
    dlig = (fi.bg.lig - fi.hd.lig)
    dx = maxs.x - mins.x
    dy = maxs.y - mins.y
    dz = maxs.z - mins.z

    # Calcul du coef du repère 3D isométrique
    coef = dcol / (dx + dy / 2)
    cl = dlig / (dz + dy / 2)
    if (cl < coef):
        coef = cl

    # Calcul du barycentre
    bary = Point3D((mins.x + maxs.x)/2, (mins.y + maxs.y)/2, (mins.z + maxs.z)/2)

    # Centrage de l'objet
    for pt in obj.pts:
        pt.x -= bary.x
        pt.y -= bary.y
        pt.z -= bary.z

    # Calcul de l'origine dans l'image
    orig = PointImage(fi.bg.col + dcol // 2, fi.hd.lig + dlig // 2)

    # Calcul du reprère 3D isométrique
    repIso = RepereIso(orig, coef)

    return repIso
################################################################################

################################################################################
# Projection d'un point 3D dans repère isométrique image
################################################################################
def ProjectionIso(A, repIso):
    res = PointImage()

    #
    # À COMPLÉTER
    #

    return res
################################################################################

################################################################################
# Dessin isométrique d'un objet 3D
################################################################################
def DessineObjet(obj, repIso, coul, fi = None, projection = False):

    #
    # À COMPLÉTER
    #

    # Calcul des projections des pts 3D sur l'image
    if (projection):
        pass

    # Dessin des faces

################################################################################
