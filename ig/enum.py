#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Définition rudimentaire d'énumérations entières
#
################################################################################

################################################################################
# Définition de la fonction IntEnum et d'un conteneur pour créer
# des énumération entières
################################################################################
class Conteneur(object):
    pass

def IntEnum(liste):
  obj = Conteneur()
  num = 0
  for cle in liste.split():
    setattr(obj, cle, num)
    num = num + 1
  return obj
################################################################################
