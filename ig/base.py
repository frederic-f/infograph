#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Fonctions de base du module ig
#
################################################################################

################################################################################
# Chargement des modules standards
################################################################################
import pygame
import time
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
import ecran as ecr
import donnees as don
################################################################################

################################################################################
# Couleur d'un pixel
################################################################################
def CouleurPixel(col, lig, fen):
    coul = don.Couleur()
    coul.R, coul.V, coul.B, coul.A = ecr.fen.get_at((col, lig))
    coul.A = 255 - coul.A # Inversion du canal alpha pour respecter NOTRE convention
    return coul
################################################################################

################################################################################
# Coloriage d'un pixel
################################################################################
def ColoriePixel(col, lig, coul):
    if (coul.A == None):
        ecr.fen.set_at((col, lig), (coul.R, coul.V, coul.B))
    else:
        prec = CouleurPixel(col, lig, ecr.fen)
        alpha = coul.A / 255.0
        combi = don.Couleur()
        combi.R = alpha * prec.R + (1.0 - alpha) * coul.R
        combi.V = alpha * prec.V + (1.0 - alpha) * coul.V
        combi.B = alpha * prec.B + (1.0 - alpha) * coul.B
        ecr.fen.set_at((col, lig), (combi.R, combi.V, combi.B))
################################################################################

################################################################################
# Coloriage d'un point de taille donnée
################################################################################
def ColoriePoint(pt, coul, rayon = 1):
    r2 = rayon * rayon
    for lig in range(-rayon, rayon + 1):
        for col in range (-rayon, rayon + 1):
            dst = col * col + lig * lig
            if (dst <= r2):
                ColoriePixel(pt.col+col, pt.lig+lig, coul)
################################################################################

################################################################################
# Coloriage de tous les pixels en noir ("vide" la fenêtre)
################################################################################
def Effacer(zone=None):
    if zone == None:
        ecr.fen.fill((don.fond.R, don.fond.V, don.fond.B))
    else:
        ecr.fen.fill((don.fond.R, don.fond.V, don.fond.B), zone)
################################################################################

################################################################################
# Affichage d'un texte à une position donnée
################################################################################
def AfficheTexte(texte, pos, coul, centre=False, taille=None, font=None):
    col = int(round(pos[0]))
    lig = int(round(pos[1]))
    policeLoc = ecr.police
    if (taille != None or font != None):
        tail = ecr.taillePolice
        if (taille != None and taille != tail):
            tail = taille
        if (font == None):
            policeLoc = pygame.font.SysFont("Quicksand,Comfortaa,Courier,Arial", tail)
        else:
            policeLoc = pygame.font.SysFont(font, tail)
    rgba = (coul.R, coul.V, coul.B, 255)
    if (coul.A != None):
        rgba = (coul.R, coul.V, coul.B, coul.A)
    surfTxt = policeLoc.render(texte.decode('utf-8'), True, rgba)

    if (centre):
        decLarg = surfTxt.get_width() / 2
        decHaut = surfTxt.get_height() / 2
        ecr.fen.blit(surfTxt, (col-decLarg, lig-decHaut))
    else:
        ecr.fen.blit(surfTxt, pos)
################################################################################

################################################################################
# Modification taille par défaut du texte
################################################################################
def TailleTexte(taille):
    if (taille != ecr.taillePolice):
        ecr.taillePolice = taille
        ecr.police = pygame.font.SysFont("Quicksand,Comfortaa,Courrier,Arial", ecr.taillePolice)
################################################################################

################################################################################
# Mise à jour de l'écran
################################################################################
def MiseAJour(zone=None):
    # Mise à jour éventuelle
    if don.aMettreAJour:
        don.aMettreAJour = False
        if zone == None:
            pygame.display.update()
        else:
            pygame.display.update(zone)

    # Attente de l'intervalle de temps (30 images / seconde)
    temps = time.time()
    if (temps - don.chrono < 1.0 / don.frameRate):
        time.sleep(0.01)
    else:
        don.chrono = temps
################################################################################

################################################################################
# Sortie du programme
################################################################################
def Sortie():
    print("Programme terminé.")
    pygame.quit()
    quit()
################################################################################
