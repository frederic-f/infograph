#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Définition des types de données du module ig
#
################################################################################

################################################################################
# Chargement des modules standards
################################################################################
from enum import IntEnum
import sys
import os.path
import time
################################################################################

################################################################################
# Chargement des définitions persos
################################################################################
import ecran as ecr
################################################################################

################################################################################
# DÉCLARATION DES TYPES DE DONNÉES
#
################################################################################
# Description d'une couleur à partir des composantes Rouge, Vert et Bleu
################################################################################
class Couleur:
    R = None # Canal rouge
    V = None # Canal vert
    B = None # Canal bleu
    A = None # Canal alpha (transparence : 0 = opaque - 255 = transparent)
    # Initialisation explicite (constructeur)
    def __init__(self, r=255, v=255, b=255, a=None): # Blanc par défaut
        self.R = r
        self.V = v
        self.B = b
        self.A = a
################################################################################

################################################################################
# Description d'un point dans l'espace image
################################################################################
class PointImage:
    col = None # Colonne dans l'image
    lig = None # Ligne dans l'image
    def __init__(self, col=-1, lig=-1): # Point hors image par défaut
        self.col = col
        self.lig = lig
################################################################################

################################################################################
# Description d'un point dans l'espace réel
################################################################################
class PointReel:
    x = None # Abscisse du point
    y = None # Ordonnée du point
    def __init__(self, x=0.0, y=0.0): # Point à l'origine par défaut
        self.x = x
        self.y = y
################################################################################

################################################################################
# Description d'un point 3D dans l'espace réel
################################################################################
class Point3D:
    x = None # Abscisse du point
    y = None # Ordonnée du point
    z = None # Hauteur du point
    def __init__(self, x=0.0, y=0.0, z=0.0): # Point à l'origine par défaut
        self.x = x
        self.y = y
        self.z = z
################################################################################

################################################################################
# Description d'une fenêtre dans l'espace image
################################################################################
class FenetreImage:
    bg = None # Point image en bas à gauche de la fenêtre
    hd = None # Point image en haut à droite de la fenêtre
    def __init__(self, bg=PointImage(0, ecr.Hauteur), hd=PointImage(ecr.Largeur, 0)):
        # La fenêtre image prend toute la fenêtre par défaut
        self.bg = bg
        self.hd = hd
################################################################################

################################################################################
# Description d'une fenêtre dans l'espace réel
################################################################################
class FenetreReel:
    bg = None # Point réel en bas à gauche de la fenêtre
    hd = None # Point réel en haut à droite de la fenêtre
    def __init__(self, bg=PointReel(-1.0, -1.0), hd=PointReel(1.0, 1.0)):
        # La fenêtre réelle par défaut est un carré centré à l'origine
        self.bg = bg
        self.hd = hd
################################################################################

################################################################################
# Description des infos de transformation entre les fenêtres réelle et image
################################################################################
class TransfosFenetres:
    fr = None # Fenêtre réelle
    fi = None # Fenêtre image
    riA, riB, riC, riD = None, None, None, None # Coefficients de transfo réel -> image
    irA, irB, irC, irD = None, None, None, None # Coefficients de transfo image -> réel
################################################################################

################################################################################
# Description d'un objet 3D par une liste de points et une liste de faces
################################################################################
class Obj:
    pts = None   # Liste de tous les points 3D de l'objet
    faces = None # Liste des faces
    projs = None # Liste de tous les points projetés sur l'image

    # Constructeur de l'objet avec possibilité d'initialisation depuis un fichier
    def __init__(self, nomFic = None, params = False):
        self.pts = []
        self.faces = []
        self.projs = []
        if (nomFic == None and params == False):
            return
        else:
            self.chargement(nomFic, params)

    # Lecture d'un fichier objet
    def lectureFichier(self, nomFic = None, echangeyz = False, inverseY = False):
        if (nomFic != None and os.path.exists(nomFic)):
           # print("lecture fichier obj %s\n" % (nomFic))
           coef = 1
           if (inverseY):
               coef = -1
           for line in open(nomFic, "r"):
               if line.startswith('#'): continue
               values = line.split()
               if not values: continue
               if values[0] == 'v':
                   if (echangeyz):
                       v = Point3D(float(values[1]), coef*float(values[3]), float(values[2]))
                       self.pts.append(v)
                   else:
                       v = Point3D(float(values[1]), coef*float(values[2]), float(values[3]))
                       self.pts.append(v)
               elif values[0] == 'f':
                   face = []
                   for v in values[1:]:
                       w = v.split('/')
                       face.append(int(w[0]) - 1)
                   self.faces.append(face)

    # Test de validité de l'objet (non vide)
    def estValide(self):
        return (len(self.pts) > 0)

    # Chargement d'un objet à partir d'un nom de fichier
    def chargement(self, nomFic = None, params = False):
        echangeYZ = False
        inverseY = False
        if (nomFic == None or params == True):
            for arg in sys.argv:
                if (arg == "-ey"):
                    echangeYZ = True
                elif (arg == "-iy"):
                    inverseY = True
                elif (arg == "-o"):
                    idx = sys.argv.index(arg)
                    if (idx < len(sys.argv)-1):
                        nomFic = sys.argv[idx + 1]
        self.lectureFichier(nomFic, echangeYZ, inverseY)

################################################################################

################################################################################
# Description du repère isométrique (origine et 3 axes)
################################################################################
class RepereIso:
    O = None                 # Origine
    X = PointReel(1.0,  0.0) # Axe X
    Y = PointReel(0.5, -0.5) # Axe Y
    Z = PointReel(0.0, -1.0) # Axe Z
    zoom = 1.0               # Coefficient de zoom

    def __init__(self, orig = None, coef = None):
        if (coef != None):
            self.X = PointReel(coef,  0.0)
            self.Y = PointReel(coef/2, -coef/2)
            self.Z = PointReel(0.0, -coef)
        if (orig == None):
            self.O = PointImage(ecr.Largeur // 2, ecr.Hauteur // 2)
        else:
            self.O = orig
################################################################################

################################################################################
# Listes des actions d'affichage prévues et à effectuer
################################################################################
Actions = IntEnum('CUBE TRIANGLES FUSEAU1 FUSEAU2 FUSEAU3 FUSEAU4 FONCTION PARAM BEZIER HORLOGE ISO TRISPLEINS')
Afaire = [Actions.CUBE, Actions.TRIANGLES, Actions.FUSEAU1, Actions.FUSEAU2, Actions.FUSEAU3, Actions.FUSEAU4, Actions.FONCTION, Actions.PARAM, Actions.BEZIER, Actions.HORLOGE, Actions.ISO, Actions.TRISPLEINS]
action = 0 # Numéro de l'action courante (à partir de 0) dans la liste des actions Afaire
################################################################################

################################################################################
# Informations diverses sur l'état d'affichage
################################################################################
fond = Couleur(0, 0, 0)             # Couleur de fond (noir)
fini = False                        # Indique si le programme est terminé ou non
dejaFait = False                    # Indique si dessin est déjà fait ou non
aMettreAJour = True                 # Indique s'il faut mettre à jour la fenêtre
posS = None                         # Position de la souris
traceS = False                      # Indique si l'on trace avec la souris
position = 0.0                      # Position courante pour les animations
tempsPrec = time.localtime()        # Temps précédent lors des animations
chrono = time.time()                # Démarrage chrono pour mises à jour
frameRate = 30                      # Nombre d'images affichées par seconde
transfoGlobale = TransfosFenetres() # Transformations entre les fenêtres
MARGE = 75                          # Marge entre le bord écran et les fenêtres image
tr1 = None                          # Transformation entre fenêtres principales
tr2 = None                          # Transformation entre fenêtres secondaires
remplissage = False                 # Indique si l'on effectue un coloriage
repIso = None                       # Position de l'origine 3D dans la fenêtre image
obj = None                          # Objet 3D à afficher
################################################################################
