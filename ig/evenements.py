#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Gestion des événements du clavier et de la souris du module ig
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
import ecran as ecr
import donnees as don
from segments import *
from transfos import *
################################################################################

################################################################################
# Gestion des touches du clavier
################################################################################
def gestionTouches():
    events = pygame.event.get([pygame.KEYDOWN, pygame.KEYUP])
    for event in events:
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q or event.key == pygame.K_ESCAPE:
                don.fini = True
            if event.key == pygame.K_r:
                if (don.Afaire[don.action] == don.Actions.BEZIER):
                    don.remplissage = not don.remplissage
                    if (not don.remplissage):
                        ecr.fenCop = None
                    don.dejaFait = False
            if event.key == pygame.K_PLUS or event.key == pygame.K_KP_PLUS:
                if (don.Afaire[don.action] == don.Actions.ISO and don.repIso != None):
                    don.repIso.zoom = don.repIso.zoom * 1.1
                    don.dejaFait = False
            if event.key == pygame.K_MINUS or event.key == pygame.K_KP_MINUS:
                if (don.Afaire[don.action] == don.Actions.ISO and don.repIso != None):
                    don.repIso.zoom = don.repIso.zoom / 1.1
                    don.dejaFait = False
            if event.key == pygame.K_UP:
                if (don.Afaire[don.action] == don.Actions.ISO and don.repIso != None):
                    don.repIso.Y.y = don.repIso.Y.y - 0.5
                    don.dejaFait = False
            if event.key == pygame.K_DOWN:
                if (don.Afaire[don.action] == don.Actions.ISO and don.repIso != None):
                    don.repIso.Y.y = don.repIso.Y.y + 0.5
                    don.dejaFait = False
            if event.key == pygame.K_LEFT:
                if (don.Afaire[don.action] == don.Actions.ISO and don.repIso != None):
                    don.repIso.Y.x = don.repIso.Y.x - 0.5
                    don.dejaFait = False
            if event.key == pygame.K_RIGHT:
                if (don.Afaire[don.action] == don.Actions.ISO and don.repIso != None):
                    don.repIso.Y.x = don.repIso.Y.x + 0.5
                    don.dejaFait = False
            elif event.key == pygame.K_BACKSPACE:
                Effacer()
                don.aMettreAJour = True
            elif event.key == pygame.K_F11:
                if not ecr.pleinEcran:
                    pygame.display.set_mode([ecr.LargEcr, ecr.HautEcr], pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF)
                    ecr.pleinEcran = True
                else:
                    pygame.display.set_mode([ecr.Largeur, ecr.Hauteur])
                    ecr.pleinEcran = False
                don.dejaFait = False
                ecr.fenCop = None
            elif event.key == pygame.K_SPACE or event.key == pygame.K_PAGEDOWN:
                don.action = (don.action + 1) % len(don.Afaire)
                ecr.fenCop = None
                don.posS = None
                if don.Afaire[don.action] == don.Actions.FONCTION:
                    don.position = -3.0
                elif don.Afaire[don.action] == don.Actions.PARAM:
                    don.position = -10.0
                elif don.Afaire[don.action] == don.Actions.HORLOGE:
                    Effacer()
                don.dejaFait = False
            elif event.key == pygame.K_PAGEUP:
                don.action = (don.action - 1 + len(don.Afaire)) % len(don.Afaire)
                ecr.fenCop = None
                don.posS = None
                don.remplissage = False
                if don.Afaire[don.action] == don.Actions.FONCTION:
                    don.position = -3.0
                elif don.Afaire[don.action] == don.Actions.PARAM:
                    don.position = -10.0
                elif don.Afaire[don.action] == don.Actions.HORLOGE:
                    Effacer()
                don.dejaFait = False
            elif event.key == pygame.K_HOME:
                don.posS = None
                don.remplissage = False
                if don.Afaire[don.action] == don.Actions.FONCTION:
                    don.position = -3.0
                elif don.Afaire[don.action] == don.Actions.PARAM:
                    don.position = -10.0
                elif don.Afaire[don.action] == don.Actions.HORLOGE:
                    Effacer()
                don.dejaFait = False
            else: # Cas par défaut : toutes les autres touches
                pass
################################################################################

################################################################################
# Gestion de la souris
################################################################################
def gestionSouris():
    events = pygame.event.get([pygame.MOUSEMOTION, pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP])
    coul = don.Couleur()
    posSn = don.PointImage()
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                don.traceS = True
                don.posS = don.PointImage(event.pos[0], event.pos[1])
                ColoriePixel(don.posS.col, don.posS.lig, coul)
                if (don.Afaire[don.action] == don.Actions.FONCTION):
                    don.dejaFait = False
                don.aMettreAJour = True
        if don.traceS == True and event.type == pygame.MOUSEMOTION:
            posSn.col = event.pos[0]
            posSn.lig = event.pos[1]
            DessineSegmentImage(don.posS, posSn, coul)
            don.posS = posSn
            ColoriePixel(event.pos[0], event.pos[1], coul)
            don.aMettreAJour = True
        if event.type == pygame.MOUSEBUTTONUP:
            don.traceS = False
            if event.button == 3:
                posSn.col = event.pos[0]
                posSn.lig = event.pos[1]
                if (don.tr1 != None):
                    if (posSn.col >= don.tr1.fi.bg.col and posSn.col <= don.tr1.fi.hd.col
                        and posSn.lig >= don.tr1.fi.hd.lig and posSn.lig <= don.tr1.fi.bg.lig):
                        affCoords(posSn, don.tr1)
                        don.aMettreAJour = True
                if (don.tr2 != None):
                    if (posSn.col >= don.tr2.fi.bg.col and posSn.col <= don.tr2.fi.hd.col
                        and posSn.lig >= don.tr2.fi.hd.lig and posSn.lig <= don.tr2.fi.bg.lig):
                        affCoords(posSn, don.tr2)
                        don.aMettreAJour = True
################################################################################

################################################################################
# Affichage coordonnées
################################################################################
def affCoords(pos, tr):
    coul = don.Couleur()
    ColoriePoint(pos, coul, 2)
    pr = TransformationIvR(pos, tr)
    texteX = "x : %.2f" % (pr.x)
    texteY = "y : %.2f" % (pr.y)
    AfficheTexte(texteX, (pos.col, pos.lig + 10), coul, True, 12)
    AfficheTexte(texteY, (pos.col, pos.lig + 22), coul, True, 12)
    don.aMettreAJour = True
################################################################################
