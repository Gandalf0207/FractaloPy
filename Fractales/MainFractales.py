import turtle
import time
from turtle import *

class MainFractaleGestion(object):
    def __init__(self, profondeur, couleurTrait, tailleTrait, turtle, screen) -> None:
        self.profondeur = profondeur
        self.couleurTrait = couleurTrait
        self.tailleTrait = tailleTrait
        self.isPaused = False
        self.segment_stack = []
        self.turtle = turtle
        self.screen = screen
        self.screen.tracer(0)  # Désactiver le traçage automatique pour un contrôle manuel du rendu

        # Paramètres Turtle
        self.turtle.speed(0)  # Vitesse maximale pour un dessin rapide
        self.turtle.hideturtle()
        self.turtle.pensize(self.tailleTrait)
        self.turtle.pencolor(self.couleurTrait)

    def Lancer(self, fractaleType):
        # Réinitialiser les variables à chaque lancement
        self.isPaused = False
        self.segment_stack = []  # Liste qui va contenir les segments à dessiner
        self.turtle.clear()  # Efface le dessin actuel

        # Initialisation du flocon de Koch : triangle équilatéral
        side_length = 200  # Taille du côté du triangle initial

        # Commencer à dessiner le flocon de Koch
        self.turtle.penup()
        self.turtle.goto(-side_length / 2, -100)  # Positionner au point de départ
        self.turtle.pendown()

        # Dessiner les 3 côtés du triangle initial
        for _ in range(3):
            self.dessiner_fractale(side_length, self.profondeur)
            self.turtle.left(120)  # Tourner pour le triangle équilatéral

    def ChangerCouleur(self, newCouleurTrait):
        self.couleurTrait = newCouleurTrait
        self.turtle.pencolor(self.couleurTrait)

    def ChangerTailleTrait(self, newTailleTrait):
        self.tailleTrait = newTailleTrait
        self.turtle.pensize(self.tailleTrait)

    def dessiner_fractale(self, longueur, profondeur):
        stack = [(longueur, profondeur)]  # Pile pour stocker les segments à traiter

        while stack:
            if self.isPaused:  # Pause si nécessaire
                return

            longueur, profondeur = stack.pop()

            if profondeur == 0:  # Cas de base, dessiner une ligne droite
                self.turtle.forward(longueur)
            else:
                # Ajouter les segments de la fractale dans la pile (en ordre inverse)
                self.segment_stack.append((longueur / 3, profondeur - 1))
                self.segment_stack.append((longueur / 3, profondeur - 1))
                self.segment_stack.append((longueur / 3, profondeur - 1))
                self.segment_stack.append((longueur / 3, profondeur - 1))

                # Ajouter les virages (angles) dans la pile
                self.segment_stack.append("LEFT_60")
                self.segment_stack.append((longueur / 3, profondeur - 1))
                self.segment_stack.append("RIGHT_120")
                self.segment_stack.append((longueur / 3, profondeur - 1))
                self.segment_stack.append("LEFT_60")
                self.segment_stack.append((longueur / 3, profondeur - 1))


            self.screen.update()

    # Méthode pour gérer la pause
    def Pause(self):
        self.isPaused = True

    def Resume(self):
        self.isPaused = False
        self.screen.update()
