#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Initialisation du module d'ingformatique graphique : ig
# pygame, police, taille écran, fenêtres
#
################################################################################

################################################################################
# Chargement des bibliothèques standards utilisées et initialisation de pygame
################################################################################
from __future__ import division
from math import *
from copy import deepcopy
import pygame
################################################################################

################################################################################
# Initialisation du module pygame et de la police de caractères pour les textes
################################################################################
pygame.init()
pygame.font.init()
taillePolice = 18
police = pygame.font.SysFont("Quicksand,Comfortaa,Courrier,Arial", taillePolice)
################################################################################

################################################################################
# Dimensions de l'écran (utile pour le mode plein écran)
################################################################################
Largeur = 1365  # Largeur par défaut de la fenêtre
Hauteur = 768   # Hauteur par défaut de la fenêtre
AutoRes = False # Active le réglage auto de la taille de fenêtre
infos = pygame.display.Info()
LargEcr = infos.current_w
HautEcr = infos.current_h
if AutoRes:     # Réglage auto de la taille de la fenêtre selon l'écran
    Largeur = LargEcr
    Hauteur = HautEcr
pleinEcran = False # Indique si on est en plein écran ou en mode fenêtre
################################################################################

################################################################################
# Construction de la fenêtre et initialisation avec fond noir
################################################################################
fen = pygame.display.set_mode([Largeur, Hauteur])    # Fenêtre d'affichage
pygame.display.set_caption("Informatique graphique") # Titre de la fenêtre
fenCop = None                                        # Copie de la fenêtre
                                                     # pour certains affichages
################################################################################
