#!/usr/bin/python2.7
# -*- coding: utf-8 -*-
#
# Université de Lorraine - Licence informatique
# Programme de mise en oeuvre des éléments du cours d'informatique graphique
# utilisant le module pygame
#
################################################################################

################################################################################
# Chargement des modules personnels
################################################################################
import ig
# Redéfinition de la liste des affichages à effectuer
ig.don.Afaire = [ig.don.Actions.TRIANGLES]

################################################################################
# CORPS DU PROGRAMME
################################################################################

# Initialisation de la fenêtre avec la couleur de fond (noir)
ig.Effacer()
# Réglage taille des textes
ig.TailleTexte(24)
# Appel de la fonction d'affichage effectuant les dessins
ig.Affichage(ig.don.Afaire[ig.don.action])
# Boucle de gestion des évènements
while (not ig.don.fini):
    # Gestion du clavier
    ig.gestionTouches()
    # Gestion de la souris
    ig.gestionSouris()
    # Appel de la fonction d'affichage effectuant les dessins
    ig.Affichage(ig.don.Afaire[ig.don.action])
    # Mise à jour de la fenêtre
    ig.MiseAJour()
# Fin du programme
ig.Sortie()
